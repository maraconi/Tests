import requests

token = "ххх"
url = "https://cloud-api.yandex.net/v1/disk/resources/"


def create_folder(path: str):
    params = {'path': path}
    headers = {"Accept": "application/json",
               "Authorization": "OAuth " + token}
    create_dir = requests.api.put(url, headers=headers, params=params)
    return create_dir.status_code


if __name__ == '__main__':
    create_folder()

