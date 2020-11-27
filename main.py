import webbrowser
from get_massage import check_message
import time
import pyautogui
from global_var import x_pos_reg, y_pos_reg, x_pos_submit, y_pos_submit, x_pos_button, y_pos_button

stop_list = []


def act(url):
    if url in stop_list:
        print('Url has already been used')  # не бульте плиз
    else:
        stop_list.append(url)
        print(url)
        webbrowser.open(url)
        time.sleep(5)
        pyautogui.click(x_pos_reg, y_pos_reg)
        time.sleep(3)
        pyautogui.click(x_pos_submit, y_pos_submit)
        time.sleep(3)
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
    print(mess)
    if mess['text'].find("events.webinar.ru") + 1:
        print(mess['text'])
        act(check(mess['text']))
    if mess['attachments']:
        if 'link' in mess['attachments'][0]:
            if mess['attachments'][0]['link']['url'].find("events.webinar.ru") + 1:
                act(check(mess['attachments'][0]['link']['url']))
    if 'fwd_messages' in mess:
        if mess['fwd_messages']:
            m = mess['fwd_messages'][0]
            find_url(m)


if __name__ == "__main__":
    messages = check_message()
    num = messages['count']
    while True:
        messages = check_message()
        if num < messages['count']:
            for i in range(0, messages['count'] - num):
                find_url(messages['items'][i])
            num = messages['count']
        time.sleep(60)
