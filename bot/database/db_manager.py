# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config

class Database:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ɴᴇᴜʀᴀʟ-ɴᴏꜱQʟ ᴍᴏɴɢᴏᴅʙ ᴍᴀɴᴀɢᴇʀ."""

    def __init__(self):
        self.client = AsyncIOMotorClient(Config.DATABASE_URL)
        self.db = self.client.files_bot
        self.users = self.db.users

    async def get_user(self, user_id):
        user = await self.users.find_one({"user_id": user_id})
        if not user:
            user = {"user_id": user_id, "thumbnail": None, "caption": None}
            await self.users.insert_one(user)
        return user

    async def set_thumbnail(self, user_id, file_id):
        await self.users.update_one(
            {"user_id": user_id},
            {"$set": {"thumbnail": file_id}},
            upsert=True
        )

    async def get_thumbnail(self, user_id):
        user = await self.users.find_one({"user_id": user_id})
        return user.get("thumbnail") if user else None

    async def get_all_users(self):
        return await self.users.find().to_list(length=None)

db = Database()
