# (ᴄ) 2026 ᴀᴅɪᴛʏᴀ | ᴜɴɪᴠᴇʀꜱᴇ-ᴄʟᴀꜱꜱ ꜰɪʟᴇ ʙᴏᴛ
# ᴛʜɪꜱ ᴄᴏᴅᴇʙᴀꜱᴇ ɪꜱ ᴘʀᴏᴠɪᴅᴇᴅ ᴀꜱ-ɪꜱ. ꜰᴏʀᴋɪɴɢ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴡɪᴛʜ ᴄʀᴇᴅɪᴛ.

class Aesthetics:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ᴀᴇꜱᴛʜᴇᴛɪᴄꜱ ᴇɴɢɪɴᴇ ꜰᴏʀ ᴄᴜꜱᴛᴏᴍ ᴛʏᴘᴏɢʀᴀᴘʜʏ."""

    @staticmethod
    def small_caps(text: str) -> str:
        """ᴄᴏɴᴠᴇʀᴛꜱ ꜱᴛᴀɴᴅᴀʀᴅ ᴛᴇxᴛ ᴛᴏ ꜱᴍᴀʟʟ ᴄᴀᴘꜱ."""
        if not text:
            return ""
        
        mapping = {
            'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ', 'g': 'ɢ', 'h': 'ʜ',
            'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ',
            'q': 'Q', 'r': 'ʀ', 's': 'ꜱ', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
            'y': 'ʏ', 'z': 'ᴢ',
            'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ꜰ', 'G': 'ɢ', 'H': 'ʜ',
            'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ', 'O': 'ᴏ', 'P': 'ᴘ',
            'Q': 'Q', 'R': 'ʀ', 'S': 'ꜱ', 'T': 'ᴛ', 'U': 'ᴜ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x',
            'Y': 'ʏ', 'Z': 'ᴢ'
        }
        
        return "".join(mapping.get(char, char) for char in text)

    @classmethod
    def bold_small_caps(cls, text: str) -> str:
        """ʀᴇᴛᴜʀɴꜱ ʙᴏʟᴅᴇᴅ ꜱᴍᴀʟʟ ᴄᴀᴘꜱ."""
        return f"**{cls.small_caps(text)}**"

# ᴇxᴀᴍᴘʟᴇ ᴜꜱᴀɢᴇ:
# print(Aesthetics.small_caps("God Level Telegram Bot"))
