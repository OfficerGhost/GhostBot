import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import random
import asyncio

client = commands.Bot(command_prefix='+')



responses = [
    'It is certain.', 'Without a doubt', 'Yes - definitely.',
    'It is decidedly so.', ' You may rely on it', 'As I see it, yes.',
    'most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
    'Reply hazy - try again', 'Ask agian later.', 'Better not tell you now.',
    'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.",
    ' My reply is no.', 'Outlook not good.', 'Very doubtful'
]

roulette = ["click", "click", "click", "click", "click", "boom"]


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    snipe_message_author[message.channel.id] = None
    snipe_message_content[message.channel.id] = None


# cool and all, but this isn't needed
async def on_message(self, message):
    if message.author.id == self.user.id:
        return


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command(aliases=['8ball', '8'])
async def _8(ctx, *, question):
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}'
                )


@client.command(aliases=['clean', 'clear'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name,
                                            member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(
                f'{user.name}#{user.discriminator} has been unbanned')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.member, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    return


@client.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, member: discord.member, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
    return


@client.command()
async def rr(ctx):

    await ctx.send(f'{random.choice(roulette)}')


@client.command()
async def twitch(ctx):
    await ctx.send("https://twitch.tv/OfficerGhost04")


@client.command()
async def sandwich(ctx):
    await ctx.send("sandwich")


@client.command()
async def schedule(ctx):
    await ctx.send("No Streams Scheduled Until June 2022")


@client.command()
async def rules(ctx):
    await ctx.send("please refer to the rules in the <#634822660563402763> channel")


@client.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

@client.command()
async def apply(ctx):
    await ctx.send ('If you wish to join our staff team you may apply for one of the following applications \n \n Moderator application: https://forms.gle/kNq4AP8it5Jb5hMg9 \n \n Stage mod application: https://forms.gle/yLZQYzjPvYXpMLNB8')

@client.command()
async def appall(ctx): 
    await ctx.send("you may apply to join our staff team by checking the message below to see what postions are available \n \n :ballot_box_with_check: = open    :negative_squared_cross_mark: = closed \n \n Moderator application: :ballot_box_with_check: \n  https://forms.gle/kNq4AP8it5Jb5hMg9 \n \n Stage mod application: :ballot_box_with_check: \n https://forms.gle/yLZQYzjPvYXpMLNB8")

@client.command()
async def appmod(ctx):
    await ctx.send("you may apply to join our staff team by checking the message below to see what positions are available \n \n :ballot_box_with_check: = open   :negative_squared_cross_mark: = closed \n \n Moderator application: :ballot_box_with_check: \n https://forms.gle/kNq4AP8it5Jb5hMg9 \n \n Stage mod application: :negative_squared_cross_mark:")

@client.command()
async def appstage(ctx):
    await ctx.send("you may apply to join our staff team by checking the message bleow to see what postionsare available \n \n :ballot_box_with_check: = open  :negative_squared_cross_mark: = closed \n \n Mod application: :negative_squared_cross_mark: \n \n Stage mod application: :ballot_box_with_check: \n https://forms.gle/yLZQYzjPvYXpMLNB8")

@client.command() 
async def appclosed(ctx):
    await ctx.send("all staff applications are currently closed... you may apply when they open back up")

@client.command()
async def snipe(ctx):
    channel = ctx.channel
    try:
        snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        snipeEmbed.set_footer(text=f"deleted by {snipe_message_author[channel.id]}")
        await ctx.send (embed=snipeEmbed)
    except:
        await ctx.send(f"there are no deleted messages in #{channel.name}")


keep_alive()
client.run(os.environ['TOKEN'])