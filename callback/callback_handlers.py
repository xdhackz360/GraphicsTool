from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

# Define the inline keyboards for the menus
main_menu_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Envato Elements", callback_data="envato_elements"), InlineKeyboardButton("Motion Array", callback_data="motion_array")],
    [InlineKeyboardButton("Freepik", callback_data="freepik"), InlineKeyboardButton("Unsplash", callback_data="unsplash")],
    [InlineKeyboardButton("Scribd", callback_data="scribd"), InlineKeyboardButton("Slideshare", callback_data="slideshare")],
    [InlineKeyboardButton("Free Access", callback_data="free_access"), InlineKeyboardButton("Paid Access", callback_data="paid_access")],
    [InlineKeyboardButton("For Reseller", callback_data="for_reseller"), InlineKeyboardButton("❌ Close", callback_data="close")]
])

# Responses dictionary for different commands
responses = {
    "envato_elements": (
        "<b>🌟 Quick Guide to Access Envato</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>Downloading Envato Elements File</b>\n"
        "   -  Type <code>/env1</code> followed by an Envato URL.\n"
        "   -  Example: <code>/env1 https://elements.envato.com/crystal-logo</code>\n\n"
        "<b>2:</b> 👑 <b>Pro Features</b>\n"
        "   -  Plans Daily/Weekly/Monthly\n"
        "   -  Unlimited Download Limit\n"
        "   -  Download Files with license key\n"
        "   -  24x7 Downloading Service with No Downtime\n\n"
        "<b>3:</b> 👑 <b>Buy Subscription</b>\n"
        "   -  To Buy Envato subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "motion_array": (
        "<b>🌟 Quick Guide to Access Motion Array</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>Downloading Motion Array File</b>\n"
        "   -  Type <code>/mot</code> followed by a Motion Array URL.\n"
        "   -  Example: <code>/mot https://motionarray.com/stock-video/group-of-young-urban-men-holding-gun-bat-and-basketball-in-alley-2895091/</code>\n\n"
        "<b>2:</b> 👑 <b>Pro Features</b>\n"
        "   -  Plans Daily/Weekly/Monthly\n"
        "   -  100 downloads per day.\n"
        "   -  24x7 Downloading Service with No Downtime\n\n"
        "<b>3:</b> 👑 <b>Buy Subscription</b>\n"
        "   -  To Buy Motion Array subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "freepik": (
        "<b>🌟 Quick Guide to Access Freepik</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>Downloading Freepik File</b>\n"
        "   -  Type <code>/pik1</code> followed by a Freepik URL.\n"
        "   -  Example: <code>/pik1 https://www.freepik.com/premium-photo/sunny-forest.htm</code>\n\n"
        "<b>2:</b> 👑 <b>Pro Features</b>\n"
        "   -  Plans Daily/Weekly/Monthly\n"
        "   -  Custom downloads Limit.\n"
        "   -  24x7 Downloading Service with No Downtime\n\n"
        "<b>3:</b> 👑 <b>Buy Subscription</b>\n"
        "   -  To Buy Freepik subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "unsplash": (
        "<b>🌟 Quick Guide to Access Unsplash+</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>Downloading Unsplash File</b>\n"
        "   -  Type <code>/uns</code> followed by an Unsplash URL.\n"
        "   -  Example: <code>/uns https://unsplash.com/photos/a-baby</code>\n\n"
        "<b>2:</b> 👑 <b>Pro Features</b>\n"
        "   -  Plans Daily/Weekly/Monthly\n"
        "   -  100 downloads per day.\n"
        "   -  24x7 Downloading Service with No Downtime\n\n"
        "<b>3:</b> 👑 <b>Buy Subscription</b>\n"
        "   -  To Buy Unsplash subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "scribd": (
        "<b>🌟 Quick Guide to Access Scribd</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>Downloading Scribd File</b>\n"
        "   -  Type <code>/scribd1</code> followed by a Scribd URL.\n"
        "   -  Example: <code>/scribd1 https://www.scribd.com/document/12345678/example-document</code>\n\n"
        "<b>2:</b> 👑 <b>Pro Features</b>\n"
        "   -  Plans Daily/Weekly/Monthly\n"
        "   -  Unlimited Download Limit\n"
        "   -  24x7 Downloading Service with No Downtime\n\n"
        "<b>3:</b> 👑 <b>Buy Subscription</b>\n"
        "   -  To Buy Scribd subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "slideshare": (
        "<b>🌟 Quick Guide to Access Slideshare</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>Downloading Slideshare File</b>\n"
        "   -  Type <code>/slide1</code> followed by a Slideshare URL.\n"
        "   -  Example: <code>/slide1 https://www.slideshare.net/xyz/example-presentation</code>\n\n"
        "<b>2:</b> 👑 <b>Pro Features</b>\n"
        "   -  Plans Daily/Weekly/Monthly\n"
        "   -  Unlimited Download Limit\n"
        "   -  24x7 Downloading Service with No Downtime\n\n"
        "<b>3:</b> 👑 <b>Buy Subscription</b>\n"
        "   -  To Buy Slideshare subscription Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "free_access": (
        "<b>Graphics-Tool Free Access</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>To Get Free Access</b>\n"
        "   -  Join this Group <a href='https://t.me/abir_x_official_graphics_hub'>Graphics - Hub🌟</a>\n\n"
        "<b>2:</b> 👑 <b>Free Features</b>\n"
        "   -  Lifetime Plan\n"
        "   -  Fast Download Services\n\n"
        "<b>3:</b> ✅ <b>Daily Limits</b>\n"
        "   -  Envato : 1\n"
        "   -  Freepik : 1\n"
        "   -  Unsplash+ : 1\n"
        "━━━━━━━━━━━━━━━━\n"
        "All Commands Explanation : <a href='https://t.me/ItsGraphicsHubs/4'>Join Now</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "paid_access": (
        "<b>Graphics-Tool Paid Access</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>1:</b> 🔗 <b>Buy Subscription</b>\n"
        "   -  Contact to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>\n\n"
        "<b>2:</b> 👑 <b>Paid Features</b>\n"
        "   -  Fast Download Services\n"
        "   -  Cheap Price\n"
        "   -  Daily/Weekly/Monthly plan\n\n"
        "<b>3:</b> ✅ <b>Daily Limits</b>\n"
        "   -  Envato : Unlimited\n"
        "   -  Freepik : Custom\n"
        "   -  Unsplash : 100 \n"
        "━━━━━━━━━━━━━━━━\n"
        "Any Questions? DM to <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "for_reseller": (
        "<b>Instructions for Resellers to Sell Bot Subscriptions</b>\n"
        "━━━━━━━━━━━━━━━━\n"
        "<b>Step 1:</b> <b>Contact the Bot Owner</b>\n"
        "   -  Telegram Username: <a href='https://t.me/abirxdhackz'>Abir Arafat Chawdhury</a>\n\n"
        "<b>Step 2:</b> <b>Take Reseller Subscription</b>\n"
        "   -  Reach out to Bot Owner to obtain reseller information.\n"
        "   -  Discuss pricing and payment details directly with Bot Owner.\n\n"
        "<b>Step 3:</b> <b>Acquire User IDs</b>\n"
        "   -  Collect the Telegram user IDs of customers interested in purchasing the bot subscription.\n\n"
        "<b>Step 4:</b> <b>Send User IDs for Activation</b>\n"
        "   -  Send the collected user IDs to Bot Owner for activation.\n"
        "   -  Activation will be processed promptly upon receiving the user IDs.\n\n"
        "<b>Step 5:</b> <b>Confirm Activation</b>\n"
        "   -  Once the subscriptions are activated, Bot Owner will notify you.\n"
        "   -  Inform your customers that their subscriptions are now active.\n\n"
        "<b>Step 6:</b> <b>Process Payment</b>\n"
        "   -  After confirming the subscription activation, make the payment to Bot Owner for the subscriptions.\n\n"
        "Ensure timely payments to maintain a smooth reselling process and good standing."
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    ),
    "about_me": (
        "<b>Name:</b> Graphics Tool️⚙️\n"
        "<b>Version:</b> 3.0 (Beta Testing) 🛠\n\n"
        "<b>Development Team:</b>\n"
        "- <b>Creator:</b> <a href='https://t.me/abirxdhackz'>⏤͟͞〲ᗩᗷiᖇ 𓊈乂ᗪ𓊉 👨‍💻</a>\n"
        "<b>Technical Stack:</b>\n"
        "- <b>Language:</b> Python 🐍\n"
        "- <b>Libraries:</b> Aiogram, Pyrogram And Telethon 📚\n"
        "- <b>Database:</b> MongoDB Database 🗄\n"
        "- <b>Hosting:</b> Hostinger VPS 🌐\n\n"
        "<b>About:</b> Smart Tool ⚙️ The ultimate Telegram toolkit! Education, AI, downloaders, temp mail, finance tools & more—simplify life!\n\n"
        ">🔔 For Bot Update News: <a href='https://t.me/ModVipRM'>Join Now</a>"
        ,
        {'parse_mode': ParseMode.HTML, 'disable_web_page_preview': True}
    )
}

async def handle_callback_query(client, callback_query):
    call = callback_query

    if call.data in responses:
        # Determine which keyboard to use for the back button based on the current menu
        if call.data == "about_me":
            back_button = InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="start_message")]
            ])
        else:
            back_button = InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
            ])

        await call.message.edit_text(
            responses[call.data][0],  # text is the first element in the tuple
            parse_mode=responses[call.data][1]['parse_mode'],
            disable_web_page_preview=responses[call.data][1]['disable_web_page_preview'],
            reply_markup=back_button
        )
    elif call.data == "main_menu":
        await call.message.edit_text(
            "<b>Here are the Graphics Tool Options:</b>",
            parse_mode=ParseMode.HTML,
            reply_markup=main_menu_keyboard
        )
    elif call.data == "start_message":
        full_name = f"{call.message.from_user.first_name} {call.message.from_user.last_name}" if call.message.from_user.last_name else call.message.from_user.first_name

        # Main welcome message
        start_message = (
            f"<b>Hi {full_name}! Welcome to this bot</b>\n"
            "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
            "<b><a href='https://t.me/abirxdhackz'>Graphics Tool️⚙️</a></b>: is the most complete Bot to help you with Graphics Resources, Effortless Downloads - Say goodbye to browsing hassles! Get your desired assets with a simple click. 💾\n"
            "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
            "<b>Don't forget to <a href='https://t.me/ModVipRM'>join</a> for updates!</b>"
        )

        await call.message.edit_text(
            start_message,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💾 Main Menu", callback_data="main_menu")],
                [InlineKeyboardButton("🔄 Updates", url="https://t.me/ModVipRM"),
                 InlineKeyboardButton("ℹ️ About Me", callback_data="about_me")]
            ]),
            disable_web_page_preview=True,
        )
    elif call.data == "freepik":
        await call.message.edit_text(
            responses["freepik"][0],
            parse_mode=responses["freepik"][1]['parse_mode'],
            disable_web_page_preview=responses["freepik"][1]['disable_web_page_preview'],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
            ])
        )
    elif call.data == "unsplash":
        await call.message.edit_text(
            responses["unsplash"][0],
            parse_mode=responses["unsplash"][1]['parse_mode'],
            disable_web_page_preview=responses["unsplash"][1]['disable_web_page_preview'],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
            ])
        )
    elif call.data == "free_access":
        await call.message.edit_text(
            responses["free_access"][0],
            parse_mode=responses["free_access"][1]['parse_mode'],
            disable_web_page_preview=responses["free_access"][1]['disable_web_page_preview'],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
            ])
        )
    elif call.data == "paid_access":
        await call.message.edit_text(
            responses["paid_access"][0],
            parse_mode=responses["paid_access"][1]['parse_mode'],
            disable_web_page_preview=responses["paid_access"][1]['disable_web_page_preview'],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
            ])
        )
    elif call.data == "for_reseller":
        await call.message.edit_text(
            responses["for_reseller"][0],
            parse_mode=responses["for_reseller"][1]['parse_mode'],
            disable_web_page_preview=responses["for_reseller"][1]['disable_web_page_preview'],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
            ])
        )
    elif call.data == "close":
        await call.message.delete()