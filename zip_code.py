# Импорт необходимых библиотек
import requests
import json

# Определение конечной точки API
url = "https://api.zippopotam.us"

# Определение темы поиска и параметров для запроса API
# subject = 'Artificial intelligence'
params = {}

params["country"] = input('Enter country code(for exm. us or ru):  ')
params["index"] = input('Enter zip code (for exm. 10001 or 117574): ')

# params = {
#     "country": 'us',
#     "index": '10001'
# }


full_url = url+'/'+ params["country"] + '/' + params["index"]
print(full_url)
# Отправка запроса API с помощью метода requests.get
response = requests.get(full_url, params=params)

print(response)

# Проверка кода состояния ответа для подтверждения успешности запроса API
if response.status_code == 200:
    print("\nУспешный запрос API! \n")
else:
    print("Запрос API отклонен с кодом состояния:", response.status_code)

# Загрузка данных ответа в виде объекта JSON
data = json.loads(response.text)
print(data)