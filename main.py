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


def check(str="nope"):
    i = str.find("https")
    url = ""
    while i != len(str) and str != ' ':
        url += str[i]
        i += 1
    return url


def find_url(mess):
    print(1)
    if mess['text'].find("events.webinar.ru") + 1:
        print(mess['text'])
        act(check(mess['text']))
    if mess['attachments']:
        if mess['attachments'][0]['link']['url'].find("events.webinar.ru") + 1:
            act(check(mess['attachments'][0]['link']['url']))
    if 'fwd_messages' in mess:
        if mess['fwd_messages']:
            m = mess['fwd_messages'][0]
            find_url(m)


if __name__ == "__main__":
    while True:
        messages = check_message()['items'][0]
        find_url(messages)
        time.sleep(2)
