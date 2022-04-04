import vk
import time
import os


def starter():
    try:
        while True:
            if "token" in os.environ:
                print("System Started")
                session = vk.Session(access_token=os.environ.get('token'))
                api = vk.API(session, v="5.95")
                while True:
                    api.account.setOnline(voip=0)
                    time.sleep(180)
            else:
                raise Exception("Error: Token Missing")
    except Exception:
        print("A critical error has occurred")
        starter()


starter()
