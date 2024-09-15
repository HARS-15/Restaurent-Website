from django.http import Http404

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the admin page
        if request.path.startswith('/admin/'):
            # Check if the user is authenticated and is a superuser
            if not (request.user.is_authenticated and request.user.is_superuser):
                raise Http404("Page not found")
        
        response = self.get_response(request)
        return response
