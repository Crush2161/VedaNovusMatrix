from pyrogram import filters, Client
from pyrogram.types import Message
from unidecode import unidecode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TusharMusic import app
from TusharMusic.misc import SUDOERS
from TusharMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from TusharMusic.utils.database import add_served_chat
from TusharMusic.utils.database import get_assistant

async def generate_join_link(chat_id: int):
    invite_link = await app.export_chat_invite_link(chat_id)
    return invite_link

def ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix


@app.on_message(filters.command(["join","vc","song","rankings", "config", "topgroups", "topusers", "topgame", "mytop", "ok", "bye", "welcome", "thanks","hii"] ,prefixes=["","/"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


@app.on_message(filters.command(["activevc", "activevoice"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:            await mystic.edit_text(f"» No active voice chats on {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» List of Currently Active Voice Chats :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» Getting active video chats list...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» No Active Video Chats on {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» List of currently active video chats:</b>\n\n{text}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.command(["ac","all","av"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(f"✫ <b><u>Active Chats Info</u></b>:\n\nVoice: {ac_audio}\nVideo: {ac_video}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('✯ Close ✯', callback_data=f"close")]]))
