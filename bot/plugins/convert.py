import os
import time
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image
from bot.core.aesthetics import Aesthetics
from bot.modules.archive_tools import archive_master
from bot.modules.ffmpeg_tools import ffmpeg_engine
from bot.config import Config
from bot.utils.progress import progress_for_pyrogram
from bot.utils.logger import logger

@Client.on_message(filters.private & (filters.video | filters.document))
async def media_handler(client, message):
    if message.video or (message.document and message.document.mime_type.startswith("video/")):
        await logger.log_user(client, message, "VIDEO_RECEIVED")
        buttons = [
            [InlineKeyboardButton(Aesthetics.small_caps("🎵 ᴇxᴛʀᴀᴄᴛ ᴀᴜᴅɪᴏ"), callback_data=f"to_audio_{message.id}")],
            [InlineKeyboardButton(Aesthetics.small_caps("🎬 ᴛᴏ ᴍᴘ4 (ɪɴꜱᴛᴀɴᴛ)"), callback_data=f"to_mp4_{message.id}")],
            [InlineKeyboardButton(Aesthetics.small_caps("🖼️ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ"), callback_data=f"gen_thumb_{message.id}")]
        ]
        await message.reply_text(
            text=Aesthetics.bold_small_caps("🎬 ᴠɪᴅᴇᴏ ᴅᴇᴛᴇᴄᴛᴇᴅ!") + "\n\n" + Aesthetics.small_caps("ᴡʜᴀᴛ ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ᴅᴏ?"),
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    elif message.document and message.document.file_name.endswith(('.zip', '.rar', '.tar', '.gz', '.7z')):
        await logger.log_user(client, message, "ARCHIVE_DETECTED")
        buttons = [[InlineKeyboardButton(Aesthetics.small_caps("🔓 ᴇxᴛʀᴀᴄᴛ"), callback_data=f"extract_{message.id}")]]
        await message.reply_text(
            text=Aesthetics.bold_small_caps("📦 ᴀʀᴄʜɪᴠᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ!") + "\n\n" + Aesthetics.small_caps("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴛʜɪꜱ?"),
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )

@Client.on_message(filters.sticker & filters.private)
async def sticker_handler(client, message):
    await logger.log_user(client, message, "STICKER_RECEIVED")
    buttons = [[InlineKeyboardButton(Aesthetics.small_caps("🖼️ ᴛᴏ ɪᴍᴀɢᴇ"), callback_data=f"to_img_{message.id}")]]
    await message.reply_text(
        text=Aesthetics.bold_small_caps("🎭 ꜱᴛɪᴄᴋᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ!"),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

@Client.on_callback_query(filters.regex(r"^to_audio_"))
async def to_audio_callback(client, query):
    msg_id = int(query.data.split("_")[2])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴀᴜᴅɪᴏ..."))
    
    file_path = await client.download_media(original_msg)
    audio_path = file_path + ".mp3"
    
    if ffmpeg_engine.convert_to_audio(file_path, audio_path):
        await client.send_audio(
            chat_id=query.message.chat.id,
            audio=audio_path,
            caption=Aesthetics.small_caps("✅ ᴀᴜᴅɪᴏ ᴇxᴛʀᴀᴄᴛᴇᴅ!")
        )
        await ms.delete()
    else:
        await ms.edit(Aesthetics.small_caps("❌ ᴄᴏɴᴠᴇʀꜱɪᴏɴ ꜰᴀɪʟᴇᴅ."))
    
    if os.path.exists(file_path): os.remove(file_path)
    if os.path.exists(audio_path): os.remove(audio_path)

@Client.on_callback_query(filters.regex(r"^to_img_"))
async def to_img_callback(client, query):
    msg_id = int(query.data.split("_")[2])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴛᴏ ɪᴍᴀɢᴇ..."))
    
    file_path = await client.download_media(original_msg)
    img_path = file_path + ".png"
    
    try:
        Image.open(file_path).save(img_path, "PNG")
        await client.send_photo(
            chat_id=query.message.chat.id,
            photo=img_path,
            caption=Aesthetics.small_caps("✅ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ɪᴍᴀɢᴇ ᴄᴏᴍᴘʟᴇᴛᴇ!")
        )
        await ms.delete()
    except Exception:
        await ms.edit(Aesthetics.small_caps("❌ ᴄᴏɴᴠᴇʀꜱɪᴏɴ ꜰᴀɪʟᴇᴅ."))
    
    if os.path.exists(file_path): os.remove(file_path)
    if os.path.exists(img_path): os.remove(img_path)

@Client.on_callback_query(filters.regex(r"^to_mp4_"))
async def to_mp4_callback(client, query):
    msg_id = int(query.data.split("_")[2])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ɪɴꜱᴛᴀɴᴛ ʀᴇᴍᴜxɪɴɢ..."))
    
    file_path = await client.download_media(original_msg)
    output_path = file_path + ".mp4"
    
    if ffmpeg_engine.remux_to_mp4(file_path, output_path):
        await client.send_video(
            chat_id=query.message.chat.id,
            video=output_path,
            caption=Aesthetics.small_caps("✅ ɪɴꜱᴛᴀɴᴛʟʏ ʀᴇᴍᴜxᴇᴅ ᴛᴏ ᴍᴘ4!")
        )
        await ms.delete()
    else:
        await ms.edit(Aesthetics.small_caps("❌ ʀᴇᴍᴜxɪɴɢ ꜰᴀɪʟᴇᴅ."))
    
    if os.path.exists(file_path): os.remove(file_path)
    if os.path.exists(output_path): os.remove(output_path)

@Client.on_callback_query(filters.regex(r"^extract_"))
async def extract_callback(client, query):
    msg_id = int(query.data.split("_")[1])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    
    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀʀᴄʜɪᴠᴇ..."))
    
    download_path = await client.download_media(
        message=original_msg,
        progress=progress_for_pyrogram,
        progress_args=(Aesthetics.small_caps("⏬ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ"), ms, time.time())
    )
    
    extract_dir = os.path.join(Config.DOWNLOAD_DIR, f"extract_{query.from_user.id}_{time.time()}")
    await ms.edit(Aesthetics.small_caps("🔓 ᴇxᴛʀᴀᴄᴛɪɴɢ..."))
    
    if archive_master.extract(download_path, extract_dir):
        files = os.listdir(extract_dir)
        await ms.edit(Aesthetics.small_caps(f"✅ ᴇxᴛʀᴀᴄᴛᴇᴅ {len(files)} ꜰɪʟᴇꜱ! ᴜᴘʟᴏᴀᴅɪɴɢ..."))
        
        for file in files:
            file_path = os.path.join(extract_dir, file)
            if os.path.isfile(file_path):
                await client.send_document(
                    chat_id=query.message.chat.id,
                    document=file_path,
                    caption=Aesthetics.small_caps(f"📄 {file}")
                )
        
        shutil.rmtree(extract_dir)
    else:
        await ms.edit(Aesthetics.small_caps("❌ ᴇxᴛʀᴀᴄᴛɪᴏɴ ꜰᴀɪʟᴇᴅ."))
    
    if os.path.exists(download_path): os.remove(download_path)
    await ms.delete()
