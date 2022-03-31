import requests
import random
import string
import time
from colored import fg, attr

color = fg("#6cc644")
res = attr("reset")


class Main:
    def Checker():
        print(f"{color}|{res} GitHub Username Checker ")

        FILE_EXT = "".join(random.choices(string.digits, k=6))
        FILE_NAME = str(FILE_EXT)

        AMOUNT = int(input(f"\n{color}|{res} Amount of Usernames: {color}"))
        LENGTH = int(input(f"{color}|{res} Length of Usernames: {color}"))
        print()

        with open(f"{FILE_NAME}.txt", "w") as USERNAME_LIST:
            for _ in range(AMOUNT):
                USERNAME = "".join(
                    random.choices(
                        string.digits + string.ascii_lowercase + string.ascii_uppercase,
                        k=LENGTH,
                    )
                )

                USERNAME_LIST.write(f"{USERNAME}\n")

        with open(f"{FILE_NAME}.txt", "r") as USERNAME_LIST:
            LINES = USERNAME_LIST.readlines()

            for line in LINES:
                username = line.strip()

                REQUEST_URL = f"https://github.com/{username}"

                MAIN_REQUEST = requests.get(REQUEST_URL)

                if MAIN_REQUEST.status_code == 404:
                    print(
                        f"{color}|{res} {username} {color}-{res} {color} Available{res}"
                    )
                elif MAIN_REQUEST.status_code == 200:
                    print(f"{color}|{res} {username} {color}-{res} Unavailable")
                else:
                    print(
                        f"{color}|{res} {username} {color}-{res} Error {color}-{res} Sleeping 15s..."
                    )
                    time.sleep(15)


if __name__ == "__main__":
    Main.Checker()
