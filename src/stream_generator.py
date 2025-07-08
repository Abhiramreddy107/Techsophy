import time
import random
import uuid

def telematics_stream(trip_id=None, duration=60):
    trip_id = trip_id or str(uuid.uuid4())
    for second in range(duration):
        yield {
            "trip_id": trip_id,
            "timestamp": second,
            "speed": random.randint(20, 120),
            "acceleration": random.uniform(-4, 4),
            "braking": random.uniform(0, 1)
        }
        time.sleep(0.1)

