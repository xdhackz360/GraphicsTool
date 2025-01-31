import requests
import logging
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace these with your actual API details
API_ID = "28239710"
API_HASH = "7fc5b35692454973318b86481ab5eca3"
BOT_TOKEN = "8138984256:AAFEJuQ0hl0HR9H8B4-x4NSBH0YjCWBT084"

# Initialize Bot
app = Client("url_shortener_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Logger setup
logging.basicConfig(level=logging.INFO)

def format_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url

def shorten_url(service, url, slug=None):
    url = format_url(url)
    apis = {
        "tinyurl": f"https://tinyurl.com/api-create.php?url={url}",
        "isgd": f"https://is.gd/create.php?format=simple&url={url}",
        "vgd": f"https://v.gd/create.php?format=simple&url={url}",
        "clck": "https://clck.ru/--",
        "dagd": f"https://da.gd/s?url={url}",
        "cleanuri": "https://cleanuri.com/api/v1/shorten",
        "arshort": "https://arshort.com/api"
    }
    
    if service not in apis:
        return None
    
    if service == "clck":
        response = requests.post(apis[service], data={"url": url})
    elif service == "cleanuri":
        response = requests.post(apis[service], data={"url": url}).json()
        return response.get("result_url", "Failed to shorten URL.")
    elif service == "arshort":
        data = {"url": url}
        if slug:
            data["slug"] = slug
        response = requests.post(apis[service], json=data).json()
        return response.get("shortenedUrl", "Failed to shorten URL.")
    else:
        response = requests.get(apis[service])
    
    return response.text.strip() if response.ok else "Failed to shorten URL."

@app.on_message(filters.command(["tinyurl", "isgd", "vgd", "clck", "dagd", "cleanuri", "arshort"]))
def shorten_command(client, message):
    parts = message.text.split()
    if len(parts) < 2:
        message.reply_text("**❌ Please provide a valid URL.**", parse_mode=ParseMode.MARKDOWN)
        return
    
    service = message.command[0].lower()
    url = parts[1]
    slug = parts[2] if len(parts) > 2 and service == "arshort" else None
    
    shortened_url = shorten_url(service, url, slug)
    
    if not shortened_url or shortened_url.startswith("Failed"):
        message.reply_text("**❌ Failed to shorten URL.**", parse_mode=ParseMode.MARKDOWN)
        return
    
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔗 Open URL", url=shortened_url)]]
    )
    
    message.reply_text(f"**✅ Shortened URL:** `{shortened_url}`", parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)

@app.on_message(filters.command("unshorten"))
def unshorten_command(client, message):
    parts = message.text.split()
    if len(parts) < 2:
        message.reply_text("**❌ Please provide a shortened URL.**", parse_mode=ParseMode.MARKDOWN)
        return
    
    url = format_url(parts[1])
    try:
        response = requests.get(url, allow_redirects=False)
        original_url = response.headers.get("Location", "Could not retrieve original URL.")
    except requests.RequestException:
        original_url = "Failed to unshorten URL."
    
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔗 Open URL", url=original_url)]]
    )
    
    message.reply_text(f"**🔗 Original URL:** `{original_url}`", parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)

@app.on_message(filters.text & filters.private)
def default_shortener(client, message):
    url = format_url(message.text.strip())
    shortened_url = shorten_url("tinyurl", url)
    if shortened_url.startswith("Failed"):
        message.reply_text("**❌ Failed to shorten URL.**", parse_mode=ParseMode.MARKDOWN)
        return
    
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔗 Open URL", url=shortened_url)]]
    )
    
    message.reply_text(f"**✅ Shortened URL:** `{shortened_url}`", parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)

if __name__ == "__main__":
    app.run()
