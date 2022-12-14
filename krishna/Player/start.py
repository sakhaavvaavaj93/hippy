import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from krishna.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT


ALIVE_PIC = START_PIC

HOME_TEXT = """ðð» **Hi Sir [{}](tg://user?id={})** \n\nð¤ Im **krishna Vc Player**. \n**I Can Stream music On Voice Chat Of Telegram Groups**"""

HELP_TEXT = """
ð·ï¸ **Setup Guide** :

\u2022 Start a voice chat in your group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Done Setup Process Read Commands Below ð.
"""



USER_TEXT = """
ð·ï¸ **Users Commands** :

\u2022 /play <Query> To Play a Song.
\u2022 /song To Download A Audio file from YouTube. 
\u2022 /video to download Videos.
"""

ADMIN = """
ð·ï¸ **admin Commands** :

\u2022 /userbotjoin To Invite Assistant To Your Chat.
\u2022 /end To End Streaming.
\u2022 /pause To Pause Stream.
\u2022 /resume To Resume Stream.
\u2022 /volume To Set Volume.
\u2022 /skip To Skip Tracks.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("ð® Aá´á´ÉªÉ´ê±", url="https://telegra.ph/ðooo--âá´ê°á´-á´ê°ê°ÊÉªÉ´á´-05-17-2"),
                InlineKeyboardButton("ð¨ï¸ Uê±á´Êê±", callback_data="users"),
            ],
            [
                InlineKeyboardButton("ð Bá´á´á´", callback_data="home"),
                InlineKeyboardButton("ð¤· CÊá´ê±á´", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("ð§ Aá´á´ Má´ Tá´ Yá´á´Ê CÊá´á´", url='https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("ð Sá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("ð·ï¸ CÊá´É´É´á´Ê", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("ð¤ Há´Êá´ & Cá´á´á´á´É´á´ê±", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users":
        buttons = [
            [
                InlineKeyboardButton("ð Bá´á´á´", callback_data="help"),
                InlineKeyboardButton("ð¤· CÊá´ê±á´", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="admins":
        buttons = [
            [
                InlineKeyboardButton("ð Bá´á´á´", callback_data="help"),
                InlineKeyboardButton("ð¤· CÊá´ê±á´", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(ADMIN, reply_markup=reply_markup)
        except MessageNotModified:
            pass
    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons = [
            [
                InlineKeyboardButton("ð§ Aá´á´ Má´ Tá´ Yá´á´Ê CÊá´á´", url=f'https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("ð Sá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("ð·ï¸ Oê°ê°Éªá´Éªá´Ê CÊá´É´É´á´Ê", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("ð¤ Há´Êá´ & Cá´á´á´á´É´á´ê±", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client: Client, message: Message):
    get_me = await client.get_me()   
    buttons = [
            [
                InlineKeyboardButton("ð® Aá´á´ÉªÉ´ê±", url="https://telegra.ph/ðooo--âá´ê°á´-á´ê°ê°ÊÉªÉ´á´-05-17-2"),
                InlineKeyboardButton("ð¨ï¸ Uê±á´Êê±", callback_data="users"),
            ],
            [
                InlineKeyboardButton("ð Bá´á´á´", callback_data="home"),
                InlineKeyboardButton("ð¤· CÊá´ê±á´", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=f"{HELP_TEXT}", reply_markup=reply_markup)
