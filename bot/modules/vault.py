from bot.config import Config
from bot.core.aesthetics import Aesthetics

class InfiniteCloud:
    """ᴛᴇʟᴇɢʀᴀᴍ-ᴄʜᴀɴɴᴇʟ ʙᴀꜱᴇᴅ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅᴀᴛᴀʙᴀꜱᴇ."""

    @staticmethod
    async def mirror_to_vault(client, message):
        """ꜱᴀᴠᴇ ᴀɴʏ ꜰɪʟᴇ ᴏʀ ᴅᴀᴛᴀ ᴛᴏ ᴛʜᴇ ɪɴꜰɪɴɪᴛᴇ ᴄʟᴏᴜᴅ."""
        if not Config.DATABASE_CHANNEL:
            return None
        
        try:
            vault_msg = await message.copy(Config.DATABASE_CHANNEL)
            print(f"☁️ ɪɴꜰɪɴɪᴛᴇ ᴄʟᴏᴜᴅ: ꜰɪʟᴇ ᴠᴀᴜʟᴛᴇᴅ (ᴍꜱɢ_ɪᴅ: {vault_msg.id})")
            return vault_msg.id
        except Exception as e:
            print(f"❌ ᴠᴀᴜʟᴛ ᴇʀʀᴏʀ: {e}")
            return None

cloud = InfiniteCloud()
