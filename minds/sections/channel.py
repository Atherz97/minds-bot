from minds.utils import requires_auth
from minds.endpoints import *


class ChannelAPI:
    def channel_top(self, offset: int=None, limit: int=24) -> dict:
        """Returns *channel* section *top* subsection channels

        :param offset: pagination offset
        :param limit: pagination limit
        """
        return self._directory(CHANNELS_TOP_URL, offset, limit)

    @requires_auth
    def channel_subscriptions(self, offset: int=None, limit: int=24) -> dict:
        """Returns *channel* section *subscriptions* subsection channels

        :param offset: pagination offset
        :param limit: pagination limit

        .. note:: requires auth
        """
        """Returns channel section subscriptions subsection channels"""
        return self._directory(CHANNELS_SUBSCRIPTIONS_URLF(self.guid), offset, limit)

    @requires_auth
    def channel_subscribers(self, offset: int=None, limit: int=24) -> dict:
        """Returns *channel* section *subscribers* subsection channels

        :param offset: pagination offset
        :param limit: pagination limit

        .. note:: requires auth
        """
        return self._directory(CHANNELS_SUBSCRIBERS_URLF(self.guid), offset, limit)

    @requires_auth
    def get_channel(self, name):
        """ returns channel """
        resp = self.con.get(CHANNEL_GUIDF(name))
        return resp.json()
        
