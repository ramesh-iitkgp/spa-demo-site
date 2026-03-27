# WhatsApp Campaign Generator

Generate personalized WhatsApp campaigns with automatic injection of business details.

## Features
- Loads leads from CSV file
- Injects: business name, city, address, contact number
- Generates WhatsApp web links
- Outputs campaign ready for sending
- Supports fallback demo links

## Usage

### Basic
```bash
python3 whatsapp_campaign_generator.py [business_type] [city] [leads_file] [output_format]
```

### Examples
```bash
# Generate cafe campaign for Bangalore
python3 whatsapp_campaign_generator.py cafe Bangalore leads_bangalore.csv csv

# Generate gym campaign for Kolkata (JSON output)
python3 whatsapp_campaign_generator.py gym Kolkata leads_kolkata.csv json

# Auto-detect latest leads file
python3 whatsapp_campaign_generator.py salon Mumbai
```

## Input CSV Format
- **name** - Business name
- **phone** - Contact number
- **address** - Business address (optional)
- **city** - City name (optional, used if not provided)
- **demo_link** - Custom demo link (optional, uses default if not provided)

## Output CSV Columns
- **name** - Business name
- **phone** - Contact number
- **address** - Business address
- **city** - City
- **business_type** - Category
- **demo_link** - Website/demo URL
- **message** - Personalized WhatsApp message
- **whatsapp_link** - Direct WhatsApp web link
- **status** - Campaign status
- **timestamp** - Generation timestamp

## Example Workflow

```bash
# 1. Generate leads
python3 scripts/fetch_leads.py Bangalore cafe

# 2. Generate campaigns
python3 scripts/whatsapp_campaign_generator.py cafe Bangalore data/leads/leads_bangalore.csv csv

# 3. Campaign file will be created - ready to send!
```

## Business Types Supported
- barber
- cafe
- clinic
- dental
- dermatologist
- gym
- hotel
- interior
- medical
- resort
- restaurant
- salon
- spa

## Demo Link Structure
If demo_link not provided, falls back to:
`https://ramesh-iitkgp.github.io/{business_type}-demo-site/`

