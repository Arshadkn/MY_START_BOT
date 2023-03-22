from pyrogram import Client, filters 


API_ID = "11266671"
API_HASH = "e46ba5c5399e3407a1d973cb93aaeabd"
BOT_TOKEN = "5559287245:AAGRi6k45DJ_IVuHaCygLnfX9vtpk1qhND4"


ARSHAD = Client(
    name="Pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@ARSHAD.on_message(filters.command("start"))
async def start_cmd(client, message): 
    await message.reply_text("✨ Hey I am Just a Test Bot")


@ARSHAD.on_message(filters.command("help"))
async def help_cmd(client, message):    
    await message.reply_text("My owner Was Testing.Currently I have Yet feature 📝")

@ARSHAS.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.reply_text("Still Online")



print("I Am STARTING")


ARSHAD.run()











