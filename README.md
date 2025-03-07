# 🤖 Eniax-X: Chatbot Inteligente Empresarial

**Solución de Asistencia Automatizada con IA Avanzada**  
*Powered by Flask & NLP - Sistema de Conversación Empresarial Nivel Enterprise*

[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-ff69b4)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org)
[![Stack Tecnológico](https://img.shields.io/badge/Stack-Flask%20%7C%20ChatterBot%20%7C%20SpaCy-orange)](https://spacy.io)

![Interfaz del Chatbot](demo-preview.gif)

## 🌟 Características Principales

- **Motor de NLP Avanzado** con comprensión contextual
- **Entrenamiento Dual**: Datos personalizados + Corpus en español
- **Interfaz Profesional** con animaciones fluidas
- **Sistema de Aprendizaje Continuo** (Auto-update de conocimiento)
- **Seguridad Empresarial** con sanitización de inputs

## 🚀 Instalación Express

```bash
# Clonar repositorio
git clone https://github.com/EFRAN033/Chatbot.git
cd chatbot-Eniax-x

# Crear entorno virtual (Linux/Mac)
python -m venv eniax-env
source eniax-env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor
python server.py


🧠 Estructura del Proyecto


chatbot-Eniax-x/
├── static/
│   └── style.css           # Estilos premium
├── templates/
│   └── index.html          # Interfaz profesional
├── database.sqlite3        # Base de conocimiento
├── server.py               # Núcleo del sistema
└── requirements.txt        # Dependencias certificadas


🔧 Configuración Personalizada

# Configuración Avanzada (server.py)

class EniaxConfig:
    NLP_THRESHOLD = 0.85    # Precisión requerida
    SECURITY_LEVEL = 'Tier3'# Protocolos OWASP
    AUTO_LEARNING = True    # Mejora automática
    RESPONSE_MODES = {      # Perfiles de respuesta
        'basic': 'Modo Rápido',
        'pro': 'Modo Contextual',
        'enterprise': 'IA Predictiva'
    }

📚 Base de Conocimiento

# Datos de Entrenamiento (custom_data)
[
    "¿Horario de atención? - ⏰ Lunes-Viernes 9AM-7PM",
    "¿Ubicación? - 📍 Av. Principal 123, Ciudad",
    "¿Métodos de pago? - 💳 Tarjetas/Transferencias/Efectivo",
    "¿Soporte técnico? - 🛠 24/7 via soporte@eniax.com"
]


🌐 API Enterprise


POST /api/v1/dialog
Content-Type: application/json

{
  "message": "Consulta del usuario",
  "context": {"user_id": "ABC-123"},
  "mode": "pro"
}

Respuesta de Éxito

{
  "response": "Respuesta generada",
  "confidence": 0.92,
  "suggestions": ["Opción 1", "Opción 2"],
  "timestamp": "2025-03-07T15:30:00Z"
}

