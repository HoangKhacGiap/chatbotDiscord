import requests
import random
import time


# channelId = "input your channel id here"
# token = "input your token here"

print ("=====================auto chat bot==========================")
channelId = input("|input your channel id here: ")
token = input("|input your token here: ")

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
    
# Get the number of iterations from the user
num_iterations = int(input("|Số lần test: "))
print("============================================================")

for _ in range(num_iterations):
    interval = random.randint(interval_min, interval_max)
    send_message(interval)
    time.sleep(interval)