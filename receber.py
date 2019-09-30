#!/usr/bin/env python
import pika, os
import json
from pymongo import MongoClient 
import base64

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('popzhidh', 'amqp://popzhidh:SUZJ6DD-2XCF2ms9b35bv3hgIqMOXyB4@spider.rmq.cloudamqp.com/popzhidh')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))
    data = []
    data = json.loads(body)
    print(body)

    client = MongoClient("mongodb://localhost:27017/")
    mydatabase = client['teste']
    mycol = mydatabase['col']
    mycol.insert(data)



channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)


print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()


