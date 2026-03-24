# 📖 COMPLETE WORKFLOW GUIDE

## 🎯 End-to-End Business Outreach Automation

This guide shows the complete process from **collecting leads → campaign generation → GitHub deployment → WhatsApp outreach**.

---

## 🔄 COMPLETE WORKFLOW (5 Steps)

```
Step 1: Collect Leads
        ↓
Step 2: Clean & Validate Data  
        ↓
Step 3: Deploy Templates to GitHub
        ↓
Step 4: Generate Campaign with Demo Links
        ↓
Step 5: Send WhatsApp Messages
```

---

## 📍 STEP 1: COLLECT LEADS

### From CSV File
```bash
cd /home/rumm/MTech_Studies/Business/Websites/Cafes

# Example CSV: beats_bangalore_cafes.csv
# Columns: name, phone_number, email, address, rating

# Supported input formats:
# - beats_bangalore_*.csv (Google Maps leads)
# - Any CSV with columns: name, phone_number
```

### Using Google Maps Data
1. Export from Google Maps → CSV
2. Ensure columns: `name`, `phone_number`
3. Place in `data/leads/` folder

**Sample Data:**
```csv
name,phone_number,email
Trippy Goat Cafe,+919731655707,trippy@cafe.com
Makkah Cafe,+918456123456,makkah@cafe.com
```

---

## 🧹 STEP 2: CLEAN & VALIDATE DATA

### Using simple_workflow.py

```bash
# Run the workflow
python3 simple_workflow.py

# What it does:
# 1. Loads CSV file
# 2. Cleans phone numbers (removes duplicates, validates format)
# 3. Generates WhatsApp message templates
# 4. Creates demo link URLs
# 5. Exports to campaign_*_ready.csv
```

### Manual Step-by-Step

```python
import pandas as pd

# 1. Load leads
df = pd.read_csv('data/leads/beats_bangalore_cafes.csv')

# 2. Clean phone numbers
def clean_phone(phone):
    phone = str(phone).strip()
    if not phone.startswith('+91'):
        phone = '+91' + phone.lstrip('0')
    return phone

df['phone'] = df['phone'].apply(clean_phone)

# 3. Remove duplicates
df = df.drop_duplicates(subset=['phone'])

# 4. Export
df.to_csv('data/campaigns/cafe_outreach_bangalore.csv', index=False)
```

**Output Files:**
```
data/campaigns/
├── cafe_outreach_bangalore_cleaned.csv    ← Cleaned leads
├── campaign_report_bangalore_*.json       ← Statistics
└── cafe_outreach_github_bangalore.csv     ← Ready with demo links
```

---

## 🌐 STEP 3: DEPLOY TEMPLATES TO GITHUB

### Prerequisites
- Templates exist in `templates/[type]/index.html`
- GitHub repo cloned in `deployment/business-demo-site/`
- Git configured with credentials

### Deployment Process

```bash
# 1. Verify templates are ready
ls -la templates/cafe/index.html
ls -la templates/gym/index.html
# (should exist)

# 2. Run deployment
python3 scripts/deploy.py

# Expected output:
# ✅ Validating templates...
# ✅ Cafe template valid
# ✅ Gym template valid
# ✅ Syncing templates...
# ✅ Committing changes...
# ✅ Pushed to GitHub successfully!
# ✅ Deployment complete!

# 3. Verify live (wait 1-2 minutes)
# Visit: https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo/?name=test&location=bangalore
```

### What Deployment Does
- ✅ Validates all templates have required IDs
- ✅ Copies from `templates/[type]/` to `deployment/business-demo-site/[type]/demo/`
- ✅ Commits with timestamped message
- ✅ Pushes to GitHub
- ✅ GitHub Pages automatically serves updated version

---

## 📧 STEP 4: GENERATE CAMPAIGN WITH DEMO LINKS

### Using the Campaign Generator

```bash
# Method 1: Using simple_workflow.py (includes all steps)
python3 simple_workflow.py
# Outputs: cafe_outreach_github_bangalore.csv

# Method 2: Generate links separately
python3 scripts/generate_links.py \
    --business=cafe \
    --city=bangalore \
    --template=templates/cafe/
```

### Campaign Structure

```csv
name,phone,location,demo_link,message,whatsapp_link,status
Trippy Goat Cafe,+919731655707,Bangalore,https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo?name=trippy-goat-cafe&location=bangalore,"Check out our cafe...",https://wa.me/+919731655707?text=Check%20out...,pending
```

### Demo Link Format

```
https://github-username.github.io/business-demo-site/[type]/demo/?name=[slug]&location=[city]
```

**URL Parameters:**
- `name`: Business name (slug format: lowercase, hyphens)
- `location`: City name
- `debug=1`: (optional) Show console logs

**Example URLs:**
```
# Cafe
https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo?name=trippy-goat-cafe&location=bangalore

# With debug
https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo?name=trippy-goat-cafe&location=bangalore&debug=1

# Gym
https://ramesh-iitkgp.github.io/business-demo-site/gym/demo?name=gold-gym&location=mumbai

# Salon
https://ramesh-iitkgp.github.io/business-demo-site/salon/demo?name=beauty-salon&location=bangalore
```

### Message Template

```
Hey 👋

Check out our showcase:
[DEMO_LINK]

We specialize in [SERVICE] at [LOCATION]. 
📱 Book your spot now!

Cheers!
```

---

## 💬 STEP 5: SEND WHATSAPP MESSAGES

### Using auto_whatsapp_sender.py

```bash
# 1. Verify WhatsApp links are correct
head -5 cafe_outreach_github_bangalore.csv | column -t -s,

# 2. Send messages (manual or automated)

# Option A: Manual - Open each link in browser
# Recipients click link → WhatsApp opens with pre-filled message

# Option B: Automated - Use auto_whatsapp_sender.py
python3 auto_whatsapp_sender.py cafe_outreach_github_bangalore.csv

# What happens:
# - Opens each WhatsApp link in browser
# - Pre-filled message appears in chat
# - You click "Send" manually (WhatsApp blocks auto-send for security)
```

### WhatsApp Link Format

```
https://wa.me/[PHONE]?text=[MESSAGE]
```

**Phone Format:**
- Include country code: `+919731655707`
- Message: URL-encoded text

**Example Link:**
```
https://wa.me/+919731655707?text=Check%20out%20our%20cafe%3A%20https%3A%2F%2Fgithub.io%2F...
```

### Tracking Responses

```bash
# 1. Send campaign
python3 auto_whatsapp_sender.py cafe_outreach_github_bangalore.csv

# 2. Manually track in WhatsApp:
# - "Sent" = Message delivered
# - "Read" = User opened message
# - "Replied" = Engagement!

# 3. Update campaign CSV status
# name,phone,location,demo_link,message,whatsapp_link,status
# Trippy Goat Cafe,+91...,Bangalore,...,...,...,sent
# Gold Gym,+91...,Bangalore,...,...,...,delivered
```

---

## 🔍 QUICK REFERENCE COMMANDS

### Load Leads
```bash
python3 simple_workflow.py
```

### Test Template Locally
```bash
# Start server
python3 -m http.server 8000

# Visit in browser
http://localhost:8000/templates/cafe/index.html?name=test-cafe&location=bangalore
```

### Deploy to GitHub
```bash
python3 scripts/deploy.py
```

### Generate Campaign
```bash
python3 scripts/generate_links.py --business=cafe --city=bangalore
```

### Send WhatsApp
```bash
python3 auto_whatsapp_sender.py cafe_outreach_github_bangalore.csv
```

---

## 📊 EXAMPLE: COMPLETE BANGALORE CAFE CAMPAIGN

### Scenario: Outreach to 20 Bangladesh cafes

**Step 1: Collect Leads** ✅
```bash
# File: beats_bangalore_cafes.csv (20 cafes)
```

**Step 2: Clean Data** ✅
```bash
python3 simple_workflow.py
# Output: 20 cleaned cafes in cafe_outreach_github_bangalore.csv
```

**Step 3: Deploy Template** ✅
```bash
python3 scripts/deploy.py
# Cafe template live on GitHub Pages
```

**Step 4: Campaign Ready** ✅
```csv
Trippy Goat Cafe,+919731655707,Bangalore,https://ramesh-iitkgp.github.io/.../cafe/demo?name=trippy-goat-cafe&location=bangalore,Message...,https://wa.me/+919731655707?text=...,pending
Makkah Cafe,+918456123456,Bangalore,https://ramesh-iitkgp.github.io/.../cafe/demo?name=makkah-cafe&location=bangalore,Message...,https://wa.me/+918456123456?text=...,pending
[... 18 more rows ...]
```

**Step 5: Send WhatsApp** ✅
```bash
python3 auto_whatsapp_sender.py cafe_outreach_github_bangalore.csv
# 20 WhatsApp chats open automatically
# Each with pre-filled message + cafe demo link
# Ready to send manually
```

---

## 🎯 BEST PRACTICES

### Template Management
- ✅ Keep templates in `templates/[type]/` 
- ✅ Always include 5 required IDs in HTML
- ✅ Test locally before deploying
- ✅ Version control templates with Git

### Campaign Generation
- ✅ Clean phone numbers first (remove duplicates)
- ✅ Use consistent name slug format (lowercase, hyphens)
- ✅ Test demo links with URL parameters
- ✅ Verify WhatsApp links are wa.me format

### WhatsApp Outreach
- ✅ Personalize messages per business
- ✅ Include demo link in message
- ✅ Use professional but friendly tone
- ✅ Track responses in campaign CSV
- ✅ Follow up within 3-5 days

### Multi-City Campaigns
```bash
# Repeat workflow for each city:
python3 simple_workflow.py --city=mumbai
python3 scripts/generate_links.py --business=cafe --city=mumbai
python3 auto_whatsapp_sender.py cafe_outreach_mumbai.csv
```

---

## 🛠️ TROUBLESHOOTING

### Issue: Leads CSV not found
```bash
# Check data/leads/ folder
ls -la data/leads/
# Make sure file matches expected name: beats_[city]_*.csv
```

### Issue: Campaign not generating
```bash
# Check phone number format
head -3 data/leads/beats_bangalore_cafes.csv | cut -d, -f1,2

# Should be: name, phone (with or without country code)
# Script auto-converts to +91 format
```

### Issue: Demo link not working
```bash
# Test locally first
http://localhost:8000/templates/cafe/index.html?name=test&location=bangalore

# Check:
# - Template has all 5 required IDs
# - inject-template.js is included
# - URL parameters use correct format
```

### Issue: WhatsApp link error
```bash
# Check URL encoding
# Message should be URL-encoded:
# Space = %20
# : = %3A
# / = %2F
# = = %3D
# ? = %3F

# Verify format:
https://wa.me/+919731655707?text=Hello%20-%20check%20this%3A%20https%3A%2F%2Fgithub.io%2F...
```

### Issue: GitHub link takes too long to load
```bash
# GitHub Pages caches updates for 1-2 minutes
# Wait, then hard refresh:
Ctrl + Shift + R  (Chrome/Firefox)
Cmd + Shift + R   (Safari)

# Check GitHub repo for recent commits
cd deployment/business-demo-site
git log --oneline | head -3
```

---

## 📈 SCALING TO MULTIPLE CITIES

```bash
# Template setup (one-time)
python3 scripts/deploy.py

# For each city:
# 1. Collect leads
# 2. Run workflow
python3 simple_workflow.py --city=mumbai

# 3. Generate campaign
python3 scripts/generate_links.py --business=cafe --city=mumbai

# 4. Send WhatsApp
python3 auto_whatsapp_sender.py cafe_outreach_mumbai.csv
```

---

## 📊 SCALING TO MULTIPLE BUSINESS TYPES

```bash
# Add new template type (e.g., gym)
mkdir -p templates/gym
cp templates/cafe/index.html templates/gym/index.html
# Edit gym/index.html with gym-specific content

# Deploy all templates
python3 scripts/deploy.py

# Update deploy.py:
# BUSINESS_TYPES = ["cafe", "gym", "salon"]

# Generate campaigns for each type
python3 scripts/generate_links.py --business=cafe --city=bangalore
python3 scripts/generate_links.py --business=gym --city=bangalore
python3 scripts/generate_links.py --business=salon --city=bangalore
```

---

## ✅ WORKFLOW CHECKLIST

Before starting:
- [ ] CSV file with leads in `data/leads/`
- [ ] Templates created with required IDs in `templates/[type]/`
- [ ] GitHub repo cloned in `deployment/business-demo-site/`
- [ ] Git credentials configured
- [ ] Python scripts in `scripts/` folder

For each campaign:
- [ ] Run `simple_workflow.py` to clean leads
- [ ] Run `scripts/deploy.py` to update GitHub
- [ ] Verify demo links with URL parameters
- [ ] Test WhatsApp links in browser
- [ ] Run `auto_whatsapp_sender.py` to send
- [ ] Track responses in CSV

---

## 📞 SUPPORT

For issues with specific steps:
- **Step 1 (Leads)**: See `data/leads/README.md`
- **Step 2 (Cleaning)**: See `scripts/README.md`
- **Step 3 (Deployment)**: See `docs/DEPLOYMENT_GUIDE.md`
- **Step 4 (Campaign)**: See `docs/WORKFLOW_GUIDE.md`
- **Step 5 (WhatsApp)**: See `AUTO_SENDER_GUIDE.md`

For template issues:
- See `docs/TEMPLATE_STANDARDIZATION.md`

For architecture questions:
- See `docs/PROJECT_STRUCTURE.md`

