import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

# Configura el logging para ver errores y mensajes
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Las funciones que manejan eventos ahora deben ser asíncronas (async)
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Esta función se ejecuta cada vez que se recibe un documento PDF.
    Descarga el archivo y responde al usuario.
    """
    document = update.message.document
    file = await document.get_file()
    # El nombre del método para descargar cambió en versiones recientes
    await file.download_to_drive('input.pdf')
    await update.message.reply_text("PDF recibido y guardado como input.pdf")

def main() -> None:
    """Inicia el bot y lo mantiene corriendo."""
    # Leemos el token de la variable de entorno
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    if not TOKEN:
        logging.error("La variable de entorno TELEGRAM_TOKEN no está definida.")
        sys.exit("Por favor, define la variable de entorno TELEGRAM_TOKEN con tu token de bot de Telegram.")

    # Usamos Application.builder para crear la aplicación del bot (la forma moderna)
    application = Application.builder().token(TOKEN).build()

    # Añadimos un manejador que solo responde a documentos PDF.
    application.add_handler(MessageHandler(filters.Document.PDF, handle_document))

    # Inicia el bot. run_polling() es bloqueante y maneja el ciclo de vida.
    print("Bot iniciado. Esperando PDFs...")
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
