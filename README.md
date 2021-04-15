# DiscordRNNBot
A Discord bot that generates messages that would be said on the Discord server of your choice.

You must use Python3. Python2 does not work.

Python libraries required: discord.py, tensorflow (gpu or cpu), and textgenrnn

# How to Create the Dataset
To create the dataset seperate each message into seperate lines in a text file. To get the messages, I would suggest you use a Discord chat exporter. I suggest making a dataset that contains only the messages and no usernames.
# Training
1. To train on the dataset, change the string that says "Dataset Path" on line 6 to the path of your dataset.
2. To train the RNN type in, `python trainRNN.py <amount of epochs>`
3. Change the `batch_size` section on line 6 to the batch size that would be best optimized for your hardware. Good practice is to make the batch size a power of two, but it really doesn't matter what you set it too (just don't kill your VRAM/RAM).
# Testing the RNN Before Starting the Bot
To test the trained RNN, run `python genTest.py <the temperature of the bot>`. The higher the temperature is the more creative the RNN is, the lower the temperature the less creative the RNN is.
# Bot Setup
To setup the Discord bot input your Discord bot token in line 53 of the `discordBotRNN.py` script. If you don't do this the bot won't work.
Then run `python discordBotRNN.py` to start the Discord bot.
Add it to your server and have some fun with it.
Type `.help` to get started.
