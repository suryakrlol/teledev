# pip install python-telegram-bot
# pip install pytz
# python bot.py

import logging
from datetime import datetime, timedelta
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7490917900:AAEZ_jIe_I1tcM2PpvdjA_dtc7o6-PoCA40'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def get_indian_time_with_offset(offset_seconds):
    # Define the Indian timezone
    india_tz = pytz.timezone('Asia/Kolkata')
    
    # Get the current time in Indian timezone
    current_time = datetime.now(india_tz)
    
    # Add the offset to the current time
    new_time = current_time + timedelta(seconds=offset_seconds)
    
    # Format the new time as a string
    formatted_time = new_time.strftime('%Y-%m-%d %I:%M:%S %p %Z')  # 12-hour format
    
    return formatted_time

async def process_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name
    # Get the command arguments
    command_args = context.args
    
    # Check if the command has enough parts
    if len(command_args) < 4:
        await update.message.reply_text(f"{user_name},\n𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐜𝐨𝐦𝐦𝐚𝐧𝐝.\nUse: /ddos <target> <port> <time> <threads>")
        return
    
    # Extract the time part and convert it to an integer
    try:
        offset_seconds = int(command_args[2])
    except ValueError:
        await update.message.reply_text(f"{user_name},\n𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙩𝙞𝙢𝙚 𝙛𝙤𝙧𝙢𝙖𝙩. 𝙏𝙞𝙢𝙚 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙖𝙣 𝙞𝙣𝙩𝙚𝙜𝙚𝙧 𝙧𝙚𝙥𝙧𝙚𝙨𝙚𝙣𝙩𝙞𝙣𝙜 𝙨𝙚𝙘𝙤𝙣𝙙𝙨.")
        return
    
    # Adjust the offset by subtracting 10 seconds
    adjusted_offset_seconds = offset_seconds - 10
    
    # Get the current Indian time with the adjusted offset
    response_time = get_indian_time_with_offset(adjusted_offset_seconds)
    
    # Introduce a 10-second delay before sending the reply
    await asyncio.sleep(10)
    
    # Reply with the calculated time
    await update.message.reply_text(f"{user_name},\n𝐒𝐭𝐫𝐢𝐤𝐞 𝐰𝐢𝐥𝐥 𝐞𝐧𝐝 𝐨𝐧 \n{response_time}")

    Warning_offset_seconds = adjusted_offset_seconds - 10

    await asyncio.sleep(Warning_offset_seconds)

    await update.message.reply_text(f"{user_name},\n𝐒𝐭𝐫𝐢𝐤𝐞 𝐰𝐢𝐥𝐥 𝐞𝐧𝐝 𝐢𝐧 10 𝙨𝙚𝙘𝙤𝙣𝙙𝙨.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name
    response = f'''𝐖𝐞𝐥𝐜𝐨𝐦𝐞, {user_name} 
𝑰 𝒕𝒂𝒌𝒆 𝒂 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 𝒘𝒊𝒕𝒉 𝒔𝒆𝒗𝒆𝒓𝒂𝒍 𝒑𝒂𝒓𝒂𝒎𝒆𝒕𝒆𝒓𝒔 𝒂𝒏𝒅 𝒓𝒆𝒔𝒑𝒐𝒏𝒅 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒄𝒂𝒍𝒄𝒖𝒍𝒂𝒕𝒆𝒅 𝒕𝒊𝒎𝒆 𝒂𝒇𝒕𝒆𝒓 𝒂 𝒃𝒓𝒊𝒆𝒇 𝒅𝒆𝒍𝒂𝒚.'''
    await update.message.reply_text(response)

def main():
    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Register the command handlers
    application.add_handler(CommandHandler("ddos", process_command))
    application.add_handler(CommandHandler("start", start))
    
    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
