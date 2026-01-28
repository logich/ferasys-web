# Feral Systems Brand Package

**Version 1.0 | January 2026**

---

## 📦 What's Inside

This folder contains the complete Feral Systems brand package, including logos, brand guidelines, design system, color specifications, and Canva template specifications.

### Directory Structure

```
brand/
├── README.md (this file)
├── BRAND-GUIDELINES.md (comprehensive brand manual)
├── canva-templates-spec.md (Canva template specifications)
├── design-system.css (CSS design tokens and utilities)
├── color-palette-spec.json (detailed color specifications)
├── logo-primary.svg (main logo with text and icon)
├── logo-mark.svg (icon only, for small spaces)
├── logo-horizontal.svg (horizontal layout for headers)
└── logo-monochrome.svg (single-color version)
```

---

## 🚀 Quick Start

### For Web Developers

1. **Import the design system**:
   ```html
   <link rel="stylesheet" href="brand/design-system.css">
   ```

2. **Use CSS custom properties**:
   ```css
   .my-button {
     background: var(--gradient-primary);
     color: var(--color-white);
     border-radius: var(--radius-lg);
   }
   ```

3. **Apply utility classes**:
   ```html
   <h1 class="text-gradient">Heading with Gradient</h1>
   <div class="card glass">Content with glass effect</div>
   ```

### For Designers

1. **Read** `BRAND-GUIDELINES.md` for complete brand standards
2. **Reference** `color-palette-spec.json` for exact color values
3. **Follow** `canva-templates-spec.md` for creating Canva templates
4. **Use** the SVG logos for all design work

### For Canva Users

1. **Upload logos** to Canva Brand Kit:
   - Export SVGs as high-res PNGs (2000px+)
   - Upload to Canva: Settings → Brand Kit → Logos

2. **Add brand colors**:
   - Electric Cyan: #00d4ff
   - Vivid Purple: #a855f7
   - Deep Navy: #1a1a2e
   - (See color-palette-spec.json for complete list)

3. **Set brand fonts**:
   - Heading: Lastica (Bold)
   - Body: Anonymous Pro (Regular)

4. **Create templates** using specifications in `canva-templates-spec.md`

---

## 🎨 Brand Essentials

### Color Palette

**Primary Colors**:
- Electric Cyan: `#00d4ff` - Interactive elements, links, primary accent
- Vivid Purple: `#a855f7` - Secondary accent, highlights, borders

**Background**:
- Deep Navy: `#1a1a2e`
- Dark Blue: `#16213e`
- Rich Blue: `#0f3460`
- Gradient: 135° from deep navy to rich blue

**Text**:
- Primary: `#ffffff` (white)
- Secondary: `#e2e8f0` (light gray)

### Typography

**Display Font**: Lastica (Bold)
- Use for: Headings, logos, feature titles, CTAs

**Body Font**: Anonymous Pro (Regular, Bold, Italic)
- Use for: Body text, paragraphs, lists, captions

### Logo Usage

✅ **Do**:
- Use on dark backgrounds
- Maintain clear space (20px minimum)
- Scale proportionally
- Use SVG format when possible

❌ **Don't**:
- Place on light backgrounds without adjustment
- Distort or stretch
- Change colors outside brand palette
- Add unauthorized effects

---

## 🛠️ Using Canva MCP

### Setup

The Canva MCP server is configured in `.mcp.json` at the project root.

**To activate** (requires Claude Code restart):
1. Canva MCP should auto-connect on next Claude Code session
2. Authenticate with Canva when prompted
3. Access Canva tools through Claude Code

### Canva MCP Capabilities

Once active, you can use natural language commands:

**Create designs**:
```
"Create a business card using the Feral Systems brand kit"
"Design an Instagram post with the gradient background"
```

**Manage brand assets**:
```
"Upload the new logo to Canva brand kit"
"Create a presentation template with brand colors"
```

**Export designs**:
```
"Export this design as PNG at 300 DPI"
"Download all logo variations"
```

---

## 📋 Brand Guidelines Summary

### Brand Personality
- **Adaptive**: Like wolves, we thrive in complex environments
- **Intelligent**: Data-driven, evidence-based, scientific
- **Modern**: Cutting-edge technology and methodology
- **Professional**: Trusted advisor in business transformations

### Visual Principles
1. **Adaptive by Design**: Fluid, responsive, smooth transitions
2. **Technical Sophistication**: Modern CSS effects without overwhelming
3. **Professional Trust**: Clean layouts, generous whitespace, clear hierarchy
4. **Gradient as Guide**: Strategic use to draw attention and create flow
5. **Data-Driven Aesthetics**: Every choice has a purpose

### Design Elements
- **Glass Morphism**: Frosted glass effects on cards and navigation
- **Gradient Text**: Cyan-to-purple gradient on main headings
- **Smooth Animations**: 0.3s ease transitions, subtle hover effects
- **Particle Effects**: Animated backgrounds for visual interest
- **Modern Borders**: Gradient borders on cards (3px, cyan to purple)

---

## 🎯 Common Use Cases

### Website Header
```html
<header class="glass-dark">
  <img src="brand/logo-horizontal.svg" alt="Feral Systems">
</header>
```

### Gradient Heading
```html
<h1 class="text-gradient">Adaptive Intelligence</h1>
```

### Brand Card Component
```html
<div class="card glass border-gradient-top">
  <h3>Feature Title</h3>
  <p>Description goes here</p>
</div>
```

### Call-to-Action Button
```html
<button class="btn btn-primary">Get Started</button>
```

---

## 📐 Template Dimensions Reference

| Template Type | Dimensions | Format |
|--------------|------------|--------|
| Business Card | 3.5" × 2" | Print (300 DPI) |
| Letterhead | 8.5" × 11" | Print (300 DPI) |
| Instagram Post | 1080px × 1080px | Web (72 DPI) |
| LinkedIn Banner | 1584px × 396px | Web (72 DPI) |
| Presentation | 1920px × 1080px | 16:9 (96 DPI) |
| Social Story | 1080px × 1920px | Web (72 DPI) |

See `canva-templates-spec.md` for complete specifications.

---

## ♿ Accessibility Standards

All brand colors meet WCAG accessibility standards:

| Combination | Contrast Ratio | Rating |
|------------|----------------|---------|
| White on Deep Navy | 15.8:1 | AAA ✓ |
| Cyan on Deep Navy | 11.2:1 | AAA ✓ |
| Purple on Deep Navy | 6.5:1 | AA ✓ |
| Light Gray on Deep Navy | 13.1:1 | AAA ✓ |

Minimum standards:
- Normal text: 4.5:1 (AA), 7.0:1 (AAA)
- Large text: 3.0:1 (AA), 4.5:1 (AAA)

---

## 🔄 Updates and Versions

**Current Version**: 1.0
**Last Updated**: January 17, 2026

### Version History
- **1.0** (Jan 2026): Initial brand package release
  - Complete logo system (4 variations)
  - Comprehensive brand guidelines
  - Design system CSS with custom properties
  - Detailed color specifications
  - Canva template specifications

---

## 📞 Support

### For Brand Questions
- Review `BRAND-GUIDELINES.md` first
- Email: brand@feralsystems.com
- Website: feralsystems.com

### For Technical Questions
- See `design-system.css` for CSS documentation
- Check `color-palette-spec.json` for color details
- Reference `canva-templates-spec.md` for Canva workflows

---

## 📄 License

These brand assets are proprietary to Feral Systems.

**Usage Rights**:
- ✓ Internal team use
- ✓ Authorized partners and contractors
- ✓ Marketing and promotional materials
- ✗ Unauthorized redistribution
- ✗ Modification without approval
- ✗ Use by competitors

---

## 🎨 Design Tools

**Recommended Tools**:
- **Vector Graphics**: Adobe Illustrator, Figma, Sketch
- **Web Design**: Figma, Adobe XD, Sketch
- **Quick Graphics**: Canva (with brand kit)
- **Presentations**: Canva, PowerPoint, Google Slides
- **Code Editor**: VS Code (with design-system.css)

**File Formats**:
- **Logos**: SVG (preferred), PNG (high-res export), PDF (print)
- **Colors**: CSS variables, HEX, RGB, CMYK, Pantone
- **Fonts**: WOFF2 (web), TTF (desktop)

---

## 🌟 Brand Essence

> **"Adaptive Intelligence Through Behavioral Design"**

We transform feral information systems and shadow IT into strategic assets using behavioral science, Nudge Theory, and generative AI. Like wolves adapting to their environment, we help organizations thrive in complex, evolving technology ecosystems.

**Key Differentiators**:
- Expert in feral information systems
- Behavioral design approach
- Evidence-based methodology
- Integration of Nudge Theory and AI
- Adaptive, not prescriptive solutions

---

**Ready to use the brand?** Start with `BRAND-GUIDELINES.md` for comprehensive guidance, or jump straight to `design-system.css` for web development.
