# stream_generator.py
import time, random

def telematics_stream(trip_id="trip-001", duration=60):
    for second in range(duration):
        yield {
            "trip_id": trip_id,
            "timestamp": second,
            "speed": random.randint(20, 120),
            "acceleration": random.uniform(-4, 4),
            "braking": random.uniform(0, 1)
        }
        time.sleep(0.1)

