import asyncio
from pyrogram import Client, filters
from bot.config import Config
from bot.database.db_manager import db
from bot.core.aesthetics import Aesthetics

@Client.on_message(filters.command("broadcast") & filters.user(Config.SUDO_USERS))
async def broadcast_handler(client, message):
    if not message.reply_to_message:
        return await message.reply_text(Aesthetics.small_caps("❌ ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ."))
    
    ms = await message.reply_text(Aesthetics.small_caps("⏳ ꜱᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀꜱᴛ..."))
    
    session = db.get_session()
    users = session.query(db.User).all()
    
    success = 0
    failed = 0
    
    for user in users:
        try:
            await message.reply_to_message.copy(user.user_id)
            success += 1
            await asyncio.sleep(0.1) # ᴘʀᴇᴠᴇɴᴛ ꜰʟᴏᴏᴅ
        except Exception:
            failed += 1
            
    await ms.edit(
        Aesthetics.bold_small_caps("📢 ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!") + "\n\n" +
        Aesthetics.small_caps(f"✅ ꜱᴜᴄᴄᴇꜱꜱ: {success}\n❌ ꜰᴀɪʟᴇᴅ: {failed}")
    )
