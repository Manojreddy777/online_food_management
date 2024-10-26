from django.shortcuts import redirect
from django.urls import reverse

# class EnsureLoggedInMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         # Exclude the login and registration pages from the check
#         if not request.user.is_authenticated and request.path not in [reverse('login'), reverse('register')]:
#             return redirect('login')  # Redirect to the login page if not authenticated
#
#         response = self.get_response(request)
#         return response

from django.shortcuts import redirect
from django.urls import reverse

class RequireLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path matches '/loggedin/' and the user is not authenticated
        if request.path == reverse('loggedin') and not request.user.is_authenticated:
            return redirect('login')  # Redirect to the login page

        # Process the request as usual
        response = self.get_response(request)
        return response

from django.shortcuts import redirect
from django.urls import reverse

class RedirectInvalidUrlsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the response is a 404 (Page not found)
        if response.status_code == 404:
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return redirect(reverse('login'))  # Redirect to login page

        return response
