import logging
from datetime import datetime, timedelta
import pytz
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

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
    formatted_time = new_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    return formatted_time

def process_command(update: Update, context: CallbackContext) -> None:
    # Get the command arguments
    command_args = context.args
    
    # Check if the command has enough parts
    if len(command_args) < 4:
        update.message.reply_text("Invalid command. Use: /bgmi <target> <port> <time> <threads>")
        return
    
    # Extract the time part and convert it to an integer
    try:
        offset_seconds = int(command_args[2])
    except ValueError:
        update.message.reply_text("Invalid time format. Time should be an integer representing seconds.")
        return
    
    # Get the current Indian time with the offset
    response_time = get_indian_time_with_offset(offset_seconds)
    
    # Reply with the calculated time
    update.message.reply_text(f"Current Indian time plus {offset_seconds} seconds is: {response_time}")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(BOT_TOKEN)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Register the command handler
    dispatcher.add_handler(CommandHandler("bgmi", process_command))
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
