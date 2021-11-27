import requests, os

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_head(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path, filename):
        file_path = os.path.normpath(file_path)
        uploadurl = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": file_path, "overwrite": "true"}
        HEADERS = self.get_head()
        response_url = requests.get(url=uploadurl, headers=HEADERS, params=params)
        print(response_url)
        url = response_url.json().get('href')
        FILES = {"file": {open(filename, 'rb')}}
        response_upload = requests.put(url, data = FILES, headers = HEADERS)
        if response_upload.status_code == 201:
            print(f'Успешно загружен: {filename}')


if __name__ == '__main__':
    token = 'AQAAAAA2ANzJAADLW4g3j9vSgEkluxq-e0Wa0dk'
    file = "D%%Разработка%homeworkreqT2%"
    filename = "Test.txt"
    uploader = YaUploader(token=token)
    result = uploader.upload(file_path=file, filename=filename)