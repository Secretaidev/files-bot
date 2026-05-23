import os
import mimetypes
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from bot.core.client import app
from bot.config import Config

web_app = FastAPI()

@web_app.get("/")
async def health_check():
    return {"status": "running", "bot": "God-Level File Bot"}

@web_app.get("/stream/{file_id}")
async def stream_file(file_id: str, request: Request):
    """ɪɴꜱᴛᴀɴᴛ ꜱᴛʀᴇᴀᴍɪɴɢ ʟᴏɢɪᴄ."""
    try:
        # ᴛʜɪꜱ ɪꜱ ᴀ ʜɪɢʜ-ʟᴇᴠᴇʟ ᴀʙꜱᴛʀᴀᴄᴛɪᴏɴ ꜰᴏʀ ꜱᴛʀᴇᴀᴍɪɴɢ
        # ɪɴ ᴀ ʀᴇᴀʟ ꜱᴄᴇɴᴀʀɪᴏ, ᴡᴇ ᴡᴏᴜʟᴅ ᴜꜱᴇ ᴀ ʀᴀɴɢᴇ-ʜᴀɴᴅʟᴇʀ
        file_info = await app.get_messages(None, int(file_id)) # ꜱɪᴍᴘʟɪꜰɪᴇᴅ
        
        async def file_sender():
            async for chunk in app.stream_media(file_info):
                yield chunk

        mime_type, _ = mimetypes.guess_type(file_info.document.file_name if file_info.document else "file.dat")
        return StreamingResponse(file_sender(), media_type=mime_type or "application/octet-stream")
    except Exception as e:
        return {"error": str(e)}

def run_web_server():
    import uvicorn
    uvicorn.run(web_app, host="0.0.0.0", port=Config.PORT)
