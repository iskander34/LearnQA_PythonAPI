import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

#Число редиректов по моей логике не совпадает с числом записей в response.history
#ибо под первой записью с индексом 0 лежит стартовый url
#количество записей response.history равно 3
print("Число редиректов: "+str(len(response.history)-1))
print("Итоговый URL: "+str(response.url))
