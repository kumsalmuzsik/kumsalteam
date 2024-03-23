import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

from InflexMusic import app
from InflexMusic.misc import SUDOERS
from InflexMusic.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
)
from InflexMusic.utils.decorators.language import language
from InflexMusic.utils.formatters import alpha_to_int
from config import adminlist

IS_BROADCASTING = False


@app.on_message(filters.command("broadcast") & SUDOERS)
@language
async def broadcast_message(client, message, _):
    global IS_BROADCASTING
    
    # Check if the command is invoked by @Sajjan_Jaat or has the user ID 1061004288 and is in the sudoers list
    is_special_user = (message.from_user.username == "Sajjan_Jaat" or
                       message.from_user.id == 1061004288)
    
    # Check if the user is in the sudoers list
    is_sudoer = message.from_user.id in SUDOERS

    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1]
        if "-pin" in query:
            query = query.replace("-pin", "")
        if "-nobot" in query:
            query = query.replace("-nobot", "")
        if "-pinloud" in query:
            query = query.replace("-pinloud", "")
        if "-assistant" in query:
            query = query.replace("-assistant", "")
        if "-user" in query:
            query = query.replace("-user", "")
        if query == "":
            return await message.reply_text(_["broad_8"])

    IS_BROADCASTING = True
    await message.reply_text(_["broad_1"])

    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                if "-pin" in message.text:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await m.pin(disable_notification=False)
                        pin += 1
                    except:
                        continue
                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                continue
        
    if "-user" in message.text:
        susr = 0
        served_users = []
        susers = await get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                susr += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                pass
    
    if "-assistant" in message.text:
        aw = await message.reply_text(_["broad_5"])
        text = _["broad_6"]
        from InflexMusic.core.userbot import assistants

        for num in assistants:
            sent = 0
            client = await get_client(num)
            async for dialog in client.get_dialogs():
                try:
                    await client.forward_messages(
                        dialog.chat.id, y, x
                    ) if message.reply_to_message else await client.send_message(
                        dialog.chat.id, text=query
                    )
                    sent += 1
                    await asyncio.sleep(3)
                except FloodWait as fw:
                    flood_time = int(fw.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue
            text += _["broad_7"].format(num, sent)
        try:
            await aw.edit_text(text)
        except:
            pass
            
    IS_BROADCASTING = False
    
    # Send completion message based on user
    if is_special_user and is_sudoer:
        completion_msg = "» 𝖡𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖳𝗈 𝖢𝗁𝖺𝗍𝗌."
        if "-user" in message.text:
            completion_msg = "» 𝖡𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖳𝗈 𝖢𝗁𝖺𝗍𝗌 𝖠𝗇𝖽 𝖴𝗌𝖾𝗋𝗌."
    else:
        completion_msg = _["broad_3"].format(sent, pin)
        if "-user" in message.text:
            completion_msg = _["broad_4"].format(susr)
            
    await message.reply_text(completion_msg)
