import os
import asyncio
from aiohttp import web
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID", "1234567"))
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
PORT = int(os.environ.get("PORT", "8080"))

# Event Loop එක නිවැරදිව සැකසීම
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

app = Client(
    "cineverse_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    command_args = message.command
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🌐 Official Website 🌐", url="https://www.CineVerseLK.com"),
            InlineKeyboardButton("🏆 Telegram Channel 🏆", url="https://t.me/Oyaage_Channel")
        ],
        [
            InlineKeyboardButton("🗣 Community Group 🗣️", url="https://t.me/Oyaage_Group")
        ]
    ])
    
    if len(command_args) > 1:
        movie_id = command_args[1]
        await message.reply_text(
            f"🎬 **CineVerseLK Movie Download**\n\nඔබ ඉල්ලූ චිත්‍රපටය මෙන්න! (Movie ID: {movie_id})\n\n👇 පහත බොත්තම මඟින් ඩවුන්ලෝඩ් කරගන්න.",
            reply_markup=keyboard
        )
    else:
        await message.reply_text(
            "👋 ආයුබෝවන්! CineVerseLK වෙත සාදරයෙන් පිළිගනිමු.\n\nකරුණාකර අපගේ වෙබ් අඩවියට ගොස් ඩවුන්ලෝඩ් බටන් එක ක්ලික් කිරීම මඟින් මෙතැනට පැමිණෙන්න.",
            reply_markup=keyboard
        )

async def handle(request):
    return web.Response(text="CineVerseLK Bot is running!")

async def web_server():
    server = web.Application()
    server.add_routes([web.get("/", handle)])
    runner = web.AppRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

async def main():
    await web_server()
    await app.start()
    print("CineVerseLK Bot and Web Server are running...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop.run_until_complete(main())
