# Peach State Intertie Website

**A modern, easy-to-maintain website for the Peach State Emergency Intertie System**

Last Updated: January 2026

---

## 📁 Website Files

This website consists of simple HTML and CSS files:

- `index.html` - Homepage
- `repeaters.html` - Detailed repeater information
- `nets.html` - Net schedules and information
- `skywarn.html` - Skywarn information
- `diagram.html` - Diagrams and maps
- `blog.html` - Blog/news page
- `styles.css` - The stylesheet that controls the look of ALL pages
- `images/` - Folder containing all website images

---

## 🎨 How to Change Colors

All website colors are defined at the **top of styles.css** (lines 16-25).

To change a color, just edit the value after the colon:

```css
:root {
    --primary-blue: #1e5a8e;     /* Main blue color */
    --light-blue: #73aad5;       /* Light blue accents */
    --dark-gray: #333;           /* Dark gray for text */
    --red-accent: #e74c3c;       /* Red for OFFLINE status */
    --green-accent: #27ae60;     /* Green for ONLINE status */
}
```

**Example:** To make the main blue darker, change `#1e5a8e` to `#0d2f4a`

---

## ✏️ How to Update Content

### Changing Text on a Page

1. Open the HTML file (like `index.html`) in a text editor
2. Find the text you want to change
3. Edit it between the `>` and `<` symbols
4. Save the file

**Example:**
```html
<p>This is some text</p>
```
Change "This is some text" to whatever you want.

### Adding a New Repeater to the Homepage

Find this section in `index.html`:

```html
<li class="repeater-item">
    <span class="repeater-name">Irwinton</span>
    <span class="repeater-frequency">147.24+ (77.0 Tone)</span>
    <span class="status online">Online</span>
</li>
```

Copy and paste it, then change:
- `Irwinton` to the new repeater name
- `147.24+ (77.0 Tone)` to the new frequency
- `online` to `offline` or `standby` to change the status color

### Changing a Repeater Status

Find the repeater in the HTML file and change the status:

```html
<span class="status online">Online</span>    <!-- Green -->
<span class="status offline">Offline</span>  <!-- Red -->
<span class="status standby">Standby</span>  <!-- Orange -->
```

---

## 🖼️ How to Add/Change Images

1. Put your image file in the `images/` folder
2. In the HTML file, add or change:

```html
<img src="images/your-image.jpg" alt="Description of image">
```

Replace `your-image.jpg` with your filename.

---

## 📱 Mobile Friendly

This website automatically adjusts for phones and tablets. No extra work needed!

---

## 🔍 Website Structure Explained

### Every Page Has 3 Main Parts:

1. **Header** - The blue top section with the title
2. **Navigation** - The dark menu bar with links
3. **Footer** - The bottom section with contact info

### Content Sections

Content is organized in boxes called "content-section":

```html
<div class="content-section">
    <h2>Title Here</h2>
    <p>Text here</p>
</div>
```

To add a new section, copy and paste this block!

---

## 💡 Common Tasks

### Task: Update the "Last Updated" Date

1. Open `index.html` (and other pages)
2. Find this near the bottom:

```html
<p>Established 2008 | Webpage Updated January 2026</p>
```

3. Change the date

### Task: Add a New External Link to Footer

Find this section in any HTML file:

```html
<a href="https://www.gaares.org" target="_blank">GA ARES</a> |
```

Copy it and change:
- The URL in `href=""`
- The text between `>` and `</a>`

### Task: Change Contact Email

Find this in any HTML file:

```html
<p><strong>K4DBN@PEACHSTATEINTERTIE.COM</strong> - Intertie Manager</p>
```

Change the email address.

---

## 🎨 CSS Classes You Can Use

Add these classes to any element to style it:

- `text-center` - Center the text
- `text-red` - Make text red
- `text-green` - Make text green
- `text-large` - Make text larger
- `bold` - Make text bold

**Example:**
```html
<p class="text-center bold text-red">Important Message!</p>
```

---

## 📦 Highlight Boxes

To make something stand out, wrap it in a highlight box:

```html
<div class="highlight-box">
    <p>This text will appear in a gray box with a blue border</p>
</div>
```

For important warnings:
```html
<div class="highlight-box important">
    <p>This appears in a yellow box - great for warnings!</p>
</div>
```

---

## 🆘 Help & Tips

### Tip 1: Always make a backup
Before making changes, copy the file and name it something like `index-backup.html`

### Tip 2: Test your changes
Open the HTML file in a web browser to see how it looks before publishing

### Tip 3: Keep it consistent
If you change contact info on one page, change it on all pages

### Tip 4: Comments are your friend
Lines starting with `<!--` are comments (notes to yourself). They don't show on the website:

```html
<!-- This is a reminder note that only you can see -->
```

---

## 📞 Need Help?

The website uses:
- **HTML5** - The latest version of HTML (very simple)
- **CSS3** - Modern styling (all in styles.css)
- **No JavaScript** - Keeps it simple!

Everything is well-commented. Look for lines starting with `<!--` in HTML files or `/*` in the CSS file.

---

## ✅ Checklist for Making Changes

- [ ] Open the file in a text editor
- [ ] Make your changes
- [ ] Save the file
- [ ] Open it in a web browser to check
- [ ] If it looks good, upload to your web server
- [ ] Check the live website

---

**Remember:** You can't break anything! If something goes wrong, just restore from your backup copy.

Good luck! 🎉
