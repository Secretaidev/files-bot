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
        "ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ꜰɪʟᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.\n"
        "ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴛᴏ ꜱᴛᴀʀᴛ ᴍᴀɢɪᴄ!\n\n"
        "© 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ᴛᴇᴄʜ"
    )
    
    buttons = [
        [
            InlineKeyboardButton(Aesthetics.small_caps("💡 ʜᴇʟᴘ"), callback_data="help"),
            InlineKeyboardButton(Aesthetics.small_caps("⚙️ ꜱᴇᴛᴛɪɴɢꜱ"), callback_data="settings")
        ],
        [
            InlineKeyboardButton(Aesthetics.small_caps("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ"), url="https://t.me/its_me_secret")
        ]
    ]
    
    await message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

@Client.on_callback_query(filters.regex(r"^help_"))
@zen_resilience
async def help_pagination(client, query):
    page = query.data.split("_")[1]
    
    if page == "main":
        text = Aesthetics.bold_small_caps("🔱 ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ᴄᴏᴍᴍᴀɴᴅ ᴏʀᴀᴄʟᴇ") + "\n\n"
        text += Aesthetics.small_caps("ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ɢᴜɪᴅᴇ. ꜱᴇʟᴇᴄᴛ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ᴛᴏ ᴜɴʟᴏᴄᴋ ɪᴛꜱ ꜱᴇᴄʀᴇᴛꜱ:")
        buttons = [
            [
                InlineKeyboardButton(Aesthetics.small_caps("📁 ꜰɪʟᴇꜱ"), callback_data="help_files"),
                InlineKeyboardButton(Aesthetics.small_caps("🎬 ᴍᴇᴅɪᴀ"), callback_data="help_media")
            ],
            [
                InlineKeyboardButton(Aesthetics.small_caps("📦 ᴀʀᴄʜɪᴠᴇꜱ"), callback_data="help_arc"),
                InlineKeyboardButton(Aesthetics.small_caps("🚀 ʟᴇᴇᴄʜ"), callback_data="help_leech")
            ],
            [
                InlineKeyboardButton(Aesthetics.small_caps("👑 ᴀᴅᴍɪɴ"), callback_data="help_admin")
            ],
            [InlineKeyboardButton(Aesthetics.small_caps("⬅️ ʙᴀᴄᴋ"), callback_data="start_back")]
        ]
    
    elif page == "files":
        text = Aesthetics.bold_small_caps("📁 ꜰɪʟᴇ ᴍᴀꜱᴛᴇʀʏ") + "\n\n"
        text += Aesthetics.small_caps(
            "• /start - ᴀᴄᴛɪᴠᴀᴛᴇ ᴛʜᴇ ʙᴏᴛ.\n"
            "• /zip - ᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ᴍᴏᴅᴇ ᴛᴏ ꜱᴛᴀᴄᴋ ꜰɪʟᴇꜱ.\n"
            "• /stopzip - ᴄʀᴇᴀᴛᴇ ᴀ ᴢɪᴘ ꜰʀᴏᴍ ꜱᴛᴀᴄᴋᴇᴅ ꜰɪʟᴇꜱ.\n"
            "• /settings - ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰᴇʀᴇɴᴄᴇꜱ.\n\n"
            "✨ ꜰᴇᴀᴛᴜʀᴇꜱ:\n"
            "- ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍɪɴɢ ᴡɪᴛʜ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟꜱ.\n"
            "- ᴀᴜᴛᴏ-ꜱᴘʟɪᴛᴛɪɴɢ ꜰᴏʀ ꜰɪʟᴇꜱ > 2ɢʙ."
        )
        buttons = [[InlineKeyboardButton(Aesthetics.small_caps("⬅️ ʙᴀᴄᴋ"), callback_data="help_main")]]

    elif page == "media":
        text = Aesthetics.bold_small_caps("🎬 ᴍᴇᴅɪᴀ ᴀʟᴄʜᴇᴍʏ") + "\n\n"
        text += Aesthetics.small_caps(
            "ꜱᴇɴᴅ ᴀɴʏ ᴠɪᴅᴇᴏ/ᴀᴜᴅɪᴏ/ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ:\n\n"
            "- ᴛᴏ ᴀᴜᴅɪᴏ: ᴇxᴛʀᴀᴄᴛ ᴍᴘ3 ꜰʀᴏᴍ ᴠɪᴅᴇᴏ.\n"
            "- ᴛᴏ ᴍᴘ4: ɪɴꜱᴛᴀɴᴛ ʀᴇᴍᴜxɪɴɢ (0% ᴄᴘᴜ).\n"
            "- ɢᴇɴ ᴛʜᴜᴍʙ: ᴀᴜᴛᴏ-ᴇxᴛʀᴀᴄᴛ ᴠɪᴅᴇᴏ ꜰʀᴀᴍᴇꜱ.\n"
            "- ᴛᴏ ᴘᴅꜰ: ᴄᴏɴᴠᴇʀᴛ ɪᴍᴀɢᴇꜱ ᴛᴏ ᴅᴏᴄᴜᴍᴇɴᴛꜱ.\n"
            "- ꜱᴛɪᴄᴋᴇʀ: ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ʜɪɢʜ-Qᴜᴀʟɪᴛʏ ᴘɴɢ."
        )
        buttons = [[InlineKeyboardButton(Aesthetics.small_caps("⬅️ ʙᴀᴄᴋ"), callback_data="help_main")]]

    elif page == "arc":
        text = Aesthetics.bold_small_caps("📦 ᴀʀᴄʜɪᴠᴇ ɴᴇxᴜꜱ") + "\n\n"
        text += Aesthetics.small_caps(
            "ꜱᴇɴᴅ ᴀɴʏ .ᴢɪᴘ, .ʀᴀʀ, ᴏʀ .7ᴢ ꜰɪʟᴇ:\n\n"
            "- 1-ᴛᴀᴘ ᴇxᴛʀᴀᴄᴛ: ᴜɴᴘᴀᴄᴋ ᴇᴠᴇʀʏᴛʜɪɴɢ ɪɴꜱᴛᴀɴᴛʟʏ.\n"
            "- ᴀᴜᴛᴏ-ᴜᴘʟᴏᴀᴅ: ᴇxᴛʀᴀᴄᴛᴇᴅ ꜰɪʟᴇꜱ ꜱᴇɴᴛ ʙᴀᴄᴋ ᴛᴏ ʏᴏᴜ.\n"
            "- ꜱᴜᴘᴘᴏʀᴛꜱ: ᴀʟʟ ᴍᴀᴊᴏʀ ᴄᴏᴍᴘʀᴇꜱꜱɪᴏɴ ꜰᴏʀᴍᴀᴛꜱ."
        )
        buttons = [[InlineKeyboardButton(Aesthetics.small_caps("⬅️ ʙᴀᴄᴋ"), callback_data="help_main")]]

    elif page == "leech":
        text = Aesthetics.bold_small_caps("🚀 ɴᴇᴜʀᴀʟ ʟᴇᴇᴄʜᴇʀ") + "\n\n"
        text += Aesthetics.small_caps(
            "ꜱᴇɴᴅ ᴀɴʏ ᴠᴀʟɪᴅ ᴜʀʟ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ:\n\n"
            "- ᴀʀɪᴀ2: 16x ᴍᴜʟᴛɪ-ᴛʜʀᴇᴀᴅᴇᴅ ꜱᴘᴇᴇᴅ.\n"
            "- ꜱᴛʀᴇᴀᴍ ʟɪɴᴋ: ɢᴇɴᴇʀᴀᴛᴇ ᴅɪʀᴇᴄᴛ ʜᴛᴛᴘ ʟɪɴᴋꜱ.\n"
            "- ꜱᴜᴘᴘᴏʀᴛꜱ: ʏᴏᴜᴛᴜʙᴇ, ɪɴꜱᴛᴀ, ᴅɪʀᴇᴄᴛ ʟɪɴᴋꜱ."
        )
        buttons = [[InlineKeyboardButton(Aesthetics.small_caps("⬅️ ʙᴀᴄᴋ"), callback_data="help_main")]]

    elif page == "admin":
        if query.from_user.id not in Config.SUDO_USERS:
            return await query.answer("❌ ᴀᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ: ꜱᴏᴠᴇʀᴇɪɢɴꜱ ᴏɴʟʏ.", show_alert=True)
        text = Aesthetics.bold_small_caps("👑 ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ") + "\n\n"
        text += Aesthetics.small_caps(
            "• /users - ᴛᴏᴛᴀʟ ᴜꜱᴇʀ ᴄᴏᴜɴᴛ.\n"
            "• /stats - ꜰᴜʟʟ ꜱʏꜱᴛᴇᴍ & ᴅʙ ᴍᴇᴛʀɪᴄꜱ.\n"
            "• /broadcast - ꜱᴇɴᴅ ᴍꜱɢ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.\n"
            "• /status - ʀᴇᴀʟ-ᴛɪᴍᴇ ꜱᴇʀᴠᴇʀ ʜᴇᴀʟᴛʜ.\n"
            "• /ban - ʙᴀɴɪꜱʜ ᴀ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴛʜᴇ ᴜɴɪᴠᴇʀꜱᴇ."
        )
        buttons = [[InlineKeyboardButton(Aesthetics.small_caps("⬅️ ʙᴀᴄᴋ"), callback_data="help_main")]]

    await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("^help$"))
async def help_callback(client: Client, query):
    # ʀᴇ-ʀᴏᴜᴛᴇ ᴛᴏ ᴍᴀɪɴ ᴘᴀɢᴇ
    query.data = "help_main"
    await help_pagination(client, query)

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
