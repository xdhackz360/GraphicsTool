import requests
import logging
from pyrogram import Client, filters
from pyrogram.enums import ParseMode

# Replace these with your actual API details
API_ID = "28239710"
API_HASH = "7fc5b35692454973318b86481ab5eca3"
BOT_TOKEN = "8138984256:AAFEJuQ0hl0HR9H8B4-x4NSBH0YjCWBT084"

# Initialize Bot
app = Client("url_shortener_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Logger setup
logging.basicConfig(level=logging.INFO)

def shorten_url(service, url, slug=None):
    apis = {
        "tinyurl": f"https://tinyurl.com/api-create.php?url={url}",
        "isgd": f"https://is.gd/create.php?format=simple&url={url}",
        "vgd": f"https://v.gd/create.php?format=simple&url={url}",
        "clck": "https://clck.ru/--",
        "dagd": f"https://da.gd/s?url={url}",
        "cleanuri": "https://cleanuri.com/api/v1/shorten",
        "arshort": "https://arshort.com/api"
    }
    
    if service == "clck":
        response = requests.post(apis[service], data={"url": url})
    elif service == "cleanuri":
        response = requests.post(apis[service], data={"url": url})
    elif service == "arshort":
        data = {"url": url}
        if slug:
            data["slug"] = slug
        response = requests.post(apis[service], json=data)
    else:
        response = requests.get(apis[service])
    
    return response.text.strip() if response.ok else "Failed to shorten URL."

@app.on_message(filters.command(["tinyurl", "isgd", "vgd", "clck", "dagd", "cleanuri", "arshort"]))
def shorten_command(client, message):
    parts = message.text.split()
    if len(parts) < 2:
        message.reply_text("❌ Please provide a valid URL.")
        return
    
    service = message.command[0]
    url = parts[1]
    slug = parts[2] if len(parts) > 2 and service == "arshort" else None
    
    shortened_url = shorten_url(service, url, slug)
    message.reply_text(f"✅ Shortened URL: `{shortened_url}`", parse_mode=ParseMode.MARKDOWN)

@app.on_message(filters.command("unshorten"))
def unshorten_command(client, message):
    parts = message.text.split()
    if len(parts) < 2:
        message.reply_text("❌ Please provide a shortened URL.")
        return
    
    url = parts[1]
    try:
        response = requests.get(url, allow_redirects=False)
        original_url = response.headers.get("Location", "Could not retrieve original URL.")
    except requests.RequestException:
        original_url = "Failed to unshorten URL."
    
    message.reply_text(f"🔗 Original URL: `{original_url}`", parse_mode=ParseMode.MARKDOWN)

@app.on_message(filters.text & filters.private)
def default_shortener(client, message):
    url = message.text.strip()
    if url.startswith("http"):
        shortened_url = shorten_url("tinyurl", url)
        message.reply_text(f"✅ Shortened URL: `{shortened_url}`", parse_mode=ParseMode.MARKDOWN)
    else:
        message.reply_text("❌ Invalid URL. Please send a valid link.")

if __name__ == "__main__":
    app.run()
