import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views import View
from email_validator import EmailNotValidError
from rest_framework.authtoken.models import Token


def my_email_validator(test_email):
    if '@' not in test_email:
        return False
    else:
        return (' ' not in test_email) and ('@.' not in test_email) and (test_email.find('.', test_email.find('@')) != -1)


class Registration(View):

    def post(self, request, *args, **kwargs):
        getting_data = json.loads(request.body)
        try:
            if not my_email_validator(getting_data['email']):
                raise EmailNotValidError
            User.objects.create_user(username=getting_data['email'], first_name=getting_data['name'],
                                     last_name=getting_data['surname'],
                                     email=getting_data['email'], password=getting_data['password'])
            return JsonResponse("", safe=False, status=200)
        except IntegrityError:  # если какой-то параметр не уникален
            return JsonResponse("", safe=False, status=404)
        except EmailNotValidError:
            return JsonResponse("", safe=False, status=400)


class Authorize(View):

    def post(self, request, *args, **kwargs):
        credentials = json.loads(request.body)
        user = authenticate(request, username=credentials['email'], password=credentials['password'])
        if user:
            token = Token.objects.get_or_create(user=user)
            response = {"roles": ["USER"], "token": "Bearer " + str(token[0])}
            return JsonResponse(response, safe=False, status=200)
        else:
            return JsonResponse("User no found", safe=False, status=404)
