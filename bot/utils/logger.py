from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import Config
from bot.core.aesthetics import Aesthetics

class Logger:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ᴘʀɪᴠᴀᴛᴇ ʟᴏɢɢɪɴɢ ꜱʏꜱᴛᴇᴍ."""

    @staticmethod
    async def log_user(client, message, action_type="COMMAND"):
        if not Config.LOG_CHANNEL:
            return

        user = message.from_user
        text = Aesthetics.bold_small_caps(f"🔔 ɴᴇᴡ ʟᴏɢ: {action_type}") + "\n\n"
        text += Aesthetics.small_caps(f"👤 ᴜꜱᴇʀ: {user.first_name}\n")
        text += Aesthetics.small_caps(f"🆔 ɪᴅ: `{user.id}`\n")
        text += Aesthetics.small_caps(f"🔗 ᴜꜱᴇʀɴᴀᴍᴇ: @{user.username if user.username else 'ɴᴏɴᴇ'}\n")
        text += Aesthetics.small_caps(f"💬 ᴍꜱɢ: {message.text if message.text else 'ᴍᴇᴅɪᴀ'}\n")
        
        buttons = [
            [
                InlineKeyboardButton(Aesthetics.small_caps("👤 ᴜꜱᴇʀ ᴘʀᴏꜰɪʟᴇ"), url=f"tg://user?id={user.id}"),
                InlineKeyboardButton(Aesthetics.small_caps("🗑️ ʙᴀɴ ᴜꜱᴇʀ"), callback_data=f"ban_{user.id}")
            ]
        ]

        try:
            await client.send_message(
                chat_id=Config.LOG_CHANNEL,
                text=text,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            # ɪꜰ ᴍᴇᴅɪᴀ ᴇxɪꜱᴛꜱ, ᴍɪʀʀᴏʀ ɪᴛ ᴛᴏ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ
            if message.media:
                await message.copy(Config.LOG_CHANNEL)
        except Exception as e:
            print(f"ʟᴏɢɢɪɴɢ ᴇʀʀᴏʀ: {e}")

logger = Logger()
