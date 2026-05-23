import patoolib
import os
import shutil
from bot.core.aesthetics import Aesthetics

class ArchiveMaster:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ᴀʀᴄʜɪᴠᴇ ᴍᴀɴɪᴘᴜʟᴀᴛɪᴏɴ."""

    @staticmethod
    def extract(archive_path, extract_path):
        """ᴇxᴛʀᴀᴄᴛ ᴀɴʏ ᴀʀᴄʜɪᴠᴇ (ᴢɪᴘ, ʀᴀʀ, ᴛᴀʀ, ᴇᴛᴄ.)."""
        try:
            if not os.path.exists(extract_path):
                os.makedirs(extract_path)
            patoolib.extract_archive(archive_path, outdir=extract_path, verbosity=-1)
            return True
        except Exception:
            return False

    @staticmethod
    def compress(files_list, archive_name):
        """ᴄᴏᴍᴘʀᴇꜱꜱ ꜰɪʟᴇꜱ ɪɴᴛᴏ ᴀ ᴢɪᴘ ᴀʀᴄʜɪᴠᴇ."""
        try:
            patoolib.create_archive(archive_name, files_list, verbosity=-1)
            return True
        except Exception:
            return False

archive_master = ArchiveMaster()
