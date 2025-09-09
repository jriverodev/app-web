from telegram.ext import Updater, MessageHandler, filters
import logging
import os
import sys

# Configura el logging para ver errores y mensajes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Lee el token de una variable de entorno para mayor seguridad.
# Antes de ejecutar el bot, asegúrate de haber definido la variable de entorno TELEGRAM_TOKEN.
# Por ejemplo, en tu terminal:
# export TELEGRAM_TOKEN="TU_TOKEN_AQUI"
TOKEN = os.getenv('TELEGRAM_TOKEN')

if not TOKEN:
    logging.error("La variable de entorno TELEGRAM_TOKEN no está definida.")
    sys.exit("Por favor, define la variable de entorno TELEGRAM_TOKEN con tu token de bot de Telegram.")

def handle_document(update, context):
    """
    Esta función se ejecuta cada vez que se recibe un documento PDF.
    Descarga el archivo y responde al usuario.
    """
    document = update.message.document
    file = document.get_file()
    file.download('input.pdf')
    update.message.reply_text("PDF recibido y guardado como input.pdf")

def main():
    """Inicia el bot."""
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Añadimos un manejador que solo responde a documentos PDF.
    dp.add_handler(MessageHandler(filters.Document.PDF, handle_document))

    # Inicia el bot
    updater.start_polling()
    print("Bot iniciado. Esperando PDFs...")
    updater.idle()

if __name__ == '__main__':
    main()
