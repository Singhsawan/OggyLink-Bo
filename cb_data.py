from botbtns import *

API_ID = 29362464
API_HASH = '31973315b0872a0478886de31a1e4848'

TOKEN = '6053293403:AAH1CVfHg-Yxfv2D-Ei9CvtV1tQVkziwuE0'


@app.on_callback_query(filters.regex('about_data'))
async def query_handler(_, query):
    name = query.from_user.first_name
    await query.message.edit(
        text=f'<b>{about_txt}</b>'.format(name), reply_markup=about_btns, disable_web_page_preview=True)


@app.on_callback_query(filters.regex('back_data'))
async def back_handler(_, query):
    name = query.from_user.first_name
    await query.message.edit(text=start_msg_txt.format(name), reply_markup=start_btns, disable_web_page_preview=True)

@app.on_callback_query(filters.regex('help_data'))
async def back_handler(_, query):
    name = query.from_user.first_name
    await query.message.edit(text=commands.format(name), reply_markup=about_btns, disable_web_page_preview=True)


@app.on_callback_query(filters.regex('connect_api'))
async def connect_handler(_, query):
    await query.message.edit(
        text=connect_txt, reply_markup=connect_btns, disable_web_page_preview=True)
