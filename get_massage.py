import vk
from global_var import token, sid


def check_message():
    session = vk.Session(access_token=token)
    vk_api = vk.API(session)
    return vk_api.messages.getHistory(peer_id=sid, access_token=token, v=5.126)
