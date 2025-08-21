import logging
import threading
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import time
import os

TOKEN = os.getenv("TELEGRAM_TOKEN", "8381115677:AAFHBAQmlA35dFfyrvKqPGT69q5zf4Hc7UU")
PORT = int(os.environ.get("PORT", 10000))

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot Telegram DarkAI en ligne et actif 24/7"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Bienvenue dans DarkAI Bot.\nTape /help pour voir les commandes.")

async def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.bot_data["start_time"] = time.time()

    from commands.kick import kick
    from commands.unban import unban
    from commands.help_cmd import help_command
    from commands.info import info
    from commands.ttp import ttp
    from commands.lirik import lirik
    from commands.ass import ass
    from commands.boobs import boobs
    from commands.hboobs import hboobs
    from commands.ipinfo import ipinfo
    from commands.darkgen import darkgen
    from commands.darkweather import darkweather
    from commands.defdark import defdark
    from commands.darkquote import darkquote
    from commands.ping import ping
    from commands.uptime import uptime
    from commands.nsfw import nsfw
    from commands.ai_kyo import ai_kyo
    from commands.ban import ban
    from commands.mute import mute
    from commands.unmute import unmute
    from commands.nightmode import nightmode
    from commands.lock import lock
    from commands.tagall import tagall
    from commands.welcome import welcome
    from commands.vpninfo import vpninfo_handler
    from commands.voice import voice_handler

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("kick", kick))
    application.add_handler(CommandHandler("unban", unban))
    application.add_handler(CommandHandler("ban", ban))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("ttp", ttp))
    application.add_handler(CommandHandler("lirik", lirik))
    application.add_handler(CommandHandler("ass", ass))
    application.add_handler(CommandHandler("boobs", boobs))
    application.add_handler(CommandHandler("hboobs", hboobs))
    application.add_handler(CommandHandler("ipinfo", ipinfo))
    application.add_handler(CommandHandler("darkgen", darkgen))
    application.add_handler(CommandHandler("darkweather", darkweather))
    application.add_handler(CommandHandler("defdark", defdark))
    application.add_handler(CommandHandler("darkquote", darkquote))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("uptime", uptime))
    application.add_handler(CommandHandler("nsfw", nsfw))
    application.add_handler(CommandHandler(["ai","kyo"], ai_kyo))
    application.add_handler(CommandHandler("mute", mute))
    application.add_handler(CommandHandler("unmute", unmute))
    application.add_handler(CommandHandler("nightmode", nightmode))
    application.add_handler(CommandHandler("lock", lock))
    application.add_handler(CommandHandler("tagall", tagall))
    application.add_handler(CommandHandler("vpninfo", vpninfo_handler))
    application.add_handler(CommandHandler("voice", voice_handler))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    logger.info("Bot démarré et en écoute...")

    while True:
        await asyncio.sleep(3600)

def run_flask():
    app.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    bot_thread = threading.Thread(target=lambda: asyncio.run(run_bot()), daemon=True)

    flask_thread.start()
    bot_thread.start()

    flask_thread.join()
    bot_thread.join()
