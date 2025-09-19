import pika

def main():
print("RabbitMQ Producer Started")

text
credentials = pika.PlainCredentials('admin', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
print("Queue 'hello' declared")

message = 'Hello World from RabbitMQ!'
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" Sent: '{message}'")

connection.close()
print("Connection closed")
if name == "main":
main()
