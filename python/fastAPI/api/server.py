import json
import pika
import time

API_KEY = "API_KEY_123"
processed_ids = set()
apartments = []

MAX_RETRIES = 3

def on_request(ch, method, properties, body):
    try:
        message = json.loads(body)
        msg_id = message["id"]

        if msg_id in processed_ids:
            ch.basic_ack(method.delivery_tag)
            return

        if message.get("auth") != API_KEY:
            send_response(msg_id, "error", None, "Unauthorized")
            ch.basic_ack(method.delivery_tag)
            return

        processed_ids.add(msg_id)

        action = message["action"]
        data = message.get("data", {})

        if action == "create_apartment":
            apartment = {
                "id": f"apt-{len(apartments)+1}",
                **data
            }
            apartments.append(apartment)
            send_response(msg_id, "ok", apartment, None)

        elif action == "list_apartments":
            send_response(msg_id, "ok", apartments, None)

        else:
            send_response(msg_id, "error", None, "Unknown action")

        ch.basic_ack(method.delivery_tag)

    except Exception as e:
        retries = properties.headers.get("x-retries", 0) if properties.headers else 0

        if retries < MAX_RETRIES:
            headers = properties.headers or {}
            headers["x-retries"] = retries + 1
            time.sleep(1)

            ch.basic_publish(
                exchange="",
                routing_key="api.requests",
                body=body,
                properties=pika.BasicProperties(headers=headers)
            )
            ch.basic_ack(method.delivery_tag)
        else:
            ch.basic_nack(method.delivery_tag, requeue=False)

def send_response(corr_id, status, data, error):
    response = {
        "correlation_id": corr_id,
        "status": status,
        "data": data,
        "error": error
    }
    channel.basic_publish(
        exchange="",
        routing_key="api.responses",
        body=json.dumps(response)
    )

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(
    queue="api.requests",
    durable=True,
    arguments={
        "x-dead-letter-exchange": "",
        "x-dead-letter-routing-key": "api.requests.dlq"
    }
)

channel.queue_declare(queue="api.responses", durable=True)
channel.queue_declare(queue="api.requests.dlq", durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="api.requests", on_message_callback=on_request)

print("Server started")
channel.start_consuming()
