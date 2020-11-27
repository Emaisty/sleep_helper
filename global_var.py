import vk

name = "Kek Pek"  # имя
token = ""  # токен вк

session = vk.Session(access_token=token)
vk_api = vk.API(session)

sid = 2000000000 + vk_api.messages.searchConversations(q='ВАЖНОЕ! РГБО - 01- 20', count=1, v=5.126)['items'][0]['peer'][
    'local_id']  # номер беседы

x_pos_reg = 1340
y_pos_reg = 270

x_pos_submit = 800  # куда сместить курсор чтобы вставить имя
y_pos_submit = 640

x_pos_button = 710  # куда сместить курсор чтобы войти
y_pos_button = 445
