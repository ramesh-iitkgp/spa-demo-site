#!/usr/bin/env python3
"""
LEAD FETCHER - Using proven extraction logic from lead_fetcher.py
That worked for Siliguri and Kolkata this morning
"""

import asyncio
import csv
import re
import sys
import unicodedata
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
from collections import defaultdict


async def safe_text(locator, timeout=2000) -> str:
    try:
        return (await locator.first.inner_text(timeout=timeout)).strip()
    except Exception:
        return ""


async def safe_attr(locator, attr, timeout=2000) -> str:
    try:
        val = await locator.first.get_attribute(attr, timeout=timeout)
        return (val or "").strip()
    except Exception:
        return ""


def validate_phone(phone_raw: str) -> tuple[bool, str]:
    """Validate and normalize phone"""
    if not phone_raw:
        return False, ""
    
    # Remove non-digits
    phone = re.sub(r'\D', '', str(phone_raw))
    
    # Handle country code
    if phone.startswith('91') and len(phone) > 10:
        phone = phone[2:]
    
    # Remove leading 0
    if phone.startswith('0') and len(phone) == 11:
        phone = phone[1:]
    
    # Must be 10 digits
    if len(phone) == 10 and phone.isdigit():
        return True, phone
    
    return False, ""


def clean_name(name: str) -> str:
    """
    Clean cafe name:
    - Handle unicode normalization
    - Remove special characters (keep alphanumeric, space, &, -, ')
    - Trim whitespace
    - Title case
    """
    if not name:
        return ""
    
    # Normalize unicode
    name = unicodedata.normalize('NFKD', str(name))
    name = name.encode('ascii', 'ignore').decode('ascii')
    
    # Remove problematic characters, keep common ones
    name = re.sub(r'[^a-zA-Z0-9\s&\-\']', '', name)
    
    # Clean whitespace
    name = ' '.join(name.split()).title()
    
    return name.strip()


def remove_duplicates(leads: list) -> tuple[list, dict]:
    """
    Remove duplicate leads
    Returns: (unique_leads, stats)
    """
    seen_phones = set()
    seen_names = set()
    unique_leads = []
    
    stats = {
        'total_input': len(leads),
        'duplicate_phone': 0,
        'duplicate_name': 0,
        'unique_output': 0
    }
    
    for lead in leads:
        phone = lead['phone']
        name = lead['name'].lower()
        
        # Check phone duplicate
        if phone in seen_phones:
            stats['duplicate_phone'] += 1
            continue
        
        # Check name duplicate (case-insensitive)
        if name in seen_names:
            stats['duplicate_name'] += 1
            continue
        
        seen_phones.add(phone)
        seen_names.add(name)
        unique_leads.append(lead)
    
    stats['unique_output'] = len(unique_leads)
    return unique_leads, stats


async def fetch_leads(city: str, business_type: str = "cafe"):
    """Fetch leads using proven method"""
    results = []
    
    print(f"\n{'='*70}")
    print(f"  🔍 FETCHING LEADS: {city.upper()}")
    print(f"{'='*70}\n")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            locale="en-IN",
        )
        page = await context.new_page()
        
        try:
            # Prepare search URL
            maps_url = f"https://www.google.com/maps/search/{business_type.replace(' ', '+')}+in+{city.replace(' ', '+')}"
            
            print(f"  📍 Searching: {business_type} in {city}")
            print(f"  🌐 URL: {maps_url}\n")
            
            # Navigate to Google Maps
            print("  ⏳ Loading Google Maps...")
            try:
                await page.goto(maps_url, wait_until="domcontentloaded", timeout=60000)
            except PlaywrightTimeout:
                print("  ⚠️  Page load timed out — continuing anyway...")
            
            await asyncio.sleep(4)
            
            # Dismiss consent popup
            for btn_text in ["Accept all", "Reject all", "I agree", "Agree"]:
                try:
                    btn = page.locator(f'button:has-text("{btn_text}")')
                    if await btn.is_visible(timeout=2000):
                        await btn.click()
                        await asyncio.sleep(1)
                        break
                except:
                    pass
            
            # Wait for results panel
            try:
                await page.wait_for_selector('div[role="feed"]', timeout=15000)
                print("  ✅ Results loaded\n")
            except PlaywrightTimeout:
                print("  ❌ Could not find results panel\n")
                await browser.close()
                return results
            
            # Scroll to load more listings
            print("  📜 Scrolling to load results...\n")
            results_panel = page.locator('div[role="feed"]')
            prev_count = 0
            stall_count = 0
            max_stalls = 20
            
            while True:
                await results_panel.evaluate("el => el.scrollBy(0, 3500)")
                await asyncio.sleep(1.5)
                
                cards = await page.locator('a[href*="/maps/place/"]').all()
                count = len(cards)
                print(f"     Loaded {count} listings", end='\r')
                
                if count >= 100:  # MAX_RESULTS
                    print(f"\n     ✓ Reached 100 listings")
                    break
                
                if count == prev_count:
                    stall_count += 1
                    if stall_count >= max_stalls:
                        print(f"\n     ✓ No more new listings")
                        break
                else:
                    stall_count = 0
                
                prev_count = count
            
            # Extract from each listing
            cards = await page.locator('a[href*="/maps/place/"]').all()
            print(f"\n  📋 Processing {len(cards)} listings...\n")
            
            seen = set()
            SOCIAL_DOMAINS = (
                "facebook.com", "instagram.com", "zomato.com",
                "swiggy.com", "justdial.com", "sulekha.com",
                "twitter.com", "youtube.com", "linktr.ee",
                "maps.google", "g.co",
            )
            
            for i, card in enumerate(cards):
                try:
                    # Click to open detail panel
                    await card.click()
                    await asyncio.sleep(1.2)
                    
                    # Wait for heading
                    try:
                        await page.wait_for_selector('h1', timeout=5000)
                    except:
                        pass
                    
                    # Extract name
                    name = ""
                    for name_sel in [
                        'h1.DUwDvf',
                        'h1[class*="fontHeadline"]',
                        'div[role="main"] h1',
                        'h1',
                    ]:
                        name = await safe_text(page.locator(name_sel), timeout=2000)
                        if name and name.lower() not in ("results", "google maps", ""):
                            break
                    
                    if not name or name in seen or name.lower() == "results":
                        continue
                    seen.add(name)
                    
                    # Clean name (unicode, special chars, etc)
                    name = clean_name(name)
                    
                    # Extract phone
                    phone = ""
                    phone_el = page.locator('[data-item-id^="phone:tel:"]')
                    if await phone_el.count() > 0:
                        raw = await safe_attr(phone_el, "data-item-id")
                        phone_raw = raw.replace("phone:tel:", "").strip()
                        is_valid, phone = validate_phone(phone_raw)
                        if not is_valid:
                            continue  # Skip if no valid phone
                    else:
                        continue  # Skip if no phone at all
                    
                    # Check website
                    website_url = ""
                    web_el = page.locator('[data-item-id="authority"]')
                    if await web_el.count() > 0:
                        web_anchor = web_el.locator('a')
                        if await web_anchor.count() > 0:
                            website_url = await safe_attr(web_anchor, "href")
                        if not website_url:
                            website_url = await safe_text(web_el)
                    
                    has_real_website = bool(website_url) and not any(
                        d in website_url.lower() for d in SOCIAL_DOMAINS
                    )
                    
                    if has_real_website:
                        continue  # Skip if has real website
                    
                    # Extract address
                    address = ""
                    addr_el = page.locator('[data-item-id="address"]')
                    if await addr_el.count() > 0:
                        address = await safe_text(addr_el)
                    
                    # Extract rating
                    rating = ""
                    try:
                        r_el = page.locator('span[aria-label*="stars"]').first
                        raw_r = await r_el.get_attribute("aria-label", timeout=2000)
                        rating = (raw_r or "").replace(" stars", "").strip()
                    except Exception:
                        pass
                    
                    # Get Google Maps URL
                    gmaps_url = page.url
                    
                    # Format website note
                    website_note = f"Social only: {website_url[:50]}" if website_url else "None"
                    
                    # Add result
                    results.append({
                        'name': name,
                        'phone': phone,
                        'address': address,
                        'rating': rating,
                        'website': website_note,
                        'google_maps_url': gmaps_url,
                        'city': city,
                        'business_type': business_type
                    })
                    
                    if len(results) % 5 == 0:
                        print(f"     ✓ Found {len(results)} qualified leads", end='\r')
                    
                except Exception as e:
                    continue
            
            print(f"\n\n  ✅ Extracted {len(results)} qualified leads\n")
            
        except Exception as e:
            print(f"  ❌ Error: {str(e)}\n")
        finally:
            await browser.close()
    
    return results


def save_to_csv(leads: list, city: str, stats: dict = None) -> str:
    """Save to CSV with enhanced fields"""
    if not leads:
        print("  ❌ No leads to save")
        return ""
    
    csv_filename = f"leads_{city.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    fieldnames = ['name', 'phone', 'address', 'rating', 'website', 'google_maps_url', 'city', 'business_type', 'contacted']
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for lead in leads:
            lead['contacted'] = 0
            # Only write fields that exist
            row = {k: lead.get(k, '') for k in fieldnames}
            writer.writerow(row)
    
    print(f"{'='*70}")
    print(f"  ✅ DATA CLEANING & SAVED")
    print(f"{'='*70}\n")
    
    # Show cleaning stats
    if stats:
        print(f"  📊 CLEANING STATISTICS:")
        print(f"     Initial extracted: {stats.get('initial_extracted', 0)}")
        print(f"     After name cleaning: {stats.get('after_name_cleaning', 0)}")
        print(f"     Removed (phone duplicates): {stats.get('duplicate_phone', 0)}")
        print(f"     Removed (name duplicates): {stats.get('duplicate_name', 0)}")
        print(f"     Final valid leads: {len(leads)}\n")
    
    print(f"  📁 {csv_filename}")
    print(f"  📊 {len(leads)} leads\n")
    
    print(f"  📋 Sample (first 5):\n")
    for idx, lead in enumerate(leads[:5], 1):
        print(f"     {idx}. {lead['name']}")
        print(f"        ☎️  {lead['phone']}")
        if lead['address']:
            print(f"        📍 {lead['address'][:50]}")
    
    return csv_filename


def parse_business_type(input_str: str) -> str:
    """Convert numeric menu selection or business type name to lowercase business type"""
    business_types = {
        '1': 'cafe',
        '2': 'restaurant',
        '3': 'salon',
        '4': 'gym',
        '5': 'clinic',
        '6': 'dental',
        '7': 'hotel',
        '8': 'barber'
    }
    
    # If numeric selection, convert to business type
    if input_str in business_types:
        return business_types[input_str]
    
    # Otherwise return as-is (lowercase)
    return input_str.lower()


async def main():
    # Get city and business type from arguments or prompts
    if len(sys.argv) >= 3:
        city = sys.argv[1].strip()
        business_type = parse_business_type(sys.argv[2].strip())
    elif len(sys.argv) == 2:
        city = sys.argv[1].strip()
        print("\n  Available business types:")
        print("    1. cafe")
        print("    2. restaurant")
        print("    3. salon")
        print("    4. gym")
        print("    5. clinic")
        print("    6. dental")
        print("    7. hotel")
        print("    8. barber")
        choice = input("\n  Enter business type (1-8 or name, default: cafe): ").strip() or "cafe"
        business_type = parse_business_type(choice)
    else:
        print("\n" + "="*60)
        print("  🚀 LEAD FETCHER - City & Business Type Selector")
        print("="*60)
        city = input("\n  Enter city name (e.g., kharagpur, delhi, mumbai): ").strip()
        if not city:
            print("  ❌ City name cannot be empty")
            sys.exit(1)
        
        print("\n  Available business types:")
        print("    1. cafe")
        print("    2. restaurant")
        print("    3. salon")
        print("    4. gym")
        print("    5. clinic")
        print("    6. dental")
        print("    7. hotel")
        print("    8. barber")
        choice = input("\n  Enter business type (1-8 or name, default: cafe): ").strip() or "cafe"
        business_type = parse_business_type(choice)
    
    leads = await fetch_leads(city, business_type)
    
    if leads:
        print(f"\n  🧹 CLEANING DATA...\n")
        
        initial_count = len(leads)
        
        # Clean names
        for lead in leads:
            lead['name'] = clean_name(lead['name'])
        
        after_clean_count = len(leads)
        
        # Remove duplicates
        leads, dup_stats = remove_duplicates(leads)
        
        stats = {
            'initial_extracted': initial_count,
            'after_name_cleaning': after_clean_count,
            'duplicate_phone': dup_stats['duplicate_phone'],
            'duplicate_name': dup_stats['duplicate_name'],
        }
        
        save_to_csv(leads, city, stats)
        print(f"\n✅ DONE!\n")
    else:
        print("❌ No leads found\n")


if __name__ == "__main__":
    asyncio.run(main())
