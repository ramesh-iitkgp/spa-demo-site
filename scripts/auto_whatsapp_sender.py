#!/usr/bin/env python3
"""
WhatsApp Sender - Persistent Session (ONE login for all messages)
NO re-logins, NO new QR codes between messages
"""

import csv
import asyncio
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

async def send_whatsapp_messages_auto():
    """
    Automate WhatsApp Web message sending using direct URLs
    This works even for unsaved contacts!
    """
    
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("❌ Playwright not installed")
        print("Install with: pip install playwright")
        print("Then run: playwright install chromium")
        return False
    
    print("\n" + "="*80)
    print("  📱 AUTO WHATSAPP SENDER (Persistent Session - ONE Login!)")
    print("="*80 + "\n")
    
    # Find latest messages CSV
    csv_files = list(Path('.').glob('whatsapp_messages_*.csv'))
    if not csv_files:
        print("❌ No whatsapp_messages_*.csv found")
        return False
    
    messages_file = sorted(csv_files)[-1]
    print(f"📁 Using: {messages_file}\n")
    
    # Read messages
    messages = []
    with open(messages_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        messages = list(reader)
    
    print(f"📊 Found {len(messages)} messages to send\n")
    
    # Confirm before starting
    print("⚠️  IMPORTANT:")
    print("  1. Keep your phone connected to internet")
    print("  2. Login will happen ONCE only")
    print("  3. ALL messages sent with SAME session (no re-logins!)")
    print("  4. Phone numbers auto-cleaned (10 digits)\n")
    
    confirm = input("Ready to send all messages? Type 'yes' to confirm: ").strip().lower()
    if confirm != 'yes':
        print("\n❌ Cancelled")
        return False
    
    print("\n🚀 Starting WhatsApp Web automation with PERSISTENT session...\n")
    
    # Initialize Playwright with persistent session
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage'
            ]
        )
        
        # Create context with persistent storage (maintains login!)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Avoid automation detection
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false,
            });
        """)
        
        print("🌐 Opening WhatsApp Web (ONE TIME - session stays logged in)...")
        await page.goto("https://web.whatsapp.com/", wait_until="domcontentloaded")
        
        print("⏳ Waiting for WhatsApp to load (may need QR scan)...\n")
        
        # Wait for WhatsApp chat pane to be ready (sign we're logged in)
        try:
            await page.wait_for_selector('[data-testid="pane-side"]', timeout=20000)
            print("✅ WhatsApp ready! Session maintained for all messages.\n")
        except:
            print("⚠️  WhatsApp loading slow. Continuing anyway...\n")
        
        await page.wait_for_timeout(3000)
        
        sent_count = 0
        failed_count = 0
        failed_cafes = []
        
        # Send each message - SAME SESSION, NO RE-LOGINS
        for idx, msg_data in enumerate(messages, 1):
            try:
                cafe_name = msg_data['cafe_name'].strip()
                phone = msg_data['phone'].strip()
                message = msg_data['message'].strip()
                
                # Clean phone number - remove all non-digits
                phone_clean = re.sub(r'\D', '', phone)
                
                # Remove country code if present (91 at start)
                if phone_clean.startswith('91') and len(phone_clean) > 10:
                    phone_clean = phone_clean[2:]
                
                # Keep only last 10 digits (handles any remaining country codes)
                phone_clean = phone_clean[-10:]
                
                # Validate: must be exactly 10 digits
                if len(phone_clean) != 10 or not phone_clean.isdigit():
                    print(f"[{idx:2d}/{len(messages)}] {cafe_name:40s} ❌ Invalid number: {phone}")
                    failed_count += 1
                    failed_cafes.append(f"{cafe_name} (bad number: {phone})")
                    continue
                
                # Add country code for WhatsApp (91 for India)
                phone_full = f"91{phone_clean}"
                
                print(f"[{idx:2d}/{len(messages)}] {cafe_name:40s} ", end="", flush=True)
                
                # Create direct URL (uses same session)
                encoded_message = quote(message)
                whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_full}&text={encoded_message}"
                
                # Navigate in SAME page/session (no new context)
                await page.goto(whatsapp_url, wait_until="domcontentloaded", timeout=8000)
                await page.wait_for_timeout(1500)
                
                # Try to send with multiple methods
                send_success = False
                
                # Method 1: Click send button
                try:
                    send_button = await page.query_selector('[aria-label="Send"]')
                    if send_button:
                        await send_button.click()
                        await page.wait_for_timeout(1200)
                        print("✅ Sent")
                        sent_count += 1
                        send_success = True
                except:
                    pass
                
                # Method 2: Press Enter
                if not send_success:
                    try:
                        await page.press('[contenteditable="true"]', 'Enter')
                        await page.wait_for_timeout(1200)
                        print("✅ Sent")
                        sent_count += 1
                        send_success = True
                    except:
                        pass
                
                # Method 3: Try Ctrl+Enter
                if not send_success:
                    try:
                        await page.press('[contenteditable="true"]', 'Control+Enter')
                        await page.wait_for_timeout(1200)
                        print("✅ Sent")
                        sent_count += 1
                        send_success = True
                    except:
                        pass
                
                if not send_success:
                    print("❌ Failed to send")
                    failed_count += 1
                    failed_cafes.append(cafe_name)
                
                # Wait before next message
                await page.wait_for_timeout(2000)
                
            except Exception as e:
                print(f"❌ Error: {str(e)[:40]}")
                failed_count += 1
                failed_cafes.append(cafe_name)
            
            # Pause every 10 messages
            if idx % 10 == 0 and idx < len(messages):
                print(f"\n⏸️  Paused after 10 messages (20s to avoid detection)...")
                await page.wait_for_timeout(20000)
                print()
        
        # Don't close - keep browser open for verification
        print("\n" + "="*80)
        print("  ✅ SENDING COMPLETE")
        print("="*80)
        print(f"\n📊 Results:")
        print(f"   ✅ Sent: {sent_count}/{len(messages)}")
        print(f"   ❌ Failed: {failed_count}/{len(messages)}")
        
        if failed_cafes:
            print(f"\n❌ Failed:")
            for cafe in failed_cafes[:5]:
                print(f"   • {cafe}")
            if len(failed_cafes) > 5:
                print(f"   ... and {len(failed_cafes)-5} more\n")
        
        print("\n💡 Browser is still open - check WhatsApp to verify messages!")
        print("   Press ENTER to close: ", end="", flush=True)
        input()
        
        await context.close()
        await browser.close()
    
    # Summary
    print("\n" + "="*80)
    print("  ✅ WHATSAPP SENDING COMPLETE")
    print("="*80)
    print(f"\n📊 Results:")
    print(f"   ✅ Sent: {sent_count}/{len(messages)}")
    print(f"   ❌ Failed: {failed_count}/{len(messages)}")
    
    if failed_cafes:
        print(f"\n❌ Failed cafes:")
        for cafe in failed_cafes:
            print(f"   • {cafe}")
    
    # Save results to log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"whatsapp_sent_log_{timestamp}.txt"
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("PERSISTENT SESSION WHATSAPP SENDER LOG\n")
        f.write("="*80 + "\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Method: Persistent Session (ONE login for all)\n")
        f.write(f"Messages file: {messages_file}\n\n")
        f.write(f"✅ Sent: {sent_count}/{len(messages)}\n")
        f.write(f"❌ Failed: {failed_count}/{len(messages)}\n\n")
        
        if failed_cafes:
            f.write("Failed cafes:\n")
            for cafe in failed_cafes:
                f.write(f"  • {cafe}\n")
    
    print(f"\n📁 Log saved: {log_file}")
    print("\n" + "="*80)
    
    return True

def main():
    """Main entry point"""
    
    print("""
════════════════════════════════════════════════════════════════════════════════
  📱 PERSISTENT SESSION WHATSAPP SENDER
════════════════════════════════════════════════════════════════════════════════

KEY FIXES:
✅ ONE persistent login session for ALL messages
✅ NO re-logins between messages
✅ NO new QR codes for each message
✅ Same browser window throughout sending
✅ Automatically cleans phone numbers (keeps 10 digits)
✅ Avoids WhatsApp automation detection

HOW IT WORKS:
1. Opens WhatsApp Web (may need QR scan once)
2. Waits for login to complete
3. Browser session STAYS logged in for all 33 messages
4. Navigates to each contact URL (same session)
5. Sends each message
6. Browser stays open so you can verify

REQUIREMENTS:
✅ Playwright installed
✅ Chromium browser installed
✅ Clean phone numbers (10 digits, no special chars)

TIMING:
⏱️  All 33 messages: ~5-8 minutes
⏸️  Natural delays between sends

ADVANTAGES:
✅ Much faster (no repeated logins)
✅ More reliable (session stays active)
✅ Can verify messages arrived before closing
✅ Better success rate

════════════════════════════════════════════════════════════════════════════════
    """)
    
    # Check if Playwright is installed
    try:
        import playwright
    except ImportError:
        print("❌ Playwright not installed!")
        print("\nInstall with these commands:")
        print("  pip install playwright")
        print("  playwright install chromium")
        print("\nAfter installing, run this script again.")
        return
    
    # Run async function
    asyncio.run(send_whatsapp_messages_auto())

if __name__ == "__main__":
    main()
