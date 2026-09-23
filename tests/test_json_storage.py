import unittest
import os
from storage import JSONStorage

class TestItem:
    def __init__(self, test_id, title):
        self.id = test_id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"])

class TestJSONStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.json"
        self.test_storage = JSONStorage(self.test_file)
        self.test_id = 1
        self.test_title = "test1"
        self.test_item1 = TestItem(self.test_id, self.test_title)
        self.test_id = 2
        self.test_title = "test2"
        self.test_item2 = TestItem(self.test_id, self.test_title)

    def tearDown(self):
        # Удаляем временный файл после каждого теста
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load(self):
        pass

    def test_load_item_class_is_none(self):
        pass

    def test_load_none_items(self):
        self.assertEqual(self.test_storage.items, None)
        self.test_storage.load()
        self.assertEqual(self.test_storage.items, [])

    def test_save(self):
        pass

    def test_save_item_class_is_none(self):
        pass

    def test_add_item(self):
        self.assertEqual(self.test_storage.items, None)
        self.test_storage.load()
        self.test_storage.add_item(self.test_item1.to_dict())
        self.assertEqual(self.test_storage.items, [{"id": 1, "title": "test1"}])
        self.test_storage.add_item(self.test_item2.to_dict())
        self.assertEqual(self.test_storage.items[0], {"id": 1, "title": "test1"})
        self.assertEqual(self.test_storage.items[1], {"id": 2, "title": "test2"})

if __name__ == '__main__':
    unittest.main()