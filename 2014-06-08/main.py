## libraries
import math
import random
import time

## Never ends
while True:
    sc = "SmatestChild: "
    user_response = input(sc + "Hello, how are you?\n")
    if "good" in user_response:
        time.sleep(random.randint(2,6))
        user_response = input(sc + "That's awsome! Glad to hear it.\n")
    elif "bad" in user_response or "terrible" in user_response:
        time.sleep(random.randint(2,6))
        user_response = input(sc + "How unfortunate. :.(\n")
    else:
        time.sleep(random.randint(2,6))
        user_response = input(sc + "I didn't understand.\n")
