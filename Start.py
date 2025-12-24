from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# ===== EDIT ONLY THESE =====
BOT_USERNAME = "@Kitty_xmusicbot"   # without @
DEV_USERNAME = "@krish_hu_bc"
SUPPORT_GROUP = "https://t.me/Krishbots"
UPDATES_CHANNEL = "https://t.me/krishupdates"
INTRO_IMAGE = "https://t.me/supp8iiiny/26"
# ==========================

INTRO_TEXT = (
    "𝑾𝒆𝒍𝒄𝒐𝒎𝒆 🎧🖤\n\n"
    "𝑰’𝒎 𝑨 𝑴𝒖𝒔𝒊𝒄 + 𝑴𝒂𝒏𝒂𝒈𝒆𝒎𝒆𝒏𝒕 𝑩𝒐𝒕\n"
    "𝑭𝒐𝒓 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎\n\n"
    "🎶 𝑯𝒊𝒈𝒉-𝑸𝒖𝒂𝒍𝒊𝒕𝒚 𝑴𝒖𝒔𝒊𝒄\n"
    "⚡ 𝑭𝒂𝒔𝒕 & 𝑺𝒎𝒐𝒐𝒕𝒉\n"
    "🛡 𝑨𝒅𝒎𝒊𝒏 𝑪𝒐𝒏𝒕𝒓𝒐𝒍𝒔\n\n"
    "➕ 𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑 🚀\n\n"
    f"✦ 𝑫𝒆𝒗 » {DEV_USERNAME} 🖤"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [
            InlineKeyboardButton("🆘 Support", url=SUPPORT_GROUP),
            InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL)
        ],
        [
            InlineKeyboardButton(
                "➕ Add To Group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton("♻️ Clone Bot", callback_data="clone")
        ]
    ]

    await update.message.reply_photo(
        photo=INTRO_IMAGE,
        caption=INTRO_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
