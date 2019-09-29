#!/usr/bin/env python
import pika
import json
import base64

data = []
with open('file.json') as json_file:
    data = json.load(json_file)
message = json.dumps(data)


credentials = pika.PlainCredentials('dodo', 'dodo123.') 
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent 'Hello World!'")
connection.close()
