/**
 * CloudFront Function: Security Headers
 *
 * This function adds security headers to all responses from the CloudFront distribution.
 * It should be associated with the "Viewer Response" event in CloudFront.
 *
 * To deploy this function:
 * 1. Go to AWS CloudFront Console
 * 2. Navigate to Functions
 * 3. Create a new function named "ferasys-security-headers"
 * 4. Copy this code into the function editor
 * 5. Publish the function
 * 6. Associate it with your distribution's "Viewer Response" event
 *
 * These headers improve security, SEO, and compliance:
 * - Strict-Transport-Security: Enforces HTTPS
 * - X-Content-Type-Options: Prevents MIME type sniffing
 * - X-Frame-Options: Prevents clickjacking
 * - X-XSS-Protection: Basic XSS protection for older browsers
 * - Referrer-Policy: Controls referrer information
 * - Content-Security-Policy: Prevents XSS and injection attacks
 * - Permissions-Policy: Controls browser features
 */

function handler(event) {
    var response = event.response;
    var headers = response.headers;

    // Strict Transport Security - Force HTTPS for 2 years
    headers['strict-transport-security'] = {
        value: 'max-age=63072000; includeSubdomains; preload'
    };

    // Prevent MIME type sniffing
    headers['x-content-type-options'] = {
        value: 'nosniff'
    };

    // Prevent clickjacking - allow same origin framing
    headers['x-frame-options'] = {
        value: 'SAMEORIGIN'
    };

    // XSS Protection for legacy browsers
    headers['x-xss-protection'] = {
        value: '1; mode=block'
    };

    // Control referrer information
    headers['referrer-policy'] = {
        value: 'strict-origin-when-cross-origin'
    };

    // Content Security Policy - Allow inline styles and scripts (needed for your current setup)
    // In production, consider moving all inline scripts to external files and use nonces
    headers['content-security-policy'] = {
        value: "default-src 'self'; " +
               "style-src 'self' 'unsafe-inline'; " +
               "script-src 'self' 'unsafe-inline'; " +
               "img-src 'self' data:; " +
               "font-src 'self'; " +
               "connect-src 'self'; " +
               "frame-ancestors 'self'; " +
               "base-uri 'self'; " +
               "form-action 'self';"
    };

    // Permissions Policy - Disable unnecessary browser features
    headers['permissions-policy'] = {
        value: 'geolocation=(), microphone=(), camera=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=()'
    };

    // Cache-Control for HTML files (override if needed)
    // CSS and JS already have cache-control from S3
    if (event.request.uri.endsWith('.html') || event.request.uri === '/' || event.request.uri === '') {
        headers['cache-control'] = {
            value: 'public, max-age=300, must-revalidate'
        };
    }

    return response;
}
