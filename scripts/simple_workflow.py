#!/usr/bin/env python3
"""
🚀 SIMPLE START-TO-FINISH WORKFLOW
Leads → Clean → Campaign → WhatsApp Links
"""

import csv
import json
import sys
from pathlib import Path
from datetime import datetime

def main():
    print("\n" + "="*70)
    print("  START-TO-FINISH WORKFLOW")
    print("="*70)
    
    # Get city name from command line argument
    city_name = sys.argv[1] if len(sys.argv) > 1 else "default"
    city_slug = city_name.lower().replace(" ", "_")
    
    # STEP 1: READ REAL LEADS
    print("\n📍 STEP 1: LOAD EXISTING LEADS")
    
    # Get business type from script location or parameter
    script_path = Path(__file__).parent.parent
    business_type = script_path.name
    leads_dir = script_path / "data" / "leads"
    
    # Find first leads file
    leads_files = list(leads_dir.glob("leads_*.csv"))
    if not leads_files:
        print(f"❌ No leads files found in {leads_dir}")
        return
    
    leads_file = leads_files[0]
    
    leads = []
    with open(leads_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        leads = list(reader)
    
    print(f"✅ Loaded {len(leads)} leads from {leads_file}")
    if leads and 'name' in leads[0]:
        print(f"   Sample: {leads[0]['name']}")
    elif leads:
        print(f"   Sample: {leads[0]}")
    
    # STEP 2: CLEAN DATA
    print("\n🧹 STEP 2: CLEAN & VALIDATE DATA")
    valid_leads = []
    for lead in leads:
        phone = lead.get('phone', '').strip()
        name = lead.get('name', '').strip()
        
        # Simple validation
        if phone and len(phone) >= 8 and name:
            # Standardize phone format
            if not phone.startswith('+91'):
                phone = '+91' + phone.lstrip('0')
            
            lead['phone'] = phone
            valid_leads.append(lead)
    
    print(f"✅ Cleaned: {len(valid_leads)} valid leads (removed {len(leads)-len(valid_leads)} invalid)")
    
    # STEP 3: CREATE WHATSAPP CAMPAIGN
    print("\n💬 STEP 3: GENERATE WHATSAPP CAMPAIGN")
    
    whatsapp_data = []
    for i, lead in enumerate(valid_leads[:20], 1):  # First 20
        name = lead.get('name', 'Business')
        phone = lead.get('phone', '')
        
        # Create WhatsApp message
        message = f"Hi {name},\nWe have an exciting website for your cafe!\nCheck it out"
        
        # Create clickable WhatsApp link
        link = f"https://wa.me/{phone}?text={message.replace(' ', '%20').replace(chr(10), '%0A')}"
        
        whatsapp_data.append({
            'name': name,
            'phone': phone,
            'whatsapp_link': link,
            'status': 'ready_to_send'
        })
    
    print(f"✅ Created {len(whatsapp_data)} WhatsApp messages")
    
    # STEP 4: SAVE RESULTS
    print("\n💾 STEP 4: SAVE OUTPUT FILES")
    
    # Create output directories if they don't exist
    campaigns_dir = script_path / "data" / "campaigns"
    results_dir = script_path / "data" / "results"
    campaigns_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # Save campaign CSV
    campaign_file = campaigns_dir / f"campaign_{city_slug}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(campaign_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'whatsapp_link', 'status'])
        writer.writeheader()
        writer.writerows(whatsapp_data)
    
    print(f"✅ Saved: {campaign_file}")
    
    # Save report
    report = {
        'workflow': 'start-to-finish',
        'city': city_name,
        'category': business_type,
        'timestamp': datetime.now().isoformat(),
        'metrics': {
            'leads_loaded': len(leads),
            'leads_valid': len(valid_leads),
            'leads_invalid': len(leads) - len(valid_leads),
            'whatsapp_messages': len(whatsapp_data),
            'ready_to_send': len([x for x in whatsapp_data if x['status'] == 'ready_to_send'])
        }
    }
    
    report_file = results_dir / f"report_{city_slug}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"✅ Saved: {report_file}")
    
    # FINAL SUMMARY
    print("\n" + "="*70)
    print("  ✅ WORKFLOW COMPLETE")
    print("="*70)
    print(f"\n📊 RESULTS:")
    print(f"   ✅ Leads processed:     {len(valid_leads)}")
    print(f"   ✅ WhatsApp messages:   {len(whatsapp_data)}")
    print(f"   ✅ Ready to send:       {report['metrics']['ready_to_send']}")
    print(f"\n📁 OUTPUT FILES:")
    print(f"   • {campaign_file}")
    print(f"   • {report_file}")
    print("\n" + "="*70 + "\n")

if __name__ == '__main__':
    main()
