def cookielaw_accepted(request):
    """Add cookielaw_accepted context variable to the context."""
    return {
        'cookielaw_accepted': request.COOKIES.get('cookielaw_accepted') == '1'
    }
