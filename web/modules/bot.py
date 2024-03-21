import discord
from discord.ext import commands
from discord import app_commands
import properties
from log import logger
import gemini
import chatgpt

# Replace with your bot token from Discord Developer Portal
data = properties.properties_read()
bot_token = data["token"]
chat_api = data["key"]
chat_engine = data["engine"]
chat_chanel = data["chanel"]

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())


@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user.name}')
    try:
        synced = await client.tree.sync()
        logger.info(f"synced {len(synced)} commmand(s)")
    except Exception as e:
        logger.error(e)

@client.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(f"ชิ่วๆ หาทางใช้เอง บังไม่ช่วยหรอกนะ" ,ephemeral=True)
    await logger.info(f"ชิ่วๆ หาทางใช้เอง บังไม่ช่วยหรอกนะ" ,ephemeral=True)


@client.event
async def on_message(message):
    # Check if the message is from the desired channel (replace CHANNEL_ID with your channel's ID)
    if message.channel.id == int(chat_chanel) and message.author != client.user:
        # Get the message content
        message_content = message.content
        
        if message_content:
            
            user = message.author
            logger.info(f"{user} : {message_content}")

            if chat_engine == 'gemini-1.0-pro-001':
                chat_response = gemini.message_prompt(message_content)
            if chat_engine == 'gpt-4-turbo-preview':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-4-1106-preview':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-4-0613':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-4-0125-preview':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-4':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-3.5-turbo-16k-0613':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-3.5-turbo-16k':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-3.5-turbo-1106':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-3.5-turbo-0613':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-3.5-turbo-0301':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-3.5-turbo-0125':
                chat_response = chatgpt.message_prompt(message_content)
            if chat_engine == 'gpt-3.5-turbo':
                chat_response = chatgpt.message_prompt(message_content)
            

            # Split the response into chunks of 2000 characters or less
            response_chunks = [chat_response[i:i+2000] for i in range(0, len(chat_response), 2000)]

            # Get the user who sent the message
            user = message.author
            user_name = user.name
            user_id = user.id

            # Send each chunk of the response separately
            for chunk in response_chunks:
                await message.channel.send(chunk)
                logger.info(f"assistance : {chunk}")
        
    # Let the bot process other commands as well
    await client.process_commands(message)

@client.tree.command(name="clear")
@app_commands.describe(confirm = f"พิมพ์ 'confirm' เพื่อยืนยันการ Clear")
async def clear(interaction: discord.Interaction,confirm: str):
    if confirm == "confirm":
        await interaction.response.send_message(f"สำเร็จ" ,ephemeral=True,delete_after=10)
        await interaction.channel.purge()
        logger.info("Clear all message in chat")
    else:
        await interaction.response.send_message(f"กรุณาพิมพ์ ' confirm ' เพื่อยืนยันการ Clear" ,ephemeral=True)
# @clear.error


client.run(bot_token)

