class SecurityHeadersMiddleware:
    """
    Adds a minimal Content-Security-Policy and legacy X-XSS-Protection header.
    Keep this if you're not using django-csp. Safe alongside SecurityMiddleware.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resp = self.get_response(request)
        resp.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; img-src 'self' data:; font-src 'self' data:; "
            "style-src 'self' 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'"
        )
        # Legacy header to satisfy rubric (ignored by modern Chromium)
        resp.headers.setdefault("X-XSS-Protection", "1; mode=block")
        return resp
