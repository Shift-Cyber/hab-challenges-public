import time
import socket
from threading import Thread

# Define your host and port
host = 'localhost'
port = 12345

# List of dictionaries with 'flag' and 'time' fields
times_and_flags = [
    {'flag': 'flag{szavmarpjr}', 'time': 1684548000}, # 7pm Friday, 19 May 2023
    {'flag': 'flag{vvmjubpmoy}', 'time': 1684598400}, # 9am Saturday, 20 May 2023
    {'flag': 'flag{ofwbtxzjxs}', 'time': 1684605600}, # 11am Saturday, 20 May 2023
    {'flag': 'flag{cerpwbdttn}', 'time': 1684612800}, # 1pm Saturday, 20 May 2023
    {'flag': 'flag{bdlhcmlsos}', 'time': 1684620000}, # 3pm Saturday, 20 May 2023
    {'flag': 'flag{ealcdabqzg}', 'time': 1684627200}, # 5pm Saturday, 20 May 2023
    {'flag': 'flag{niszgdwchf}', 'time': 1684684800}, # 9am Sunday, 21 May 2023
    {'flag': 'flag{zmesyvfsjo}', 'time': 1684692000}, # 11am Sunday, 21 May 2023
]

def send_message(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(message.encode() + b'\n')
        print(f'Sent message: "{message}"')
    except ConnectionError:
        print('Server not open, nothing sent...')

def handle_flag(flag_dict):
    while True:
        current_time = int(time.time())
        if current_time >= flag_dict['time'] - 3 and current_time <= flag_dict['time'] + 3:
            send_message(flag_dict['flag'])
            time.sleep(1)

def alive_check():
    while True:
        send_message(f'The flag server is alive as of epoch:{int(time.time())}')
        time.sleep(60)

if __name__ == "__main__":
    # Start the alive checker
    Thread(target=alive_check).start()

    # Start a handler for each flag
    for flag_dict in times_and_flags:
        Thread(target=handle_flag, args=(flag_dict,)).start()
