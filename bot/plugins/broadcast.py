# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

import asyncio
from pyrogram import Client, filters
from bot.config import Config
from bot.database.db_manager import db
from bot.core.aesthetics import Aesthetics
from bot.utils.resilience import zen_resilience

@Client.on_message(filters.command("broadcast") & filters.user(Config.SUDO_USERS))
@zen_resilience
async def broadcast_handler(client, message):
    if not message.reply_to_message:
        return await message.reply_text(Aesthetics.small_caps("❌ ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ."))
    
    ms = await message.reply_text(Aesthetics.small_caps("⏳ ɪɴɪᴛɪᴀᴛɪɴɢ ɴᴇᴜʀᴀʟ ʙʀᴏᴀᴅᴄᴀꜱᴛ..."))
    
    users = await db.get_all_users()
    
    success = 0
    failed = 0
    
    for user in users:
        try:
            await message.reply_to_message.copy(user["user_id"])
            success += 1
            await asyncio.sleep(0.05) # ᴏᴘᴛɪᴍɪᴢᴇᴅ ɴᴇᴜʀᴀʟ ᴅᴇʟᴀʏ
        except Exception:
            failed += 1
            
    await ms.edit(
        Aesthetics.bold_small_caps("📢 ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴘʀᴏᴘᴀɢᴀᴛᴇᴅ!") + "\n\n" +
        Aesthetics.small_caps(f"✅ ꜱᴜᴄᴄᴇꜱꜱ: {success}\n❌ ꜰᴀɪʟᴇᴅ: {failed}")
    )
