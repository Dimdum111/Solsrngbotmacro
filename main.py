# -- IMPORTS --
from pyrogram import Client, filters
import asyncio
from datetime import datetime
import threading
from dotenv import load_dotenv
import os

load_dotenv()

app = Client('SolsRNGbotMacro', api_id=int(os.environ['api_id']), api_hash=os.environ['api_hash'])
rollcd = 1.75 # Recomened Cooldown.
rolling = False

helpMsg = """🍀 Sol's RNG Bot macro (v0.1)
`--=[ HELP ]=--`
.help - This message 📃
.about - About this macro 🛠️
.setrollcd - Set's roll colldown (Wip. not implemented yet)
.roll - Start the macro (Toggle on/off) 🎲
`--=[ HELP ]=--`

Macro by Dimdum111, Join @solsrngsimbotnews pls :)"""

aboutMsg = """
🍀 Sol's RNG Bot macro (v0.1) (?)

`--=[ ABOUT ]=--`
✦ Macro by - Dimdum111
✧ Sol's RNG bot by - Underrosta & Dimdum111
✦ Sol's RNG by - Sol's rng team
`--=[ ABOUT ]=--`

Check .help for help:D
And join @solsrngsimbotnews pls"""

async def rolling_loop(message):
    while rolling:
        await message.reply("🎲 Roll")
        await asyncio.sleep(rollcd)

@app.on_message(filters.command("help", prefixes=".") & filters.me)
async def help(client, message):
    await message.edit_text(helpMsg)
    
@app.on_message(filters.command("about", prefixes=".") & filters.me)
async def about(client, message):
    await message.edit_text(aboutMsg)

@app.on_message(filters.command("roll", prefixes=".") & filters.me)
async def roll(client, message):
    global rolling
    rolling = not rolling
    now = datetime.now()
    time = now.strftime("%d.%m.%Y, %H:%M:%S")
    
    if rolling:
        await message.reply(f"[✅] Macro started at {time}, with rollcd = {rollcd}S")
        asyncio.create_task(rolling_loop(message))
    else:
        await message.reply(f"[❌] Macro stopped at {time}, with rollcd = {rollcd}S")
app.run()