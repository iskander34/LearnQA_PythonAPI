import requests

# 1. Запрос без указания параметра method
response_no_method = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response_no_method.text)
print(response_no_method.status_code)

# 2. Запрос с методом не из списка
response_fail_method = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method':'HEAD'})

print(response_fail_method.text)
print(response_fail_method.status_code)

# 3. Запрос с верным параметром method
response_good_method = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method':'POST'})

print(response_good_method.text)
print(response_good_method.status_code)
print()

# 4. Запрос с перебором типов параметра
for i in ['GET','POST','PUT','DELETE']:
    payload = {"method": i}
    print("Параметр: "+i)
    response_all_method = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = payload)
    print(response_all_method.text, end=' ')
    print("Тип запроса GET " + str(response_all_method.status_code))
    print()
    response_all_method = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
    print(response_all_method.text, end=' ')
    print("Тип запроса POST " + str(response_all_method.status_code))
    print()
    response_all_method = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
    print(response_all_method.text, end=' ')
    print("Тип запроса PUT " + str(response_all_method.status_code))
    print()
    response_all_method = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
    print(response_all_method.text, end=' ')
    print("Тип запроса DELETE " + str(response_all_method.status_code))
    print()

