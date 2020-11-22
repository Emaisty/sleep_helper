# Sleep helper

Зачем вставать к 1 паре, если можно сделать так, чтобы бот за тебя туда приходил?
Вот решение!

## Запуск

Используя [pip](https://pip.pypa.io/en/stable/) устанавливаем.

```bash
pip install webbrowser
pip install pyautogui
pip install vk
```
Далее в файле [global_var.py](https://github.com/Emaisty/sleep_helper/blob/master/global_var.py) меняем:

-Name(какое будет отображаться на лекции(Русский язык пока что не поддерживается))

-token(ваш вк токен чтобы бот мог читать сообщения (см приложение 1))

-при необходимости меняем координаты поля ввода имени и запуска вебинара 


## Использование

```python
python main.py
```
Все! Теперь ждете, пока староста отправит в группу ссылку и программа сама войдет на лекцию!

### Приложение 1
Получение вк токена

1) Переходим на [страницу](https://vkhost.github.io/)

2) Нажимаем на VK Admin

3) Даем доступ(это официальная страница вк админов. Доступ нужен для прочтения сообщений)

4) В браузерной строке выделяем access_token

https://oauth.vk.com/blank.html#access_token=(выбираем то, что тут)&expires_in=0&user_id=(id)&email=(email)
  
5) Вставляем его в программу

## License
[MIT](https://choosealicense.com/licenses/mit/)
