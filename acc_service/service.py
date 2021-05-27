from rest_framework.request import Request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class AccountManager:
    def page_permission(self, request: Request):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def register(self, acc_data):
        try:
            user = User()
            user.username = acc_data['username']
            user.set_password(acc_data['password1'])
            user.email = acc_data['email']
            user.save()
            return True
        except:
            return False

    def login(self, acc_data, request):
        username = acc_data['name']
        password = acc_data['password']
        user = authenticate(username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False

    def logout(self, request):
        logout(request)
        return True