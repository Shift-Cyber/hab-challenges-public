import random
import time

flag = b"\xf9\xf3\xfe\xf8\xe4\xeb\xf7\xf6\xec\xc0\xf6\xec\xf1\xeb\xc0\xec\xef\xfe\xf1\xf6\xec\xf7\xc0\xfd\xea\xeb\xc0\xf6\xc0\xec\xeb\xf6\xf3\xf3\xc0\xf1\xfa\xfa\xfb\xc0\xfe\xf1\xc0\xf6\xf1\xeb\xfa\xed\xef\xed\xfa\xeb\xfa\xed\xe2"

class ANSI:
    COLORS = [ "\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m",
               "\033[0;36m", "\033[0;37m", "\033[1;30m", "\033[1;31m", "\033[1;32m", "\033[1;33m",
               "\033[1;34m", "\033[1;35m", "\033[1;36m", "\033[1;37m" ]

    STYLES = [ "\033[1m", "\033[2m", "\033[3m", "\033[4m", "\033[5m", "\033[7m", "\033[9m" ]
    
    END = "\033[0m"

if __name__ == '__main__':
    try:
        while True:
            print("",end="\r")
            for i in flag: print(f"{random.choice(ANSI.COLORS)}{chr(i ^ 0x9F)}{ANSI.END}", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("",end="\r")
        for i in flag: print(f"{chr(i ^ 0x9F)}", end="")
        print("  ")