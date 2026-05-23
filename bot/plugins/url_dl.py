import os
import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.core.aesthetics import Aesthetics
from bot.modules.url_tools import leecher
from bot.config import Config
from bot.utils.progress import progress_for_pyrogram

from bot.utils.logger import logger

from bot.modules.ffmpeg_tools import ffmpeg_engine

@Client.on_message(filters.private & filters.regex(r'^https?://[^\s]+'))
async def url_handler(client: Client, message: Message):
    await logger.log_user(client, message, "URL_LEECH")
    url = message.text
    ms = await message.reply_text(Aesthetics.small_caps("🔍 ᴀɴᴀʟʏᴢɪɴɢ ʟɪɴᴋ..."))
    
    info = await leecher.get_info(url)
    if not info:
        return await ms.edit(Aesthetics.small_caps("❌ ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ ᴏʀ ᴜɴꜱᴜᴘᴘᴏʀᴛᴇᴅ ꜱɪᴛᴇ."))

    title = info.get('title', 'Downloaded_File')
    await ms.edit(Aesthetics.small_caps(f"⏬ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ: {title}..."))
    
    download_dir = os.path.join(Config.DOWNLOAD_DIR, str(message.from_user.id))
    if not os.path.exists(download_dir): os.makedirs(download_dir)
    
    success = await leecher.download(url, download_dir)
    
    if success:
        files = os.listdir(download_dir)
        if files:
            file_path = os.path.join(download_dir, files[0])
            await ms.edit(Aesthetics.small_caps("⌛ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴍᴇᴅɪᴀ..."))
            
            thumb_path = None
            if file_path.lower().endswith(('.mp4', '.mkv', '.mov', '.avi')):
                auto_thumb = f"{file_path}_thumb.jpg"
                if ffmpeg_engine.extract_frame(file_path, auto_thumb):
                    thumb_path = auto_thumb
            
            detailed_info = ffmpeg_engine.get_detailed_info(file_path)
            
            await ms.edit(Aesthetics.small_caps("⏫ ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ..."))
            start_time = time.time()
            await client.send_document(
                chat_id=message.chat.id,
                document=file_path,
                thumb=thumb_path,
                caption=Aesthetics.small_caps(f"✅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʟᴇᴇᴄʜᴇᴅ: {title}\n📊 {detailed_info}"),
                progress=progress_for_pyrogram,
                progress_args=(Aesthetics.small_caps("⏫ ᴜᴘʟᴏᴀᴅɪɴɢ"), ms, start_time)
            )
            os.remove(file_path)
            if thumb_path: os.remove(thumb_path)
        await ms.delete()
    else:
        await ms.edit(Aesthetics.small_caps("❌ ᴅᴏᴡɴʟᴏᴀᴅ ꜰᴀɪʟᴇᴅ."))
