#!/usr/bin/env python3
"""
Universal WhatsApp Campaign Generator
Generates WhatsApp outreach campaigns with personalized message injection
Works for all 13 business categories with custom templates
"""

import csv
import json
import sys
import os
from pathlib import Path
from urllib.parse import quote, quote_plus
from datetime import datetime

# Short, universal WhatsApp message template used for ALL business types
BASE_MESSAGE = """Hello Sir,

I made a sample website for [BUSINESS_NAME]:
[DEMO_LINK]

I'm studying at IIT Kharagpur and working on helping local businesses get online.
If you like it, I can set it up properly for you.

Regards,
Ramesh
ramesh25@kgpian.iitkgp.ac.in
"""

BUSINESS_TYPES = [
    'barber', 'cafe', 'clinic', 'dental', 'dermatologist',
    'gym', 'hotel', 'interior', 'medical', 'resort',
    'restaurant', 'salon', 'spa'
]

MESSAGE_TEMPLATES = {btype: BASE_MESSAGE for btype in BUSINESS_TYPES}


def generate_demo_link(business_type, business_name, phone, city):
    """Generate dynamic GitHub Pages demo link with name/location/phone."""
    base_url = f"https://ramesh-iitkgp.github.io/{business_type}-demo-site/"

    # Slugify business name for URL
    slug = ''.join(c.lower() if c.isalnum() else '-' for c in business_name).strip('-') or 'business'

    # Keep only digits in phone
    digits = ''.join(filter(str.isdigit, phone))

    params = [f"name={quote_plus(slug)}"]
    if city:
        params.append(f"location={quote_plus(city)}")
    if digits:
        params.append(f"phone={quote_plus(digits)}")

    return base_url + ("?" + "&".join(params) if params else "")


def generate_whatsapp_link(phone, message):
    """Generate direct WhatsApp Web link"""
    # Clean phone - remove non-digits
    phone_clean = ''.join(filter(str.isdigit, phone))
    
    # Add country code if needed
    if len(phone_clean) == 10:
        phone_clean = "91" + phone_clean
    
    encoded_message = quote(message)
    whatsapp_link = f"https://web.whatsapp.com/send?phone={phone_clean}&text={encoded_message}"
    
    return whatsapp_link


def generate_campaign(leads_csv, business_type, city_name, output_format='csv'):
    """
    Generate WhatsApp campaign from leads CSV
    
    Args:
        leads_csv: Path to leads CSV file
        business_type: Type of business (cafe, gym, etc.)
        city_name: City name for personalization
        output_format: 'csv' or 'json'
    
    Returns:
        List of campaign records
    """
    
    if business_type not in MESSAGE_TEMPLATES:
        print(f"❌ Unknown business type: {business_type}")
        return []
    
    template = MESSAGE_TEMPLATES[business_type]
    campaigns = []
    
    print(f"\n📖 Reading leads from: {leads_csv}")
    
    # Read leads
    try:
        with open(leads_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            leads = list(reader)
        print(f"   ✅ Loaded {len(leads)} leads")
    except FileNotFoundError:
        print(f"❌ File not found: {leads_csv}")
        return []
    
    print(f"✓ Found {len(leads)} leads\n")
    
    # Process each lead
    skipped = 0
    for idx, lead in enumerate(leads, 1):
        name = lead.get('name', 'Business').strip()
        phone = lead.get('phone', '').strip()
        address = lead.get('address', '').strip()
        city = lead.get('city', city_name).strip()
        
        # Build demo_link: prefer existing, else generate dynamic GitHub demo URL
        demo_link = lead.get('demo_link', lead.get('website_link', '')).strip()
        if not demo_link:
            demo_link = generate_demo_link(business_type, name, phone, city)
        
        # Skip if missing phone or name
        if not phone or not name:
            skipped += 1
            continue
        
        # Inject personalized data into template
        message = template.strip()  # Remove extra whitespace
        message = message.replace('[BUSINESS_NAME]', name)
        message = message.replace('[CITY]', city)
        message = message.replace('[ADDRESS]', address)
        message = message.replace('[CONTACT]', phone)
        message = message.replace('[DEMO_LINK]', demo_link)
        
        # Generate WhatsApp link
        whatsapp_link = generate_whatsapp_link(phone, message)
        
        campaign_record = {
            'name': name,
            'phone': phone,
            'address': address,
            'city': city,
            'business_type': business_type,
            'demo_link': demo_link,
            'message': message,
            'whatsapp_link': whatsapp_link,
            'status': 'ready',
            'timestamp': datetime.now().isoformat()
        }
        
        campaigns.append(campaign_record)
        print(f"  ✓ {idx}. {name:<30} ({phone})")
    
    print(f"\n✓ Processed: {len(campaigns)} campaigns")
    if skipped > 0:
        print(f"⚠️  Skipped: {skipped} (missing phone/demo_link)")
    
    return campaigns


def save_campaigns(campaigns, business_type, city_name, output_format='csv'):
    """Save campaign to file"""
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_dir = Path('.')
    campaigns_dir = base_dir / 'data' / 'campaigns'
    campaigns_dir.mkdir(parents=True, exist_ok=True)

    if output_format == 'csv':
        filename = campaigns_dir / f"campaign_{city_name}_{timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'name', 'phone', 'address', 'city', 'business_type',
                'demo_link', 'message', 'whatsapp_link', 'status', 'timestamp'
            ])
            writer.writeheader()
            writer.writerows(campaigns)
    
    elif output_format == 'json':
        filename = campaigns_dir / f"campaign_{city_name}_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(campaigns, f, indent=2, ensure_ascii=False)
    
    return filename


def main():
    """Main execution"""
    
    if len(sys.argv) < 3:
        print("\n📌 WHATSAPP CAMPAIGN GENERATOR")
        print("=" * 70)
        print("\n📖 Usage:")
        print("  python3 whatsapp_campaign_generator.py <business_type> <city_name> [leads_file] [output_format]")
        print("\n✓ Business types:")
        for btype in sorted(MESSAGE_TEMPLATES.keys()):
            print(f"    - {btype}")
        print("\n✓ Example:")
        print("  python3 whatsapp_campaign_generator.py cafe Bangalore leads_bangalore.csv csv")
        print("\n" + "=" * 70 + "\n")
        return
    
    business_type = sys.argv[1].lower()
    city_name = sys.argv[2]
    
    # Auto-find leads file if not provided
    if len(sys.argv) > 3:
        leads_file = sys.argv[3]
    else:
        # Try to find latest leads file
        leads_files = list(Path('.').glob('leads_*.csv'))
        if not leads_files:
            print(f"❌ No leads file found. Provide as: leads_file parameter")
            return
        leads_file = str(sorted(leads_files)[-1])
    
    # Now verify the leads file with details
    leads_path = Path(leads_file)
    if not leads_path.exists():
        print(f"❌ Leads file not found: {leads_file}")
        return
    
    leads_mtime = datetime.fromtimestamp(leads_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    
    output_format = sys.argv[4].lower() if len(sys.argv) > 4 else 'csv'
    
    print("\n" + "=" * 70)
    print("  🚀 WHATSAPP CAMPAIGN GENERATOR")
    print("=" * 70)
    print(f"\n⚙️  Configuration:")
    print(f"   Business Type: {business_type}")
    print(f"   City: {city_name}")
    print(f"   📁 Leads File: {leads_path.name}")
    print(f"      Full path: {leads_path.resolve()}")
    print(f"      Last modified: {leads_mtime}")
    print(f"   Output Format: {output_format}")
    
    # Generate campaigns
    campaigns = generate_campaign(leads_file, business_type, city_name, output_format)
    
    if campaigns:
        # Save campaigns
        output_file = save_campaigns(campaigns, business_type, city_name, output_format)
        
        print(f"\n✅ Campaign saved to: {output_file}")
        print(f"\n📊 Summary:")
        print(f"   Total campaigns: {len(campaigns)}")
        print(f"   Ready to send: {len([c for c in campaigns if c['status'] == 'ready'])}")
        print("\n" + "=" * 70 + "\n")
    else:
        print("\n❌ No campaigns generated")


if __name__ == '__main__':
    main()
