# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

import os
import time
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from PIL import Image
from bot.core.aesthetics import Aesthetics
from bot.modules.archive_tools import archive_master
from bot.modules.ffmpeg_tools import ffmpeg_engine
from bot.modules.pdf_tools import pdf_wizard
from bot.modules.vault import cloud
from bot.database.db_manager import db
from bot.config import Config
from bot.utils.progress import progress_for_pyrogram
from bot.utils.logger import logger
from bot.utils.resilience import zen_resilience

@Client.on_message(filters.private & (filters.video | (filters.document & filters.regex(r'\.(mp4|mkv|mov|avi|webm)$'))))
@zen_resilience
async def video_nexus_handler(client: Client, message: Message):
    await logger.log_user(client, message, "VIDEO_RECEIVED")
    await cloud.mirror_to_vault(client, message)
    text = Aesthetics.bold_small_caps("🎬 ᴠɪᴅᴇᴏ ɴᴇxᴜꜱ") + "\n\n"
    text += Aesthetics.small_caps("ꜱᴇʟᴇᴄᴛ ᴀɴ ᴀᴄᴛɪᴏɴ ꜰᴏʀ ʏᴏᴜʀ ᴍᴇᴅɪᴀ:")
    
    buttons = [
        [
            InlineKeyboardButton(Aesthetics.small_caps("🎵 ᴛᴏ ᴀᴜᴅɪᴏ"), callback_data=f"vid_audio_{message.id}"),
            InlineKeyboardButton(Aesthetics.small_caps("🎬 ᴛᴏ ᴍᴘ4"), callback_data=f"vid_mp4_{message.id}")
        ],
        [
            InlineKeyboardButton(Aesthetics.small_caps("🖼️ ɢᴇɴ ᴛʜᴜᴍʙ"), callback_data=f"vid_thumb_{message.id}"),
            InlineKeyboardButton(Aesthetics.small_caps("📊 ᴍᴇᴛᴀᴅᴀᴛᴀ"), callback_data=f"vid_meta_{message.id}")
        ],
        [
            InlineKeyboardButton(Aesthetics.small_caps("📡 ꜱᴛʀᴇᴀᴍ ʟɪɴᴋ"), callback_data=f"vid_stream_{message.id}"),
            InlineKeyboardButton(Aesthetics.small_caps("✏️ ʀᴇɴᴀᴍᴇ"), callback_data=f"vid_rename_{message.id}")
        ]
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)

@Client.on_message(filters.private & filters.document & filters.regex(r'\.(zip|rar|tar|7z|gz)$'))
@zen_resilience
async def archive_nexus_handler(client: Client, message: Message):
    await logger.log_user(client, message, "ARCHIVE_RECEIVED")
    await cloud.mirror_to_vault(client, message)
    text = Aesthetics.bold_small_caps("📦 ᴀʀᴄʜɪᴠᴇ ɴᴇxᴜꜱ") + "\n\n"
    text += Aesthetics.small_caps("ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ᴜɴᴘᴀᴄᴋ ᴛʜɪꜱ ᴄᴏɴᴛᴀɪɴᴇʀ?")
    
    buttons = [[InlineKeyboardButton(Aesthetics.small_caps("🔓 ᴇxᴛʀᴀᴄᴛ ᴀʟʟ"), callback_data=f"arc_ext_{message.id}")]]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)

@Client.on_message(filters.private & filters.photo)
@zen_resilience
async def image_nexus_handler(client: Client, message: Message):
    await logger.log_user(client, message, "IMAGE_RECEIVED")
    await cloud.mirror_to_vault(client, message)
    text = Aesthetics.bold_small_caps("🖼️ ɪᴍᴀɢᴇ ɴᴇxᴜꜱ") + "\n\n"
    text += Aesthetics.small_caps("ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴀʟᴄʜᴇᴍʏ:")
    
    buttons = [
        [InlineKeyboardButton(Aesthetics.small_caps("📄 ᴛᴏ ᴘᴅꜰ"), callback_data=f"img_pdf_{message.id}")],
        [InlineKeyboardButton(Aesthetics.small_caps("✨ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ"), callback_data=f"img_setthumb_{message.id}")]
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)

@Client.on_message(filters.private & filters.sticker)
@zen_resilience
async def sticker_nexus_handler(client: Client, message: Message):
    await logger.log_user(client, message, "STICKER_RECEIVED")
    buttons = [[InlineKeyboardButton(Aesthetics.small_caps("🖼️ ᴛᴏ ɪᴍᴀɢᴇ"), callback_data=f"stk_img_{message.id}")]]
    await message.reply_text(Aesthetics.bold_small_caps("🎭 ꜱᴛɪᴄᴋᴇʀ ᴀʟᴄʜᴇᴍʏ"), reply_markup=InlineKeyboardMarkup(buttons), quote=True)

@Client.on_message(filters.private & filters.reply & filters.text)
@zen_resilience
async def reply_nexus_handler(client, message):
    if message.reply_to_message.reply_markup and isinstance(message.reply_to_message.reply_markup, ForceReply):
        if "ɴᴇᴡ ɴᴀᴍᴇ" in message.reply_to_message.text:
            return await vid_rename_process(client, message)

# --- ᴄᴀʟʟʙᴀᴄᴋ ʜᴀɴᴅʟᴇʀꜱ ---

@Client.on_callback_query(filters.regex(r"^vid_"))
@zen_resilience
async def video_callbacks(client, query):
    action = query.data.split("_")[1]
    msg_id = int(query.data.split("_")[2])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    
    if action == "rename":
        return await query.message.reply_text(Aesthetics.small_caps("ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ɴᴇᴡ ɴᴀᴍᴇ:"), reply_markup=ForceReply(True))
    
    if action == "stream":
        stream_link = f"{Config.FQDN}/stream/{msg_id}" if Config.FQDN else f"http://localhost:{Config.PORT}/stream/{msg_id}"
        return await query.message.edit_text(Aesthetics.bold_small_caps("📡 ꜱᴛʀᴇᴀᴍ ʟɪɴᴋ") + f"\n\n`{stream_link}`")

    if action == "meta":
        ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴘʀᴏʙɪɴɢ..."))
        file_path = await client.download_media(original_msg)
        detailed_info = ffmpeg_engine.get_detailed_info(file_path)
        os.remove(file_path)
        return await ms.edit_text(Aesthetics.bold_small_caps("📊 ᴍᴇᴅɪᴀ ɪɴꜰᴏ") + f"\n\n{detailed_info}")

    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴘʀᴏᴄᴇꜱꜱɪɴɢ..."))
    file_path = await client.download_media(original_msg, progress=progress_for_pyrogram, progress_args=(Aesthetics.small_caps("⏬ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ"), ms, time.time()))

    if action == "audio":
        output = file_path + ".mp3"
        if ffmpeg_engine.convert_to_audio(file_path, output):
            await client.send_audio(query.message.chat.id, audio=output, caption=Aesthetics.small_caps("✅ ᴀᴜᴅɪᴏ ᴇxᴛʀᴀᴄᴛᴇᴅ"))
        else: await ms.edit(Aesthetics.small_caps("❌ ꜰᴀɪʟᴇᴅ"))
    
    elif action == "mp4":
        output = file_path + ".mp4"
        if ffmpeg_engine.remux_to_mp4(file_path, output):
            await client.send_video(query.message.chat.id, video=output, caption=Aesthetics.small_caps("✅ ʀᴇᴍᴜxᴇᴅ"))
        else: await ms.edit(Aesthetics.small_caps("❌ ꜰᴀɪʟᴇᴅ"))

    elif action == "thumb":
        output = file_path + "_thumb.jpg"
        if ffmpeg_engine.extract_frame(file_path, output):
            await client.send_photo(query.message.chat.id, photo=output, caption=Aesthetics.small_caps("✅ ᴛʜᴜᴍʙɴᴀɪʟ ɢᴇɴᴇʀᴀᴛᴇᴅ"))
        else: await ms.edit(Aesthetics.small_caps("❌ ꜰᴀɪʟᴇᴅ"))

    for f in [file_path, locals().get('output')]:
        if f and os.path.exists(f): os.remove(f)
    await ms.delete()

@Client.on_callback_query(filters.regex(r"^arc_"))
@zen_resilience
async def archive_callbacks(client, query):
    msg_id = int(query.data.split("_")[2])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴜɴᴘᴀᴄᴋɪɴɢ..."))
    
    archive_path = await client.download_media(original_msg, progress=progress_for_pyrogram, progress_args=(Aesthetics.small_caps("⏬ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ"), ms, time.time()))
    extract_dir = os.path.join(Config.DOWNLOAD_DIR, f"ext_{query.from_user.id}_{time.time()}")
    
    if archive_master.extract(archive_path, extract_dir):
        for file in os.listdir(extract_dir):
            f_path = os.path.join(extract_dir, file)
            if os.path.isfile(f_path):
                await client.send_document(query.message.chat.id, document=f_path, caption=Aesthetics.small_caps(f"📄 {file}"))
        shutil.rmtree(extract_dir)
    else: await ms.edit(Aesthetics.small_caps("❌ ꜰᴀɪʟᴇᴅ"))
    
    if os.path.exists(archive_path): os.remove(archive_path)
    await ms.delete()

@Client.on_callback_query(filters.regex(r"^img_"))
@zen_resilience
async def image_callbacks(client, query):
    action = query.data.split("_")[1]
    msg_id = int(query.data.split("_")[2])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    
    if action == "setthumb":
        await db.set_thumbnail(query.from_user.id, original_msg.photo.file_id)
        return await query.message.edit_text(Aesthetics.small_caps("✅ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ"))

    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴄᴏɴᴠᴇʀᴛɪɴɢ..."))
    path = await client.download_media(original_msg)
    output = path + ".pdf"
    
    if pdf_wizard.images_to_pdf([path], output):
        await client.send_document(query.message.chat.id, document=output, caption=Aesthetics.small_caps("✅ ᴘᴅꜰ ᴄʀᴇᴀᴛᴇᴅ"))
    else: await ms.edit(Aesthetics.small_caps("❌ ꜰᴀɪʟᴇᴅ"))
    
    for f in [path, output]:
        if os.path.exists(f): os.remove(f)
    await ms.delete()

@Client.on_callback_query(filters.regex(r"^stk_"))
@zen_resilience
async def sticker_callbacks(client, query):
    msg_id = int(query.data.split("_")[2])
    original_msg = await client.get_messages(query.message.chat.id, msg_id)
    ms = await query.message.edit_text(Aesthetics.small_caps("⏳ ᴄᴏɴᴠᴇʀᴛɪɴɢ..."))
    
    path = await client.download_media(original_msg)
    output = path + ".png"
    Image.open(path).save(output, "PNG")
    
    await client.send_photo(query.message.chat.id, photo=output, caption=Aesthetics.small_caps("✅ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ɪᴍᴀɢᴇ"))
    for f in [path, output]:
        if os.path.exists(f): os.remove(f)
    await ms.delete()

async def vid_rename_process(client, message):
    new_name = message.text
    original_msg = message.reply_to_message.reply_to_message
    ms = await message.reply_text(Aesthetics.small_caps("⏳ ʀᴇɴᴀᴍɪɴɢ..."))
    
    path = await client.download_media(original_msg, progress=progress_for_pyrogram, progress_args=(Aesthetics.small_caps("⏬ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ"), ms, time.time()))
    thumb_id = await db.get_thumbnail(message.from_user.id)
    thumb_path = await client.download_media(thumb_id) if thumb_id else None
    
    chunks = ffmpeg_engine.split_file(path)
    for i, chunk in enumerate(chunks):
        await client.send_document(
            message.chat.id, document=chunk, thumb=thumb_path, file_name=os.path.basename(chunk) if len(chunks)>1 else new_name,
            caption=Aesthetics.small_caps(f"✅ {new_name}") + (f"\n📎 ᴘᴀʀᴛ {i+1}" if len(chunks)>1 else ""),
            progress=progress_for_pyrogram, progress_args=(Aesthetics.small_caps(f"⏫ ᴜᴘʟᴏᴀᴅɪɴɢ {i+1}"), ms, time.time())
        )
        if len(chunks)>1: os.remove(chunk)
    
    if os.path.exists(path): os.remove(path)
    if thumb_path: os.remove(thumb_path)
    await ms.delete()
