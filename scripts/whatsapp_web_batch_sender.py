#!/usr/bin/env python3
"""
WhatsApp Web Batch Contact Opener
Open WhatsApp Web once, then navigate through contacts
Pre-fills messages and waits for you to press Send
No page reloads - keeps session alive
"""

import csv
import sys
import time
from pathlib import Path
from urllib.parse import quote

# Check if Selenium is installed
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False
    print("⚠️  Selenium not installed")
    print("Install with: pip install selenium")


# ============================================================================
# METHOD 1: Selenium Browser Automation (WhatsApp Web)
# ============================================================================

class WhatsAppWebBatchSender:
    """
    Opens WhatsApp Web in browser and sends messages in batch.
    Keeps session alive - no page reloads between contacts.
    """
    
    def __init__(self):
        self.driver = None
        self.wait_time = 10
    
    def start_whatsapp_web(self):
        """
        Start WhatsApp Web in Chrome.
        """
        if not SELENIUM_AVAILABLE:
            print("❌ Selenium not installed")
            return False
        
        try:
            print("\n📱 Starting WhatsApp Web...")
            
            # Chrome options
            options = webdriver.ChromeOptions()
            # options.add_argument('--start-maximized')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            # Start Chrome
            self.driver = webdriver.Chrome(options=options)
            
            # Open WhatsApp Web
            print("🌐 Opening https://web.whatsapp.com")
            self.driver.get("https://web.whatsapp.com")
            
            # Wait for scan or dashboard
            print("\n⏳ Waiting for WhatsApp Web to load...")
            print("   - If first time: Scan QR code with your phone")
            print("   - If logged in: Will auto-load chats")
            print("   - This may take 10-30 seconds...\n")
            
            time.sleep(5)
            
            return True
        
        except Exception as e:
            print(f"❌ Error starting Chrome: {str(e)}")
            print("   Make sure: chromedriver is installed")
            print("   Install with: pip install webdriver-manager")
            return False
    
    def search_contact(self, phone):
        """
        Search for a contact by phone number in WhatsApp.
        """
        try:
            # Click search box
            search_box = self.driver.find_element(By.XPATH, "//input[@title='Search input textbox']")
            search_box.clear()
            search_box.send_keys(phone)
            
            time.sleep(1)
            
            # Click first result
            contact = self.driver.find_element(By.XPATH, "//div[@role='option']")
            contact.click()
            
            time.sleep(2)
            return True
        
        except Exception as e:
            print(f"  ❌ Could not find contact {phone}: {str(e)}")
            return False
    
    def type_message(self, message):
        """
        Type message in WhatsApp chat box.
        """
        try:
            # Find message input box
            msg_box = self.driver.find_element(
                By.XPATH, 
                "//div[@role='textbox'][@aria-label='Type a message']"
            )
            msg_box.click()
            msg_box.send_keys(message)
            
            time.sleep(1)
            return True
        
        except Exception as e:
            print(f"  ❌ Could not type message: {str(e)}")
            return False
    
    def wait_for_send(self, timeout=300):
        """
        Wait for user to press Send button.
        Timeout after 5 minutes.
        """
        print("  ⏳ Waiting for you to press Send...")
        print("     (Press Send in WhatsApp, then press Enter here)")
        
        # Simple approach: Wait for user input
        try:
            input("  ➡️  Press Enter once you've sent the message: ")
            return True
        except KeyboardInterrupt:
            return False
    
    def send_message_to_lead(self, phone, message):
        """
        Send message to a single lead.
        """
        print(f"\n📱 Sending to: {phone}")
        print(f"   Message: {message[:60]}...")
        
        # Search contact
        if not self.search_contact(phone):
            return False
        
        # Type message
        if not self.type_message(message):
            return False
        
        # Wait for user to send
        if not self.wait_for_send():
            return False
        
        print("   ✅ Sent!")
        return True
    
    def process_csv_batch(self, csv_file, max_leads=None, start_index=0):
        """
        Process CSV file and send to all leads.
        """
        csv_path = Path(csv_file)
        
        if not csv_path.exists():
            print(f"❌ File not found: {csv_file}")
            return
        
        print(f"\n" + "="*70)
        print(f"📊 Processing: {csv_path.name}")
        print(f"="*70 + "\n")
        
        sent_count = 0
        skipped_count = 0
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for idx, row in enumerate(reader):
                    if idx < start_index:
                        continue
                    
                    if max_leads and sent_count >= max_leads:
                        break
                    
                    name = row.get('name', 'Unknown').strip()
                    phone = row.get('phone', '').strip()
                    message = row.get('message', '').strip()
                    
                    if not phone or not message:
                        print(f"⚠️  [{idx + 1}] Skipped: {name} (missing data)")
                        skipped_count += 1
                        continue
                    
                    # Send to this lead
                    if self.send_message_to_lead(phone, message):
                        sent_count += 1
                    else:
                        skipped_count += 1
            
            print(f"\n" + "="*70)
            print(f"✅ Complete!")
            print(f"   Sent: {sent_count}")
            print(f"   Skipped: {skipped_count}")
            print("="*70 + "\n")
        
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        finally:
            # Keep browser open for user
            print("\n✅ Browser still open - review all messages")
            print("Press Ctrl+C in terminal to close WhatsApp Web")
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n\nClosing WhatsApp Web...")
                if self.driver:
                    self.driver.quit()


# ============================================================================
# METHOD 2: Simple Links (Manual)
# ============================================================================

def open_links_in_browser(csv_file, max_leads=None, start_index=0):
    """
    Generate links and open in browser (manual approach).
    """
    import webbrowser
    
    csv_path = Path(csv_file)
    
    if not csv_path.exists():
        print(f"❌ File not found: {csv_file}")
        return
    
    print(f"\n" + "="*70)
    print(f"🔗 Generating WhatsApp Web Links")
    print(f"="*70 + "\n")
    
    opened_count = 0
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for idx, row in enumerate(reader):
                if idx < start_index:
                    continue
                
                if max_leads and opened_count >= max_leads:
                    break
                
                name = row.get('name', 'Unknown').strip()
                phone = row.get('phone', '').strip()
                message = row.get('message', '').strip()
                link = row.get('whatsapp_link', '').strip()
                
                if not link:
                    continue
                
                print(f"[{opened_count + 1}] {name}")
                print(f"    🔗 Opening link...")
                
                # Open in browser
                webbrowser.open(link)
                opened_count += 1
                
                # Wait for user to send
                input("    ➡️  Press Enter once you've sent the message: ")
        
        print(f"\n✅ Complete! Opened {opened_count} chats\n")
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(f"""
╔════════════════════════════════════════════════════════════════════╗
║          WhatsApp Web - Batch Contact Opener (Browser)             ║
╚════════════════════════════════════════════════════════════════════╝

USAGE:
  
  METHOD 1 - Browser Automation (Recommended):
    python3 whatsapp_web_batch_sender.py <csv_file> [method] [num_leads]
  
  METHOD 2 - Manual Links:
    python3 whatsapp_web_batch_sender.py <csv_file> manual [num_leads]

EXAMPLES:

  1️⃣  Auto-send first 5 gym leads (browser automation):
      python3 whatsapp_web_batch_sender.py gym_outreach_ready.csv auto 5

  2️⃣  Generate links for first 10 cafe leads (manual):
      python3 whatsapp_web_batch_sender.py cafe_outreach_ready.csv manual 10

  3️⃣  Auto-send all leads from category:
      python3 whatsapp_web_batch_sender.py gym_outreach_ready.csv auto all

HOW IT WORKS:

  ✅ Auto Method:
    - Opens WhatsApp Web in Chrome
    - Keeps browser open (no reloads)
    - Searches contact
    - Types message
    - You press Send
    - Auto-moves to next contact
  
  ✅ Manual Method:
    - Generates clickable links from CSV
    - Opens each link in browser
    - You copy-paste message or use pre-filled
    - You press Send
    - Click next link

INSTALL DEPENDENCIES:

  For auto method (browser automation):
    pip install selenium webdriver-manager
  
  For manual method:
    No extra dependencies needed

""")
        return
    
    csv_file = sys.argv[1]
    method = "auto"
    if len(sys.argv) > 2:
        method = sys.argv[2].lower()
    
    max_leads = None
    if len(sys.argv) > 3:
        arg = sys.argv[3]
        if arg.lower() != 'all':
            try:
                max_leads = int(arg)
            except ValueError:
                print(f"❌ Invalid max_leads: {arg}")
                return
    
    # Choose method
    if method == "manual":
        open_links_in_browser(csv_file, max_leads, 0)
    else:
        # Auto method (browser automation)
        if not SELENIUM_AVAILABLE:
            print("\n❌ Selenium not installed")
            print("Install with: pip install selenium webdriver-manager")
            print("\nOr use manual method:")
            print("  python3 whatsapp_web_batch_sender.py <csv_file> manual <num>\n")
            return
        
        sender = WhatsAppWebBatchSender()
        
        # Start WhatsApp Web
        if sender.start_whatsapp_web():
            # Wait for QR code scan or login
            input("\n✅ Ready! Press Enter once you're logged into WhatsApp: ")
            
            # Process leads
            sender.process_csv_batch(csv_file, max_leads, 0)


if __name__ == "__main__":
    main()
