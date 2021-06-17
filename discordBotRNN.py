import discord
from discord.ext import commands
from textgenrnn import textgenrnn

temp = 0.6
upLimit = 5.0
downLimit = 0.1

textgen = textgenrnn('textgenrnn_weights.hdf5')

client = commands.Bot(command_prefix = '.')

client.remove_command('help')

@client.event
async def on_ready():
	print('Bot is Ready')
	
@client.command()
async def speak(ctx):
	global temp
	text = textgen.generate(temperature=temp, return_as_list=True)
	
	text = "".join(text)
	
	print (text)
	await ctx.send(text)

@client.command()
async def help(ctx):
	await ctx.send('>>> `Help Menue: \n.help, opens help menu \n.speak, the bot says stuff \n.temp or .temperature, changes the temperature of the bot (how creative it is). \n\n The temperature is a number.\n For Example, .temp 0.9, changes the temperature to 0.9. \n The lower the temperature of the bot is the less creative it is (copies from the training data) \n The higher the temperature of the bot is the more creative it is (Starts to make up words and sound stupid) \n The temperature range of the bot is 0.1-5.0 \n\n .wtemp, Displays the current temperature.\n The bots code can be found here: https://github.com/catjacks38/DiscordRNNBot`')

@client.command(aliases=['temperature', 'temp'])
async def _temp(ctx, *, question):

	global temp
	
	if (float(question) <= upLimit and float(question) >= downLimit):
		temp = float(question)
	
	
		print (temp)
	
		await ctx.send('The temperature is now: ' + str(temp))
	else:
		await ctx.send('The temperature is not in the supported range: ' + str(downLimit) +'-' + str(upLimit))
	
@client.command()
async def wtemp(ctx):
	global temp
	await ctx.send('The temperature is: ' + str(temp))

client.run('insert bot token hear')
