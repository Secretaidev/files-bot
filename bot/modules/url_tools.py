import yt_dlp
import os
import asyncio
from bot.core.aesthetics import Aesthetics

class Leecher:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ʟᴇᴇᴄʜɪɴɢ ᴇɴɢɪɴᴇ ᴡɪᴛʜ ᴀʀɪᴀ2 ᴀᴄᴄᴇʟᴇʀᴀᴛɪᴏɴ."""

    @staticmethod
    async def get_info(url):
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        loop = asyncio.get_event_loop()
        try:
            info = await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts).extract_info(url, download=False))
            return info
        except Exception:
            return None

    @staticmethod
    async def download(url, download_path):
        """ᴜʟᴛʀᴀ-ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴜꜱɪɴɢ ᴀʀɪᴀ2ᴄ."""
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'external_downloader': 'aria2c',
            'external_downloader_args': [
                '--min-split-size=1M',
                '--max-connection-per-server=16',
                '--max-concurrent-downloads=5',
                '--split=16'
            ],
        }
        loop = asyncio.get_event_loop()
        try:
            await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts).download([url]))
            return True
        except Exception:
            return False

leecher = Leecher()
