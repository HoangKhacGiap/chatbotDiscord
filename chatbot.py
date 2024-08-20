import discord
import random
import asyncio
import requests

# Khởi tạo bot với intents phù hợp
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Cần thiết để đọc nội dung tin nhắn
client = discord.Client(intents=intents)

# Token và Channel ID cố định
TOKEN = input("|input your bot token here: ").strip()  # Gán giá trị nhập vào cho biến TOKEN
USER_TOKEN = input("|input your user token here: ").strip()  # Gán giá trị nhập vào cho biến USER_TOKEN
CHANNEL_ID = input("|input your channel id here: ").strip()  # Gán giá trị nhập vào cho biến CHANNEL_ID

# Biến để kiểm soát việc dừng bot
stop_bot = False

# Định nghĩa sự kiện khi bot sẵn sàng
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(send_messages())

# Định nghĩa sự kiện khi nhận được tin nhắn
@client.event
async def on_message(message):
    global stop_bot, pause_bot
    if message.content.upper() == "STOP":
        stop_bot = True
        pause_bot = False
        await message.channel.send("Bot has been stopped.")
    elif message.content.upper() == "CONTINUE":
        if stop_bot:
            await message.channel.send("Bot has been stopped and cannot continue.")
        else:
            pause_bot = False
            await message.channel.send("Bot has been continued.")

# Hàm gửi tin nhắn ngẫu nhiên
async def send_messages():
    interval_min = 15  # Minimum interval in seconds
    interval_max = 20  # Maximum interval in seconds
    
    # Get the list of messages from the user
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

    while not stop_bot:
        for message in messages:
            if stop_bot:
                break
            interval = random.randint(interval_min, interval_max)
            await send_message(interval, message)
            await asyncio.sleep(interval)

# Hàm gửi tin nhắn
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

# Chạy bot với token đã cố định
client.run(TOKEN)