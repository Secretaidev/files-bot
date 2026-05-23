import asyncio
import os
import shutil
import aiohttp
from bot.config import Config
from bot.core.aesthetics import Aesthetics

class PulseEngine:
    """ᴘᴇʀᴘᴇᴛᴜᴀʟ ᴘᴜʟꜱᴇ ᴀɴᴅ ᴠᴏɪᴅ-ᴄʟᴇᴀɴᴇʀ."""

    @staticmethod
    async def ping_loop():
        """ᴘɪɴɢ ᴛʜᴇ ɪɴᴛᴇʀɴᴀʟ ꜱᴇʀᴠᴇʀ ᴇᴠᴇʀʏ 3 ᴍɪɴᴜᴛᴇꜱ."""
        url = f"http://0.0.0.0:{Config.PORT}"
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    async with session.get(url) as response:
                        print(f"💓 ᴘᴜʟꜱᴇ: ꜱᴇʀᴠᴇʀ ɪꜱ ᴀʟɪᴠᴇ ({response.status})")
                except Exception as e:
                    print(f"💔 ᴘᴜʟꜱᴇ ꜰᴀɪʟᴇᴅ: {e}")
                await asyncio.sleep(180) # 3 ᴍɪɴᴜᴛᴇꜱ

    @staticmethod
    async def void_cleaner():
        """ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ꜱᴇʀᴠᴇʀ ʟᴏɢꜱ/ᴛᴇᴍᴘ ꜰɪʟᴇꜱ ᴇᴠᴇʀʏ 30 ᴍɪɴᴜᴛᴇꜱ."""
        while True:
            try:
                if os.path.exists(Config.DOWNLOAD_DIR):
                    shutil.rmtree(Config.DOWNLOAD_DIR)
                    os.makedirs(Config.DOWNLOAD_DIR)
                    print("🧹 ᴠᴏɪᴅ-ᴄʟᴇᴀɴᴇʀ: ʟᴏᴄᴀʟ ᴛᴇᴍᴘ ꜰɪʟᴇꜱ ᴘᴜʀɢᴇᴅ.")
            except Exception as e:
                print(f"❌ ᴄʟᴇᴀɴᴇʀ ᴇʀʀᴏʀ: {e}")
            await asyncio.sleep(1800) # 30 ᴍɪɴᴜᴛᴇꜱ

pulse = PulseEngine()
