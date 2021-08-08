import discord
import asyncio
import random

client = discord.Client()

token = "ODczODg4MTU4OTg1NjQ2MTEw.YQ-9xQ.WxpuT3pg3JxTqpijYH7vlDKOIE0"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 불러와졌습니다.')
    game = discord.Game('시그널타운 전용 봇')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "시그널":
        await message.channel.send("https://discord.gg/z5eNHDh5Xr")

    if message.content == "타운장 정보":
        await message.channel.send("남자 / 비공 / 특징 : 여친있음")
    
    if message.content == "랜덤뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            d = "실패"
        if ran == 1:
            d = "성공"
        await message.channel.send(d)

client.run(token)