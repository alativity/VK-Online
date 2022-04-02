import vk
import time
import os

if "token" in os.environ:
    session = vk.Session(access_token=os.environ.get('token'))
    api = vk.API(session, v="5.95")
    while True:
        exit = api.account.setOnline(voip=0)
        time.sleep(180)
else:
    print("Error: Token Missing")
    exit()