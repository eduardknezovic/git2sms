

"""
TODO:

- get the state from the repository

"""
import time


def get_current_commit_from_github_repo():
    raise NotImplementedError

def get_last_remembered_commit():
    return None

def send_sms():
    print("The repo has been updated!")

def main():
    remembered_commit = get_last_remembered_commit()
    while True:
        current_commit = get_current_commit_from_github_repo()
        if remembered_commit is not current_commit:
            send_sms()
            remembered_commit = current_commit # Update state
        time.sleep(5)

if __name__ == "__main__":
    main()