import ffmpeg
import os
from bot.core.aesthetics import Aesthetics

class FFmpegEngine:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ᴍᴇᴅɪᴀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴇɴɢɪɴᴇ."""

    @staticmethod
    def get_metadata(file_path):
        try:
            probe = ffmpeg.probe(file_path)
            return probe
        except Exception:
            return None

    @staticmethod
    def convert_to_audio(video_path, audio_path):
        """ᴇxᴛʀᴀᴄᴛ ᴀᴜᴅɪᴏ ꜰʀᴏᴍ ᴠɪᴅᴇᴏ."""
        try:
            ffmpeg.input(video_path).output(audio_path, acodec='libmp3lame').run(overwrite_output=True)
            return True
        except Exception:
            return False

    @staticmethod
    def extract_frame(video_path, output_path, time_offset="00:00:05"):
        """ᴇxᴛʀᴀᴄᴛ ᴀ ꜰʀᴀᴍᴇ ꜰʀᴏᴍ ᴠɪᴅᴇᴏ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ."""
        try:
            (
                ffmpeg
                .input(video_path, ss=time_offset)
                .filter('scale', 320, -1)
                .output(output_path, vframes=1)
                .run(overwrite_output=True, quiet=True)
            )
            return True
        except Exception:
            return False

    @staticmethod
    def get_detailed_info(file_path):
        """ɢᴇᴛ ʜɪɢʜ-ꜰɪᴅᴇʟɪᴛʏ ᴍᴇᴅɪᴀ ᴍᴇᴛᴀᴅᴀᴛᴀ."""
        try:
            probe = ffmpeg.probe(file_path)
            video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            if not video_stream:
                return "ɴ/ᴀ"
            
            res = f"{video_stream.get('width')}x{video_stream.get('height')}"
            codec = video_stream.get('codec_name', 'ᴜɴᴋɴᴏᴡɴ').upper()
            duration = float(probe.get('format', {}).get('duration', 0))
            
            return f"{res} | {codec} | {int(duration // 60)}ᴍ {int(duration % 60)}ꜱ"
        except Exception:
            return "ᴇʀʀᴏʀ ᴘʀᴏʙɪɴɢ"

    @staticmethod
    def remux_to_mp4(input_path, output_path):
        """ᴢᴇʀᴏ-ᴡᴀɪᴛ ᴀʟᴄʜᴇᴍʏ: ꜱᴡᴀᴘ ᴄᴏɴᴛᴀɪɴᴇʀꜱ ᴡɪᴛʜᴏᴜᴛ ʀᴇ-ᴇɴᴄᴏᴅɪɴɢ (0% ᴄᴘᴜ)."""
        try:
            (
                ffmpeg
                .input(input_path)
                .output(output_path, vcodec='copy', acodec='copy')
                .run(overwrite_output=True, quiet=True)
            )
            return True
        except Exception:
            return False

    @staticmethod
    def split_file(file_path, chunk_size=1900*1024*1024):
        """ꜱᴘʟɪᴛ ᴀ ꜰɪʟᴇ ɪɴᴛᴏ ᴄʜᴜɴᴋꜱ (ꜰᴏʀ ᴛᴇʟᴇɢʀᴀᴍ'ꜱ 2ɢʙ ʟɪᴍɪᴛ)."""
        chunks = []
        file_size = os.path.getsize(file_path)
        
        if file_size <= chunk_size:
            return [file_path]

        with open(file_path, 'rb') as f:
            chunk_num = 1
            while True:
                chunk_data = f.read(chunk_size)
                if not chunk_data:
                    break
                
                chunk_name = f"{file_path}.part{chunk_num}"
                with open(chunk_name, 'wb') as chunk_file:
                    chunk_file.write(chunk_data)
                
                chunks.append(chunk_name)
                chunk_num += 1
        
        return chunks

ffmpeg_engine = FFmpegEngine()
