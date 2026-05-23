import math
import time
from bot.core.aesthetics import Aesthetics

def humanbytes(size):
    if not size:
        return "0 ʙ"
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'ᴋ', 2: 'ᴍ', 3: 'ɢ', 4: 'ᴛ'}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {Dic_powerN[n]}ʙ"

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    parts = []
    if days: parts.append(f"{days}ᴅ")
    if hours: parts.append(f"{hours}ʜ")
    if minutes: parts.append(f"{minutes}ᴍ")
    if seconds: parts.append(f"{seconds}ꜱ")
    
    return " ".join(parts) if parts else "0ꜱ"

async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    # ᴜᴘᴅᴀᴛᴇ ᴇᴠᴇʀʏ 5 ꜱᴇᴄᴏɴᴅꜱ ᴏʀ ᴏɴ ᴄᴏᴍᴘʟᴇᴛɪᴏɴ ᴛᴏ ᴍɪɴɪᴍɪᴢᴇ ꜰʟᴏᴏᴅ ᴀɴᴅ ᴇɴꜱᴜʀᴇ ꜱᴍᴏᴏᴛʜɴᴇꜱꜱ
    if round(diff % 5.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        
        elapsed_time_str = TimeFormatter(elapsed_time)
        eta_str = TimeFormatter(time_to_completion)

        # ᴜʟᴛʀᴀ-ᴄʟᴇᴀɴ ᴘʀᴏɢʀᴇꜱꜱ ʙᴀʀ
        filled_length = int(15 * current // total)
        bar = '◈' * filled_length + '◇' * (15 - filled_length)

        # ᴘʀᴇᴍɪᴜᴍ ᴛᴇᴍᴘʟᴀᴛᴇ
        status = f"**{Aesthetics.small_caps(ud_type)}**\n"
        status += f"`{bar}` **{round(percentage, 1)}%**\n\n"
        status += Aesthetics.small_caps(
            f"⚡ ꜱᴘᴇᴇᴅ: {humanbytes(speed)}/ꜱ\n"
            f"📦 ᴘʀᴏᴄᴇꜱꜱᴇᴅ: {humanbytes(current)} ᴏꜰ {humanbytes(total)}\n"
            f"⏱️ ᴇᴛᴀ: {eta_str}"
        )
        
        try:
            await message.edit_text(status)
        except Exception:
            pass
