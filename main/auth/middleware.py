from django.contrib.auth.middleware import get_user
from django.utils.functional import SimpleLazyObject
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
from config.constant import COOKIE_NAME

EXCLUDE_FROM_MIDDLEWARE = ['main.auth.authenticate', 'main.auth.AdminAuthenticate']


class JWTAuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))
        return self.get_response(request)

    @staticmethod
    def get_jwt_user(request):
        jwt_authentication = JWTAuthentication()
        print("Getting jwt user")
        if jwt_authentication.get_header(request):
            print("Got header")
            user, jwt = jwt_authentication.authenticate(request)
        return user


class AuthorizationMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        view_name = '.'.join((view_func.__module__, view_func.__name__))
        print(view_name, "view name")
        if view_name in EXCLUDE_FROM_MIDDLEWARE:
            return None

    def __call__(self, request):
        print("Performing authorization")
        if request.COOKIES.get(COOKIE_NAME):
            token_dict = json.loads(request.COOKIES.get(COOKIE_NAME))
            access_token = token_dict['access']
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
        return self.get_response(request)