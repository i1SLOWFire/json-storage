import json

class JSONStorage:
    """
    Универсальное хранилище списка объектов в JSON.
    """

    def __init__(self, filename, item_class=None):
        """
        :param filename: имя JSON-файла.
        :param item_class: класс элементов, у которых есть методы to_dict() и from_dict().
        """
        self.filename = filename
        self.item_class = item_class
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def load(self):
        """
        Загружает список из JSON и превращает словари в объекты.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if self.item_class is None:
                self.items = data
            else:
                self.items = [self.item_class.from_dict(item) for item in data]
        except FileNotFoundError:
            self.items = []
        except json.JSONDecodeError:
            print(f"Файл {self.filename} повреждён. Будет создан новый список.")
            self.items = []

    def save(self):
        """
        Сохраняет текущий список объектов в JSON.
        """
        if self.item_class is None:
            to_save = self.items
        else:
            to_save = [item.to_dict() for item in self.items]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(to_save, f, indent=2, ensure_ascii=False)

    def add_item(self, item):
        """
        Добавляет объект в список и сохраняет.
        """
        if self.item_class and not isinstance(item, self.item_class):
            raise TypeError(f"Ожидается {self.item_class.__name__}, получен {type(item).__name__}")
        self.items.append(item)
        self.save()

    def remove_item(self, item):
        """
        Удаляет объект из списка и сохраняет.
        """
        if item not in self.items:
            raise ValueError(f"Элемент {item} не найден")
        self.items.remove(item)
        self.save()

    def clear(self):
        """
        Очищает список и сохраняет
        """
        self.items.clear()
        self.save()