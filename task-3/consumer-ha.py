import pika
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 5672
print(f" Consumer started on port {port}")
print("To exit press CTRL+C")

credentials = pika.PlainCredentials('admin', 'password')

def callback(ch, method, properties, body):
print(f" Received: {body.decode()}")

connection = pika.BlockingConnection(pika.ConnectionParameters(
host='localhost', port=port, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
