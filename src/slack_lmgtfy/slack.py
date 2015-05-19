from requests import post
from requests.exceptions import RequestException

class IncomingMessage(object):
    def __init__(self):
        self._payload = {}

    def set_text(self, text):
        self._payload["text"] = text

    def set_channel(self, channel):
        self._payload["channel"] = channel

    def as_dict(self):
        return self._payload


class SlackError(Exception):
    pass


def send_message(message, webhook_url):
    # TODO wrap the exception
    try:
        request = post(webhook_url, json=message.as_dict())
        request.raise_for_status()
    except RequestException as e:
        raise SlackError() from e

