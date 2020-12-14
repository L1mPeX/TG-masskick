import telebot
import telethon
from telethon import TelegramClient, events
from time import sleep as ts
import logging
import datetime
import asyncio
import string
import re
import threading
from telethon.tl.functions.account import UpdateProfileRequest
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

bot=telebot.TeleBot('')

api_id = 
api_hash = ''
bot_token=''
client = TelegramClient('ani', api_id, api_hash)
client.parse_mode=None
 
@client.on(events.NewMessage)

async def my_event_handler(event):

  if event.raw_text=="/allsucks":
    await event.delete()
    
    chatId = event.chat_id
    i = 0
    while i == 0:
        async for u in client.iter_participants(int(event.chat_id)):
    	    try:
    		    if u.id != ... and u.id != ...:
    		      if u.id != ...:
    		  	    bot.kick_chat_member(chatId, u.id)
    		        
    	    except Exception as e:
    	      print(str(u.id) + " is administrator")
    	      pass



client.start()
client.run_until_disconnected()

#@hackvslom - Telegram

#@hackvslom - Telegram

#@hackvslom - Telegram
