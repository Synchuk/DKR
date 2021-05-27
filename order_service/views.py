import redis
from json import loads
from json import dumps
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import GoodModelSerializer
#from database.utils import DataBaseCar
from acc_service.service import AccountManager
from db_service.service import DbCRUD
host = 'localhost'
port = 6379
db = 1

# host = os.environ.get("REDIS_HOST")
# port = os.environ.get("REDIS_PORT")
# db = os.environ.get("REDIS_DB")
cache_redis = redis.Redis(host, port=port, db=db)


class GoodView(APIView):
    def __init__(self):
        super().__init__()
        self.manager = AccountManager()
        self.db_service = DbCRUD()
        self.serializer = GoodModelSerializer

    def get(self, request: Request):
        id = request.query_params.get('id', None)
        if id is None:
            goods = self.db_service.all()
            goods_serializer = self.serializer(goods, many=True)
            return Response(goods_serializer.data, status=200)
        else:
            return self.get_detail(id)

    def get_detail(self, id):
        record = cache_redis.get(id)
        if record is not None:
            data = loads(record)
            return Response(data, status=200)

        record = self.db_service.get_record(id)
        if record is None:
            return Response(status=400)

        record_serializer = self.serializer(record)
        data = record_serializer.data

        cache_redis.set(id, dumps(data))

        return Response(data, status=200)

    def post(self, request: Request):
        if not self.manager.page_permission(request):
            return Response(status=400)

        data = loads(request.body)
        data_serializer = self.serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)

        id = data_serializer.data['id']
        if not self.db_service.update(data_serializer.data, id):
            return Response(status=400)
        cache_redis.delete(id)
        return Response(status=200)

    def put(self, request: Request):
        if not self.manager.page_permission(request):
            return Response(status=400)

        data = loads(request.body)
        data_serializer = self.serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)

        if not self.db_service.create(data_serializer.data):
            return Response(status=400)
        return Response(status=200)

    def delete(self, request: Request):
        if not self.manager.page_permission(request):
            return Response(status=400)

        id = loads(request.body)['id']
        if not self.db_service.delete(id):
            return Response(status=400)
        cache_redis.delete(id)
        return Response(status=200)


