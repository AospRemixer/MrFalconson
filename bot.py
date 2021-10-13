import discord
from discord.ext import commands
import asyncio

token = ""
bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print("Mr. Falconson is ready!")

@bot.command()
async def ping(ctx):
    await ctx.channel.send('**Pong!**')

@bot.command()
async def typeFor(ctx, prenum):
    num = int(prenum)
    if(isinstance(num, int)):
            async with ctx.channel.typing():
                await asyncio.sleep(num)
            await ctx.channel.send(f"I've been typing for **{prenum}** seconds!")
    else:
        await ctx.channel.send('Bro, its ``.typeFor (number)``, example... ``.typeFor 3``')

@bot.command()
async def MrFalconson(ctx, what, are, solar, panels):
    async with ctx.channel.typing():
        await asyncio.sleep(4)
    await ctx.channel.send("‎‎ㅤㅤㅤㅤㅤFirstly I would like to thank Prabhdeep Singh for inviting me to this great interview, it's my pleasure to be here. So, have you ever wondered how we can make our sun useful to us, this is when Solar Panels come in. Solar panels are a new revolutionary way of converting Solar Energy to electricity, which can further be used for our everyday electricity products (Komp, 2016). Our earth deflects an incredible 173000000000000000 (1.73 x 10^17; one hundred seventy-three quadrillion) terawatts of solar energy, which is 10 times the power earth's whole population uses (Komp, 2016). Solar panels consume that energy and transform it into electricity, which is why they are revolutionary (Komp, 2016).\n\n                                                                                        **References** \n\nKomp, R. (2016, January 5). How do solar panels work? - Richard Komp.\nRetrieved from <https://www.youtube.com/watch?v=xKxrkht7CpY&ab_channel=TED-Ed>")
    await ctx.channel.send("https://energyeducation.ca/wiki/images/f/fc/Energytosurface2.png")

@bot.command()
async def Well(ctx, how, do, they, work):
    async with ctx.channel.typing():
        await asyncio.sleep(4)
    await ctx.channel.send("ㅤㅤㅤㅤㅤSolars panels have a very clever design, which was designed through many trial and errors over time. Solar panels need the sun to create energy, which is because natural sunlight contains photons that the solar panels need inorder to create electricity (Komp, 2016). Solar panels have many mini solar cells in them which are jammed together with silicon (Komp, 2016). One thing to note is that silicon is the 2nd most abundant element on planet earth, which makes making solar panels easier (Komp, 2016). Each solar cell atom is connected to other atoms with 4 bonds on each side which allows the electrons to be in place and block any current flow (Komp, 2016).")
    await ctx.channel.send("https://i.snipboard.io/cRhUe6.jpg")
    await ctx.channel.send("ㅤㅤㅤㅤㅤEvery solar cell uses 2 different layers of silicon, an N type silicon and a P type silicon (Komp, 2016). The N type silicon has extra electrons, and the P type silicon has extra holes for electrons (Komp, 2016). This grats electrons the ability to cruise around in the p/n junction (Komp, 2016). This creates a positive charge on one side, and a negative charge on the other side (Komp, 2016). When the photons from natural sunlight contact a silicon cell with enough energy it will dispatch an electron from its position and leave a hole (Komp, 2016). The electric field in the p/n junction will forward the hole to the P type silicon and the electrons will forward to the N type silicon (Komp, 2016). Finally the electrons are transferred through small metal fingers, which are directly connected to any of your electrical appliances.\n\n                                                                                        **References** \n\nKomp, R. (2016, January 5). How do solar panels work? - Richard Komp.\nRetrieved from <https://www.youtube.com/watch?v=xKxrkht7CpY&ab_channel=TED-Ed>")
    await ctx.channel.send("https://s9.gifyu.com/images/ezgif.com-gif-makera60c3a0aac4a5caf.gif")
    await ctx.channel.send("https://s9.gifyu.com/images/How_do_solar_panels_work__Richard_Komp-2.gif")

@bot.command()
async def That(ctx, all, thanks, MrFalconson):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
    await ctx.channel.send("Wait wait, before you go please take some time to checkout these great research papers. They have a lot of details, and I know you will love them!\nhttps://docs.google.com/presentation/d/1s2staB-UUyMccmFl27v-NnEHcxrgpxyL57YnxKmSJ9A/edit?usp=sharing")

bot.run(token)