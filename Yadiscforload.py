import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        file_name = file_path.split('\\')
        file_name = file_name[-1]
        reponse = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params={'path': f'/{file_name}', 'overwrite': True}, headers=HEADERS)
        url = reponse.json()['href']
        with open(file_path, 'rb') as f:
            requests.put(url, params={'path': '/'}, headers=HEADERS, files={"file": f})
        return print(reponse.text)

if __name__ == '__main__':
    uploader = YaUploader('INSERT TOKEN')
    result = uploader.upload('INSERT FILE PATH') # seporator is (\\)