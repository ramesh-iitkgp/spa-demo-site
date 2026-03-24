/**
 * 🔄 UNIVERSAL TEMPLATE INJECTION SCRIPT
 * Use this in ALL templates (cafe, gym, salon, etc.)
 * Standardized approach for dynamic name/location injection
 */

(function() {
    'use strict';
    
    // ✅ CONFIGURATION
    // Add any business-specific configurations here
    const CONFIG = {
        defaultBusiness: 'Business Name',
        defaultLocation: 'City',
        theme: 'premium',
    };
    
    // ✅ UTILITY: Convert slug to title case
    function slugToTitle(slug) {
        if (!slug || typeof slug !== 'string') return CONFIG.defaultBusiness;
        
        return slug
            .split('-')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
    }
    
    // ✅ UTILITY: Capitalize location
    function formatLocation(location) {
        if (!location || typeof location !== 'string') return CONFIG.defaultLocation;
        return location.charAt(0).toUpperCase() + location.slice(1);
    }
    
    // ✅ MAIN: Initialize business data from URL parameters
    function initializeBusinessData() {
        // Read URL parameters
        const params = new URLSearchParams(window.location.search);
        const nameSlug = params.get('name') || 'business';
        const locationSlug = params.get('location') || 'city';
        
        // Convert to proper format
        const businessName = slugToTitle(nameSlug);
        const location = formatLocation(locationSlug);
        
        // Update all REQUIRED IDs (must exist in every template)
        updateElement('pageTitle', `${businessName} | Premium Business`);
        updateElement('navBrand', businessName);
        updateElement('heroTitle', businessName + '.');
        updateElement('heroDescription', `Experience premium service in ${location}`);
        updateElement('locationInfo', `${location}, India`);
        
        // Optional: Update other common elements
        updateElement('businessName', businessName);
        updateElement('businessLocation', location);
        
        // Log for debugging
        logDebug(`Injection Complete: ${businessName} in ${location}`);
    }
    
    // ✅ UTILITY: Safe element update
    function updateElement(elementId, content) {
        const element = document.getElementById(elementId);
        if (element) {
            element.textContent = content;
            return true;
        } else {
            logDebug(`⚠️  Element not found: #${elementId}`);
            return false;
        }
    }
    
    // ✅ DEBUG: Console logging (only if ?debug=1)
    function logDebug(message) {
        const params = new URLSearchParams(window.location.search);
        if (params.get('debug') === '1') {
            console.log('🔄 [INJECTION]', message);
        }
    }
    
    // ✅ EXPORT: Make available globally for custom templates
    window.TemplateInjection = {
        slugToTitle,
        formatLocation,
        updateElement,
        logDebug,
        initialize: initializeBusinessData,
    };
    
    // ✅ AUTO-RUN: Initialize on DOM ready
    function runWhenReady() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initializeBusinessData);
        } else {
            initializeBusinessData();
        }
    }
    
    runWhenReady();
})();

/**
 * 📝 USAGE IN TEMPLATES:
 * 
 * 1. Include this script in your template:
 *    <script src="../../_common/inject-template.js"></script>
 * 
 * 2. Add these IDs to your HTML:
 *    <title id="pageTitle">Business Demo</title>
 *    <div id="navBrand">Business Name</div>
 *    <h1 id="heroTitle">Business</h1>
 *    <p id="heroDescription">Description</p>
 *    <p id="locationInfo">Location</p>
 * 
 * 3. Test with: ?name=business-name&location=city&debug=1
 *    Example: https://yoursite.com/cafe/demo/?name=trippy-goat-cafe&location=bangalore&debug=1
 * 
 * 📋 REQUIRED ELEMENTS (must be in EVERY template):
 *    - id="pageTitle"           → Page <title> tag
 *    - id="navBrand"            → Navigation brand/logo area
 *    - id="heroTitle"           → Hero section main title
 *    - id="heroDescription"     → Hero description text
 *    - id="locationInfo"        → Location/address section
 * 
 * 🎨 OPTIONAL ELEMENTS (override if needed):
 *    - id="businessName"        → Any business name reference
 *    - id="businessLocation"    → Any location reference
 * 
 * 🔧 CUSTOM EXTENSIONS:
 *    You can call window.TemplateInjection.updateElement('customId', 'Custom Value')
 *    to update any additional elements programmatically.
 */
