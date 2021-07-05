import requests
import time

url_link = "https://playground.learnqa.ru/ajax/api/longtime_job"

#создаем задачу.парсим ответ
response = requests.get(url_link)
parsed_response1 = response.json()

#забираем поля token и seconds
parsed_token = parsed_response1["token"]
parsed_time = parsed_response1["seconds"]

payload = {'token': parsed_token}

#запрос с токеном ДО.парсим ответ
response = requests.get(url_link, params = payload)
parsed_response2 = response.json()

#забираем поле status с проверкой
parsed_status = parsed_response2["status"]
if parsed_status == 'Job is NOT ready':

    time.sleep(parsed_time)

    #запрос с токеном После ожидания.Парсим ответ.
    response = requests.get(url_link, params = payload)
    parsed_response3 = response.json()

    # забираем поля статус и результат
    parsed_status = parsed_response3["status"]
    parsed_result = parsed_response3["result"]

    #проверяем на выполнение положительных условий кейса
    if parsed_status == 'Job is ready' and parsed_result !=0:
        print(parsed_result, end = ' ')
        print(parsed_status)
    else:
        print("Что-то пошло не так!")
else:
    print("Статус задачи не корректный. Тест не прошёл")