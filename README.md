# Feral Systems Website

A modern, professional website for Feral Systems - Information Systems for Complex Problems.

## 🐺 Overview

This website showcases Feral Systems as an information systems consultancy that leverages **Nudge Theory** and **Generative AI** to help organizations understand, manage, and optimize "feral information systems" - the unofficial solutions that emerge when formal IT systems don't meet real-world needs. The design uses a wolf theme to convey adaptability, intelligence, and natural problem-solving instincts.

## 🎨 Design Features

- **Modern Gradient Background**: Deep blue gradient that evokes trust and professionalism
- **Wolf Branding**: Consistent use of wolf imagery and metaphors
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Smooth Animations**: Subtle animations and transitions for professional feel
- **Particle Effects**: Animated background particles for visual interest
- **Glass Morphism**: Modern frosted glass effects on cards and navigation

## 📁 File Structure

```
ferasys-web/
├── index.html              # Main website file
├── ferasys.png            # Company logo
├── wolf.jpg               # Hero section wolf image
├── wolf.webp             # Optimized wolf image
├── deploy.sh             # Deployment script for AWS
├── README.md             # This file
├── index-original-backup.html  # Backup of original site
└── FeralSystems/         # Old Canva export (can be removed)
```

## 🚀 Deployment

### Prerequisites
- AWS CLI installed and configured
- S3 bucket set up for static website hosting
- CloudFront distribution (optional but recommended)

### Quick Deployment
1. Edit `deploy.sh` and update these variables:
   ```bash
   S3_BUCKET="your-actual-bucket-name"
   CLOUDFRONT_DISTRIBUTION_ID="your-distribution-id"
   AWS_PROFILE="personal"  # or your preferred AWS profile
   ```

2. Run the deployment script:
   ```bash
   ./deploy.sh
   ```

### Manual Deployment
If you prefer to deploy manually:

```bash
# Sync to S3
aws s3 sync . s3://your-bucket-name --exclude "*.sh" --exclude "*.DS_Store"

# Invalidate CloudFront (optional)
aws cloudfront create-invalidation --distribution-id YOUR_DISTRIBUTION_ID --paths "/*"
```

## 🛠️ Customization

### Content Updates
The website content is organized in clear sections. To update:

1. **Company Information**: Edit the hero section and about section in `index.html`
2. **Services**: Modify the services grid to reflect your actual offerings
3. **Contact Information**: Update email addresses and contact methods
   - Current email: consulting@ferasys.com
   - Domain: ferasys.com
4. **Branding**: Replace `ferasys.png` with your actual logo

### Styling Changes
The CSS is embedded in the HTML file for simplicity. Key customization areas:

- **Colors**: Look for color variables like `#00d4ff` (cyan) and `#a855f7` (purple)
- **Fonts**: Currently uses system fonts, but you can add Google Fonts
- **Layout**: Grid layouts are responsive and can be easily modified

### Adding New Sections
To add new sections:

1. Add the HTML structure following the existing pattern
2. Add corresponding CSS styles
3. Update the navigation menu
4. Add smooth scrolling JavaScript if needed

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px to 1199px
- **Mobile**: Below 768px

## 🔧 Technical Features

- **SEO Optimized**: Proper meta tags, semantic HTML, and structured data
- **Performance**: Optimized images, minimal JavaScript, efficient CSS
- **Accessibility**: Proper contrast ratios, semantic markup, keyboard navigation
- **Security**: No external dependencies, minimal attack surface

## 📈 Analytics & Monitoring

Consider adding:
- Google Analytics or similar for traffic monitoring
- Contact form with backend processing
- Security headers for enhanced protection

## 🎯 Content Strategy

The website positions Feral Systems as:
- **Expert**: Specialists in feral information systems and shadow IT using advanced methodologies
- **Innovative**: Leveraging Nudge Theory and Generative AI for complex problem solving
- **Behavioral**: Understanding human psychology and decision-making in system design
- **Adaptive**: Like wolves, able to understand and work with naturally emerging systems
- **Scientific**: Evidence-based approach using behavioral economics and machine learning
- **Integrative**: Helping organizations optimize rather than eliminate valuable workaround systems

## 🔒 Version Control & Security

### Protected Files
The following files are excluded from version control for security:
- `deploy.sh` - Contains actual AWS bucket names and distribution IDs
- `.env*` - Environment variables and secrets
- `.aws/` - AWS credentials and configuration
- `*.key`, `*.pem` - Private keys and certificates

### Safe Deployment
1. Copy `deploy.sh.template` to `deploy.sh`
2. Update the configuration variables with your actual values
3. Never commit the actual `deploy.sh` file
4. Use environment variables for sensitive data when possible

### Git Best Practices
```bash
# Check what files will be committed
git status

# Add specific files only
git add index.html styles.css

# Create meaningful commit messages
git commit -m "Update hero section content and styling"

# Push to remote repository
git push origin main
```

## 🔄 Maintenance

### Regular Updates
- Keep content fresh and relevant
- Update service offerings as they evolve
- Refresh case studies and testimonials
- Monitor and fix any broken links

### Security
- Regularly update any dependencies
- Monitor for security vulnerabilities
- Keep AWS infrastructure updated
- Review and update security headers
- Rotate AWS credentials periodically

## 📞 Support

For questions about this website:
- Check the comments in `index.html` for technical details
- Review AWS documentation for hosting questions
- Consider professional web development support for major changes

## 🏆 Best Practices Implemented

- ✅ Mobile-first responsive design
- ✅ Fast loading times
- ✅ SEO-friendly structure
- ✅ Professional visual design
- ✅ Clear call-to-actions
- ✅ Consistent branding
- ✅ Accessible design patterns
- ✅ Modern web standards

---

**Feral Systems** - *Information Systems for Complex Problems*

*"In complex organizations, the most adaptive systems survive and thrive."*
