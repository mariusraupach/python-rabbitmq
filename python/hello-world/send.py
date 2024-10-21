import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")

channel.queue_declare(queue="hello")

channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)
