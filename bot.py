from telegram.ext import Updater, MessageHandler, Filters
import logging

# Configura el logging para ver errores y mensajes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '7538941927:AAHQ2-oSzSTzPCOOOgt6MyiUvsEmYl5jNdg'

def handle_document(update, context):
    document = update.message.document
    if document.mime_type == 'application/pdf':
        file = document.get_file()
        file.download('input.pdf')
        update.message.reply_text("PDF recibido y guardado como input.pdf")
    else:
        update.message.reply_text("Por favor, envía un archivo PDF.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.document.mime_type("application/pdf"), handle_document))

    updater.start_polling()
    print("Bot iniciado. Esperando PDFs...")
    updater.idle()

if __name__ == '__main__':
    main()
pip install --no-index --find-links=. flit_core-3.12.0.tar.gz
pip install --no-index --find-links=. setuptools_scm-9.2.0.tar.gz
pip install --no-index --find-links=. calver-2025.4.17.tar.gz
pip install --no-index --find-links=. setuptools-80.9.0.tar.gz
pip install --no-index --find-links=. wheel-0.45.1.tar.gz
pip install --no-index --find-links=. pluggy-1.6.0.tar.gz
pip install --no-index --find-links=. trove_classifiers-2025.9.8.13.tar.gz
pip install --no-index --find-links=. pillow-11.3.0.tar.gz
pip install --no-index --find-links=. packaging-25.0.tar.gz
pip install --no-index --find-links=. pathspec-0.12.1.tar.gz
pip install --no-index --find-links=. hatchling-1.27.0.tar.gz
pip install --no-index --find-links=. httpx-0.28.1.tar.gz
pip install --no-index --find-links=. python_telegram_bot-22.3.tar.gz

