import requests
from dataclasses import dataclass
import datetime

class getAppCubes:
    def __init__(self):
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
        self.PROXIES = {}
        self.BASE_URL = 'https://apps.moons14.com/api/developer/'

    def apps(self, count = 30, loginonly = False):
        endpoint = 'apps'
        params =  {'count': count, 'loginonly': loginonly}
        response = self.__send_requests(endpoint, params)
        return [AppCubesApp(**app) for app in response['apps']]
    
    def search(self, query, count = 30, loginonly = False):
        endpoint = 'search'
        params =  {'q': query, 'count': count, 'loginonly': loginonly}
        response = self.__send_requests(endpoint, params)
        return [AppCubesApp(**app) for app in response['apps']]

    def __send_requests(self, endpoint, params):
        response = requests.get(self.BASE_URL + endpoint, params=params, headers=self.HEADERS, proxies=self.PROXIES)
        response.raise_for_status()
        response_json = response.json()
        if response_json['status'] != 'success':
            raise Exception('\n'.join([error['message'] for error in response_json['errors']]))
        return response_json

@dataclass
class AppCubesApp:
    id: str = None
    loginonly: str = None
    type: str = None
    jp: dict = None
    en: dict = None
    updated_at: str = None

    def __post_init__(self):
        TIMEZONE = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
        BASEURL = 'https://apps.moons14.com/apps/'
        self.url = BASEURL + self.id
        self.loginonly = bool(self.loginonly)
        self.updated_at = datetime.datetime.fromtimestamp(int(self.updated_at), TIMEZONE)
        self.jp = AppCubesAppLang(**self.jp)
        self.en = AppCubesAppLang(**self.en)

@dataclass
class AppCubesAppLang:
    name: str = None
    explanation: str = None
    tags: str = None

    def __post_init__(self):
        self.tags = self.tags.split(',')