# 🚀 DEPLOYMENT GUIDE

## Overview

This guide explains how to deploy business templates to GitHub Pages with automated validation and version control.

---

## 📋 Prerequisites

1. **Git configured** for your GitHub repo
2. **Python 3.6+** installed
3. **Templates ready** in `templates/` folder
4. **All required template IDs** present (see TEMPLATE_STANDARDIZATION.md)
5. **GitHub repo cloned** in `deployment/business-demo-site/`

---

## 🔧 Setup (One-Time)

### 1. Verify Folder Structure

```
project/
├── templates/
│   ├── _common/
│   │   └── inject-template.js
│   ├── cafe/
│   │   └── index.html
│   ├── gym/
│   │   └── index.html
│   └── salon/
│       └── index.html
├── scripts/
│   ├── deploy.py
│   └── generate_links.py
└── deployment/
    └── business-demo-site/
        ├── cafe/demo/
        ├── gym/demo/
        └── salon/demo/
```

### 2. Update deploy.py (if needed)

```python
# In scripts/deploy.py, line ~15
REPO_URL = "https://github.com/YOUR-GITHUB-USERNAME/business-demo-site.git"
PROJECT_ROOT = "/home/rumm/MTech_Studies/Business/Websites/Cafes"
```

### 3. Clone Deployment Repo

```bash
cd /home/rumm/MTech_Studies/Business/Websites/Cafes

# Clone if not already present
git clone https://github.com/YOUR-USERNAME/business-demo-site.git deployment/business-demo-site

# Create required folders
mkdir -p deployment/business-demo-site/cafe/demo
mkdir -p deployment/business-demo-site/gym/demo
mkdir -p deployment/business-demo-site/salon/demo
```

---

## 🚀 DEPLOYMENT WORKFLOW

### Option 1: Full Deployment (Recommended)

```bash
cd /home/rumm/MTech_Studies/Business/Websites/Cafes

# Deploy all templates with validation and Git push
python3 scripts/deploy.py

# Output:
# ✅ Validating templates...
# ✅ Cafe template valid
# ✅ Syncing cafe template...
# ✅ Committing and pushing changes...
# ✅ Deployment complete!
```

**What it does:**
1. ✅ Validates all templates have required IDs
2. ✅ Syncs from `templates/[type]/` to `deployment/business-demo-site/[type]/demo/`
3. ✅ Commits to Git with timestamped message
4. ✅ Pushes to GitHub `origin/main`
5. ✅ Logs all operations to `deployment/sync.log`

---

### Option 2: Deploy Without Validation

```bash
python3 scripts/deploy.py --no-validate

# Skips template validation, useful if making quick edits
```

---

### Option 3: Deploy Without Git Push

```bash
python3 scripts/deploy.py --no-push

# Syncs locally but doesn't push to GitHub
# Useful for testing before committing
```

---

### Option 4: Deploy Only Specific Template

Edit `scripts/deploy.py` and change:
```python
# Line ~20
BUSINESS_TYPES = ["cafe"]  # Only deploy cafe
```

Then run:
```bash
python3 scripts/deploy.py
```

---

## ✅ VERIFICATION

### 1. Check Deployment Folder

```bash
ls -la deployment/business-demo-site/cafe/demo/
# Should show: index.html with full template
```

### 2. Check Git Status

```bash
cd deployment/business-demo-site
git log --oneline | head -5
# Should show recent commits from deploy.py
```

### 3. Check Sync Log

```bash
cat deployment/sync.log
# Should show timestamps of all deploys
```

### 4. Verify on GitHub

Visit: `https://github.com/YOUR-USERNAME/business-demo-site`
- Check recent commits (should see deploy-bot messages)
- Verify cafe/gym/salon folders present
- Check demo/index.html files exist

---

## 🌐 LIVE TESTING

Once deployed, test links:

```bash
# Cafe demo with parameter injection
https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo/?name=trippy-goat-cafe&location=bangalore

# Gym demo
https://ramesh-iitkgp.github.io/business-demo-site/gym/demo/?name=gold-gym&location=mumbai

# Salon demo
https://ramesh-iitkgp.github.io/business-demo-site/salon/demo/?name=beauty-salon&location=bangalore
```

**Expected behavior:**
- Page title shows business name
- Navigation shows business name
- Hero section shows business name + location
- JavaScript injection logged to console (add `?debug=1` to URL)

---

## 🔄 WORKFLOW: Making Template Changes

### Step 1: Edit Template Locally
```bash
# Edit the cafe template
nano templates/cafe/index.html

# Add new sections, update styling, etc.
```

### Step 2: Test Locally
```bash
# Start HTTP server
cd /home/rumm/MTech_Studies/Business/Websites/Cafes
python3 -m http.server 8000

# Visit in browser
http://localhost:8000/templates/cafe/index.html?name=test-cafe&location=bangalore
```

### Step 3: Validate & Deploy
```bash
# Deploy to GitHub
python3 scripts/deploy.py

# Script validates + syncs + commits + pushes automatically
```

### Step 4: Verify Live
```bash
# Wait ~1 minute for GitHub Pages to update
# Then test live URL in browser
https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo/?name=trippy-goat-cafe&location=bangalore
```

---

## 🛠️ TROUBLESHOOTING

### Problem: "Git command failed"
```bash
# Solution: Check Git configuration
cd deployment/business-demo-site
git config user.name
git config user.email

# If needed, configure:
git config user.name "Your Name"
git config user.email "your@email.com"
```

### Problem: "Template validation failed"
```bash
# Solution: Check which element is missing
python3 scripts/deploy.py --no-push

# Look for validation errors in output
# Run: python3 -c "exec(open('scripts/deploy.py').read())" to see detailed errors
```

### Problem: "Permission denied" on Git
```bash
# Solution: Set up SSH or HTTPS credentials
# If using HTTPS:
cd deployment/business-demo-site
git config credential.helper store

# Then try deployment again - will prompt for password
```

### Problem: GitHub Pages not updating
```bash
# Solution: GitHub Pages caches for ~1 minute
# WAIT 2-3 minutes, then:
# 1. Hard refresh browser (Ctrl+Shift+R)
# 2. Check GitHub Deployments tab for status
# 3. If status shows "failure", fix template and redeploy
```

### Problem: URL parameters not updating page
```bash
# Solution: Check browser console for errors
# Add ?debug=1 to URL:
https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo/?name=test&location=bangalore&debug=1

# Look for TemplateInjection logs
# Verify all 5 required IDs exist in HTML
```

---

## 📊 DEPLOYMENT STATUS

### View Deployment History
```bash
# Show last 10 deployments
tail -10 deployment/sync.log

# Sample output:
# [2024-03-23 15:23:45] Starting deployment...
# [2024-03-23 15:23:45] Validating cafe template...
# [2024-03-23 15:23:45] Syncing cafe template...
# [2024-03-23 15:23:46] Committing changes...
# [2024-03-23 15:23:47] Deployment complete!
```

### Check GitHub Actions (if set up)
```bash
cd deployment/business-demo-site
# Check GitHub Pages deployment history in repo settings
```

---

## 🔐 SECURITY NOTES

1. **Git credentials**: Store securely, use HTTPS or SSH
2. **Template content**: Don't commit API keys or secrets
3. **GitHub Pages**: Content is PUBLIC, suitable only for demo sites
4. **Version control**: All deploys are tracked, can revert if needed

---

## 📱 MULTI-DEVICE TESTING

After deployment, test on:
- [ ] Desktop (Chrome, Firefox, Safari)
- [ ] Mobile (iOS Safari, Android Chrome)
- [ ] Tablet (iPad, Android tablet)
- [ ] WhatsApp link behavior on mobile

---

## 🎯 COMMON DEPLOYMENT SCENARIOS

### Scenario 1: Add New Business Type
```bash
# 1. Create new template
mkdir -p templates/salon
cp templates/cafe/index.html templates/salon/index.html

# 2. Edit template (change content)
nano templates/salon/index.html

# 3. Update deploy.py to include salon
# Edit line: BUSINESS_TYPES = ["cafe", "gym", "salon"]

# 4. Deploy
python3 scripts/deploy.py
```

### Scenario 2: Fix Template Bug in Production
```bash
# 1. Edit cafe template
nano templates/cafe/index.html

# 2. Test locally (don't deploy yet)
# Visit: http://localhost:8000/templates/cafe/index.html?name=test&location=bangalore

# 3. Once confirmed working, deploy
python3 scripts/deploy.py

# 4. Verify on GitHub Pages (wait ~2 min)
```

### Scenario 3: Revert Last Deployment
```bash
cd deployment/business-demo-site

# See recent commits
git log --oneline | head -3

# Revert to previous version
git revert HEAD --no-edit
git push origin main

# GitHub Pages will update in ~1 minute
```

---

## 🚀 ADVANCED: CI/CD Integration

### GitHub Actions Setup (Optional)
Create `.github/workflows/deploy.yml` in your repo:

```yaml
name: Deploy Templates
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: python3 scripts/deploy.py
```

This automatically deploys when you push to GitHub.

---

## 📞 SUPPORT CHECKLIST

Before troubleshooting, verify:
- [ ] All 5 required template IDs present
- [ ] Git credentials configured
- [ ] deployment/ folder exists and is a Git repo
- [ ] GitHub Pages enabled in repo settings
- [ ] Template HTML is valid (no syntax errors)
- [ ] URL parameters use correct format: `?name=slug&location=city`

---

## ✅ SUMMARY

**Deployment = 1 command:**
```bash
python3 scripts/deploy.py
```

**This does:**
1. ✅ Validates templates
2. ✅ Syncs to deployment folder  
3. ✅ Commits to Git
4. ✅ Pushes to GitHub
5. ✅ Logs everything

**Testing:**
1. ✅ Test locally first (http://localhost:8000)
2. ✅ Run deploy script
3. ✅ Test live on GitHub Pages (wait 1-2 min)
4. ✅ Check sync.log for history

