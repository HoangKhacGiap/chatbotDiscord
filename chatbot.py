import discord
import random
import asyncio
import requests

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  
client = discord.Client(intents=intents)

TOKEN = input("|input your token here: ").strip()  # Gán giá trị nhập vào cho biến TOKEN
USER_TOKEN = input("|input your user token here: ").strip()  # Gán giá trị nhập vào cho biến USER_TOKEN
CHANNEL_ID = input("|input your channel id here: ").strip()  # Gán giá trị nhập vào cho biến CHANNEL_ID

stop_bot = False
pause_bot = False

messages = []

send_messages_task = None

@client.event
async def on_ready():
    global send_messages_task
    print(f'Logged in as {client.user}')
    send_messages_task = client.loop.create_task(send_messages())

@client.event
async def on_message(message):
    global stop_bot, pause_bot, messages, send_messages_task
    if "human" in message.content:
        stop_bot = True
        pause_bot = False
        await message.channel.send("@everyone Bot has been stopped.")
    elif message.content.upper() == "CAPCHA DONE":
        stop_bot = False
        pause_bot = False
        if not messages:  # Chỉ yêu cầu nhập lại nếu danh sách tin nhắn hiện tại trống
            messages = get_messages_from_user()
        await message.channel.send("Bot has been continued.")
        if send_messages_task is None or send_messages_task.done():
            send_messages_task = client.loop.create_task(send_messages())

def get_messages_from_user():
    messages = []
    print("Nhập tin nhắn của bạn (nhập 'OK' để dừng):")
    i = 0
    while True:
        i += 1
        message = input(f"|Nhập tin nhắn thứ {i}: ")
        if message.upper() == "OK":
            break
        messages.append(message)
    print("============================================================")
    return messages

async def send_messages():
    global messages
    interval_min = 8  
    interval_max = 9  
    
    if not messages:
        messages = get_messages_from_user()

    while not stop_bot:
        for message in messages:
            while stop_bot:
                await asyncio.sleep(1)  
            while pause_bot:
                await asyncio.sleep(1)  
            interval = random.randint(interval_min, interval_max)
            await send_message(interval, message)
            await asyncio.sleep(interval)

async def send_message(random_time, message):
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": USER_TOKEN
    }
    payload = {
        "content": f"{message}"
    }
    res = requests.post(url, json=payload, headers=headers)
    print(f"Message sent: {res.status_code} + time: {random_time} ")

client.run(TOKEN)