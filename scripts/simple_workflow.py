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

# Allow importing the shared WhatsApp campaign generator in this scripts folder
SCRIPT_DIR = Path(__file__).parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.append(str(SCRIPT_DIR))

from whatsapp_campaign_generator import generate_campaign, save_campaigns

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
    
    # Find LATEST leads file for THIS SPECIFIC CITY
    city_slug = city_name.lower().replace(" ", "_")
    leads_files = list(leads_dir.glob(f"leads_{city_slug}_*.csv"))
    
    if not leads_files:
        print(f"⚠️  No leads found for city '{city_name}'. Checking for any available leads...")
        leads_files = list(leads_dir.glob("leads_*.csv"))
    
    if not leads_files:
        print(f"❌ No leads files found in {leads_dir}")
        return
    
    leads_file = sorted(leads_files)[-1]  # Get LATEST for this city
    
    leads = []
    with open(leads_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        leads = list(reader)
    
    leads_mtime = datetime.fromtimestamp(leads_file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    print(f"✅ Loaded {len(leads)} leads from LATEST file:")
    print(f"   📁 File: {leads_file.name}")
    print(f"   ⏰ Modified: {leads_mtime}")
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
    
    # STEP 3: CREATE WHATSAPP CAMPAIGN using UNIVERSAL generator
    print("\n💬 STEP 3: GENERATE WHATSAPP CAMPAIGN")
    
    # Use the universal campaign generator so all businesses share the same IIT-KGP template
    campaigns = generate_campaign(str(leads_file), business_type, city_name, output_format='csv')
    print(f"✅ Created {len(campaigns)} WhatsApp messages")
    
    # STEP 4: SAVE RESULTS
    print("\n💾 STEP 4: SAVE OUTPUT FILES")
    
    # Create output directories if they don't exist
    campaigns_dir = script_path / "data" / "campaigns"
    results_dir = script_path / "data" / "results"
    campaigns_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # Save campaign via shared saver (writes full columns including message/demo_link/whatsapp_link)
    campaign_file = save_campaigns(campaigns, business_type, city_name, output_format='csv')
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
            'whatsapp_messages': len(campaigns),
            'ready_to_send': len([x for x in campaigns if x.get('status') == 'ready_to_send'])
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
    print(f"   ✅ WhatsApp messages:   {len(campaigns)}")
    print(f"   ✅ Ready to send:       {report['metrics']['ready_to_send']}")
    print(f"\n📁 OUTPUT FILES:")
    print(f"   • {campaign_file}")
    print(f"   • {report_file}")
    print("\n" + "="*70 + "\n")

if __name__ == '__main__':
    main()
