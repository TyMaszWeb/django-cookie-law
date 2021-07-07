
def cookielaw(request):
    """Add cookielaw context variable to the context."""

    cookie = request.COOKIES.get('cookielaw_accepted')
    return {
        'cookielaw': {
            'notset': cookie is None,
            'accepted': cookie == '1',
            'rejected': cookie == '0',
        }
    }
