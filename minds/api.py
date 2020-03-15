# -*- coding: utf-8 -*-
from pprint import pprint

from requests.utils import dict_from_cookiejar, cookiejar_from_dict

from minds.connections import XSRFSession
from minds.exceptions import AuthenticationError
from minds.profile import Profile
from minds.utils import add_url_kwargs
from minds.endpoints import *
from minds.sections import NewsfeedAPI, ChannelAPI, NotificationsAPI, PostingAPI, InteractAPI


class Minds(NewsfeedAPI, ChannelAPI, NotificationsAPI, PostingAPI, InteractAPI):
    _xsrf_retries = 5

    def __init__(self, profile=None, login=True):
        self.con = XSRFSession()
        self.profile = profile
        if self.profile:
            if profile.cookie:
                self.con.cookies = cookiejar_from_dict(profile.cookie)
            if profile.proxy:
                self.con.proxies = {'https': profile.proxy, 'http': profile.proxy}
        self._establish_xsrf()
        if self.profile and login and not self.is_authenticated:
            if profile.username and profile.password:
                self.authenticate(profile.username, profile.password)

    def _test_proxy(self):
        data = self.con.get('https://httpbin.org/ip').json()
        print(data)

    def _directory(self, base, offset=None, limit=12) -> dict:
        """Base for paginated directory endpoints"""
        url = add_url_kwargs(base, offest=offset, limit=limit)
        resp = self.con.get(url)
        return resp.json()

    @staticmethod
    def is_guid(guid: str) -> bool:
        """Check whether text is minds 18digit long GUID"""
        if guid.isdigit() and len(guid) == 18:
            return True
        return False

    def _establish_xsrf(self):
        """
        Minds required XSRF-TOKEN cookie to be present as header for whatever reason
        Go to log in page to get the cookie and save it
        """
        # todo figure out why sometimes login page doesn't return xsrf token cookies
        # maybe submitting loggedin=0 cookie will force it to do that
        if 'XSRF-TOKEN' in self.con.cookies:
            return
        retries = 0
        while retries < self._xsrf_retries:
            resp = self.con.get('https://www.minds.com/login')
            if 'XSRF-TOKEN' in resp.cookies:
                break
            retries += 1
        else:
            raise AuthenticationError("could not establish minds connection: can't find xsrf-token")

    def register(self, email) -> dict:
        """register user using self.profile credentials

        Try to register a profile using credentials ``self.profile.username`` and ``self.profile.password``.
        The profile will be saved locally if possible.

        :param email: email is required for registration however it's not used anywhere by minds.com
        """
        data = {
            "username": self.profile.username,
            "email": email,
            "password": self.profile.password,
            "password2": self.profile.password,
            "captcha": ""
        }
        resp = self.con.post(REGISTER_URL, json=data)
        resp_data = resp.json()
        if resp_data['status'] == 'success':
            self.profile.save()
        return resp_data

    def get_cookies(self) -> dict:
        """get current connection cookies
        """
        whitelist = ['XSRF-TOKEN', 'loggedin', 'minds']
        cookies = dict_from_cookiejar(self.con.cookies)
        return {k: v for k, v in cookies.items() if k in whitelist}

    def authenticate(self, username, password, save_profile=True) -> dict:
        """
        Authenticate current instance with given user
        :param: save_profile: whether to save profile locally
        """
        auth = {
            'username': username,
            'password': password
        }
        resp = self.con.post(AUTHENTICATE_URL, json=auth)
        self.user = resp.json()
        if self.user['status'] == 'failed':
            raise AuthenticationError("Couldn't log in with the given credentials")
        self.guid = self.user['user']['guid']
        if save_profile:
            Profile(
                username=username,
                password=password,
                cookie=self.get_cookies(),
                proxy=self.con.proxies.get('https'),
            ).save()
        return resp.json()

    @property
    def is_authenticated(self) -> bool:
        """Return whether current instance is authenticated"""
        return bool(int(self.con.cookies.get('loggedin', '0')))

    def comments(self, guid, offset=None, limit=12) -> dict:
        """Return comments of GUID post
        :param guid: 18digit minds.com guid
        """
        return self._directory(COMMENT_URLF(guid), offset, limit)

    def get_guid(self, clue: str) -> str:
        """get GUID from a clue
        :param clue: either url, channel id or guid (will return itself after checking)
        :return: guid
        """
        if 'minds.com' in clue:
            channel_name = clue.strip('/').split('/')[-1]
        else:
            channel_name = clue
        if self.is_guid(channel_name):
            return channel_name
        data = self.con.get(CHANNEL_URLF(channel_name)).json()
        return data['channel']['guid']

