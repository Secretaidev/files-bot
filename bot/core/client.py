# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

import os
import sys
from pyrogram import Client
from bot.config import Config

# ʜɪɢʜ-ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ ᴇᴠᴇɴᴛ ʟᴏᴏᴘ
if sys.platform != 'win32':
    try:
        import uvloop
        uvloop.install()
    except ImportError:
        pass

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="FilesBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="bot/plugins"),
            workers=min(32, os.cpu_count() + 4) * 4, # ᴏᴘᴛɪᴍɪᴢᴇᴅ ᴡᴏʀᴋᴇʀ ᴘᴏᴏʟ
            sleep_threshold=60,
            max_concurrent_transmissions=10 # ɴᴇᴜʀᴀʟ-ᴄᴏɴᴄᴜʀʀᴇɴᴄʏ ᴄᴏɴᴛʀᴏʟ
        )

    async def start(self):
        await super().start()
        print("⚡ ɢᴏᴅ-ʟᴇᴠᴇʟ ꜰɪʟᴇ ʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ!")

    async def stop(self, *args):
        await super().stop()
        print("💤 ʙᴏᴛ ꜱʜᴜᴛᴛɪɴɢ ᴅᴏᴡɴ...")

    async def log_error(self, trace):
        if Config.LOG_CHANNEL:
            try:
                await self.send_message(
                    Config.LOG_CHANNEL,
                    Aesthetics.bold_small_caps("🆘 ꜱʏꜱᴛᴇᴍ ᴀʟᴇʀᴛ: ᴇxᴄᴇᴘᴛɪᴏɴ") + f"\n\n`{trace[:3500]}`"
                )
            except:
                pass

app = Bot()
