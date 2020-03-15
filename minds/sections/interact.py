from minds.utils import requires_auth
from minds.endpoints import *


class InteractAPI:
    @requires_auth
    def delete(self, url: str) -> dict:
        """Delete any sort of post

        :param url: direct url to object to be deleted

        .. note:: requires auth
        """
        return self.con.delete(url).json()

    @requires_auth
    def upvote(self, guid: str) -> dict:
        """Upvote any sort of post

        :param guid: guid of post object

        .. note:: requires auth
        """
        resp = self.con.put(UPVOTE_URLF(guid))
        return resp.json()

    @requires_auth
    def downvote(self, guid) -> dict:
        """Downvote any sort of post

        :param guid: guid of post object

        .. note:: requires auth
        """
        resp = self.con.put(DOWNVOTE_URLF(guid))
        return resp.json()

    @requires_auth
    def remind(self,guid) -> dict:
        """ remind
        :param guids: guid of post
        .. note:: requires auth
        """
        resp = self.con.post(REMIND_URLF(guid))
        return resp.json()
     
    @requires_auth
    def subscribe(self,guids) -> dict:
        """ subscribe
        :param guids: guids of channel
        .. note:: requires auth
        """
        resp = self.con.post(SUBSCRIBE_URLF(guids))
        return resp.json()
    
    @requires_auth
    def unsubscribe(self,guids) -> dict:
        """ unsubscribe
        :param guids: guids of channel
        .. note:: requires auth
        """
        resp = self.con.delete(SUBSCRIBE_URLF(guids))
        return resp.json()
