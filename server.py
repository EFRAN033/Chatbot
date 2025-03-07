from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer 

app = Flask(__name__)
CORS(app)


chatbot = ChatBot(
    'MiBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'No entendí tu pregunta. ¿Puedes reformularla?',
            'maximum_similarity_threshold': 0.85  
        }
    ]
)

trainer = ListTrainer(chatbot) 


custom_data = [
    "¿Cuál es tu horario de atención? - Nuestro horario es de 9:00 AM a 7:00 PM.",
    "¿Dónde están ubicados? - Estamos en Av. Principal 123, Ciudad.",
    "¿Cómo puedo contactarlos? - Escríbenos a contacto@empresa.com",
    "¿Qué métodos de pago aceptan? - Aceptamos tarjetas, transferencias y efectivo.",
    "¿Tienen envíos a domicilio? - Sí, realizamos envíos a toda la ciudad.",
    "hola - ¡Hola! ¿En qué puedo ayudarte?",
    "adiós - ¡Gracias por contactarnos! Hasta luego.",
]


trainer.train(custom_data) 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train("chatterbot.corpus.spanish")  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message'].lower()  
    
   
    if "horario" in user_message:
        return jsonify({'response': '⏰ Horario: Lunes a Viernes de 9:00 AM a 7:00 PM.'})
    
    if "ubicación" in user_message or "dirección" in user_message:
        return jsonify({'response': '📍 Estamos en Av. Principal 123, Ciudad.'})
    
    
    bot_response = chatbot.get_response(user_message)
    return jsonify({'response': str(bot_response)})

if __name__ == '__main__':
    app.run(debug=True)