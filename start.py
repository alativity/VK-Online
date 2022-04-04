from subprocess import run
from time import sleep

fp = "main.py"

restart_timer = 2


def start_script():
    try:
        run("pip install -r requirements.txt", check=True)
        run("python3 " + fp, check=True)
    except:
        print("A critical error has occurred in the program")
        handle_crash()


def handle_crash():
    sleep(restart_timer)
    start_script()


start_script()
