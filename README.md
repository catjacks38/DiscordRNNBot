# DiscordRNNBot
A Discord bot that generates messages that would be said on the discord server of your choice.

Using python3 is required. Python2 does not work.

Python libraries required: discord.py, tensorflow (gpu or cpu), and textgenrnn

I suggest making a dataset that contains only the messages and no usernames.
To train on the data, set change the string that says "Dataset Path" on line 6 to the path of your dataset.
To train the RNN type in, `python trainRNN.py (amount of epochs)` (change amount of epochs to the amount of epochs you want to train the RNN for)
Change the `batch_size` section in line 6 to the batch size that would be most optimized for your PC. The batch size has to be divisable by 8.

To test the trained RNN, run `python genTest.py (the temperature of the bot)`. The higher the temperature is the more creative the RNN is, the lower the temperature the less creative the bot is.

To setup the Discord bot input the token of the bot you want to control in line 53 of the discordBotRNN.py script. This is a required step.
Then run `python discordBotRNN.py` to start the Discord bot.
Add it to your server and have some fun with it.
Type `.help` to get started.
