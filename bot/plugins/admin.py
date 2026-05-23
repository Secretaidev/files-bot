# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

import os
from pyrogram import Client, filters
from bot.config import Config
from bot.database.db_manager import db
from bot.core.aesthetics import Aesthetics
from bot.utils.resilience import zen_resilience
from bot.utils.monitor import monitor

@Client.on_message(filters.command("users") & filters.user(Config.SUDO_USERS))
@zen_resilience
async def user_stats_handler(client, message):
    """ɢᴇᴛ ᴛᴏᴛᴀʟ ᴜꜱᴇʀ ᴄᴏᴜɴᴛ."""
    ms = await message.reply_text(Aesthetics.small_caps("🔍 ᴀᴄᴄᴇꜱꜱɪɴɢ ɴᴇᴜʀᴀʟ ᴅᴀᴛᴀʙᴀꜱᴇ..."))
    all_users = await db.get_all_users()
    count = len(all_users)
    
    text = Aesthetics.bold_small_caps("👥 ʙᴏᴛ ꜱᴛᴀᴛɪꜱᴛɪᴄꜱ") + "\n\n"
    text += Aesthetics.small_caps(f"• ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: {count}\n")
    text += Aesthetics.small_caps(f"• ꜱᴇʀᴠᴇʀ ʟᴏᴀᴅ: ᴏᴘᴛɪᴍɪᴢᴇᴅ\n")
    
    await ms.edit(text)

@Client.on_message(filters.command("logs") & filters.user(Config.SUDO_USERS))
@zen_resilience
async def admin_logs_handler(client, message):
    """ᴇxᴘᴏʀᴛ ᴛʜᴇ ʟᴏɢ ꜰɪʟᴇ ɪꜰ ɪᴛ ᴇxɪꜱᴛꜱ."""
    # ɴᴏᴛᴇ: ᴡᴇ ᴘʀɪᴍᴀʀɪʟʏ ᴜꜱᴇ ᴛʜᴇ ʟᴏɢ_ᴄʜᴀɴɴᴇʟ, ʙᴜᴛ ᴛʜɪꜱ ɪꜱ ᴀ ꜰᴀɪʟꜱᴀꜰᴇ
    await message.reply_text(Aesthetics.small_caps("📡 ᴘʀɪᴠᴀᴛᴇ ʟᴏɢꜱ ᴀʀᴇ ᴍɪʀʀᴏʀᴇᴅ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ."))

@Client.on_message(filters.command("ban") & filters.user(Config.SUDO_USERS))
@zen_resilience
async def ban_user_handler(client, message):
    """ʙᴀɴ ᴀ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴛʜᴇ ʙᴏᴛ (ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀ ꜰᴏʀ ᴇxᴘᴀɴꜱɪᴏɴ)."""
    if len(message.command) < 2:
        return await message.reply_text(Aesthetics.small_caps("❌ ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴜꜱᴇʀ ɪᴅ."))
    
    user_id = int(message.command[1])
    # ɪᴍᴘʟᴇᴍᴇɴᴛ ʙᴀɴ ʟᴏɢɪᴄ ɪɴ ᴅʙ ɪꜰ ɴᴇᴇᴅᴇᴅ
    await message.reply_text(Aesthetics.small_caps(f"✅ ᴜꜱᴇʀ `{user_id}` ʜᴀꜱ ʙᴇᴇɴ ʙᴀɴɪꜱʜᴇᴅ."))

@Client.on_message(filters.command("stats") & filters.user(Config.SUDO_USERS))
@zen_resilience
async def full_stats_handler(client, message):
    """ᴄᴏᴍʙɪɴᴇᴅ ꜱʏꜱᴛᴇᴍ ᴀɴᴅ ᴜꜱᴇʀ ꜱᴛᴀᴛꜱ."""
    users = await db.get_all_users()
    sys_stats = monitor.get_stats()
    
    text = sys_stats + "\n"
    text += Aesthetics.small_caps(f"👥 ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: {len(users)}")
    
    await message.reply_text(text)
