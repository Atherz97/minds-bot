import os
from pathlib import Path
import toml

CONFIG_DIR = Path(os.environ.get('XDG_CONFIG_HOME', os.path.expanduser('~/.config'))) / 'minds'
CONFIG_DIR.mkdir(parents=True, exist_ok=True)


class Profile:
    config_dir = CONFIG_DIR

    def __init__(self, username, password, cookie=None, proxy=None):
        """
        :param username:
        :param password:
        :param cookie: cookie dict
        :param proxy: proxy string with protocol prefix (e.g. http://)
        :param save: whether to save the profile locally
        """
        self.username = username
        self.password = password
        self.proxy = proxy
        self.dir = self.config_dir / self.username
        self.cookie = cookie

    def __repr__(self):
        return str.format('Profile@{}',self.dir)
        # return f'Profile@{self.dir}'

    @classmethod
    def from_config(cls, username):
        with open(cls.config_dir / username) as f:
            data = toml.loads(f.read())
        return cls(data['username'], data['password'], proxy=data.get('proxy'), cookie=data.get('cookie'))

    def save(self):
        if not self.username:
            raise NotImplementedError('username is required for saving')
        data = {
            'username': self.username,
            'password': self.password,
            'proxy': self.proxy,
            'cookie': self.cookie,
        }
        data = toml.dumps(data)
        with open(str(self.dir), 'w') as f:
            f.write(data)

    def __eq__(self, other):
        keys = ['username', 'password', 'proxy', 'dir', 'cookie']
        for k in keys:
            if getattr(self, k, None) != getattr(other, k, None):
                return False
        return True
