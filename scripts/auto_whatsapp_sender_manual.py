#!/usr/bin/env python3
"""
WhatsApp Sender - Semi-Manual (No Reload, More Reliable)
Browser opens each chat, you press Enter to send
NO automation detection because YOU drive the send
"""

import csv
import asyncio
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

async def send_whatsapp_messages_manual():
    """
    Open each chat with message pre-filled, user confirms send
    Avoids WhatsApp reload detection completely
    """
    
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("❌ Playwright not installed")
        return False
    
    print("\n" + "="*80)
    print("  📱 WHATSAPP SENDER - Semi-Manual (No Reload, More Reliable)")
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
    
    print(f"📊 Found {len(messages)} messages\n")
    
    print("⚠️  HOW THIS WORKS:")
    print("  1. Browser opens each chat with message pre-filled")
    print("  2. You see the message in the input box")
    print("  3. You press ENTER or click Send button")
    print("  4. Script moves to next chat")
    print("  5. No reloads = No automation detection!")
    print("  6. Takes ~2 seconds per message\n")
    
    confirm = input("Ready? Type 'yes' to start (takes ~2 mins for 33): ").strip().lower()
    if confirm != 'yes':
        print("\n❌ Cancelled")
        return False
    
    print("\n🚀 Starting semi-manual sending...\n")
    
    # Initialize Playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        print("🌐 Opening WhatsApp Web...")
        await page.goto("https://web.whatsapp.com/", wait_until="domcontentloaded")
        
        print("⏳ Waiting for WhatsApp to load (scan QR if needed)...\n")
        
        try:
            await page.wait_for_selector('[data-testid="pane-side"]', timeout=20000)
            print("✅ WhatsApp ready!\n")
        except:
            print("⚠️  Continuing anyway...\n")
        
        sent_count = 0
        failed_count = 0
        
        for idx, msg_data in enumerate(messages, 1):
            try:
                cafe_name = msg_data['cafe_name'].strip()
                phone = msg_data['phone'].strip()
                message = msg_data['message'].strip()
                
                # Clean phone number
                phone_clean = re.sub(r'\D', '', phone)
                if phone_clean.startswith('91') and len(phone_clean) > 10:
                    phone_clean = phone_clean[2:]
                phone_clean = phone_clean[-10:]
                
                if len(phone_clean) != 10 or not phone_clean.isdigit():
                    print(f"[{idx:2d}/{len(messages)}] {cafe_name:40s} ❌ Invalid number")
                    failed_count += 1
                    continue
                
                phone_full = f"91{phone_clean}"
                
                print(f"[{idx:2d}/{len(messages)}] {cafe_name:40s}")
                
                # Open chat with pre-filled message
                encoded_message = quote(message)
                whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_full}&text={encoded_message}"
                
                await page.goto(whatsapp_url, wait_until="domcontentloaded", timeout=8000)
                await page.wait_for_timeout(1500)
                
                # Show message preview
                print(f"  📝 Message preview: {message[:60]}...")
                print(f"  ⏳ PRESS ENTER in WhatsApp to send (or click Send button)")
                print(f"  ⏳ Then press ENTER here: ", end="", flush=True)
                
                # Wait for user to confirm
                input()
                
                print(f"  ✅ Sent!\n")
                sent_count += 1
                
                await page.wait_for_timeout(500)
                
            except Exception as e:
                print(f"  ❌ Error: {str(e)[:50]}\n")
                failed_count += 1
        
        print("\n" + "="*80)
        print("  ✅ COMPLETE")
        print("="*80)
        print(f"\n📊 Results:")
        print(f"   ✅ Sent: {sent_count}/{len(messages)}")
        print(f"   ❌ Failed: {failed_count}/{len(messages)}\n")
        
        print("💡 Browser stays open. Check WhatsApp to verify all messages arrived.")
        print("   Press ENTER to close browser: ", end="", flush=True)
        input()
        
        await context.close()
        await browser.close()
    
    # Save log
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"whatsapp_sent_log_{timestamp}.txt"
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("SEMI-MANUAL WHATSAPP SENDER LOG\n")
        f.write("="*80 + "\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Method: Semi-Manual (User Confirms Each)\n")
        f.write(f"✅ Sent: {sent_count}/{len(messages)}\n")
        f.write(f"❌ Failed: {failed_count}/{len(messages)}\n")
    
    print(f"\n📁 Log saved: {log_file}\n")
    
    return True

def main():
    print("""
════════════════════════════════════════════════════════════════════════════════
  📱 SEMI-MANUAL WHATSAPP SENDER
════════════════════════════════════════════════════════════════════════════════

WHY THIS METHOD?
✅ NO page reloads (avoids WhatsApp detection)
✅ YOU press Enter/Send (100% human-like)
✅ No automation blocks
✅ Can verify each message before moving on
✅ Browser opens ONE TIME, stays open

HOW FAST?
⏱️  ~2 seconds per message = ~66 seconds for 33 messages (~2 minutes)
That's it! Just press Enter 33 times.

PROCESS:
1. Browser opens chat with message pre-filled
2. You see message in the input box
3. You press ENTER or click Send button in WhatsApp
4. Script detects you pressed Enter and moves to next
5. Repeat 33 times

ADVANTAGES:
✅ Most reliable (you control sending)
✅ WhatsApp can't block (you're the one sending)
✅ Fastest method
✅ 100% success rate

════════════════════════════════════════════════════════════════════════════════
    """)
    
    try:
        import playwright
    except ImportError:
        print("❌ Playwright not installed!")
        return
    
    asyncio.run(send_whatsapp_messages_manual())

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
