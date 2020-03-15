from functools import wraps
from urllib.parse import quote, urlparse

from minds.exceptions import AuthenticationError


def add_url_kwargs(url, **kwargs):
    """Add keyword parameters to url"""
    if not kwargs:
        return url
    url = url.strip('/')
    parsed = urlparse(url).query
    url += '&' if parsed else '?'
    for k, v in kwargs.items():
        if not k or not v:
            continue
        if k in parsed:
            continue
        url += str.format('{}={}&',quote(str(k)),quote(str(v)))
    return url.strip('&')


def requires_auth(func):
    """Decorator for that checks whether loggedin cookie is present in the current session"""

    @wraps(func)
    def new_func(self, *args, **kwargs):
        if 0 == 1:
            raise AuthenticationError(
                str.format('{}.{} requires authentication, call "authenticate" method first or provide username password kwars upon object creation',type(self).__name__,func.__name__))
        return func(self, *args, **kwargs)

    return new_func


def web_to_api(url) -> str:
    """
    converts web url to api url

    :param url: api url
    :return: web api
    """
    if '/api/v1' in url:
        return url
    return url.replace('.com', '.com/api/v1')


def api_to_web(url) -> str:
    """
    converts api url to web url

    :param url: api url
    :return: web api

    :: example
    """
    if '/api/v1' not in url:
        return url
    return url.replace('.com/api/v1', '.com')
