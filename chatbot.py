import requests
import random
import time


channelId = "1236923417668747315"
token = "NzU2MTYxNTE4MjE0NzA5Mjc4.G_8eXn.hgJ_QsiC1_lUYDTnPclNbAP20Xxg4xMXscmhW0"
url = "https://discord.com/api/v9/channels/" + channelId + "/messages"
headers = {
    "Authorization" : token
}


def send_message(random_time):
    payload = {
        "content": f"test owo chatbot in {random_time} seconds"
    }
    res = requests.post(url, json=payload, headers=headers)
    print(f"Message sent: {res.status_code} + time: {random_time} ")

interval_min = 1  # Minimum interval in seconds
interval_max = 10  # Maximum interval in seconds

# while True:
#     interval = random.randint(interval_min, interval_max)
#     send_message(interval)
#     time.sleep(interval)
    
# Get the number of iterations from the user
num_iterations = int(input("Số lần test: "))

for _ in range(num_iterations):
    interval = random.randint(interval_min, interval_max)
    send_message(interval)
    time.sleep(interval)