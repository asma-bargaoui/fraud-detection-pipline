from kafka import KafkaProducer
from faker import Faker
import json
import time
import random
import uuid

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(1, 50)}",
        "amount": round(random.uniform(5, 2000), 2),
        "location": fake.city(),
        "merchant": fake.company(),
        "card_type": random.choice(["visa", "mastercard"]),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    while True:
        txn = generate_transaction()
        producer.send('transactions', value=txn)
        print(f"Sent: {txn}")
        time.sleep(random.uniform(0.5, 2))