import requests

# URL вашего API endpoint для создания вещи
url = "http://example.com/api/v1/thing/"

# Данные для создания вещи (название, описание, и т.д.)
data = {
    "name": "Название вашей вещи",
    "description": "Описание вашей вещи",
    "category": 1,  # Идентификатор категории вашей вещи
    "owner": 1,  # Идентификатор владельца вещи (пользователя)
}

# Файл изображения для отправки
files = {
    "images": open("logo192.png", "rb")  # Укажите путь к вашему изображению
}

# Отправка POST запроса
response = requests.post(url, data=data, files=files)

# Печать ответа
print(response.json())
