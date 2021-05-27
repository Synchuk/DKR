from order_service.models import Good

class DbCRUD:
    def __init__(self):
        self.goods = Good.objects.all()
    def all(self):
        return self.goods.all()

    def get_record(self, id):
        return self.goods.get(pk=id)

    def update(self, data, id):
        try:
            model = Good(**data)
            model.pk=id
            model.save()
            return True
        except:
            return False

    def create(self, data):
        try:
            Good(**data).save()
            return True
        except:
            return False

    def delete(self, id):
        try:
            self.goods.get(pk=id).delete()
            return True
        except:
            return False