import pika
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 5672
print(f" Producer started on port {port}")

credentials = pika.PlainCredentials('admin', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
host='localhost', port=port, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
message = f'Test message to port {port}'
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" Sent: '{message}'")

connection.close()
