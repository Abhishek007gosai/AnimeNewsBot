import os

API_ID = 29245477
API_HASH = "0abc83883262245c90ca337b7a0375c4"
BOT_TOKEN = ""
OWNER_ID = 8667251104
ADMIN_ID = int(os.environ.get("ADMIN_ID", "8667251104"))
LOG_CHANNEL = -1003746574484
UPDATE_INTERVAL = int(os.environ.get("UPDATE_INTERVAL", "2")) # minutes
PORT = 8080 # for web health checks
DB_NAME = "toukaxbot"
DB_URL = ""
START_MSG = os.environ.get("START_MSG", "Bᴀᴋᴀᴀᴀᴀ {mention}... \n<blockquote><b>Iᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ Aᴜᴛᴏ ᴀɴɪᴍᴇ ɴᴇᴡs Bᴏᴛ ᴡʜɪᴄʜ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴜᴘʟᴏᴀᴅs ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴀɴɪᴍᴇ ɴᴇᴡs ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.</b></blockquote>")
HELP_MSG = os.environ.get("HELP_MSG", "<b><u>Hᴇʀᴇ ᴍʏ Cᴏᴍᴍᴀɴᴅs</u></b>:- \n\n<blockquote>• /add_rss - ᴛᴏ ᴀᴅᴅ ɴᴇᴡ ғᴇᴇᴅ (Mᴀx 2 ᴀᴛ ᴏɴᴄᴇ) \n• /rem_rss - ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀɴʏ ʀss ғᴇᴇᴅ. \n• /view_rss - ᴛᴏ ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ʀss ғᴇᴇᴅs. \n• /add_chnl - ʀᴏᴜᴛᴇ ɴᴇᴡs ᴛᴏ ᴄʜᴀɴɴᴇʟ. \n• /rem_chnl  : Rᴇᴍᴏᴠᴇ ᴄʜᴀɴɴᴇʟ ʀᴏᴜᴛᴇ. \n•/view_chnl : ᴛᴏ ᴠɪᴇᴡ ᴀᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟ ʀᴏᴜᴛᴇs. \n•/status : ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ sᴛᴀᴛᴜs.</blockquote>")
ABOUT_MSG = os.environ.get("ABOUT_MSG", "<b><blockquote>◈sᴜᴘʀᴇᴀᴍ : <a href='https://t.me/AnimeNexusNetwork'>ɴᴇᴛᴡᴏʀᴋ</a>\n◈ᴀɴɪᴍᴇ : <a href='https://t.me/Anime_Eternals'>ᴀɴɪᴍᴇ ᴇᴛᴇʀɴᴀʟꜱ</a>\n◈ᴇᴄᴄʜɪ : <a href='https://t.me/Ecchi_Dex'>ᴇᴄᴄʜɪ ᴅᴇx</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href='https://t.me/EternalsHelplineBot'>ʜᴇʟᴘʟɪɴᴇ</a></blockquote></b>")
START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/4k0jx6.jpg")
HELP_PIC = os.environ.get("HELP_PIC", "https://files.catbox.moe/4k0jx6.jpg")
ABOUT_PIC = os.environ.get("ABOUT_PIC", "https://files.catbox.moe/4k0jx6.jpg")
CHNL_USERNAME = "@Anime_News_Arena"
