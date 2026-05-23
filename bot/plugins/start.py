from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from bot.core.aesthetics import Aesthetics
from bot.config import Config
from bot.utils.logger import logger

from bot.utils.resilience import zen_resilience

@Client.on_message(filters.command("start") & filters.private)
@zen_resilience
async def start_handler(client: Client, message: Message):
    await logger.log_user(client, message, "START_COMMAND")
    text = Aesthetics.bold_small_caps(Config.START_MSG) + "\n\n"
    text += Aesthetics.small_caps(
        "ɪ ᴀᴍ ᴛʜᴇ ᴡᴏʀʟᴅ'ꜱ ᴍᴏꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ꜰɪʟᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.\n"
        "ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴛᴏ ꜱᴛᴀʀᴛ ᴍᴀɢɪᴄ!\n\n"
        "© 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ᴛᴇᴄʜ"
    )
    
    buttons = [
        [
            InlineKeyboardButton(Aesthetics.small_caps("💡 ʜᴇʟᴘ"), callback_data="help"),
            InlineKeyboardButton(Aesthetics.small_caps("⚙️ ꜱᴇᴛᴛɪɴɢꜱ"), callback_data="settings")
        ],
        [
            InlineKeyboardButton(Aesthetics.small_caps("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ"), url="https://t.me/BotFather")
        ]
    ]
    
    await message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

@Client.on_callback_query(filters.regex("^help$"))
async def help_callback(client: Client, query):
    text = Aesthetics.bold_small_caps("🔱 ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ᴛᴏᴏʟᴋɪᴛ") + "\n\n"
    text += Aesthetics.small_caps(
        "• 📁 **ꜰɪʟᴇ ʀᴇɴᴀᴍᴇʀ**: ꜱᴇɴᴅ ᴀɴʏ ꜰɪʟᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ.\n"
        "• ✂️ **ᴀᴜᴛᴏ-ꜱᴘʟɪᴛᴛᴇʀ**: ꜰɪʟᴇꜱ > 2ɢʙ ᴀʀᴇ ꜱᴘʟɪᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ.\n"
        "• 📥 **ʙᴀᴛᴄʜ ᴢɪᴘᴘᴇʀ**: ᴜꜱᴇ /zip ᴛᴏ ꜱᴛᴀᴄᴋ ᴍᴜʟᴛɪᴘʟᴇ ꜰɪʟᴇꜱ.\n"
        "• 🎬 **ᴍᴇᴅɪᴀ ᴀɪ**: ᴀᴜᴛᴏ-ᴛʜᴜᴍʙɴᴀɪʟꜱ & ᴅᴇᴇᴘ ᴘʀᴏʙɪɴɢ.\n"
        "• 📡 **ꜱᴛʀᴇᴀᴍ ʜᴜʙ**: ɪɴꜱᴛᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜱᴛʀᴇᴀᴍ ʟɪɴᴋꜱ.\n"
        "• 🔓 **ᴀʀᴄʜɪᴠᴇʀ**: ᴇxᴛʀᴀᴄᴛ ᴀɴʏ ᴀʀᴄʜɪᴠᴇ ᴡɪᴛʜ 1-ᴛᴀᴘ."
    )
    
    buttons = [[InlineKeyboardButton(Aesthetics.small_caps("⬅️ ʙᴀᴄᴋ"), callback_data="start_back")]]
    await query.message.edit_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("^start_back$"))
async def start_back_callback(client: Client, query):
    text = Aesthetics.bold_small_caps(Config.START_MSG) + "\n\n"
    text += Aesthetics.small_caps(
        "ɪ ᴀᴍ ᴛʜᴇ ᴡᴏʀʟᴅ'ꜱ ᴍᴏꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ꜰɪʟᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.\n"
        "ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴛᴏ ꜱᴛᴀʀᴛ ᴍᴀɢɪᴄ!\n\n"
        "© 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ᴛᴇᴄʜ"
    )
    buttons = [
        [
            InlineKeyboardButton(Aesthetics.small_caps("💡 ʜᴇʟᴘ"), callback_data="help"),
            InlineKeyboardButton(Aesthetics.small_caps("⚙️ ꜱᴇᴛᴛɪɴɢꜱ"), callback_data="settings")
        ],
        [InlineKeyboardButton(Aesthetics.small_caps("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ"), url="https://t.me/BotFather")]
    ]
    await query.message.edit_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
