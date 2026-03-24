# 📚 DOCUMENTATION INDEX

Welcome! This folder contains all the guides you need to run the business automation system.

---

## 🚀 START HERE

### New to the system?
→ Read [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) first
- Complete step-by-step walkthrough
- From leads → campaign → deployment → WhatsApp

### Want to understand the architecture?
→ Read [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md)
- Folder organization
- File purposes
- How everything fits together

---

## 📖 COMPLETE GUIDE MAP

| Guide | Purpose | Best For |
|-------|---------|----------|
| [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) | End-to-end process (1 lead → WhatsApp) | First-time users, complete workflow |
| [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) | Architecture & folder organization | Understanding the system, scaling |
| [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md) | Creating & maintaining templates | Building cafe/gym/salon templates |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | GitHub Pages deployment automation | Deploying to GitHub, CI/CD setup |

---

## 🎯 QUICK NAVIGATION

### I want to...

**Send WhatsApp campaign to cafes**
1. Read: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) - All 5 steps
2. Run: `python3 simple_workflow.py`
3. File: `cafe_outreach_github_bangalore.csv`

**Create a new template (gym/salon)**
1. Read: [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md) - Required elements
2. Copy: `templates/cafe/` → `templates/salon/`
3. Edit: Template content while keeping required IDs
4. Deploy: `python3 scripts/deploy.py`

**Deploy templates to GitHub**
1. Read: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Setup & troubleshooting
2. Run: `python3 scripts/deploy.py`
3. Verify: Live on GitHub Pages (wait 1-2 min)

**Understand project organization**
1. Read: [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) - Complete architecture
2. Navigate: Folder structure included with explanations

**Run campaignfor multiple cities**
1. Read: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) - Section "Scaling to Multiple Cities"
2. Repeat: Steps 1-5 for each city
3. Track: All campaigns in `data/campaigns/`

**Fix template during deployment**
1. Check: [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md) - Validation checklist
2. Verify: All 5 required IDs present in HTML
3. Test: Locally before deploying with `python3 scripts/deploy.py --no-push`

**Debug parameter injection**
1. Check: [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md) - Troubleshooting
2. Test: URL with `?debug=1` to see console logs
3. Verify: Element IDs match exactly (case-sensitive)

---

## 📂 FILE STRUCTURE

```
project/
├── docs/                          ← YOU ARE HERE
│   ├── README.md                  ← This file
│   ├── WORKFLOW_GUIDE.md          ← Complete 5-step process
│   ├── TEMPLATE_STANDARDIZATION.md ← Template rules & checklist
│   └── DEPLOYMENT_GUIDE.md        ← GitHub deployment
├── PROJECT_STRUCTURE.md           ← Architecture overview
├── templates/                     
│   ├── cafe/
│   │   └── index.html
│   ├── gym/
│   │   └── index.html
│   ├── salon/
│   │   └── index.html
│   └── _common/
│       └── inject-template.js
├── scripts/
│   ├── deploy.py                  ← Deployment automation
│   ├── generate_links.py
│   └── build_templates.py
├── data/
│   ├── leads/                     ← Input CSV files
│   ├── campaigns/                 ← Generated campaigns
│   └── results/                   ← Campaign responses
└── demos/                         ← Local demo files
    └── cafe/
        └── [cafe-name].html
```

---

## 🔄 TYPICAL WORKFLOW

### Situation 1: Launch first campaign
```
1. Collect leads CSV → data/leads/beats_bangalore_cafes.csv
2. Read WORKFLOW_GUIDE.md - Steps 1-5
3. python3 simple_workflow.py
4. python3 scripts/deploy.py
5. python3 auto_whatsapp_sender.py cafe_outreach_github_bangalore.csv
```

### Situation 2: Add gym template
```
1. Read TEMPLATE_STANDARDIZATION.md
2. mkdir templates/gym && cp templates/cafe/* templates/gym/
3. Edit templates/gym/index.html (gym-specific content)
4. Edit scripts/deploy.py (add "gym" to BUSINESS_TYPES)
5. python3 scripts/deploy.py
```

### Situation 3: Scale to new city (Mumbai)
```
1. Collect leads CSV → data/leads/beats_mumbai_cafes.csv
2. Read WORKFLOW_GUIDE.md - Section "Scaling to Multiple Cities"
3. python3 simple_workflow.py --city=mumbai
4. python3 auto_whatsapp_sender.py cafe_outreach_mumbai.csv
```

### Situation 4: Template not showing dynamic names
```
1. Read TEMPLATE_STANDARDIZATION.md - Troubleshooting
2. Verify: All 5 required IDs in HTML
3. Test: http://localhost:8000/templates/cafe/index.html?name=test&location=bangalore&debug=1
4. Check: Browser console for error messages
5. Deploy: python3 scripts/deploy.py --no-push (test locally first)
```

---

## ✅ QUICK VERIFICATION

### Check project is ready:
```bash
# 1. Templates exist
ls templates/cafe/index.html
ls templates/_common/inject-template.js

# 2. Scripts exist
ls scripts/deploy.py
ls scripts/generate_links.py

# 3. Can access data
ls data/leads/beats_*.csv || echo "Add CSV files to data/leads/"

# 4. GitHub repo ready
ls deployment/business-demo-site/.git || echo "Clone repo to deployment/"
```

### Check everything works:
```bash
# 1. Test template locally
python3 -m http.server 8000
# Visit: http://localhost:8000/templates/cafe/index.html?name=test&location=bangalore

# 2. Test workflow
python3 simple_workflow.py
# Check: cafe_outreach_github_bangalore.csv created

# 3. Test deployment
python3 scripts/deploy.py
# Check: GitHub shows recent commits
```

---

## 🆘 NEED HELP?

### Common Issues

**"Template not found"**
- Check: `ls -la templates/cafe/index.html`
- Read: [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md)

**"CSV not loading"**
- Check: `ls -la data/leads/`
- Format: Ensure CSV has columns: `name`, `phone_number`
- Read: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) - Step 1

**"Deployment failed"**
- Check: Git configured with credentials
- Read: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Troubleshooting
- Try: `python3 scripts/deploy.py --no-push` (test locally)

**"URL parameters not working"**
- Check: All 5 required IDs in template (case-sensitive)
- Test: Add `?debug=1` to URL, check browser console
- Read: [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md) - Troubleshooting

**"WhatsApp link error"**
- Check: URL encoding in message (spaces=%20, etc.)
- Verify: Phone format: `+919731655707`
- Read: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) - Step 5

### Getting More Help

1. **Check the relevant guide** based on your issue
2. **Look in Troubleshooting section** of that guide
3. **Verify checklist** (all required files, configuration)
4. **Test locally** before deploying

---

## 📋 DOCUMENT CHECKLIST

### For Template Creation
- [ ] Read [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md)
- [ ] Include 5 required IDs in HTML
- [ ] Test with injection script locally
- [ ] Validate before deployment

### For Deployment
- [ ] Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- [ ] Configure Git credentials
- [ ] Verify deployment folder structure
- [ ] Test with `--no-push` first

### For Complete Workflow
- [ ] Read [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
- [ ] Prepare leads CSV in correct format
- [ ] Run simple_workflow.py
- [ ] Deploy templates with scripts/deploy.py
- [ ] Send campaign with auto_whatsapp_sender.py

---

## 🎓 LEARNING PATH

### Beginner (Just want to send campaigns)
→ [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
- Skip technical details
- Focus on commands to run
- Copy example scenarios

### Intermediate (Want to customize templates)
→ [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md)
- Understand required elements
- Learn parameter injection
- Create custom templates

### Advanced (Building scalable system)
→ [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md)
→ [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- Understand architecture
- Set up CI/CD
- Scale to multiple cities/businesses

---

## 🚀 NEXT STEPS

### Recommended:
1. **Read** [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) (10 min)
2. **Review** [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) (5 min)
3. **Run** simple_workflow.py (2 min)
4. **Deploy** with scripts/deploy.py (5 min)
5. **Send** WhatsApp campaign (varies)

### Total time: ~30 minutes to complete first campaign!

---

## 📞 FILES REFERENCE

**Main Documentation:**
- [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) - Complete 5-step process
- [TEMPLATE_STANDARDIZATION.md](TEMPLATE_STANDARDIZATION.md) - Template rules
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - GitHub deployment

**Project Documentation:**
- [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) - Architecture

**Related Files:**
- AUTO_SENDER_GUIDE.md - WhatsApp automation details
- AUTOMATION_GUIDE.md - System automation overview

---

## ✨ KEY CONCEPTS

**Template**: HTML file with required IDs for dynamic injection
**Campaign**: CSV with business data + demo links + WhatsApp messages
**Demo Link**: GitHub-hosted personalized link (e.g., cafe name in URL)
**Parameter Injection**: JavaScript reads URL parameters, updates page content
**Deployment**: Copy template to GitHub, auto-commit, push to update live site
**Workflow**: 5-step process from leads to WhatsApp outreach

---

**Last Updated**: March 2024
**Version**: 1.0
**Status**: Ready for production use

