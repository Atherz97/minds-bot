from minds.utils import requires_auth
from minds.endpoints import *


class NotificationsAPI:
    @requires_auth
    def notifications_all(self, offset: int=None, limit: int=24) -> dict:
        """get *all* notifications

        :param offset: pagination offset
        :param limit: pagination limit
        """
        return self._directory(NOTIFICATIONS_ALL, offset, limit)

    @requires_auth
    def notifications_comments(self, offset: int=None, limit: int=24) -> dict:
        """get only *comments* notifications

        :param offset: pagination offset
        :param limit: pagination limit
        """
        return self._directory(NOTIFICATIONS_COMMENTS, offset, limit)

    @requires_auth
    def notifications_groups(self, offset: int=None, limit: int=24) -> dict:
        """get only *groups* notifications

        :param offset: pagination offset
        :param limit: pagination limit
        """
        return self._directory(NOTIFICATIONS_GROUPS, offset, limit)

    @requires_auth
    def notifications_subscriptions(self, offset: int=None, limit: int=24) -> dict:
        """get only *subscriptions* notifications

        :param offset: pagination offset
        :param limit: pagination limit
        """
        return self._directory(NOTIFICATIONS_SUBSCRIPTIONS, offset, limit)

    @requires_auth
    def notifications_tags(self, offset: int=None, limit: int=24) -> dict:
        """get only *tags* notifications

        :param offset: pagination offset
        :param limit: pagination limit
        """
        return self._directory(NOTIFICATIONS_TAGS, offset, limit)

    @requires_auth
    def notifications_votes(self, offset: int=None, limit: int=24) -> dict:
        """get only *votes* notifications

        :param offset: pagination offset
        :param limit: pagination limit
        """
        return self._directory(NOTIFICATIONS_VOTES, offset, limit)

