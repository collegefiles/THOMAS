# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "28617799"))
	API_HASH = os.environ.get("7f827b42053664d9913f64c0706660c9")
	BOT_TOKEN = os.environ.get("AAE3_pQMgRp6KSVC5O0hPf9IeHqZr_La9hc")
	BOT_USERNAME = os.environ.get("THOMAS")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002044807282"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "6897230899"))
	DATABASE_URL = os.environ.get("mongodb+srv://collegefiles:coolguy123@thomas.f2alakm.mongodb.net/?retryWrites=true&w=majority&appName=THOMAS")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-4180332336")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002044807282")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a FileStore Bot. 
 

╭────[ **🔅THOMAS🔅**]────⍟
│
├🔸🤖 **My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
│
├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [Heroku](https://heroku.com)
│
╰──────[ 😎 ]───────────⍟
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
