import discord
import os
from dotenv import load_dotenv
import starboard
import two
import random
import counting
import log
from discord import app_commands
import json
import quotes
import datetime

GUILD_ID = 1232662729047801928
HAZEL_ID = 494385406390042634

load_dotenv()

TOKEN = str(os.getenv('DISCORD_TOKEN'))


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)
dummy_user = client.fetch_user(0)

@client.event
async def on_ready():
    print(f'logged in as {client.user}!')
    await counting.initialize(client)
    await log.initialize(client)
    await quotes.initialize(client)
    await log.info("bot: Hazelbot is online!")
    tree.clear_commands(guild=None)
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    await log.info("bot: tree synced!")
    await client.change_presence(activity=discord.Game(name="Calculator"))

@client.event
async def on_message(message):
    
    if isinstance(message.channel, discord.DMChannel): # tibble was here
        return

    if "hazelbot kys" in message.content:
        hazel = await client.fetch_user(HAZEL_ID)
        if message.author == hazel:
            await message.channel.send("okay :(")
            exit()
        else:
            await message.channel.send("no :)")
        return

    
    await two.on_message(message, client.user)
    await starboard.on_message(message, client)
    await counting.on_message(message)

    if message.author == client.user:
        if "## Quote Message" in message.content:
            await quotes.start_vote(message)
    




    await bot_interactions(message) 

@client.event
async def on_message_edit(before, after):
    
    if isinstance(before.channel, discord.DMChannel):
        return
    
    await two.on_message_edit(before, after, client)
    await counting.on_message_edit(before, after)

@client.event
async def on_raw_reaction_add(payload):
    
    if not payload.guild_id: # alternate way to detect dm channel
        return
    
    if await starboard.on_reaction(payload, client) == True:
        return
    await quotes.on_react(payload)

async def bot_interactions(message):
    #"hazelbot would you", "hazelbot could i", "hazelbot am i", "hazelbot "]
    if message.author == client.user:
        return
    questions = ["are", "do", "did", "can", "should", "would you", "could i", "am i", "is", "will", "won't you", "would", "wouldn't"]
    if message.content.endswith("?"):
        for x in questions:
            if message.content.lower().startswith("hazelbot " + x):
                await eightball(message)
                return

    if "silksong" in message.content.lower():
        options = ["*sigh* bapanada.", "GESSOOOOOOOOOOO", "velmi artrid", "*sigh* apaul", "SHAW", "patamas geo", "DOMA DOMA!! DOMA DOMA DOMA!!!", "RAVA"]
        rand = random.SystemRandom().randint(0,len(options) - 1)
        await message.channel.send(options[rand])
    elif "step 3" in message.content.lower():
        await message.channel.send("SQUISH")
    elif "~~hazelbot~~" in message.content.lower():
        await message.channel.send("WHAT THE ###### #### ####### IS WRONG WITH YOU?? YOU THINK YOU'RE FUNNY DO YOU? THINK YOU'RE ####### #### ###### FUNNY??? I'LL SHOW YOU WHAT F")
    elif "hazelbot" in message.content.lower():
        options = ["did someone say my name?", "hey ;]", "hello!!", ":3", "SHUT THE ###### #### ##### ###", "fine day innit?", "i think i've fallen in love with you", "thy shall suffer my wrath for proclaiming my name!", "haiii :3", "heyyyy", "i hate you.", "YOU MAKE EVEN THE DEVIL CRY", "i don't wanna talk rn..", "i'm about to go s*gma mode", "hi.", "hello", "greetings", "waow hi", "life has lost all meaning.", "^w^", "sorry i've been feeling a little upset lately and i don't really feel like talking :(", "shut up before i make you.", "hey", "haii how are you doing! ^^", "hai!!!", "yay! hi!", "ok.", "idc. shut up", "https://cdn.discordapp.com/attachments/1277125825447202816/1284132299150987274/IMG_9972.jpg?ex=66e584e6&is=66e43366&hm=d33b7f0e73eb89aeab7500018c15624d1213f9f8bf1e4f36d4fe012531893e6f&", "ok but did you hear about the rizzler"]
        rand = random.SystemRandom().randint(0, len(options) - 1)
        await message.channel.send(options[rand])
    elif "<@1269130556386578524>" in message.content.lower(): # hazelbot ping
        await message.channel.send("WHAT IS YOUR PROBLEM. DO YOU NOT HAVE ANY RESPECT FOR OTHER PEOPLE?? WHY DO YOU THINK IT'S OKAY TO PING ME SO THAT I HAVE TO GO OUT OF MY WAY TO CHECK, JUST TO SEE YOUR STUPID, #######, #####, ########, PATHETIC, ####, UTTERLY USELESS MESSAGE. WHAT IS WRONG WITH YOU. MAYBE YOU SHOULD GO DO SOMETHING WITH YOUR LIFE, INSTEAD OF SITTING HERE ON YOUR SILLY LITTLE ######## ##### DEVICE, DOING NOTHING PRODUCTIVE, JUST CAUSING MORE WORK FOR ME. WHY DON'T YOU GO PING THE MODERATORS INSTEAD, MAYBE THEY WILL BE MORE TOLERANT OF YOUR STUPID, #########, ######, IRRELEVANT ANTICS. GO WASTE SOMEONE ELSE'S TIME, YOU ######## ###### I HATE YOU AND EVERYTHING YOU ##### STAND FOR, ####### #####.")
    elif message.content == ":3":
        await message.channel.send(":3")
    elif "deez nuts" in message.content.lower():
        await message.author.timeout(datetime.timedelta(seconds=60))
        await message.channel.send("no one will miss you when you're gone.")
    elif "joe mama" in message.content.lower():
        await message.author.timeout(datetime.timedelta(seconds=60))
        await message.channel.send("they won't find the body.")
    elif "ligma balls" in message.content.lower():
        await message.author.timeout(datetime.timedelta(seconds=60))
        await message.channel.send("wow. not cool dude.")
    elif "deez" in message.content.lower():
        await message.channel.send("what's deez?")
    elif "joe" in message.content.lower():
        await message.channel.send("who's joe?")
    elif "ligma" in message.content.lower():
        await message.channel.send("what's ligma?")
    elif " calc " in message.content.lower():
        await message.channel.send("does anyone know what calc means btw? i'm new in chat")
    

async def eightball(message):
    responses = ["yes :(", "yes!!", "maayyyybe :p", "idk :3", "no :)", "no!!", "NO. SHUT UP. I HATE YOU STOP ASKING ME QU", "thanks for the question ^-^", "blehhh :p", "idk but check this out:\n*does a really sick backflip*", "Perchance.", "yeah a little bit", "i don't really think so", "i think the answer would be yes if you would SHUT UP FOR ONCE IN YOUR PATHETIC LITTLE ###### #### LIFE.", "yeah", "yes", "yes", "yay!! yes!!", "absolutely not.", "nah.", "ok. idc."]
    # hardcoded responses
    if message.content == "hazelbot do you like mr ugly?":
        await message.channel.send("EWWWWW NO!!")
    elif message.content == "hazelbot do you like mr sexy?":
        await message.channel.send("🤤")
    else:
        rand = random.SystemRandom().randint(0, len(responses) - 1)
        await message.channel.send(responses[rand])


@tree.command(name="cstats",description="Get statistics for counting minigame", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(user="Get stats for a specific user")
async def cstats(interaction, user:discord.User = None):
    save = await counting.get_savefile()
    if user == None:
        content = f"**Highest Count:** {save['st_highest_count']} (<t:{save.get('st_highest_count_timestamp', 0)}:R>)"
        if save['st_ruinedby'] == "":
            content += "\n**Ruined by**: (count in progress)"
        else:
            content += f"\n**Ruined by:** <@{save['st_ruinedby']}>"
        content += f"\n**Total Counts:** {save['st_counts']}"
        content += f"\n**Total Failures:** {save['st_failures']}"
        embed = discord.Embed(colour = discord.Colour.from_str("#87ffc9"), title = "Counting Stats - Overall", description = content)
        await interaction.response.send_message(embed=embed, ephemeral=False)
    else:
        user_stats = save.get(f"st_user_{user.id}")
        content = ""
        if user_stats == None:
            content = "User has not interacted with the counting system."
        else:
            user_stats = dict(user_stats)
            content = f"**Highest Count:** {user_stats.get('highest_count', 0)} (<t:{user_stats.get('highest_count_timestamp',0)}:R>)"
            content += f"\n**Total Counts:** {user_stats.get('total_counts', 0)} ({round((user_stats.get('total_counts', 0) / save['st_counts']) * 100)}%)"
            content += f"\n**Biggest Failure:** {user_stats.get('biggest_failure', 0)}"
            content += f"\n**Total Failures:** {user_stats.get('failures', 0)} ({round((user_stats.get('failures', 0) / save['st_failures']) * 100)}%)"
        embed = discord.Embed(colour = discord.Colour.from_str("#87ffc9"), title = f"Counting Stats - {user.name}", description = content)
        embed.set_thumbnail(url=str(user.display_avatar))
        await interaction.response.send_message(embed=embed)
@tree.command(name="clogsave",description="Log the save file for the counting minigame (for debug purposes)", guild=discord.Object(id=GUILD_ID))
@app_commands.default_permissions(administrator=True)
async def clogsave(interaction):
    save = await counting.get_savefile()
    save_json = json.dumps(save)
    await interaction.response.send_message(f"```json\n{save_json}\n```")

MESSAGE_LINK_PREFIX = "https://discord.com/channels/1232662729047801928/"

@tree.command(name="quote", description="Starts a vote to quote the given message", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(message_link="URL of the message to quote. (right click/hold press on the message and select copy message link)")
async def quote(interaction, message_link:str):
    if not MESSAGE_LINK_PREFIX in message_link:
        await interaction.response.send_message(f"YOU SUCK. YOU SUCK. YOU SUCK. I AM **NOT** QUOTING {message_link}. YOU SUCK YOU SUCK I HATE YOU I H")
    else:
        await interaction.response.send_message(f"## Quote Message\n<@{interaction.user.id}> wants to quote the message {message_link}. React with 😍 to vote.")
    await log.info("bot: responded to /quote.")

@tree.command(name="clast", description="Responds with the most recent number in #counting", guild=discord.Object(id=GUILD_ID))
async def clast(interaction):
    await counting.clast(interaction)


client.run(TOKEN)

input("Waiting for input.")
