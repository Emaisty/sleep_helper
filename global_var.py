import vk

name = "Kek Pek"  # имя
token = ""  # токен вк

session = vk.Session(access_token=token)
vk_api = vk.API(session)

sid = 2000000000 + vk_api.messages.searchConversations(q='ВАЖ', count=1, v=5.126)['items'][0]['peer'][
    'local_id']  # номер беседы

x_pos_text = 650  # куда сместить курсор чтобы вставить имя
y_pos_text = 350

x_pos_button = 700  # куда сместить курсор чтобы войти
y_pos_button = 420
