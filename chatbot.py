import requests
import random
import time


# channelId = "input your channel id here"
# token = "input your token here"

print ("=====================auto chat bot==========================")
token = input("|input your token here: ")
channelId = input("|input your channel id here: ")

url = "https://discord.com/api/v9/channels/" + channelId + "/messages"
headers = {
    "Authorization" : token
}

def send_message(random_time, message):
    payload = {
        "content": f"{message}"
    }
    res = requests.post(url, json=payload, headers=headers)
    print(f"Message sent: {res.status_code} + time: {random_time} ")

interval_min = 15  # Minimum interval in seconds
interval_max = 16  # Maximum interval in seconds


# Get the number of iterations from the user
# num_iterations = int(input("|Số lần test: "))

# Get the list of messages from the user
messages = []
# for i in range(num_iterations):
while True:
    i=0
    message = input(f"|Nhập tin nhắn thứ {i+1}: ")
    if message.upper() == "OK":
        break
    messages.append(message)  
print("============================================================")

# Send the messages
# for _ in range(num_iterations):
while True:
    for message in messages:
        interval = random.randint(interval_min, interval_max)
        send_message(interval, message)
        time.sleep(interval)