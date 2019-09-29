#!/usr/bin/env python
import pika
import json
import base64

json_file = None
with open("file.json", "rb") as imageFile:
    json_file = base64.b64encode(imageFile.read())

credentials = pika.PlainCredentials('dodo', 'dodo123.') 
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json_file)
print(" [x] Sent 'Hello World!'")
connection.close()
