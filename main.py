from pyrogram import Client, filters
import subprocess
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private & filters.text)
def download_video(client, message):
    url = message.text.strip()

    if "http" not in url:
        message.reply_text("أرسل رابط الفيديو فقط.")
        return

    message.reply_text("جارٍ التحميل... ⏳")

    try:
        filename = "video.mp4"
        subprocess.run(["yt-dlp", "-o", filename, url])

        if os.path.exists(filename):
            message.reply_video(filename)
            os.remove(filename)
        else:
            message.reply_text("حدث خطأ أثناء التحميل.")
    except Exception as e:
        message.reply_text(f"❌ خطأ: {e}")

bot.run()
