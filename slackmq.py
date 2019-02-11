from slacker import Slacker
from time import sleep


class slackmq(object):
    def __init__(self, api_token, channel, timestamp):
        self.api_token = api_token
        self.channel = channel
        self.timestamp = timestamp

    def ack(self, emoji=None, stars=None):
        try:
            slack = Slacker(self.api_token)
            slack.pins.add(channel=self.channel,
                           timestamp=self.timestamp)
            if stars is not None:
                slack.stars.add(channel=self.channel,
                                timestamp=self.timestamp)
            if emoji is not None:
                slack.reactions.add(emoji,
                                    channel=self.channel,
                                    timestamp=self.timestamp)
        except Exception:
            return False
        return True

    def unack(self, emoji=None, stars=None):
        try:
            sleep(3)
            slack = Slacker(self.api_token)
            slack.pins.remove(channel=self.channel,
                              timestamp=self.timestamp)
            if emoji is not None:
                sleep(3)
                slack.reactions.remove(emoji,
                                       channel=self.channel,
                                       timestamp=self.timestamp)
            if stars is not None:
                sleep(3)
                slack.stars.remove(channel=self.channel,
                                   timestamp=self.timestamp)
        except Exception:
            return False
