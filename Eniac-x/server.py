from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from unidecode import unidecode
import logging

app = Flask(__name__)
CORS(app)

# Configuración de logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Preprocesamiento de texto
def preprocess_text(text):
    """Normaliza el texto para mejorar el reconocimiento"""
    text = unidecode(text).lower()  # Remueve acentos y convierte a minúsculas
    return ''.join([c for c in text if c.isalnum() or c.isspace()]).strip()

chatbot = ChatBot(
    'MiBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'No entendí bien tu pregunta. ¿Podrías reformularla?',
            'maximum_similarity_threshold': 0.75
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
)

# Datos de entrenamiento en formato correcto
custom_data = [
    "¿Cuál es tu horario de atención? - ⏰ Nuestro horario es Lunes a Viernes de 9:00 AM a 7:00 PM.",
    "¿A qué hora abren? - ⏰ Nuestro horario de apertura es a las 9:00 AM.",
    "¿Dónde están ubicados? - 📍 Dirección: Av. Principal 123, Ciudad.",
    "¿Cómo los contacto? - 📧 Puedes escribirnos a contacto@empresa.com",
    "¿Qué métodos de pago tienen? - 💳 Aceptamos múltiples métodos: tarjetas, transferencias y efectivo.",
    "¿Hacen envíos? - 🚚 Sí, enviamos a toda la ciudad sin costo adicional."
]

# Entrenamiento con ListTrainer
trainer = ListTrainer(chatbot)
trainer.train([
    "Hola",
    "¡Hola! 👋 ¿En qué puedo ayudarte hoy?",
    "Gracias",
    "¡De nada! 😊 ¿Necesitas ayuda con algo más?",
    "Adiós",
    "¡Gracias por contactarnos! Hasta luego. 👋"
])

# Entrenar con los datos personalizados usando el formato correcto
for pair in custom_data:
    question, answer = pair.split(" - ")
    trainer.train([question, answer])

# Entrenamiento con corpus español
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train("chatterbot.corpus.spanish")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'response': 'Por favor envía un mensaje válido.'}), 400
        
        # Preprocesamiento
        processed_message = preprocess_text(user_message)
        logger.info(f"Mensaje recibido: {user_message} -> Procesado: {processed_message}")

        # Obtener respuesta
        response = chatbot.get_response(processed_message)
        
        # Validar confianza de respuesta
        if response.confidence < 0.3:
            return jsonify({'response': "¿Podrías reformular tu pregunta? No logro entenderla completamente."})
        
        return jsonify({'response': str(response)})
    
    except Exception as e:
        logger.error(f"Error en get_response: {str(e)}", exc_info=True)
        return jsonify({'response': "⚠️ Ocurrió un error procesando tu solicitud. Intenta nuevamente."}), 500

if __name__ == '__main__':
    app.run(debug=True)