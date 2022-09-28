# Dear Piro Plz Dont remove this line 
# By @itz_mst_boi
# source:-  https://github.com/Noob-mukesh/password

"""from pyrogram import Client, filters
from pyrogram.types import *
import requests"""
import random  
import string
"""import os
import re

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 

bot = Client(
    "mukeshBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

@bot.on_message(filters.command("start"))
async def start(client, message):
        await message.reply_text("Hi! My name is Ishi. I'm an Artificial Intelligence\n /chatbot - [on|off]")


"""
ran1=string.ascii_uppercase
#print(ran1)
ran2=string.ascii_lowercase
ran3=string.punctuation
ran4=string.digits
print("Tools to generate Random Password using Termux\n By Mukesh ")
print(" Hint ? Password Strength \n [1-test , 2-lowest , 3-lower ]\n[ 4- low 5-Normal , 6-Strong] \n[ 7- strongest, 8-very-Strong]\n")
password=int(input('Enter Password length\n'))
ran=[]
ran.extend(list(ran1))
ran.extend(list(ran2))
ran.extend(list(ran3))
ran.extend(list(ran4))
print(ran)
print('Your Password is:\n')
random.shuffle(ran)
print("" .join(ran[0:password]))
print(" \n Join @Mukeshbotzone for More  By @itz_mst_boi")
#bot.run()
