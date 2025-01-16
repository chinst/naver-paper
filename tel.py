# -*- coding: utf-8 -*-

import os
import time
import asyncio
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import urllib3
import re

#Foxtcbot
#TOKEN = "5732189158:AAE3gB-k0bBeXU4eHuFJJEbekQTLkM-L4Fo"

#foxsvcBot
TOKEN = "5803219148:AAFcQQUwTZmC3x1DzI2PhCNBLM7abIuOFzQ"
CHAT_ID = '5787735214'

# proxy_url = 'http://168.219.61.252:8080/'

def read_content(file):
    with open(file, 'rt') as f:
        content = f.read()
    return content

async def send_message(bot, msg):
    await bot.send_message(chat_id=CHAT_ID, text=msg)

async def send_long_message(bot, text):
    if len(text) <= 4096:
        await send_message(bot, text)
    else:
        parts = []
        while len(text) > 0:
            if len(text) > 4080:
                part = text[:4080]
                first_lnbr = part.rfind('\n')
                if first_lnbr != -1:
                    parts.append(part[:first_lnbr])
                    text = text[first_lnbr:]
                else:
                    parts.append(part)
                    text = text[4080:]
            else:
                parts.append(text)
                break

        for part in parts:
            await send_message(bot, part)

if __name__ == '__main__':
    content = read_content('log.txt')

    bot = telegram.Bot(token=TOKEN)
    asyncio.run(send_long_message(bot, content))
    #bot.send_message(chat_id=CHAT_ID, text=content)

