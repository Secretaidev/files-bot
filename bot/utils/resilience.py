import functools
import traceback
from bot.utils.logger import logger
from bot.core.aesthetics import Aesthetics

def zen_resilience(func):
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ɢʟᴏʙᴀʟ ᴇʀʀᴏʀ ʜᴀɴᴅʟᴇʀ ᴅᴇᴄᴏʀᴀᴛᴏʀ."""
    @functools.wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except Exception as e:
            error_trace = traceback.format_exc()
            print(f"ᴇʀʀᴏʀ ɪɴ {func.__name__}: {e}")
            # ꜱɪʟᴇɴᴛʟʏ ʟᴏɢ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜᴏᴜᴛ ᴅɪꜱᴛᴜʀʙɪɴɢ ᴛʜᴇ ᴜꜱᴇʀ
            if hasattr(client, 'log_error'):
                await client.log_error(error_trace)
            
            # ᴘᴏʟɪᴛᴇʟʏ ɪɴꜰᴏʀᴍ ᴜꜱᴇʀ ɪꜰ ɴᴇᴄᴇꜱꜱᴀʀʏ
            try:
                if hasattr(message, 'reply_text'):
                    await message.reply_text(
                        Aesthetics.small_caps("⚠️ ᴀ ᴛᴇᴍᴘᴏʀᴀʀʏ ᴅɪꜱᴛᴜʀʙᴀɴᴄᴇ ᴏᴄᴄᴜʀʀᴇᴅ. ᴛʜᴇ ꜱʏꜱᴛᴇᴍ ɪꜱ ʀᴇᴄᴏᴠᴇʀɪɴɢ...")
                    )
            except:
                pass
    return wrapper
