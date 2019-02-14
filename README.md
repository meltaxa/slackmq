# SlackMQ

Slack can do the heavy lifting of a simple Message Queue. When a message is received,
it is "locked" while being processed. This keeps other worker bots from processing the
message simultaneously.

SlackMQ is suited to high latency message queuing applications due to rate limiting.
For a minimalist architecture, leverage the power of SlackMQ and a Slack bot becomes 
highly available out of the box.

To install:
```
pip install slackmq
```

The Slack API allows pins to be added once per message per channel. Also, reactions
and stars can be added to a message once per bot. For example, a person or bot cannot
pin a message that has already been pinned. A user or bot cannot give a post a thumbs 
up twice. In the UI, if you try, the action is revoked. In the API, an exception is 
thrown.

![SlackMQ workflow](https://github.com/meltaxa/slackmq/blob/master/docs/slackmq-workflow.png?raw=true)

Slack can be made to behave like a basic Message Queuing system by using pins to 
acknowledge (lock) and unacknowledge a message, as demonstrated in the diagram above. 
Using pins is ideal as this allows "unlimited" bot workers. The Slack RTM API also 
allows a bot to connect multiple times. With this account concurrency, this method 
limits the bot to 16 concurrent workers. You may find using a combination of pins, 
stars and reactions more reliable for low latency messages.

To use SlackMQ, wrap the post acknowledgement around a bot action. Below is an example
of how a bot (using the slackbot library) uses SlackMQ to pull from the "queue", i.e, 
the channel.

```python
from slackmq import slackmq
from slackbot.bot import listen_to
import socket

API_TOKEN = 'SLACK-BOT-API-TOKEN'


@listen_to('hello')
def helloworld(message):
    post = slackmq(API_TOKEN,
                   message.body['channel'], 
                   message.body['ts'])
    if post.ack():
        message.send('Hello from {}.'.format(socket.gethostname()))
        post.unack()
```

# Implementation Examples

Troupe, which is a group of Slack bots working together to control and operate a smart 
home implements SlackMQ. 
- See Troupe's source code for an insight into SlackMQ usage: https://github.com/meltaxa/troupe.

Another implementation of SlackMQ is to perform DevOps manoeuvres, such as
Remote Management, Continuous Delivery, Canary Deployments and Rolling Updates. In the
Troupe example, a Federation of Slack bots can self-update with zero downtime using the
SlackMQ library. Watch The Travelling DevOps Troupe in action:

[![The Travelling DevOps Troupe](http://img.youtube.com/vi/7TuYA2jt-Vc/0.jpg)](https://www.youtube.com/watch?v=7TuYA2jt-Vc "The Travelling DevOps Troupe")
