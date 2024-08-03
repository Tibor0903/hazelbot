import discord
from datetime import timedelta

CHANNEL_NAME = "2"

async def two_on_message(message, bot):
    
    if message.author == bot:
        return

    if message.channel.name != CHANNEL_NAME:
        return

    print(f"two: recieved message in channel")

    if await search_string(message.content):
            print(f"two: message {message.content} is Acceptable.")
    else:
        print(f"two: message {message.content} is Unacceptable. Deleting...")
        await message.delete()

async def two_on_message_edit(before, after, bot):
    if before.author == bot:
        return

    if before.channel.name != CHANNEL_NAME:
        return
    

    print(f"message \"{before.content}\" has been edited to \"{after.content}\"")
    editValid = await search_string(after.content)
    if editValid:
        print(f"two: message edit is valid.")
    else:
        print(f"two: message edit is not valid, invoking Wrath.")
        await before.channel.send(f"<@{before.author.id}> has made an invalid edit!! they will be obli-two-rated.")
        await before.author.edit(nick = "LOOK AT THIS [LOSER]!!")
        await before.author.timeout(timedelta(seconds=30))

valid_substrings = ["2", "two", "Two", "TWo", "TWO", "tWO", "twO", "tWo", "TwO", "💕", "②","₂", "²", "⑵", "⒉", "２", "𝟐", "𝟚", "𝟤", "𝟮", "🄃", "𝟸" ]

async def search_string(string):
    for x in valid_substrings:
        if x in string:
            print(f"two: found substring {x} in string {string}!")
            return True
    print(f"two: could not find any matching substrings in {string}.")
    return False
