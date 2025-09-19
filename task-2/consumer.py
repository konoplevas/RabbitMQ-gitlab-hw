import pika

def callback(ch, method, properties, body):
print(f" Received: {body.decode()}")

def main():
print("RabbitMQ Consumer Started")
print("Waiting for messages...")
print("To exit press CTRL+C")

text
credentials = pika.PlainCredentials('admin', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
print("Queue 'hello' declared")

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
if name == "main":
main()
