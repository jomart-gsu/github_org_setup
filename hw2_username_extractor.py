import os

DIRECTORIES = [
    "Homework 2 - Development Environment Setup Download Jan 22, 2022 1029 AM",
    "Homework 2 - Development Environment Setup Download Jan 23, 2022 1117 AM",
    "Homework 2 - Development Environment Setup Download Jan 23, 2022 1116 AM",
]


def get_usernames_from_directory(dir):
    base_path = os.path.expanduser(f"~/Downloads/{dir}")
    usernames = []
    for filename in os.listdir(base_path):
        if "index" in filename:
            continue
        full_path = os.path.join(base_path, filename)
        with open(full_path) as f:
            url = f.read().strip()
            if "github.com/" in url:
                username = url.split("github.com/")[1].split("/")[0]
            elif "github.com:" in url:
                username = url.split("github.com:")[1].split("/")[0]
            else:
                print(f"No username for {url}")
            usernames.append(username)
    return usernames


if __name__ == "__main__":
    usernames = []
    for directory in DIRECTORIES:
        usernames.extend(get_usernames_from_directory(directory))

    with open("github_usernames.txt", "w") as f:
        f.write("\n".join(usernames))
