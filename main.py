from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN
from callback.callback_handlers import handle_callback_query
from privacy.privacy import setup_privacy_handler


# Initialize the bot client
app = Client(
    "app_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

setup_privacy_handler(app)

@app.on_message(filters.command("start") & filters.private)
async def send_start_message(client, message):
    chat_id = message.chat.id
    full_name = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name

    # Animation messages
    animation_message = await message.reply_text("<b>Starting Graphics Tool️...</b>", parse_mode=ParseMode.HTML)
    await asyncio.sleep(0.4)  # Use asyncio.sleep instead of sleep
    await animation_message.edit_text("<b>Preparing Your Experience Please Wait...</b>", parse_mode=ParseMode.HTML)
    await asyncio.sleep(0.4)  # Use asyncio.sleep instead of sleep
    await animation_message.delete()

    # Main welcome message
    start_message = (
        f"<b>Hi {full_name}! Welcome to this bot</b>\n"
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        "<b><a href='https://t.me/abirxdhackz'>Graphics Tool️⚙️</a></b>: is the most complete Bot to help you with Graphics Resources, Effortless Downloads - Say goodbye to browsing hassles! Get your desired assets with a simple click. 💾\n"
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        "<b>Don't forget to <a href='https://t.me/ModVipRM'>join</a> for updates!</b>"
    )

    await message.reply_text(
        start_message,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("💾 Main Menu", callback_data="main_menu")],
            [InlineKeyboardButton("🔄 Updates", url="https://t.me/ModVipRM"),
             InlineKeyboardButton("ℹ️ About Me", callback_data="about_me")]
        ]),
        disable_web_page_preview=True,
    )

@app.on_callback_query()
async def handle_callback(client, callback_query):
    await handle_callback_query(client, callback_query)

print("Bot is running...")
app.run()
