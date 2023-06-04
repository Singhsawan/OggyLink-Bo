import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.errors import MediaCaptionTooLong
from transcripts import *


sudo_users = [5651594253]

# BOT INFO
TOKEN = os.environ.get("BOT_TOKEN", "6053293403:AAH1CVfHg-Yxfv2D-Ei9CvtV1tQVkziwuE0")
API_HASH = os.environ.get("HASH", '31973315b0872a0478886de31a1e4848')
API_ID = int(os.environ.get("ID", '29362464'))


app = Client("Url-Short-app", api_id=API_ID,
             api_hash=API_HASH, bot_token=TOKEN, workers=50)


# Start Button
start_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("❓ HELP", callback_data="help_data"),
     InlineKeyboardButton("About me 🤖", callback_data="about_data"),
     ],
    [InlineKeyboardButton("Connect Your API 🔗", callback_data="connect_api"
                          ), ]
])


# Back Button
about_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("◀️ Back️", callback_data="back_data"), ],
])


# Connect button
connect_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("GET API TOKEN 🔑", url="https://omnifly.in.net/member/tools/api")],
    [InlineKeyboardButton("❓ HELP", callback_data="help_data"), InlineKeyboardButton("◀️ Back️", callback_data="back_data")]
])
