import requests
import datetime
import os
import yadisk

help(yadisk)

with open('content/tokens.txt', 'r', encoding='utf8') as file_object:
    TOKEN_VK = file_object.readline().strip()
    ID_VK = file_object.readline().strip()
    TOKEN_YA = file_object.readline().strip()
    print(TOKEN_VK)

class user_VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()  # status_code

    def get_photo(self):
        # https://api.vk.com/method/photos.get
        url = 'https://api.vk.com/method/photos.get'
        params = {'album_id': 'profile', 'owner_id': self.id, 'extended': 1}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def parsed_photo(self, photo_info: list):
        # здесь обрабатываем данные из get_photo, даем название и т.п.
        pass


class user_YA:

    def __init__(self, access_token) -> None:
        self.token = access_token

    def create_folder(self, folder_name: str):
        path = folder_name
        y = yadisk.YaDisk(self.token)
        if not y.is_dir(Path):
            y.mkdir(f'{folder_name}')
        else:
            a = 1
    #         pass

    def upload_file(self, files: list, name_dir: str):
        y.upload()
        # здесь загружаем файлы
        pass
#
#
# class user_Google:
#     # по аналогии с vk
#     def __init__(self.token = access_token
#     self.id = user_id
#     self.version = version
#     self.params = {'access_token': self.token, 'v': self.version}
#
#     def get_photo(self, ggl_id: str):
#         # https://api.google.com/method/photos.get
#         url = 'https://api.google.com/method/photos.get'
#         params = {'user_ids': self.id}
#         response = requests.get(url, params={**self.params, **params})
#         return response.json()
#
#     def parsed_photo(self, photo_info: list):
#         pass
#
#
def main():
    vk_id = ID_VK #input("Введите номер пользователя")
    dt_curr = datetime.date.today()
    print(dt_curr)
    name_directory = "Backup_" + str(dt_curr).replace('-', '_')  # input("Backup_")
    vk_token = TOKEN_VK
    vk = user_VK(vk_token, vk_id)
    json_info = vk.get_info()
    print(json_info)
    json_photo = vk.get_photo()
    # parsed_photo = user_VK.parsed_photo(json_photo)
    # choise = input("Выберите сервис для загрузки:\n"
    #                "1 - Яндекс.Диск\n"
    #                "2 - Google.Диск\n"
    #                "Введите команду:")
    choise = "1"
    if choise == "1":
        user_yandex = user_YA(TOKEN_YA)
        # y = yadisk.YaDisk(user_yandex)
        user_yandex.create_folder(name_directory)
        # y = yadisk.Yadisk(token=user_yandex)
        a = 1
        # user_yandex.upload_file(parsed_photo, name_directory)

    sp = 1
    #
    # if choise == "2":
    #     user_gooogle = user_Google()
    #     user_gooogle.create_new_folder(name_directory)
    #     user_gooogle.upload_file(parsed_photo, name_directory)


if __name__ == '__main__':
    main()