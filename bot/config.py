# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ꜰᴏʀ 4ɢʙ ᴜᴘʟᴏᴀᴅꜱ (ᴏᴘᴛɪᴏɴᴀʟ)
    SESSION_STRING = os.getenv("SESSION_STRING", "")
    
    # ᴅᴀᴛᴀʙᴀꜱᴇ - ꜱᴜᴘᴘᴏʀᴛꜱ ꜱQʟɪᴛᴇ ᴀɴᴅ ᴘᴏꜱᴛɢʀᴇꜱ
    DB_URI = os.getenv("DATABASE_URL", "sqlite:///bot_database.db")
    if DB_URI.startswith("postgres://"):
        DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)
        
    DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "downloads")
    
    # ᴡᴇʙ ꜱᴇʀᴠᴇʀ ᴄᴏɴꜰɪɢ (ꜰᴏʀ ꜱᴛʀᴇᴀᴍɪɴɢ)
    PORT = int(os.getenv("PORT", "8080"))
    FQDN = os.getenv("FQDN", "") # ꜰᴜʟʟʏ Qᴜᴀʟɪꜰɪᴇᴅ ᴅᴏᴍᴀɪɴ ɴᴀᴍᴇ (ᴇ.ɢ. ʙᴏᴛ.ʀᴇɴᴅᴇʀ.ᴄᴏᴍ)
    
    # ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ
    SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split(",") if x]
    
    # ʟᴏɢ ᴄʜᴀɴɴᴇʟ (ꜰᴏʀ ɪɴꜱᴀɴᴇ ᴛʀᴀᴄᴋɪɴɢ)
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
    
    # ᴜɴʟɪᴍɪᴛᴇᴅ ᴄʟᴏᴜᴅ ᴅᴀᴛᴀʙᴀꜱᴇ (ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ)
    DATABASE_CHANNEL = int(os.getenv("DATABASE_CHANNEL", "0"))
    
    # ᴀᴇꜱᴛʜᴇᴛɪᴄꜱ
    START_MSG = os.getenv("START_MSG", "⚡ ɢᴏᴅ-ʟᴇᴠᴇʟ ꜰɪʟᴇ ᴍᴀɴᴀɢᴇʀ ᴏɴʟɪɴᴇ!")
