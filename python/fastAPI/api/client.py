import json
import uuid
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

corr_id = str(uuid.uuid4())

request = {
    "id": corr_id,
    "version": "v1",
    "action": "create_apartment",
    "data": {
        "city": "Казань",
        "price": 9000000,
        "rooms": 3
    },
    "auth": "API_KEY_123"
}

channel.basic_publish(
    exchange="",
    routing_key="api.requests",
    body=json.dumps(request)
)

def on_response(ch, method, properties, body):
    response = json.loads(body)
    if response["correlation_id"] == corr_id:
        print(response)
        ch.stop_consuming()

channel.basic_consume(queue="api.responses", on_message_callback=on_response, auto_ack=True)
channel.start_consuming()
