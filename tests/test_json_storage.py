import unittest
import os
from storage import JSONStorage

class TestItem:
    def __init__(self, task_id, title):
        self.id = task_id
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
        self.test_id = None
        self.test_title = None
        self.test_class = TestItem(self.test_id, self.test_title)

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

if __name__ == '__main__':
    unittest.main()