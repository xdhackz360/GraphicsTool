import http.client
import json
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_KEY = "e1a91d4256msh250b999a4c95c5dp14d8d4jsn7168a5c116ff"
API_HOST = "cricbuzz-cricket.p.rapidapi.com"
MATCHES_PER_PAGE = 5

def fetch_matches():
    conn = http.client.HTTPSConnection(API_HOST)
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': API_HOST
    }
    conn.request("GET", "/matches/v1/recent", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def fetch_score(match_id):
    conn = http.client.HTTPSConnection(API_HOST)
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': API_HOST
    }
    conn.request("GET", f"/mcenter/v1/{match_id}/miniscore", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def format_matches(matches, page=1):
    if not isinstance(matches, dict) or 'typeMatches' not in matches:
        print("Debug: Expected a dictionary with 'typeMatches' but got:", type(matches))
        return "Error: Unable to retrieve match data.", None

    formatted_matches = ""
    start_idx = (page - 1) * MATCHES_PER_PAGE
    end_idx = start_idx + MATCHES_PER_PAGE
    match_list = []

    for match_type in matches['typeMatches']:
        for match in match_type.get('seriesMatches', []):
            series_ad_wrapper = match.get('seriesAdWrapper', {})
            series_name = series_ad_wrapper.get('seriesName', 'Unknown Series')
            for series in series_ad_wrapper.get('matches', []):
                match_info = series.get('matchInfo', {})
                match_list.append({
                    'seriesName': series_name,
                    'matchDesc': match_info.get('matchDesc', 'Unknown Match'),
                    'startDate': match_info.get('startDate', 'Unknown Date'),
                    'status': match_info.get('status', 'Unknown Status'),
                    'team1': match_info.get('team1', {}).get('teamName', 'Unknown Team 1'),
                    'team2': match_info.get('team2', {}).get('teamName', 'Unknown Team 2'),
                    'matchId': match_info.get('matchId', 'Unknown ID')
                })

    all_matches = match_list[start_idx:end_idx]

    for match in all_matches:
        formatted_matches += (
            f"🏆 {match['seriesName']}\n"
            f"📄 Match Info: {match['matchDesc']}\n"
            f"📅 Start Date: {match['startDate']} UTC\n"
            f"⏰ Status: {match['status']}\n"
            f"👥 Team : {match['team1']} VS {match['team2']}\n"
            f"🆔 Match ID: {match['matchId']}\n"
            "━━━━━━━━━━━━━━━━\n"
        )

    buttons = []
    if page > 1:
        buttons.append(InlineKeyboardButton("Previous ⬅️", callback_data=f"matches_page:{page-1}"))
    if end_idx < len(match_list):
        buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"matches_page:{page+1}"))

    # Ensure buttons are always in a single list to avoid invalid reply markup
    reply_markup = InlineKeyboardMarkup([buttons]) if buttons else None

    return formatted_matches, reply_markup

def format_score(score_data):
    # Debug: Print the structure of the score data
    print("Debug: Score data structure:", json.dumps(score_data, indent=2))

    if not isinstance(score_data, dict) or 'miniscore' not in score_data:
        print("Debug: Expected a dictionary with 'miniscore' but got:", type(score_data))
        return "Error: Unable to retrieve score data."

    miniscore = score_data['miniscore']
    score_text = (
        f"🏏 {miniscore.get('customStatus', 'No Status')}\n"
        f"📊 {miniscore.get('state', 'No State')}\n"
        f"---------------------------\n"
    )
    for innings in miniscore.get('inningsScoreList', []):
        score_text += (
            f"🆔 Inning {innings.get('inningsId', 'Unknown ID')} - {innings.get('batTeamName', 'Unknown Team')}\n"
            f"Score: {innings.get('score', '0')}/{innings.get('wickets', '0')} in {innings.get('overs', '0')} overs\n"
            "---------------------------\n"
        )
    return score_text

def setup_cric_handler(app):
    @app.on_message(filters.command("matches") & (filters.private | filters.group))
    async def send_matches(client, message):
        matches_data = fetch_matches()
        formatted_message, reply_markup = format_matches(matches_data)

        await message.reply_text(
            formatted_message,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )

    @app.on_message(filters.command("score") & (filters.private | filters.group))
    async def send_score(client, message):
        if len(message.command) < 2:
            await message.reply_text("Please provide a match ID. Usage: /score [match id]")
            return

        match_id = message.command[1]
        score_data = fetch_score(match_id)
        formatted_score = format_score(score_data)

        await message.reply_text(
            formatted_score,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )

    @app.on_callback_query(filters.regex(r"matches_page:(\d+)"))
    async def paginate_matches(client, callback_query):
        page = int(callback_query.data.split(":")[1])
        matches_data = fetch_matches()
        formatted_message, reply_markup = format_matches(matches_data, page)

        await callback_query.message.edit_text(
            formatted_message,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
# Replace these with your actual API details
API_ID = "28239710"
API_HASH = "7fc5b35692454973318b86481ab5eca3"
BOT_TOKEN = "8138984256:AAFEJuQ0hl0HR9H8B4-x4NSBH0YjCWBT084"

# Initialize the bot client
app = Client(
    "cric_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Setup handlers
setup_cric_handler(app)

print("Bot is running...")
app.run()
