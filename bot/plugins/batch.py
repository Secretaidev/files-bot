import os
import shutil
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot.core.aesthetics import Aesthetics
from bot.modules.archive_tools import archive_master
from bot.config import Config
from bot.utils.progress import progress_for_pyrogram
from bot.utils.resilience import zen_resilience

# ɪɴ-ᴍᴇᴍᴏʀʏ ꜱᴛᴏʀᴀɢᴇ ꜰᴏʀ ʙᴀᴛᴄʜ ᴘʀᴏᴄᴇꜱꜱɪɴɢ
user_batches = {}

@Client.on_message(filters.private & filters.command("zip"))
@zen_resilience
async def batch_zip_handler(client, message):
    user_id = message.from_user.id
    if user_id not in user_batches:
        user_batches[user_id] = []
        await message.reply_text(
            Aesthetics.bold_small_caps("📥 ʙᴀᴛᴄʜ ᴍᴏᴅᴇ: ᴀᴄᴛɪᴠᴀᴛᴇᴅ") + "\n\n" +
            Aesthetics.small_caps("ꜱᴇɴᴅ ᴍᴇ ᴛʜᴇ ꜰɪʟᴇꜱ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴢɪᴘ.\nᴜꜱᴇ /stopzip ᴛᴏ ꜰɪɴᴀʟɪᴢᴇ.")
        )
    else:
        await message.reply_text(Aesthetics.small_caps("⚠️ ʏᴏᴜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ɪɴ ʙᴀᴛᴄʜ ᴍᴏᴅᴇ."))

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio), group=-1)
async def batch_collector(client, message):
    user_id = message.from_user.id
    if user_id in user_batches:
        user_batches[user_id].append(message)
        await message.reply_text(
            Aesthetics.small_caps(f"➕ ꜰɪʟᴇ ꜱᴛᴀᴄᴋᴇᴅ! ({len(user_batches[user_id])})"),
            quote=True
        )
        message.stop_propagation()

@Client.on_message(filters.private & filters.command("stopzip"))
@zen_resilience
async def stop_zip_handler(client, message):
    user_id = message.from_user.id
    if user_id not in user_batches or not user_batches[user_id]:
        return await message.reply_text(Aesthetics.small_caps("❌ ɴᴏ ꜰɪʟᴇꜱ ɪɴ ʙᴀᴛᴄʜ ᴛᴏ ᴢɪᴘ."))

    ms = await message.reply_text(Aesthetics.small_caps("⏳ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ʙᴀᴛᴄʜ ᴀʀᴄʜɪᴠᴇ..."))
    
    batch_dir = os.path.join(Config.DOWNLOAD_DIR, f"batch_{user_id}_{time.time()}")
    os.makedirs(batch_dir)
    
    downloaded_files = []
    for file_msg in user_batches[user_id]:
        path = await client.download_media(file_msg, file_name=os.path.join(batch_dir, ""))
        downloaded_files.append(path)
    
    archive_name = os.path.join(Config.DOWNLOAD_DIR, f"Batch_Archive_{user_id}.zip")
    
    if archive_master.compress(downloaded_files, archive_name):
        await client.send_document(
            chat_id=message.chat.id,
            document=archive_name,
            caption=Aesthetics.small_caps(f"✅ ʙᴀᴛᴄʜ ᴢɪᴘ ᴄᴏᴍᴘʟᴇᴛᴇ!\nꜰɪʟᴇꜱ: {len(downloaded_files)}"),
            progress=progress_for_pyrogram,
            progress_args=(Aesthetics.small_caps("⏫ ᴜᴘʟᴏᴀᴅɪɴɢ ʙᴀᴛᴄʜ"), ms, time.time())
        )
    else:
        await ms.edit(Aesthetics.small_caps("❌ ᴀʀᴄʜɪᴠᴇ ᴄʀᴇᴀᴛɪᴏɴ ꜰᴀɪʟᴇᴅ."))

    # ᴄʟᴇᴀɴᴜᴘ
    del user_batches[user_id]
    shutil.rmtree(batch_dir)
    if os.path.exists(archive_name): os.remove(archive_name)
    await ms.delete()
