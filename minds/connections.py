from requests import Session


class XSRFSession(Session):
    """Session that is aware of xsrf token and includes them in request headers"""

    def request(self, method, url,
                params=None, data=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=None, cert=None, json=None):
        if not headers:
            headers = {}
        if 'XSRF-TOKEN' in self.cookies:
            headers.update({'x-xsrf-token': self.cookies['XSRF-TOKEN']})
        return super().request(method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects,
                               proxies, hooks, stream, verify, cert, json)
