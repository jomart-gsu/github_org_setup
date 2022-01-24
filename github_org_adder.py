import requests
import os
from time import sleep
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

print("*********** GH TOKEN *********")
print(os.getenv("GH_TOKEN"))


def get_id_by_username(username):
    id_response = requests.get(
        f"https://api.github.com/users/{username}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {os.getenv('GH_TOKEN')}",
        },
    )
    id_response = id_response.json()
    print(id_response)
    return id_response["id"]


def add_id_to_org(user_id):
    print(user_id)
    return requests.post(
        "https://api.github.com/orgs/csc4350-sp22/invitations",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {os.getenv('GH_TOKEN')}",
        },
        data=json.dumps(
            {
                "invitee_id": user_id,
            }
        ),
    )


if __name__ == "__main__":
    with open("github_usernames.txt") as f:
        for line in f:
            username = line.strip()
            user_id = get_id_by_username(username)
            response = add_id_to_org(user_id)
            if response.status_code != 201:
                print(f"Couldn't add user {line} to org: {response.json()}")
                break
            sleep(1)  # try not to get rate-limited
