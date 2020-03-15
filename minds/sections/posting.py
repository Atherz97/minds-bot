from minds.utils import requires_auth
from minds.endpoints import *


class PostingAPI:
    def _post_comment(self, guid, message, wire_treshold=None, is_rich=0, title='', description='',
                      thumbnail='', url='', attachment_guid=None, mature=0, access_id=2) -> dict:
        body = {k: v for k, v in locals().items() if k != 'self'}
        resp = self.con.post(COMMENT_URLF(guid), json=body)
        return resp.json()

    def _post_newsfeed(self, message, wire_treshold=None, is_rich=0, title='', description='',
                       thumbnail='', url='', attachment_guid=None, mature=0, access_id=2) -> dict:
        body = {k: v for k, v in locals().items() if k != 'self'}
        resp = self.con.post(NEWSFEED_URL, json=body)
        return resp.json()

    def _post_blog(self, title, description, guid='new', access_id=2, mature=0, category='',
                   license='', fileKey='header', monetized=0, published=1, wire_treshold=0,
                   custom_meta=None, slug=None, header_top=0) -> dict:
        body = {k: v for k, v in locals().items() if k != 'self'}
        resp = self.con.post(BLOG_NEW_URL, json=body)
        return resp.json()

    @requires_auth
    def post_newsfeed(self, message, attached_url='', mature=False, **kwargs) -> dict:
        """Post something to user's newsfeed.

        :param message: text message of post content
        :param attached_url: urls that should be attached to the post
        :param mature: whether post should be marked mature or not

        .. note:: requires auth
        """
        return self._post_newsfeed(message=message, url=attached_url, mature=int(mature), **kwargs)

    @requires_auth
    def post_comment(self, guid, message, mature=False, **kwargs):
        """Post comment to guid.

        :param guid: under what object message should be posted
        :param message: text message of post content
        :param attached_url: urls that should be attached to the post
        :param mature: whether post should be marked mature or not

        .. note:: requires auth
        """
        return self._post_comment(guid, message, mature=int(mature), **kwargs)

    @requires_auth
    def post_blog(self, title, body, mature=False, category='', license='', published=True, slug=None):
        """Post blog under user's blogfeed

        :param title: blog title
        :param body: html body
        :param mature: whether post should be marked mature or not
        :param category: blog category
        :param license: blog license
        :param published: whether to publish on posting (otherwise will be draft)
        :param slug: visual url slug that will be set for the blog post

        .. note:: requires auth
        """
        return self._post_blog(
            title=title, description=body, mature=int(mature),
            category=category, license=license,
            published=int(published), slug=slug
        )

