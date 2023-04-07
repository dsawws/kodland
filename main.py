import settings
import discord
import random

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)


# Когда бот будет готов, он напишет в консоли свое название!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Когда бот будет получать сообщение, он будет отправлять в этот же канал какие-то сообщения!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$num'):
        await message.channel.send(num(10))
    else:
        await message.channel.send("Я не понимаю такую команду!")






def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    
def num ():
    number=random.randint(0, 10)
    print(number)

 
client.run(settings["TOKEN"])
