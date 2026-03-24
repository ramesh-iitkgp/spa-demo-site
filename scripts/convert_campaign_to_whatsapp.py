#!/usr/bin/env python3
"""Convert campaign to WhatsApp messages format"""

import csv
from datetime import datetime
from pathlib import Path

# Find latest campaign with links
csv_files = list(Path('.').glob('campaign_with_links_*.csv'))
campaign_file = sorted(csv_files)[-1]

print(f"Converting: {campaign_file}")

messages = []
with open(campaign_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row.get('name', '').strip()
        phone = row.get('phone', '').strip()
        demo_link = row.get('demo_link', '').strip()
        
        # Create message with demo link
        message = f"""Hi {name},

We have an exciting website preview for your cafe!
Check it out: {demo_link}

This is just a sample - fully customizable with your photos, menu, and more.

Best regards,
Your Digital Partner"""
        
        messages.append({
            'cafe_name': name,
            'phone': phone,
            'message': message
        })

# Save as whatsapp_messages format
output_file = f"whatsapp_messages_cafe_bangalore_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['cafe_name', 'phone', 'message'])
    writer.writeheader()
    writer.writerows(messages)

print(f"✅ Created: {output_file}")
print(f"✅ Total messages: {len(messages)}")
