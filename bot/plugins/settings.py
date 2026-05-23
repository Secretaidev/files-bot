from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot.database.db_manager import db
from bot.core.aesthetics import Aesthetics

from bot.utils.monitor import monitor

@Client.on_message(filters.command("status") & filters.user(Config.SUDO_USERS))
async def status_handler(client, message):
    await message.reply_text(monitor.get_stats())

@Client.on_message(filters.photo & filters.private)
async def set_thumbnail_handler(client: Client, message: Message):
    user_id = message.from_user.id
    file_id = message.photo.file_id
    db.set_thumbnail(user_id, file_id)
    
    await message.reply_text(
        text=Aesthetics.bold_small_caps("✅ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!"),
        quote=True
    )

@Client.on_message(filters.command("settings") & filters.private)
async def settings_handler(client: Client, message: Message):
    user_id = message.from_user.id
    thumb = db.get_thumbnail(user_id)
    
    text = Aesthetics.bold_small_caps("⚙️ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ") + "\n\n"
    text += Aesthetics.small_caps(f"• ᴜꜱᴇʀ ɪᴅ: {user_id}\n")
    text += Aesthetics.small_caps(f"• ᴛʜᴜᴍʙɴᴀɪʟ: {'✅ ꜱᴇᴛ' if thumb else '❌ ɴᴏᴛ ꜱᴇᴛ'}")
    
    buttons = []
    if thumb:
        buttons.append([InlineKeyboardButton(Aesthetics.small_caps("🗑️ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ"), callback_data="del_thumb")])
    
    await message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons) if buttons else None,
        quote=True
    )

@Client.on_callback_query(filters.regex("^del_thumb$"))
async def del_thumb_callback(client: Client, query):
    user_id = query.from_user.id
    db.set_thumbnail(user_id, None)
    await query.message.edit_text(Aesthetics.bold_small_caps("✅ ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ!"))
