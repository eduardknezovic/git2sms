

"""
TODO:

- get the state from the repository

"""
import requests
import time

def get_current_commit_from_github_repo():
    response = requests.get("https://api.github.com/repos/eduardknezovic/git2sms/commits")
    data = response.json()
    last = data[0]
    message = last['commit']['message']
    return message

def get_last_remembered_commit():
    return None

def send_sms():
    from config import get_config
    from sms_service import send_sms
    config = get_config()
    username = config["username"]
    password = config["password"]
    to_numbers = config["to_numbers"]
    send_sms(username, password, to_numbers)
    return


def main():
    remembered_commit = get_last_remembered_commit()
    while True:
        current_commit = get_current_commit_from_github_repo()
        if remembered_commit != current_commit:
            send_sms()
            remembered_commit = current_commit # Update state
        else:
            print("Sadness")
        time.sleep(5)

if __name__ == "__main__":
    main()