from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN:Final='7675826290:AAFbYiOge74btiJxMdL2ec0rW9ATW0YXbo0'
BOT_USERNAME:Final='@Intelix_agent_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! Iam a Intellix bot')
