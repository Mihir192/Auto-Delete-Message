import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>𝐇𝐢 🙋 {},\n\n𝐈'𝐦 𝐚 𝐒𝐢𝐦𝐩𝐥𝐞 𝐓𝐆 𝐁𝐨𝐭\n\n𝐈 𝐜𝐚𝐧 𝐃𝐞𝐥𝐞𝐭𝐞 🚮 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐀𝐟𝐭𝐞𝐫 𝐚 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐨𝐟 𝐓𝐢𝐦𝐞 🕒\n\n𝐀𝐝𝐝 𝐦𝐞 𝐈𝐧 𝐆𝐫𝐨𝐮𝐩 𝐚𝐬 𝐀𝐝𝐦𝐢𝐧 𝐰𝐢𝐭𝐡 𝐃𝐞𝐥𝐞𝐭𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐚𝐬 𝐖𝐞𝐥𝐥 𝐚𝐬 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐔𝐬𝐞𝐝 𝐭𝐨 𝐂𝐫𝐞𝐚𝐭𝐞 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 𝐚𝐬 𝐀 𝐌𝐞𝐦𝐛𝐞𝐫 𝐨𝐟 𝐓𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩\n\n𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ❤️ 𝐁𝐲  @ChVivekTomar</b>"


User = Client(session_name=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(session_name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
