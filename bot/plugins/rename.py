import os
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from bot.core.aesthetics import Aesthetics
from bot.utils.progress import progress_for_pyrogram
from bot.database.db_manager import db
from bot.config import Config

from bot.utils.logger import logger

from bot.modules.ffmpeg_tools import ffmpeg_engine

from bot.modules.vault import cloud
from bot.utils.resilience import zen_resilience

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
@zen_resilience
async def rename_request_handler(client: Client, message: Message):
    await logger.log_user(client, message, "FILE_RECEIVED")
    # ᴍɪʀʀᴏʀ ᴛᴏ ɪɴꜰɪɴɪᴛᴇ ᴄʟᴏᴜᴅ ᴠᴀᴜʟᴛ ɪɴꜱᴛᴀɴᴛʟʏ
    await cloud.mirror_to_vault(client, message)
    
    file = getattr(message, message.media.value)
    filename = file.file_name
    
    # ᴘʀᴇ-ᴘʀᴏᴄᴇꜱꜱ ɪɴꜰᴏ (ɪɴꜱᴀɴᴇ ʟᴇᴠᴇʟ)
    info = "ᴀɴᴀʟʏᴢɪɴɢ..."
    
    text = Aesthetics.bold_small_caps("📁 ꜰɪʟᴇ ᴀɴᴀʟʏᴢᴇᴅ!") + "\n\n"
    text += Aesthetics.small_caps(f"ɴᴀᴍᴇ: {filename}\n")
    text += Aesthetics.small_caps(f"ꜱɪᴢᴇ: {file.file_size / (1024*1024):.2f} ᴍʙ\n\n")
    
    buttons = [
        [InlineKeyboardButton(Aesthetics.small_caps("✏️ ʀᴇɴᴀᴍᴇ"), callback_data=f"rename_{message.id}")],
        [InlineKeyboardButton(Aesthetics.small_caps("🎬 ᴍᴇᴛᴀᴅᴀᴛᴀ"), callback_data=f"meta_{message.id}")],
        [InlineKeyboardButton(Aesthetics.small_caps("📡 ꜱᴛʀᴇᴀᴍ ʟɪɴᴋ"), callback_data=f"stream_{message.id}")]
    ]
    
    await message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

@Client.on_message(filters.private & filters.reply & filters.text)
@zen_resilience
async def rename_process_handler(client: Client, message: Message):
    if not (message.reply_to_message.reply_markup and isinstance(message.reply_to_message.reply_markup, ForceReply)):
        return

    new_name = message.text
    original_msg = message.reply_to_message.reply_to_message 
    
    if not original_msg or not original_msg.media:
        return await message.reply_text(Aesthetics.small_caps("❌ ᴇʀʀᴏʀ: ᴏʀɪɢɪɴᴀʟ ᴍᴇᴅɪᴀ ɴᴏᴛ ꜰᴏᴜɴᴅ."))

    ms = await message.reply_text(Aesthetics.small_caps("⏳ ᴇxᴇᴄᴜᴛɪɴɢ ᴛᴀꜱᴋ..."))
    start_time = time.time()
    
    try:
        download_path = await client.download_media(
            message=original_msg,
            progress=progress_for_pyrogram,
            progress_args=(Aesthetics.small_caps("⏬ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ"), ms, start_time)
        )
        
        await ms.edit(Aesthetics.small_caps("⌛ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴍᴇᴅɪᴀ..."))
        
        # ᴀᴜᴛᴏ-ᴛʜᴜᴍʙɴᴀɪʟ ʟᴏɢɪᴄ
        thumb_id = await db.get_thumbnail(message.from_user.id)
        thumb_path = None
        
        if thumb_id:
            thumb_path = await client.download_media(thumb_id)
        elif original_msg.video:
            # ᴀᴜᴛᴏ-ᴇxᴛʀᴀᴄᴛ ᴛʜᴜᴍʙɴᴀɪʟ ɪꜰ ᴍɪꜱꜱɪɴɢ
            auto_thumb = f"{download_path}_thumb.jpg"
            if ffmpeg_engine.extract_frame(download_path, auto_thumb):
                thumb_path = auto_thumb
        
        detailed_info = ffmpeg_engine.get_detailed_info(download_path)
        
        await ms.edit(Aesthetics.small_caps("⏬ ꜱᴘʟɪᴛᴛɪɴɢ ɪꜰ ɴᴇᴇᴅᴇᴅ..."))
        chunks = ffmpeg_engine.split_file(download_path)
        
        for i, chunk in enumerate(chunks):
            await ms.edit(Aesthetics.small_caps(f"⏫ ᴜᴘʟᴏᴀᴅɪɴɢ ᴘᴀʀᴛ {i+1}/{len(chunks)}..."))
            
            await client.send_document(
                chat_id=message.chat.id,
                document=chunk,
                thumb=thumb_path,
                file_name=os.path.basename(chunk) if len(chunks) > 1 else new_name,
                caption=Aesthetics.small_caps(f"✅ {new_name}\n📊 {detailed_info}\n📎 ᴘᴀʀᴛ {i+1}/{len(chunks)}" if len(chunks) > 1 else f"✅ {new_name}\n📊 {detailed_info}"),
                progress=progress_for_pyrogram,
                progress_args=(Aesthetics.small_caps(f"⏫ ᴜᴘʟᴏᴀᴅɪɴɢ {i+1}/{len(chunks)}"), ms, time.time())
            )
            
            if len(chunks) > 1: os.remove(chunk)
        
        await ms.delete()
        if os.path.exists(download_path): os.remove(download_path)
        if thumb_path and os.path.exists(thumb_path): os.remove(thumb_path)

    except Exception as e:
        await ms.edit(Aesthetics.small_caps(f"❌ ᴇʀʀᴏʀ: {str(e)[:100]}"))
        if 'download_path' in locals() and os.path.exists(download_path): os.remove(download_path)
