import pika, os, sys

def main():
    # establish a connection with rabbitmq server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # re declare the queue because we are unsure whether or not the queue exists
    channel.queue_declare(queue='hello')

    # rabbitmq will trigger this function once we receive a message.
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # subscribe to hello "queue"
    channel.basic_consume(queue="hello", on_message_callback=callback , auto_ack=True)

    print(" [*] Waiting for a message. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    main()
    

