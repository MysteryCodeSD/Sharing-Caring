#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='t.me/MysterySD'>꧁❏รเlєภt ๔є๓๏ภ❏꧂</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Channel : @FuZionX\n○ Support Group : @FuZionXGroup</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("↩ 𝗕𝗮𝗰𝗸", callback_data = "back"),
                        InlineKeyboardButton("🔐 𝗖𝗹𝗼𝘀𝗲 🔐", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = f"<b>COMPLETE PROCESS TO GET THE REQUIRED CONTENT FROM THE SUB-CHANNELS</b>\n\n<i>Steps To Be Followed One By One !!</i>\n\n<b>First Of All We Have 6 Channels with Different Categories !!</b>\n\n<i><b>Step 1 :</b> Check If it is in</i> <a href='https://t.me/FuZionX'>Updates Channel</a> , <i>You can Easily Get in which Channel it is Available. Sub-Channels Description are Written at the Bottom of Every Post Given Here.</i>\n\n<i><b>Step 2 :</b> Now Check the</i> <a href='https://t.me/FuZionXPathWay/52'>SUB-CHANNELS JOINING LINKS</a> <i>, these is the Complete List of Channels with the Links.</i>\n\n<i><b>Step 3 :</b> Firstly Open the Joining Link, Click on Request to Join and You will be Added to Channel and you will be Added to Channel in 24hrs 😋.</i>\n\n<i><b>Step 4 :</b> You can See that Posts are there with Buttons (Like 𝗦𝗲𝗮𝘀𝗼𝗻 𝟭, etc ) Click On It, You will be Redirected to Our Store Bots .</i>\n\n<i><b>Step 5 :</b> Now Just Click on Start Button at the Bottom of the Screen. Then Just Watch, All Files will Be Given to You. </i>\n\n<i><b>Step 6 :</b> Now Forward Those Files to Your Saved Messages to Save for Future . Then Download the Files and Watch 🍿</i>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙇𝙞𝙣𝙠𝙨 ⚡", url = "https://t.me/FuZionX_PathWay/52")
                    ],
                    [
                        InlineKeyboardButton("↩ 𝗕𝗮𝗰𝗸", callback_data = "back"),
                        InlineKeyboardButton("🔐 𝗖𝗹𝗼𝘀𝗲 🔐", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "back":
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡ 𝗛𝗲𝗹𝗽 ⚡", callback_data = "help")
                ],
                [
                    InlineKeyboardButton("⚡ 𝗔𝗯𝗼𝘂𝘁 𝗠𝗲 ⚡", callback_data = "about"),
                    InlineKeyboardButton("⚡ 𝗖𝗹𝗼𝘀𝗲 ⚡", callback_data = "close")
                ],
                [
                    InlineKeyboardButton("⚡ 𝙁𝙪𝙕𝙞𝙤𝙣𝙓 ⚡", url = "https://t.me/FuZionX"),
                    InlineKeyboardButton("⚡ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 ⚡", url = "https://t.me/FuZionXGroup")
                ]
            ]
        )
        await query.message.edit_text(
            text = START_MSG.format(
                first = query.message.from_user.first_name,
                last = query.message.from_user.last_name,
                username = None if not query.message.from_user.username else '@' + query.message.from_user.username,
                mention = query.message.from_user.mention,
                id = query.message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
