# Using Canva MCP with Feral Systems Brand

**Quick Start Guide for Canva MCP Integration**

---

## 🚀 Getting Started

### MCP Configuration Status

✅ Canva MCP server is configured in `.mcp.json`
⏳ Requires Claude Code restart to activate

### Configuration Details

```json
{
  "mcpServers": {
    "canva": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@canva/cli@latest", "mcp"]
    }
  }
}
```

---

## 🔧 Activation Steps

1. **Restart Claude Code** to load the Canva MCP server
2. **Authenticate** when prompted (browser OAuth flow will open)
3. **Select your Canva team** and grant permissions
4. **Start using Canva tools** via natural language commands

---

## 🎨 Setting Up Your Canva Brand Kit

### Step 1: Upload Logos

Upload these logo files to your Canva Brand Kit:

**Export SVGs to PNG first** (high resolution for best quality):
```bash
# You can export SVGs to PNG using any tool, or upload SVGs directly if Canva supports it
```

**Files to upload**:
- `brand/logo-primary.svg` → Primary logo (use for presentations, featured content)
- `brand/logo-mark.svg` → Logo mark/icon (use for avatars, small spaces)
- `brand/logo-horizontal.svg` → Horizontal logo (use for headers, email signatures)
- `brand/logo-monochrome.svg` → Monochrome version (use for single-color printing)

### Step 2: Add Brand Colors

Add these exact colors to your Canva Brand Kit palette:

| Color Name | Hex Code | Usage |
|-----------|----------|-------|
| Electric Cyan | `#00d4ff` | Primary accent, interactive elements |
| Vivid Purple | `#a855f7` | Secondary accent, highlights |
| Deep Navy | `#1a1a2e` | Background (gradient start) |
| Dark Blue | `#16213e` | Background (gradient middle) |
| Rich Blue | `#0f3460` | Background (gradient end) |
| White | `#ffffff` | Primary text |
| Light Gray | `#e2e8f0` | Secondary text |

**To add colors in Canva**:
1. Go to Brand Kit settings
2. Click "Add brand color"
3. Enter hex code
4. Name the color
5. Save

### Step 3: Configure Brand Fonts

**Primary Fonts**:
1. **Lastica** (Display font for headings)
   - Upload font files: `lastica.woff2`, `lastica-bold.woff2`
   - Or use closest Canva alternative if upload not available

2. **Anonymous Pro** (Body font)
   - Available in Canva's font library
   - Or upload: `anonymous-pro-*.woff2` files

**Font Pairing**:
- **Headings**: Lastica Bold
- **Body**: Anonymous Pro Regular
- **Emphasis**: Anonymous Pro Bold or Italic

---

## 💬 Canva MCP Commands

Once Canva MCP is active, you can use natural language commands:

### Creating Designs

```
"Create a business card design for Feral Systems"
"Design an Instagram post with the brand gradient background"
"Make a LinkedIn banner using the horizontal logo"
"Create a presentation title slide with the primary logo"
```

### Using Brand Assets

```
"Apply the Feral Systems brand kit to this design"
"Add the logo mark to the top left corner"
"Use the brand colors #00d4ff and #a855f7 in this design"
"Add a gradient background from cyan to purple at 45 degrees"
```

### Modifying Designs

```
"Change the heading font to Lastica Bold"
"Make the headline text gradient from cyan to purple"
"Add a glass morphism effect to this card"
"Update the color scheme to match the brand guidelines"
```

### Exporting Designs

```
"Export this design as PNG at 300 DPI for print"
"Download this template as PDF"
"Export all logo variations"
"Save this as a reusable template"
```

---

## 📋 Common Design Tasks

### Business Cards

**Command**:
```
"Create a business card (3.5" × 2") with:
- Front: Logo mark top center, name in Lastica Bold with gradient, title in Anonymous Pro, contact info
- Back: Horizontal logo, tagline, website
- Background: Gradient from #1a1a2e to #0f3460 at 135 degrees"
```

### Social Media Post (Instagram)

**Command**:
```
"Create a 1080x1080px Instagram post with:
- Gradient background (135deg, #1a1a2e to #0f3460)
- Logo mark at top (200px)
- Headline in Lastica Bold (72pt) with cyan-to-purple gradient
- Supporting text in Anonymous Pro (36pt) white"
```

### Presentation Template

**Command**:
```
"Create a 1920x1080px presentation template with:
- Title slide: Primary logo centered, title in gradient text
- Content slides: Logo mark top left, title in Lastica Bold with gradient underline
- Gradient background throughout"
```

### LinkedIn Banner

**Command**:
```
"Create a 1584x396px LinkedIn banner with:
- Logo mark on left
- Company name 'FERAL SYSTEMS' in Lastica Bold with gradient
- Tagline 'Adaptive Intelligence Through Behavioral Design'
- Background gradient"
```

---

## 🎯 Brand Templates to Create

### Priority Templates

1. **Business Cards** (Front & Back)
2. **Letterhead** (8.5" × 11")
3. **Email Signature** (600px × 200px)
4. **Social Media Posts**:
   - Instagram Post (1080×1080px)
   - LinkedIn Post (1200×627px)
   - Twitter/X Post (1200×675px)
5. **Social Media Covers**:
   - LinkedIn Banner (1584×396px)
   - Twitter/X Header (1500×500px)
6. **Presentation** (16:9 format)
   - Title slide
   - Section slide
   - Content slide
   - Thank you slide

### Secondary Templates

7. **Instagram Story** (1080×1920px)
8. **Facebook Post** (1200×630px)
9. **Marketing One-Pager** (8.5" × 11")
10. **Flyer** (8.5" × 11")

See `canva-templates-spec.md` for detailed specifications of each template.

---

## 🎨 Design Best Practices

### Always Include

✅ Brand gradient background or solid dark background
✅ Logo (appropriate version for space)
✅ Brand colors (cyan and/or purple accents)
✅ Lastica for headings, Anonymous Pro for body
✅ Adequate white space
✅ Gradient text on main headlines

### Avoid

❌ Light backgrounds (brand is dark-themed)
❌ Colors outside the brand palette
❌ Non-brand fonts for headings
❌ Cluttered layouts
❌ Low contrast text (check accessibility)
❌ Stretching or distorting logos

---

## ✨ Advanced Techniques

### Creating Gradients in Canva

1. Use rectangle element
2. Fill with color (#00d4ff)
3. Apply gradient effect
4. Add second color (#a855f7)
5. Adjust angle (45° or 135°)

### Glass Morphism Effect

1. Create rectangle shape
2. Set fill to white at 8% opacity
3. Add blur effect (10-15)
4. Add subtle border (white at 10% opacity)

### Text Gradients

1. Create text element
2. Select text
3. Apply gradient fill
4. Use cyan (#00d4ff) to purple (#a855f7)
5. Angle at 45° for consistency

---

## 🔍 Quality Checklist

Before finalizing any Canva design:

- [ ] Brand colors used correctly (check hex codes)
- [ ] Proper fonts applied (Lastica headings, Anonymous Pro body)
- [ ] Logo has clear space around it
- [ ] Text is readable (minimum 16px for body, adequate contrast)
- [ ] Gradients at correct angles (45° or 135°)
- [ ] Design matches template specifications
- [ ] Exported at correct resolution (300 DPI print, 72 DPI web)
- [ ] File naming follows convention: `ferasys-[type]-[variant]-[date]`

---

## 📁 File Naming Convention

Use consistent naming for exported files:

**Format**: `ferasys-[type]-[variant]-[date].[ext]`

**Examples**:
- `ferasys-business-card-front-2026-01.pdf`
- `ferasys-instagram-post-announcement-2026-01-17.png`
- `ferasys-presentation-template-2026-01.pptx`
- `ferasys-linkedin-banner-2026-01.png`

---

## 📊 Export Settings Reference

### For Print
- **Format**: PDF (preferred) or PNG
- **Resolution**: 300 DPI
- **Color Mode**: CMYK (if available)
- **Bleed**: Include 0.125" bleed for professional printing

### For Web/Social
- **Format**: PNG (with transparency) or JPG (with solid backgrounds)
- **Resolution**: 72 DPI or platform-optimized
- **Color Mode**: RGB
- **Compression**: High quality (90%+)

### For Presentations
- **Format**: PPTX or PDF
- **Resolution**: 96 DPI
- **Aspect Ratio**: 16:9

---

## 🆘 Troubleshooting

### Canva MCP Not Working?

1. **Check MCP server is running**:
   ```bash
   # Restart Claude Code to reload MCP servers
   ```

2. **Verify authentication**:
   - Check if OAuth flow completed
   - Try re-authenticating if needed

3. **Check Canva account**:
   - Ensure you have a Canva account
   - Verify team permissions
   - Check API access is enabled

### Fonts Not Available?

- **Upload custom fonts** to Canva if Lastica isn't available
- **Use Canva alternatives**:
  - Lastica alternative: Montserrat Bold, Poppins Bold, or similar geometric sans
  - Anonymous Pro alternative: Roboto Mono, Source Code Pro, or similar monospace

### Colors Look Different?

- **Check color profile**: Ensure using RGB for web, CMYK for print
- **Verify hex codes**: Double-check colors match exactly
- **Monitor calibration**: Colors may appear different on various screens

---

## 🔗 Resources

### Brand Assets
- **Guidelines**: `brand/BRAND-GUIDELINES.md`
- **Design System**: `brand/design-system.css`
- **Color Specs**: `brand/color-palette-spec.json`
- **Template Specs**: `brand/canva-templates-spec.md`

### Canva Resources
- **Canva MCP Documentation**: https://www.canva.dev/docs/connect/mcp-server/
- **Brand Kit Guide**: https://www.canva.com/help/brand-kit/
- **Design School**: https://www.canva.com/learn/

### External Documentation
- [Canva Connect APIs](https://www.canva.dev/docs/connect/)
- [MCP Server Documentation](https://code.claude.com/docs/en/mcp)
- [PulseMCP - Canva Server](https://www.pulsemcp.com/servers/canva)

---

## 📈 Next Steps

1. **Restart Claude Code** to activate Canva MCP
2. **Authenticate** with your Canva account
3. **Set up Brand Kit** with logos, colors, and fonts
4. **Create templates** using the specifications provided
5. **Share templates** with your team
6. **Start designing** with AI assistance!

---

**Need Help?**
- **Brand Questions**: See `BRAND-GUIDELINES.md`
- **Technical Issues**: Check `.mcp.json` configuration
- **Design Support**: Reference `canva-templates-spec.md`

**Last Updated**: January 17, 2026
**Version**: 1.0

---

**Sources**:
- [Dev MCP server - Canva Connect APIs Documentation](https://www.canva.dev/docs/connect/mcp-server/)
- [Official Canva MCP Server | PulseMCP](https://www.pulsemcp.com/servers/canva)
- [Beyond the Prompt: A Deep Dive into the Official Canva MCP Server](https://skywork.ai/skypage/en/canva-mcp-server-dive/1977622752264253440)
- [Introducing the Canva Dev MCP Server - Canva Developers Blog](https://www.canva.dev/blog/developers/canva-dev-mcp-server/)
