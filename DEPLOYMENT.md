# Deployment Guide - Feral Systems Website

Comprehensive guide for deploying the Feral Systems website with all optimizations.

## 🚀 Deployment Overview

The website uses a multi-environment deployment strategy:
- **Production**: Main branch → CloudFront + S3
- **Preview**: Feature branches (claude/**) → S3 preview paths
- **Staging**: Staging/develop branches → Staging environment
- **Pull Requests**: Automatic preview deployments with PR comments

## 📦 Optimization Features

### File Compression
- **Gzip**: 70-80% size reduction for HTML/CSS
- **Brotli**: Even better compression (80-85% reduction)
- **Automatic**: GitHub Actions handles all compression

### Cache Strategy
- **HTML**: 5 minutes (max-age=300) - Always fresh
- **CSS/JS**: 1 year (max-age=31536000) - Immutable with cache busting
- **Images**: 1 year (max-age=31536000) - Immutable
- **Fonts**: 1 year (max-age=31536000) - Immutable

### Security Headers
Security headers are added via CloudFront Function (see `cloudfront-security-headers.js`):
- `Strict-Transport-Security`: Force HTTPS
- `Content-Security-Policy`: Prevent XSS attacks
- `X-Frame-Options`: Prevent clickjacking
- `X-Content-Type-Options`: Prevent MIME sniffing
- `Referrer-Policy`: Control referrer information
- `Permissions-Policy`: Disable unnecessary features

## 🌍 Environments

### Production
- **Branch**: `main`
- **URL**: https://ferasys.com
- **Trigger**: Push to main branch
- **Features**:
  - Full compression (gzip + brotli)
  - CloudFront invalidation
  - Security headers
  - CDN caching

### Preview (Feature Branches)
- **Branches**: `claude/**`
- **URL**: https://ferasys.com/preview/{branch-name}/index.html
- **Trigger**: Push to claude/** branches
- **Features**:
  - Same optimizations as production
  - Isolated preview environments
  - No CloudFront invalidation (saves cost)
  - Automatic PR comments with preview URLs

### Staging
- **Branch**: `staging` or `develop`
- **URL**: Configured via STAGING_DOMAIN secret
- **Trigger**: Push to staging/develop or manual dispatch
- **Features**:
  - Testing ground before production
  - Smoke tests included
  - Optional separate CloudFront distribution

## 🔧 GitHub Secrets Configuration

Configure these secrets in your GitHub repository settings:

### Required Secrets
```
AWS_ACCESS_KEY_ID          # AWS access key with S3 + CloudFront permissions
AWS_SECRET_ACCESS_KEY      # AWS secret key
S3_BUCKET                  # Production S3 bucket name
CLOUDFRONT_DISTRIBUTION_ID # Production CloudFront distribution ID
```

### Optional Secrets
```
DOMAIN                            # Your domain (default: ferasys.com)
S3_BUCKET_STAGING                 # Staging S3 bucket (optional)
CLOUDFRONT_STAGING_DISTRIBUTION_ID # Staging CloudFront ID (optional)
STAGING_DOMAIN                    # Staging domain (optional)
```

## 📝 Deployment Workflows

### 1. Production Deployment

**Automatic** (when you push to main):
```bash
git checkout main
git pull origin main
git merge your-feature-branch
git push origin main
# GitHub Actions automatically deploys
```

**What happens:**
1. Code is checked out
2. Files are compressed (gzip + brotli)
3. Uploaded to S3 with optimized headers
4. CloudFront cache invalidated (targeted paths only)
5. Website is live in ~5 minutes

### 2. Preview Deployment

**Automatic** (when you push to claude/** branches):
```bash
git checkout -b claude/your-feature-name
# Make your changes
git commit -m "Your changes"
git push -u origin claude/your-feature-name
# GitHub Actions automatically creates preview
```

**What happens:**
1. Preview URL created at `/preview/claude-your-feature-name/`
2. All optimizations applied
3. If PR exists, comment added with preview URL

### 3. Staging Deployment

**Automatic** (push to staging):
```bash
git checkout staging
git merge your-feature-branch
git push origin staging
```

**Manual** (deploy any branch to staging):
```bash
# Go to GitHub Actions → "Deploy to Staging Environment" → Run workflow
# Select your branch
```

### 4. Pull Request Previews

**Automatic** when you create a PR:
1. Create PR against main branch
2. GitHub Actions deploys preview
3. Bot comments on PR with preview URL
4. Preview updates with every commit

## 🛠️ CloudFront Function Setup

### Initial Setup (One-time)

1. **Create CloudFront Function:**
   ```bash
   # Go to AWS Console → CloudFront → Functions
   # Click "Create function"
   # Name: ferasys-security-headers
   # Copy code from cloudfront-security-headers.js
   ```

2. **Publish Function:**
   ```bash
   # In function editor, click "Publish"
   ```

3. **Associate with Distribution:**
   ```bash
   # Go to your CloudFront distribution
   # Edit behavior
   # Associate function with "Viewer Response" event
   # Choose: ferasys-security-headers
   # Save
   ```

4. **Test Headers:**
   ```bash
   curl -I https://ferasys.com
   # Should see all security headers
   ```

## 📊 Performance Optimization

### File Size Comparison

| File | Original | Gzip | Brotli | Savings |
|------|----------|------|--------|---------|
| index.html | ~35 KB | ~8 KB | ~6 KB | 83% |
| styles.css | ~25 KB | ~6 KB | ~5 KB | 80% |
| **Total** | **60 KB** | **14 KB** | **11 KB** | **82%** |

### CloudFront Invalidation Optimization

**Old approach** (expensive):
```bash
--paths "/*"  # Invalidates everything, costs more
```

**New approach** (efficient):
```bash
--paths "/index.html" "/index.html.br" "/styles.css" "/styles.css.br"
# Only invalidates changed files, saves cost
```

**Cost savings**: $0.005 per invalidation × 2 files = **$0.01** (vs $0.05+ for `/*`)

## 🧪 Testing Deployments

### Local Testing

```bash
# Install dependencies (optional - for minification)
npm install

# Test compression locally
gzip -9 -k index.html styles.css
ls -lh *.gz

# Clean up
npm run clean
```

### Test Preview URL
```bash
# After deployment, test preview
curl -I https://ferasys.com/preview/your-branch/index.html

# Should return 200 OK with compression headers
```

### Lighthouse Performance Testing
```bash
# Install globally
npm install -g lighthouse

# Run performance test
lighthouse https://ferasys.com --view

# Expected scores:
# Performance: 95+
# Accessibility: 90+
# Best Practices: 95+
# SEO: 100
```

## 🐛 Troubleshooting

### Preview URLs Not Working
- Check S3 bucket permissions (must allow public read)
- Verify CloudFront origin path configuration
- Ensure branch name doesn't have special characters

### CloudFront Invalidation Fails
- Verify `CLOUDFRONT_DISTRIBUTION_ID` secret is correct
- Check IAM permissions include `cloudfront:CreateInvalidation`
- Wait a few minutes - CloudFront can be slow

### Compression Not Applied
- Check S3 file metadata (`Content-Encoding` should be `gzip` or `br`)
- Verify CloudFront is configured to forward `Accept-Encoding` header
- Test with: `curl -H "Accept-Encoding: gzip" https://ferasys.com`

### Security Headers Missing
- Ensure CloudFront Function is published
- Verify function is associated with "Viewer Response" event
- Check function code for errors in CloudFront console

## 📈 Monitoring & Metrics

### CloudWatch Metrics to Monitor
- **CloudFront Requests**: Total traffic
- **4xx/5xx Errors**: Error rates
- **Cache Hit Ratio**: Should be >90%
- **Origin Latency**: S3 response times

### Cost Monitoring
- **S3 Storage**: ~$0.023/GB/month
- **CloudFront Data Transfer**: ~$0.085/GB (first 10 TB)
- **CloudFront Requests**: ~$0.0075 per 10,000 requests
- **Invalidations**: $0.005 per path (first 1,000 free/month)

**Monthly estimate** (1,000 visitors, 100 MB total):
- S3: $0.50
- CloudFront: $8.50
- **Total: ~$9/month**

## 🔒 Security Best Practices

1. **IAM Permissions**: Use least-privilege IAM policies
2. **Secrets Rotation**: Rotate AWS credentials every 90 days
3. **Branch Protection**: Enable branch protection on `main`
4. **Signed URLs**: Consider CloudFront signed URLs for sensitive content
5. **WAF**: Consider AWS WAF for additional security

## 🚦 Deployment Checklist

Before deploying to production:

- [ ] All tests pass locally
- [ ] Content reviewed for accuracy
- [ ] Images optimized
- [ ] No sensitive data in code
- [ ] Tested on preview environment
- [ ] Security headers verified
- [ ] Lighthouse score > 90
- [ ] CloudFront invalidation working
- [ ] Backup of current production exists

## 📚 Additional Resources

- [AWS S3 Static Website Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Web Performance Best Practices](https://web.dev/performance/)

## 🆘 Support

For deployment issues:
1. Check GitHub Actions logs
2. Review CloudWatch logs
3. Test locally with same configuration
4. Contact AWS support for infrastructure issues

---

**Last Updated**: January 2026
**Maintained By**: Feral Systems Team
