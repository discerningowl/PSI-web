# Claude Development Guide - Peach State Intertie Website

## Project Philosophy

**SIMPLICITY ABOVE ALL ELSE**

This website prioritizes simplicity and maintainability over clever solutions. Keep things straightforward and easy to understand.

## Site Structure

This is a static HTML website with no JavaScript dependencies. All pages are standalone HTML files.

### Files

- **HTML Pages**: index.html, diagram.html, repeaters.html, nets.html, skywarn.html, blog.html
- **Stylesheet**: styles.css (controls ALL styling)
- **Images**: images/ directory + PSInew.jpg
- **Templates**: header.html and footer.html (reference only - see below)
- **Deployment**: .do/ directory (DigitalOcean App Platform config)

## Header and Footer Management

### Current Implementation

Each HTML page has its header and footer **inline** (directly in the file). This is intentional for simplicity.

### Template Files

- `header.html` - Reference template for the header and navigation
- `footer.html` - Reference template for the footer

**IMPORTANT**: These are reference files only. They are NOT dynamically loaded.

### How to Update Header/Footer Across All Pages

When you need to update the header or footer on all pages:

1. Make the change in the appropriate template file (header.html or footer.html)
2. Copy the updated HTML from the template
3. Replace the corresponding section in ALL 6 HTML pages:
   - index.html
   - diagram.html
   - repeaters.html
   - nets.html
   - skywarn.html
   - blog.html

### Navigation Active State

Each page has `class="active"` on its corresponding navigation link. When updating navigation across all pages, preserve each page's active link:

- index.html: `<a href="index.html" class="active">Home</a>`
- diagram.html: `<a href="diagram.html" class="active">Diagrams</a>`
- repeaters.html: `<a href="repeaters.html" class="active">Repeaters</a>`
- nets.html: `<a href="nets.html" class="active">Nets</a>`
- skywarn.html: `<a href="skywarn.html" class="active">Skywarn</a>`
- blog.html: `<a href="blog.html" class="active">Blog</a>`

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

To update: Edit footer.html template, then copy to all 6 pages.

### Update "Last Updated" Date

Found in footer copyright section on all pages:
```html
<p>Established 2008 | Webpage Updated January 2026</p>
```

### Add/Remove Navigation Items

1. Update header.html template
2. Copy navigation to all 6 pages
3. Ensure each page's active link is correct

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

### DigitalOcean App Platform

Configuration is in `.do/` directory:
- `app.yaml` - Main deployment config
- `deploy.template.yaml` - Deployment template

**Repository**: discerningowl/PSI-web
**Domain**: peachstateintertie.com
**Auto-deploy**: Enabled on main branch

### Making Changes Live

1. Commit changes to main branch
2. Push to GitHub
3. DigitalOcean automatically deploys

## Development Principles

### DO

✓ Keep HTML simple and readable
✓ Use the template files as references
✓ Update all 6 pages when changing header/footer
✓ Test pages locally before deploying
✓ Follow existing code structure and formatting
✓ Use CSS variables for colors
✓ Keep responsive design (already implemented)

### DON'T

✗ Add JavaScript (unless absolutely necessary and approved)
✗ Over-engineer solutions
✗ Create complex build processes
✗ Add unnecessary dependencies
✗ Change the simple structure
✗ Use dynamic includes or templating

## Quick Reference

### All Pages List
1. index.html - Homepage
2. diagram.html - System diagrams
3. repeaters.html - Repeater information
4. nets.html - Net schedules
5. skywarn.html - Skywarn info
6. blog.html - Maytag's blog

### Template Update Process
1. Edit header.html or footer.html
2. Copy the updated section
3. Paste into all 6 HTML pages (preserving each page's active nav link)
4. Verify locally
5. Commit and deploy

## Notes for Future Claude Sessions

- This project values simplicity over sophistication
- Manual updates across pages is preferred over automation
- The owner wants maximum control and minimal complexity
- Header/footer are duplicated by design, not by accident
- Keep the barrier to entry LOW for future maintainers
- Anyone with basic HTML knowledge should be able to update this site

---

Last Updated: January 2026
