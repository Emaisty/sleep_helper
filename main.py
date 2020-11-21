import webbrowser
from get_massage import check_message
import time
import pyautogui
from global_var import x_pos_text, y_pos_text, x_pos_button, y_pos_button, name


def act(url):
    print(url)
    webbrowser.open(url)
    time.sleep(5)
    pyautogui.click(x_pos_text, y_pos_text)
    pyautogui.click(x_pos_text, y_pos_text)
    pyautogui.click(x_pos_text, y_pos_text)
    time.sleep(2)
    pyautogui.typewrite(name)
    time.sleep(2)
    pyautogui.click(x_pos_button, y_pos_button)
    time.sleep(2)


def check(str):
    i = str.find("https")
    url = ""
    while i != len(str) and str != ' ':
        url += str
        i += 1
    act(url)


while True:
    messages = check_message()
    print(messages['items'][0]['text'])
    if messages['items'][0]['text'].find("events.webinar.ru") + 1:
        check(messages['items'][0]['text'])
        break

    if messages['items'][0]['fwd_messages'] != []:
        if messages['items'][0]['fwd_messages'][0]['text'].find("events.webinar.ru") + 1:
            check(messages['items'][0]['fwd_messages'][0]['text'])
            break
    time.sleep(2)
