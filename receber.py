#!/usr/bin/env python
import pika
import json
from pymongo import MongoClient 
import base64

credentials = pika.PlainCredentials('dodo', 'dodo123.') 
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    
    data = json.loads(body)
    print(body)

    client = MongoClient("mongodb://localhost:27017/")
    mydatabase = client['teste']
    mycol = mydatabase['col']
    mycol.insert(data)
    
channel.basic_consume(callback,queue='hello',no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
