from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN:Final='7675826290:AAFbYiOge74btiJxMdL2ec0rW9ATW0YXbo0'
BOT_USERNAME:Final='@Intelix_agent_bot'

#comments
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! Iam a Intellix bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Iam Intelix ! Please type something so I can respond!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


#Handle responses
def handle_response(text: str)->str:
    processed: str = text.lower()
    if 'hello' in text:
        return 'Hey there!'
    if 'how are you' in text:
        return 'Iam good!'
    if 'i love python' in processed:
        return 'Remember to subscribe!'
    
    return 'I do not understand what you wrote'

async def handle_message(update: Update,context:ContextTypes.DEFAULT_TYPE ):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    #This if statement is used for mentioning in group
    if message_type =='group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
            response: str =handle_response(text)
    print('Bot',response)
    await update.message.reply_text(response)


#Error handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__=='__main__':
    print('Starting bot...')
    app=Application.builder().token(TOKEN).build()
    #commands

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    #poll the bot
    print('Polling ....')
    app.run_polling(poll_interval=3)
