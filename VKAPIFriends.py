from urllib.parse import urljoin
import requests

class VK_user:
    API_BASE_URL = 'https://api.vk.com/method/'
    TOKEN = 'TOKEN' #insert TOKEN
    V = '5.21'

    def __init__(self, user_id):
        self.user_id = user_id
        self.friend_list = list()
        self.link = (f'https://vk.com/id{user_id}')

    def __str__(self):
        return self.link

    def __and__(self, other):
        a = self.check_friends()
        b = other.check_friends()
        result = list(set(a) & set(b))
        return print(result)

    def check_friends(self):
        friends_get_url = urljoin(self.API_BASE_URL, 'friends.get')
        response = requests.get(friends_get_url, params={'access_token': self.TOKEN, 'v': self.V, 'user_id': self.user_id})
        self.friend_list = (response.json()['response']['items'])
        return self.friend_list

    def mutual_friends(self, user_id2):
        a = self.check_friends()
        b = user_id2.check_friends()
        result = list(set(a) & set(b))
        return print(result)


user1 = VK_user('''insert user ID''')
user2 = VK_user('''insert user ID''')
user1.mutual_friends(user2)
user1 & user2
print(user1)

