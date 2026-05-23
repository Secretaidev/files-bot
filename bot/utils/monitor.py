import psutil
import time
from bot.core.aesthetics import Aesthetics

class SystemMonitor:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ꜱʏꜱᴛᴇᴍ ᴍᴏɴɪᴛᴏʀɪɴɢ."""

    @staticmethod
    def get_stats():
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        uptime = time.time() - psutil.boot_time()
        
        text = Aesthetics.bold_small_caps("📊 ꜱʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ") + "\n\n"
        text += Aesthetics.small_caps(f"🖥️ ᴄᴘᴜ ᴜꜱᴀɢᴇ: {cpu}%\n")
        text += Aesthetics.small_caps(f"🧠 ʀᴀᴍ ᴜꜱᴀɢᴇ: {ram}%\n")
        text += Aesthetics.small_caps(f"💾 ᴅɪꜱᴋ ᴜꜱᴀɢᴇ: {disk}%\n")
        text += Aesthetics.small_caps(f"⏱️ ᴜᴘᴛɪᴍᴇ: {int(uptime // 3600)}ʜ {int((uptime % 3600) // 60)}ᴍ")
        
        return text

monitor = SystemMonitor()
