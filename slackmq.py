from slacker import Slacker
from time import sleep

class slackmq(object):
  def __init__(self, api_token, channel, timestamp):
    self.api_token = api_token
    self.channel = channel
    self.timestamp = timestamp

  def ack(self, emoji=None):
    try:
      slack = Slacker(self.api_token)
      slack.stars.add(channel = self.channel, timestamp = self.timestamp)
 
      if emoji != None:
        slack.reactions.add(emoji, channel = self.channel, timestamp = self.timestamp)

      slack.pins.add(channel = self.channel, timestamp = self.timestamp)
    except:
      return False

    return True

  def unack(self, emoji=None):
    try:
      slack = Slacker(self.api_token)
      slack.pins.remove(channel = self.channel, timestamp = self.timestamp)
      sleep(3)
      if emoji != None:
        slack.reactions.remove(emoji, channel = self.channel, timestamp = self.timestamp)
      sleep(5)
      slack.stars.remove(channel = self.channel, timestamp = self.timestamp)
    except:
      return False
