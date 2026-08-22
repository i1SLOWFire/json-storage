# JSONStorage — универсальное хранилище для Python-объектов

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Простой класс для сохранения и загрузки списков объектов в JSON.

---

## Установка

### Как submodule (для совместной разработки)

```bash
git submodule add https://github.com/i1SLOWFire/json-storage.git libs/json_storage
```

Импорт (если вы оставили папку libs/json_storage):

```python
from libs.json_storage.storage import JSONStorage
```

Если вы переименовали папку — скорректируйте путь.

### Копированием файла

Скопируйте storage.py в проект и импортируйте:

```python
from storage import JSONStorage
```

---

## Быстрый старт

```python
from storage import JSONStorage

class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    def to_dict(self):
        return {"id": self.id, "title": self.title, "done": self.done}

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"], data["done"])

storage = JSONStorage("tasks.json", Task)
storage.load()

storage.add_item(Task(1, "Купить хлеб"))
storage.add_item(Task(2, "Сделать ДЗ"))

print(len(storage))        # 2
print(storage[0].title)    # Купить хлеб
```

Можно хранить и простые словари:

```python
storage = JSONStorage("data.json")
storage.load()
storage.add_item({"name": "test", "value": 42})
print(storage[0])  # {'name': 'test', 'value': 42}
```

---

## Методы

| Метод | Что делает |
|-------|------------|
| `load()` | Загружает данные из JSON (если файла нет — пустой список). |
| `save()` | Сохраняет текущий список в JSON. |
| `add_item(item)` | Добавляет объект и сохраняет. |
| `remove_item(item)` | Удаляет объект и сохраняет. |
| `clear()` | Очищает список и сохраняет. |
| `__getitem__`, `__len__`, `__iter__` | Позволяют работать как со списком. |

Все методы, меняющие список, автоматически вызывают `save()`.

---

## Лицензия

MIT © 2026 Ivan Vorobyov — см. файл [LICENSE](LICENSE).