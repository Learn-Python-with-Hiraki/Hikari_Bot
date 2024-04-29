#Verion Beta

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode

from Resources.credentials import tokentelegrambot as tokenbot
from Functions.BasicFunctions import saludo, definiciones
from Functions.chat_actions import action_typing
from Resources.DataBase import help, rules
import logging
from uuid import uuid4
from html import escape

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

@action_typing
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Saluda a hikari"""
    await update.effective_message.reply_text(text=saludo(update.effective_user.first_name),
                                              reply_to_message_id=update.effective_message.id,
                                              parse_mode=ParseMode.HTML)

@action_typing
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Acerca de Hikari Bot"""
    await update.effective_message.reply_text(text=help,
                                              reply_to_message_id=update.effective_message.id,
                                              parse_mode=ParseMode.HTML)

@action_typing
async def rules_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reglas de la comunidad AprenderPython"""
    await update.effective_message.reply_text(text=rules,
                                              reply_to_message_id=update.effective_message.id,
                                              parse_mode=ParseMode.HTML)
    
@action_typing
async def quees_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Busqueda de definiciones"""
    if len(context.args) == 0:
        await update.effective_message.reply_text(text='Especifique la definición que desea buscar.',
                                                  reply_to_message_id=update.effective_message.id,
                                                  parse_mode=ParseMode.HTML) 
        return
    user_say = " ".join(context.args)
    answer = definiciones(user_say)
    await update.effective_message.reply_text(answer,
                                              reply_to_message_id=update.effective_message.id,
                                              parse_mode=ParseMode.HTML)  


def main() -> None:

    """Start the bot."""

    application = Application.builder().token(tokenbot).build()

    application.add_handler(CommandHandler("start", start_cmd))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CommandHandler("rules", rules_cmd))
    application.add_handler(CommandHandler("quees", quees_cmd))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":

    main()
