from django.test import TestCase
from .service import DbCRUD, Good

class Test(TestCase):
    def setUp(self) -> None:
        self.db_service = DbCRUD()

    def test_create(self):
        good_data = {
            'name': 'name',
            'price': 9999,
            'owner': 'owner',
            'owner_email': 'owner_email'
        }
        self.assertEqual(self.db_service.create(good_data), True)
        self.assertEqual(len(self.db_service.all()), 1)
        self.assertEqual(self.db_service.delete(1), True)
