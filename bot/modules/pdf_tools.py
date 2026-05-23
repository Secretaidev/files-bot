from PIL import Image
import os

class PDFWizard:
    """ɢᴏᴅ-ʟᴇᴠᴇʟ ᴘᴅꜰ ᴍᴀɴɪᴘᴜʟᴀᴛɪᴏɴ."""

    @staticmethod
    def images_to_pdf(image_list, output_pdf):
        """ᴄᴏɴᴠᴇʀᴛ ᴀ ʟɪꜱᴛ ᴏꜰ ɪᴍᴀɢᴇꜱ ᴛᴏ ᴀ ꜱɪɴɢʟᴇ ᴘᴅꜰ."""
        try:
            images = [Image.open(f).convert('RGB') for f in image_list]
            images[0].save(output_pdf, save_all=True, append_images=images[1:])
            return True
        except Exception:
            return False

pdf_wizard = PDFWizard()
