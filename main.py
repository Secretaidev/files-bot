# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

import asyncio
import threading
from pyrogram import Client, idle
from bot.core.client import app
from bot.core.server import run_web_server
from bot.core.pulse import pulse
from bot.config import Config

async def start_bot():
    # ᴇɴꜱᴜʀᴇ ᴅᴏᴡɴʟᴏᴀᴅ ᴅɪʀᴇᴄᴛᴏʀʏ ᴇxɪꜱᴛꜱ
    if not os.path.exists(Config.DOWNLOAD_DIR):
        os.makedirs(Config.DOWNLOAD_DIR)
        
    await app.start()
    print("⚡ ɢᴏᴅ-ʟᴇᴠᴇʟ ꜰɪʟᴇ ʙᴏᴛ ʟɪᴠᴇ!")
    
    # ʀᴜɴ ᴡᴇʙ ꜱᴇʀᴠᴇʀ ɪɴ ᴀ ꜱᴇᴘᴀʀᴀᴛᴇ ᴛʜʀᴇᴀᴅ
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    
    # ʟᴀᴜɴᴄʜ ᴘᴇʀᴘᴇᴛᴜᴀʟ ᴘᴜʟꜱᴇ ᴀɴᴅ ᴠᴏɪᴅ-ᴄʟᴇᴀɴᴇʀ
    asyncio.create_task(pulse.ping_loop())
    asyncio.create_task(pulse.void_cleaner())
    
    await idle()
    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
