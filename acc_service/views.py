from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpRequest

import json

from .serializer import AccountLoginSerializer
from .serializer import AccountSerializer
from .service import AccountManager


class AccountRegister(APIView):
    def __init__(self):
        super().__init__()
        self.manager = AccountManager()
    def post(self, request: HttpRequest):
        acc = request.body
        acc_data = json.loads(acc)
        acc_data_serializer = AccountSerializer(data=acc_data)
        if acc_data_serializer.is_valid():
            if self.manager.register(acc_data_serializer.data):
                return Response(status=200)
            return Response(status=400)
        return Response(status=400)

class AccountLogout(APIView):
    def __init__(self):
        super().__init__()
        self.manager = AccountManager()

    def post(self, request: HttpRequest):
        if self.manager.logout(request):
            return Response(status=200)
        return Response(status=400)

class AccountLogin(APIView):
    def __init__(self):
        super().__init__()
        self.manager = AccountManager()

    def post(self, request: HttpRequest):
        acc = request.body
        acc_data = json.loads(acc)
        acc_data_serializer = AccountLoginSerializer(data=acc_data)
        if acc_data_serializer.is_valid():
            if self.manager.login(acc_data_serializer.data, request):
                return Response(status=200)
            return Response(status=400)
        return Response(status=400)
