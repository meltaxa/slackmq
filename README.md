# SlackMQ

Enables a common Message Queue mechanism for "message locking" within Slack. 
When a message is sent to a channel, a Slack bot can acknowledge the message 
and “lock” it for processing. This keeps other worker bots from processing the 
message simultaneously.

SlackMQ leverages the Slack API method for pinning, reactions and starring of 
messages, where only one is allowed per post per user (or bot) account. 

A Slack worker bot can use the same API token to connect to Slack up to 16 
times. This is a restriction imposed by Slack.

SlackMQ is not a replacement for dedicated Message Brokers and Queue systems. It
only does simple message locking and is suitable for managing low bandwidth
tasks or applications. For those use cases, it's one less moving part and makes
Slack do the heavy lifting.

To install:
```
pip install slackmq
```

## Message Locking Anatomy

A star and pin action are both used to "lock" a message. 

The star is not seen in the Slack channel, as it is only visible by the user 
creating the star.

Pins and reactions are visible to everyone in the channel.

To avoid race conditions, where two or more bots simultaneously star the
same message (the Slack API says it shouldn't but it can happen), a second 
action (the star) is invoked. An optional third action (a reaction emoji) for 
extra protection can also be invoked.

## Example: The Slack Worker Bot

For high availability and scalability reasons, multiple worker bots could be 
deployed through out a network. Using the Slackbot python library to listen and 
respond to certain Slack posts, all the bots will receive the message, but the 
first to acknowledge the message will be able to process it. 

```
from slackmq import slackmq
from slackbot.bot import listen_to
import socket

API_TOKEN = 'YOUR-BOT-API-TOKEN'

@listen_to('hostname')
def myhostname(message):
    post = slackmq(API_TOKEN,
                   message.body['channel'], 
                   message.body['ts'])
    if post.ack():
        message.send('I am running on {}.'.format(socket.gethostname()))
        # Removes the visible pin (and hidden star) from the channel.
        post.unack()
```

## Example: Continuous Delivery with SlackMQ

Watch Continuous Delivery with SlackMQ in action, deploying a home automation
application across several hosts. From Continuous Integration to an automated
canary deployment. Once approved, a rolling deployment occurs with zero 
downtime.

Video has no audio:

[![Continuous Delivery with SlackMQ](http://img.youtube.com/vi/YW6IdsvdxXI/0.jpg)](http://www.youtube.com/watch?v=YW6IdsvdxXI "Continuous Delivery with SlackMQ")
