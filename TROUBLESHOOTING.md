# Troubleshooting Guide - Feral Systems Website

Common issues and solutions for deploying the Feral Systems website.

## 🚨 Access Denied Errors for Preview URLs

### Symptoms
- Preview URLs return "Access Denied" or 403 errors
- Production works fine but preview paths don't
- Files exist in S3 but can't be accessed via browser

### Root Causes
1. Files uploaded without public-read ACL
2. S3 bucket doesn't have public access enabled
3. S3 bucket policy doesn't allow public read
4. "Block Public Access" is enabled on bucket

### Solution 1: Fix GitHub Actions Workflow (✅ FIXED)

The workflow has been updated to add `--acl public-read` to all S3 uploads.

**What changed:**
```bash
# Before (doesn't work)
aws s3 cp index.html s3://bucket/preview/branch/index.html

# After (works)
aws s3 cp index.html s3://bucket/preview/branch/index.html --acl public-read
```

**Action:** Push the updated workflow and re-run the deployment.

---

### Solution 2: Update S3 Bucket Policy

**Check current bucket policy:**
```bash
aws s3api get-bucket-policy --bucket YOUR-BUCKET-NAME
```

**Apply the policy from `s3-bucket-policy-preview.json`:**

1. Replace `YOUR-BUCKET-NAME` with your actual bucket name
2. Apply the policy:

```bash
aws s3api put-bucket-policy \
    --bucket YOUR-BUCKET-NAME \
    --policy file://s3-bucket-policy-preview.json
```

Or via AWS Console:
1. Go to S3 → Your Bucket → Permissions → Bucket Policy
2. Copy content from `s3-bucket-policy-preview.json`
3. Replace `YOUR-BUCKET-NAME` with actual name
4. Click Save

---

### Solution 3: Disable "Block Public Access"

**Check block public access settings:**
```bash
aws s3api get-public-access-block --bucket YOUR-BUCKET-NAME
```

**Disable if needed (for static website hosting):**
```bash
aws s3api delete-public-access-block --bucket YOUR-BUCKET-NAME
```

Or via AWS Console:
1. Go to S3 → Your Bucket → Permissions
2. Click "Edit" under "Block public access (bucket settings)"
3. Uncheck all boxes
4. Click Save changes

⚠️ **Security Note:** Only disable this for buckets that serve public websites.

---

### Solution 4: Fix Existing Files (Manual)

If you already have files uploaded without public-read ACL:

**Option A: Re-run GitHub Actions**
- Push a commit to trigger re-deployment
- Updated workflow will fix permissions

**Option B: Fix manually via AWS CLI**
```bash
# Fix all files in preview path
aws s3 cp \
    s3://YOUR-BUCKET-NAME/preview/ \
    s3://YOUR-BUCKET-NAME/preview/ \
    --recursive \
    --acl public-read \
    --metadata-directive COPY
```

**Option C: Fix via AWS Console**
1. Go to S3 → Your Bucket → preview folder
2. Select all files
3. Actions → Change object ACL
4. Grant "Read" permission to "Everyone (public access)"
5. Save

---

### Verification

**Test if files are publicly accessible:**
```bash
# Check file ACL
aws s3api get-object-acl \
    --bucket YOUR-BUCKET-NAME \
    --key preview/branch-name/index.html

# Should see "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
```

**Test via browser:**
```bash
# Direct S3 URL (should work)
https://YOUR-BUCKET-NAME.s3.amazonaws.com/preview/branch-name/index.html

# CloudFront URL (should also work)
https://ferasys.com/preview/branch-name/index.html
```

---

## 🌐 CloudFront Issues

### Issue: CloudFront returns 404 for preview paths

**Cause:** CloudFront origin settings don't support subdirectories

**Solution:**
1. Go to CloudFront → Your Distribution → Origins
2. Edit the S3 origin
3. Set "Origin Path" to empty (blank)
4. Ensure "Origin Domain" points to S3 website endpoint, not REST API endpoint
   - ✅ Good: `bucket-name.s3-website-us-east-1.amazonaws.com`
   - ❌ Bad: `bucket-name.s3.amazonaws.com`

---

### Issue: CloudFront cache shows old content

**Solution: Invalidate CloudFront cache**
```bash
# Invalidate specific preview path
aws cloudfront create-invalidation \
    --distribution-id YOUR-DISTRIBUTION-ID \
    --paths "/preview/branch-name/*"

# Or invalidate all previews
aws cloudfront create-invalidation \
    --distribution-id YOUR-DISTRIBUTION-ID \
    --paths "/preview/*"
```

---

## 🔒 IAM Permission Issues

### Issue: GitHub Actions fails to upload

**Error:** `Access Denied` or `Forbidden` during deployment

**Solution: Update IAM policy**

Ensure your IAM user/role has these permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl",
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME"
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudfront:CreateInvalidation",
        "cloudfront:GetInvalidation"
      ],
      "Resource": "arn:aws:cloudfront::ACCOUNT-ID:distribution/*"
    }
  ]
}
```

**Note:** `s3:PutObjectAcl` is required for `--acl public-read` flag.

---

## 📦 Compression Issues

### Issue: Files not compressed or wrong content-encoding

**Check file metadata:**
```bash
aws s3api head-object \
    --bucket YOUR-BUCKET-NAME \
    --key preview/branch-name/index.html

# Should show "ContentEncoding": "gzip"
```

**Fix if wrong:**
Re-upload with correct headers (GitHub Actions does this automatically now)

---

### Issue: Browser doesn't decompress files

**Symptoms:**
- Downloading gibberish or `.gz` files
- Content appears as binary

**Cause:** Content-Encoding header not set or wrong Content-Type

**Solution:**
Ensure upload includes both:
```bash
--content-type "text/html; charset=utf-8" \
--content-encoding "gzip"
```

The updated workflow includes these headers automatically.

---

## 🔍 Debugging Commands

### Check if file exists in S3
```bash
aws s3 ls s3://YOUR-BUCKET-NAME/preview/branch-name/
```

### Check file permissions
```bash
aws s3api get-object-acl \
    --bucket YOUR-BUCKET-NAME \
    --key preview/branch-name/index.html
```

### Check file metadata
```bash
aws s3api head-object \
    --bucket YOUR-BUCKET-NAME \
    --key preview/branch-name/index.html
```

### Test direct S3 access
```bash
curl -I https://YOUR-BUCKET-NAME.s3.amazonaws.com/preview/branch-name/index.html
```

### Test CloudFront access
```bash
curl -I https://ferasys.com/preview/branch-name/index.html
```

---

## 🚑 Emergency Fixes

### Quick Fix: Make everything public
```bash
# Make all files in bucket public (use with caution)
aws s3 cp s3://YOUR-BUCKET-NAME/ s3://YOUR-BUCKET-NAME/ \
    --recursive \
    --acl public-read \
    --metadata-directive COPY
```

### Quick Fix: Force re-upload via Actions
```bash
# Push empty commit to trigger re-deployment
git commit --allow-empty -m "Force re-deployment"
git push
```

---

## 📞 Getting Help

### Check GitHub Actions Logs
1. Go to GitHub → Actions
2. Click on latest workflow run
3. Expand "Sync to S3" step
4. Look for error messages

### Check AWS CloudWatch Logs
```bash
# For CloudFront
aws logs tail /aws/cloudfront/YOUR-DISTRIBUTION --follow

# For S3 (if logging enabled)
aws s3 ls s3://YOUR-LOG-BUCKET/
```

### Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `Access Denied` | No public read permission | Add `--acl public-read` |
| `NoSuchKey` | File doesn't exist | Check upload path |
| `403 Forbidden` | Bucket policy blocks public | Update bucket policy |
| `InvalidObjectState` | Wrong storage class | Use STANDARD class |
| `SlowDown` | Too many requests | Add retry logic |

---

## ✅ Verification Checklist

After applying fixes, verify:

- [ ] GitHub Actions workflow completes successfully
- [ ] Files visible in S3 console under preview/ path
- [ ] Files show "Public" in S3 console permissions column
- [ ] Direct S3 URL works in browser
- [ ] CloudFront URL works in browser
- [ ] Files are compressed (check network tab, size < 50% of original)
- [ ] Correct content-type headers (text/html, text/css, image/png)
- [ ] Cache-control headers set correctly

---

## 🔄 Testing New Deployments

**Test preview deployment:**
1. Create a test commit on your branch
2. Push to trigger GitHub Actions
3. Wait for deployment to complete
4. Check Actions log for success message
5. Visit preview URL: `https://ferasys.com/preview/YOUR-BRANCH/index.html`
6. Verify content loads correctly
7. Check browser dev tools network tab for compression

**If issues persist:**
1. Check all solutions above
2. Review GitHub Actions logs
3. Verify AWS credentials have correct permissions
4. Test with AWS CLI manually
5. Contact AWS Support if needed

---

**Last Updated:** January 2026
**Maintained By:** Feral Systems Team
