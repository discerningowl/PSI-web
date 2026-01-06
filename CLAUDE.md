# Claude Development Guide - Peach State Intertie Website

## Project Philosophy

**SIMPLICITY ABOVE ALL ELSE**

This website prioritizes simplicity and maintainability over clever solutions. Keep things straightforward and easy to understand.

## Site Structure

This is a static HTML website that uses a simple JavaScript include system for header and footer. All pages are standalone HTML files.

### Files

- **HTML Pages**: index.html, diagram.html, repeaters.html, nets.html, skywarn.html, blog.html, 404.html
- **Stylesheet**: styles.css (controls ALL styling)
- **JavaScript**: includes.js (loads header and footer dynamically)
- **Templates**: header.html and footer.html (loaded dynamically via JavaScript)
- **Images**: images/ directory + PSInew.jpg
- **Deployment**: .github/workflows/deploy.yml (GitHub Actions for auto-deployment to GitHub Pages)

## Header and Footer Management

### Current Implementation

The site uses a simple JavaScript include system to load header and footer dynamically.

### How It Works

1. **includes.js** - JavaScript file that fetches header.html and footer.html
2. **header.html** - Contains the header section and navigation
3. **footer.html** - Contains the footer content
4. Each HTML page has placeholder divs:
   - `<div id="header-placeholder"></div>` - Loads header and navigation
   - `<div id="footer-placeholder"></div>` - Loads footer

### How to Update Header/Footer

To update the header or footer across all pages:

1. Edit `header.html` or `footer.html` directly
2. Save the file
3. The changes automatically appear on ALL pages when loaded

**That's it!** No need to manually update multiple files.

### Navigation Active State

The `includes.js` script automatically sets the `class="active"` on the navigation link that matches the current page filename. The JavaScript detects which page you're on and highlights the correct nav link.

## Important Links

### Footer External Links (Current as of January 2026)

- GA ARES: https://www.gaares.org
- ARES Roster: https://gaares.org/leadership-test/
- GSSA Radio: http://gssaradio.net/
- PTC WX: http://weather.gov/ffc/
- SELR Net: http://selinkedrepeater.net/
- ARRL GA: https://www.arrl.org/Groups/view/georgia ← **Corrected link**

## Common Maintenance Tasks

### Update Contact Information

Contact info appears in the footer of all pages:
- Intertie Manager: K4DBN@PEACHSTATEINTERTIE.COM
- Assistant Manager & Webmaster: WB4NFG@PEACHSTATEINTERTIE.COM

To update: Edit `footer.html` and save. Changes appear on all pages automatically.

### Update "Last Updated" Date

Edit the footer copyright section in `footer.html`:
```html
<p>Established 2008 | Webpage Updated January 2026</p>
```

### Add/Remove Navigation Items

1. Edit `header.html` navigation section
2. Save the file
3. Changes automatically appear on all pages (the active state is handled by JavaScript)

### Change Site Colors

All colors are defined in styles.css at the top (CSS variables):
```css
:root {
    --primary-blue: #1e5a8e;
    --light-blue: #73aad5;
    --dark-gray: #333;
    --red-accent: #e74c3c;
    --green-accent: #27ae60;
}
```

## Deployment

### GitHub Pages + GitHub Actions

The site is automatically deployed to GitHub Pages using GitHub Actions.

**Workflow File**: `.github/workflows/deploy.yml`
**Repository**: discerningowl/PSI-web
**Domain**: peachstateintertie.com
**Auto-deploy**: Triggered on every push to main branch

#### How It Works

1. When you push to the main branch, GitHub Actions automatically runs
2. The workflow deploys all files to GitHub Pages
3. Changes go live within 1-2 minutes

#### Making Changes Live

1. Commit changes to main branch
2. Push to GitHub
3. GitHub Actions automatically builds and deploys
4. Check the Actions tab in GitHub to monitor deployment status

#### Legacy DigitalOcean Configuration

The `.do/` directory contains legacy DigitalOcean App Platform configuration files. These are kept for reference but are no longer actively used:
- `app.yaml` - Legacy deployment config
- `deploy.template.yaml` - Legacy deployment template

## Development Principles

### DO

✓ Keep HTML simple and readable
✓ Edit header.html and footer.html to update all pages
✓ Test pages locally before deploying
✓ Follow existing code structure and formatting
✓ Use CSS variables for colors
✓ Keep responsive design (already implemented)
✓ Keep the JavaScript minimal (only includes.js for header/footer loading)

### DON'T

✗ Add unnecessary JavaScript beyond the simple include system
✗ Over-engineer solutions
✗ Create complex build processes
✗ Add unnecessary dependencies
✗ Change the simple structure
✗ Modify includes.js unless absolutely necessary

## Quick Reference

### All Pages List
1. index.html - Homepage
2. diagram.html - System diagrams
3. repeaters.html - Repeater information
4. nets.html - Net schedules
5. skywarn.html - Skywarn info
6. blog.html - Maytag's blog
7. 404.html - Custom 404 error page

### Template Update Process
1. Edit header.html or footer.html
2. Save the file
3. Test locally (the include system loads the updated templates automatically)
4. Commit and deploy

**Note**: No need to manually update individual pages - the JavaScript include system handles this automatically!

## Notes for Future Claude Sessions

- This project values simplicity over sophistication
- The JavaScript include system (includes.js) provides simple automation without complexity
- Header and footer are managed in single files (header.html, footer.html) and loaded dynamically
- The include system automatically handles navigation active states
- Keep the barrier to entry LOW for future maintainers
- Anyone with basic HTML/JavaScript knowledge should be able to update this site
- The includes.js file is minimal and should not be modified unless absolutely necessary

## JavaScript Include System

### How includes.js Works

The `includes.js` file provides a simple include system:

1. **Loads on page load**: Runs when DOM is ready
2. **Fetches templates**: Gets header.html and footer.html via fetch API
3. **Injects content**: Inserts the content into placeholder divs
4. **Sets active nav**: Automatically highlights the current page in navigation

### File Structure for New Pages

When creating new pages, include these elements:

```html
<head>
    <link href="styles.css" rel="stylesheet">
    <script src="includes.js"></script>
</head>
<body>
    <div class="site-container">
        <div id="header-placeholder"></div>
        <main>
            <!-- Your page content here -->
        </main>
        <div id="footer-placeholder"></div>
    </div>
</body>
```

---

Last Updated: January 2026
