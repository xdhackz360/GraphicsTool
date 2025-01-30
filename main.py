from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace these with your actual API details
API_ID = "28239710"
API_HASH = "7fc5b35692454973318b86481ab5eca3"
BOT_TOKEN = "8138984256:AAFEJuQ0hl0HR9H8B4-x4NSBH0YjCWBT084"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

OWNER_ID = 7303810912  # Updated owner ID

def is_admin(user_id, chat_id):
    try:
        member = app.get_chat_member(chat_id, user_id)
        return member.status in ["administrator", "owner"]
    except:
        # If user info cannot be fetched, assume admin/owner
        return True

def handle_error(message, error_text="**❌ An error occurred while processing the request.**"):
    message.reply_text(error_text, parse_mode=ParseMode.MARKDOWN)

@app.on_message(filters.command(["ban", "fuck"], prefixes="/"))
def handle_ban(client, message):
    if message.chat.type == "private":
        message.reply_text("**❌ Sorry, this command only works in groups.**", parse_mode=ParseMode.MARKDOWN)
        return

    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else None

    if user_id and not is_admin(user_id, chat_id) and user_id != OWNER_ID:
        message.reply_text("**❌ You don't have the necessary permissions to perform this action.**", parse_mode=ParseMode.MARKDOWN)
        return

    target_users = [word for word in message.command[1:] if word.startswith('@')]
    reason = " ".join([word for word in message.command[1:] if not word.startswith('@')])
    if not reason:
        reason = "No reason"

    if not target_users:
        message.reply_text("**❌ Please specify the username or user ID.**", parse_mode=ParseMode.MARKDOWN)
        return

    for target_user in target_users:
        try:
            # Check if the bot has permission to ban members
            bot_member = app.get_chat_member(chat_id, client.me.id)
            if not bot_member.can_restrict_members:
                handle_error(message, "**❌ Sorry Bro I Am Not Admin**")
                return

            if is_admin(target_user, chat_id):
                message.reply_text("**Why would I ban an admin? That sounds like a pretty dumb idea❌.**", parse_mode=ParseMode.MARKDOWN)
                return

            app.ban_chat_member(chat_id, target_user)
            user_info = app.get_users(target_user)
            username = user_info.username if user_info.username else user_info.first_name
            message.reply_text(
                f"**{username} has been banned for [{reason}].** ✅",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Unban", callback_data=f"unban:{target_user}")]]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
        except Exception:
            handle_error(message)

@app.on_message(filters.command(["unban", "unfuck"], prefixes="/"))
def handle_unban(client, message):
    if message.chat.type == "private":
        message.reply_text("**❌ Sorry, this command only works in groups.**", parse_mode=ParseMode.MARKDOWN)
        return

    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else None

    if user_id and not is_admin(user_id, chat_id) and user_id != OWNER_ID:
        message.reply_text("**❌ You don't have the necessary permissions to perform this action.**", parse_mode=ParseMode.MARKDOWN)
        return

    target_users = [word for word in message.command[1:] if word.startswith('@')]
    if not target_users:
        message.reply_text("**❌ Please specify the username or user ID.**", parse_mode=ParseMode.MARKDOWN)
        return

    for target_user in target_users:
        try:
            app.unban_chat_member(chat_id, target_user)
            message.reply_text(f"**User {target_user} has been unbanned.** ✅", parse_mode=ParseMode.MARKDOWN)
        except Exception:
            handle_error(message)

@app.on_message(filters.command(["fuckme", "kickme"], prefixes="/"))
def handle_self_kick(client, message):
    if message.chat.type == "private":
        message.reply_text("**❌ Sorry, this command only works in groups.**", parse_mode=ParseMode.MARKDOWN)
        return

    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else None

    try:
        # Check if the bot has permission to kick members
        bot_member = app.get_chat_member(chat_id, client.me.id)
        if not bot_member.can_restrict_members:
            handle_error(message, "**❌ Sorry Bro I Am Not Admin**")
            return

        app.kick_chat_member(chat_id, user_id)
        message.reply_text("**You have been kicked from the group.** ✅", parse_mode=ParseMode.MARKDOWN)
    except Exception:
        handle_error(message)

@app.on_callback_query(filters.regex(r"^unban:(.*)"))
def callback_unban(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id if callback_query.from_user else None
    target_user = callback_query.data.split(":")[1]

    if user_id and not is_admin(user_id, chat_id) and user_id != OWNER_ID:
        callback_query.answer("**❌ You don't have the necessary permissions to perform this action.**", show_alert=True)
        return

    try:
        app.unban_chat_member(chat_id, target_user)
        callback_query.answer("User has been unbanned.")
        callback_query.message.edit_text(f"**User {target_user} has been unbanned.** ✅", parse_mode=ParseMode.MARKDOWN)
    except Exception:
        callback_query.answer("**❌ An error occurred while processing the request.**", show_alert=True)

if __name__ == "__main__":
    app.run()
