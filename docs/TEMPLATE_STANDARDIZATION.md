# ✅ TEMPLATE STANDARDIZATION GUIDE

## 🎯 Why This Matters

All templates (cafe, gym, salon, etc.) must follow the **SAME STRUCTURE** so:
- Deployment automation works
- Parameter injection is consistent
- Adding new business types is easy
- Team members understand the pattern

---

## 📋 REQUIRED ELEMENTS (Copy-Paste into Every Template)

Every template **MUST** include these 5 HTML elements with exact IDs:

```html
<!-- 1. Page Title (in <head>) -->
<title id="pageTitle">Business Demo</title>

<!-- 2. Navigation Brand (in header/nav) -->
<div id="navBrand">Business Name</div>

<!-- 3. Hero Title (in hero section) -->
<h1 id="heroTitle">Business Name</h1>

<!-- 4. Hero Description (in hero section) -->
<p id="heroDescription">Experience premium service in City</p>

<!-- 5. Location Info (in location/footer section) -->
<p id="locationInfo">City, India</p>
```

---

## 🔄 STANDARD INJECTION PROCESS

### Include This Script (at bottom of body)
```html
<script src="../../_common/inject-template.js"></script>
```

### How it Works
When user visits: `https://yoursite/cafe/demo/?name=trippy-goat-cafe&location=bangalore`

The script:
1. Reads URL parameters
2. Converts slug to title case
3. Updates all 5 required elements
4. Result: Page shows "Trippy Goat Cafe" in "Bangalore"

---

## 🏗️ TEMPLATE STRUCTURE TEMPLATE

Use this as starting point for any new template:

```
templates/
├── [business-type]/
│   ├── index.html              ← Main template
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── custom.js           ← Optional business-specific JS
```

---

## ✏️ Example: Creating Cafe Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title id="pageTitle">Cafe Demo</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div id="navBrand">Cafe Name</div>
    </nav>

    <!-- Hero -->
    <section id="hero">
        <h1 id="heroTitle">Cafe Title</h1>
        <p id="heroDescription">Experience premium coffee in City</p>
    </section>

    <!-- Location -->
    <section id="location">
        <p id="locationInfo">City, India</p>
    </section>

    <!-- IMPORTANT: Include standard injection script -->
    <script src="../../_common/inject-template.js"></script>
</body>
</html>
```

---

## 🎨 CSS/JS GUIDELINES

### CSS (css/style.css)
- Keep styles modular
- Use CSS variables for theming
- Example:
  ```css
  :root {
      --color-primary: #C9A227;  /* Gold */
      --color-coffee: #2C1810;
      --color-cream: #FAF9F6;
  }
  ```

### JS (js/custom.js - optional)
- Business-specific functionality only
- Don't override injection script
- Example: Form handlers, animations

---

## ✅ TEMPLATE VALIDATION CHECKLIST

Before deploying, verify:

- [ ] Has `<title id="pageTitle">`
- [ ] Has `<div id="navBrand">`
- [ ] Has `<h1 id="heroTitle">`
- [ ] Has `<p id="heroDescription">`
- [ ] Has `<p id="locationInfo">`
- [ ] Includes `<script src="../../_common/inject-template.js"></script>`
- [ ] CSS is in `css/` folder
- [ ] Optional JS in `js/` folder
- [ ] No hardcoded business names (use IDs instead)

---

## 🚀 DEPLOYMENT TESTING

### Test Locally
```bash
# Run local server
python3 -m http.server 8000

# Visit URL with parameters
http://localhost:8000/templates/cafe/index.html?name=trippy-goat&location=bangalore&debug=1
```

### Verify Injection
- Check browser console (should show debug logs)
- Verify page title changed
- Verify nav brand updated
- Verify all IDs updated

### Deploy to GitHub
```bash
python3 scripts/deploy.py
# Automatically syncs to deployment/ folder and pushes to GitHub
```

---

## 🔄 ADDING NEW BUSINESS TYPES

1. **Create folder:**
   ```bash
   mkdir templates/salon
   ```

2. **Copy template structure:**
   ```bash
   cp -r templates/cafe/* templates/salon/
   ```

3. **Customize:**
   - Edit HTML branding
   - Update CSS colors (if needed)
   - Keep all 5 required IDs

4. **Add to deployer:**
   ```python
   # In scripts/deploy.py
   self.business_types = ["cafe", "gym", "salon"]  ← Add here
   ```

5. **Deploy:**
   ```bash
   python3 scripts/deploy.py
   ```

---

## 📊 Example: Multi-Template Usage

### Campaign CSV
```csv
name,phone,demo_link,message
Trippy Goat Cafe,+919731655707,https://ramesh-iitkgp.github.io/business-demo-site/cafe/demo?name=trippy-goat-cafe&location=bangalore,Hello...
Gold Gym,+919876543210,https://ramesh-iitkgp.github.io/business-demo-site/gym/demo?name=gold-gym&location=bangalore,Hello...
Beauty Salon,+919123456789,https://ramesh-iitkgp.github.io/business-demo-site/salon/demo?name=beauty-salon&location=bangalore,Hello...
```

Each uses the SAME injection logic, different templates.

---

## 🛠️ TROUBLESHOOTING

**Problem:** Page title not changing
- **Solution:** Verify `<title id="pageTitle">` exists in <head>

**Problem:** Elements showing default text
- **Solution:** Check element ID matches exactly (case-sensitive)

**Problem:** Injection not running
- **Solution:** Add `?debug=1` to URL, check browser console

**Problem:** GitHub not updating
- **Solution:** Run `python3 scripts/deploy.py` again, verify git push succeeded

---

## 📝 BEST PRACTICES

1. **Always test locally first** (before deploying)
2. **Keep templates identical in structure** (only content differs)
3. **Never hardcode business names** (use IDs + JavaScript)
4. **Version control templates** (Git track all changes)
5. **Document customizations** (add comments in HTML)
6. **Validate before deployment** (use deploy script's validation)

---

## 📚 FILES REFERENCE

| File | Purpose |
|------|---------|
| `templates/[type]/index.html` | Main template (required IDs) |
| `templates/_common/inject-template.js` | Universal injection script |
| `scripts/deploy.py` | Deployment automation |
| `deployment/business-demo-site/[type]/demo/index.html` | GitHub deployment copy |

---

## ✨ SUMMARY

**Template = HTML with 5 specific IDs**
**Injection = JavaScript fills those IDs from URL**
**Deployment = Python copies to GitHub + pushes**
**Scaling = Repeat 3 steps for new business types**

