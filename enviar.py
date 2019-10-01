#!/usr/bin/env python
import pika, os
import json
import base64
import urllib

response = urllib.urlopen("file.json").read()

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('popzhidh', 'amqp://popzhidh:SUZJ6DD-2XCF2ms9b35bv3hgIqMOXyB4@spider.rmq.cloudamqp.com/popzhidh')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(json.loads(response)))

print(" [x] Sent 'Hello World!'")
connection.close()

