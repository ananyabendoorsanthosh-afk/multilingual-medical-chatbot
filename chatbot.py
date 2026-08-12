conversation = []
current_language = "English"


def detect_language(text):
    text = text.lower()

    hindi = ["namaste", "mera", "mujhe", "hai", "kya", "chahiye"]
    kannada = ["namaskara", "nanage", "enu", "beku", "hege"]
    spanish = ["hola", "quiero", "necesito", "como", "gracias"]

    if any(word in text.split() for word in hindi):
        return "Hindi"

    if any(word in text.split() for word in kannada):
        return "Kannada"

    if any(word in text.split() for word in spanish):
        return "Spanish"

    return "English"


def get_response(text, language):
    text = text.lower()

    if "order" in text or "pedido" in text:
        intent = "order"
    elif "help" in text or "madad" in text or "ayuda" in text:
        intent = "help"
    else:
        intent = "general"

    if language == "Hindi":
        if intent == "order":
            return "Main aapke order ki jankari check karne mein madad karunga."
        elif intent == "help":
            return "Bilkul, main aapki madad karunga."
        return "Ji, main aapki baat samajh gaya."

    elif language == "Kannada":
        if intent == "order":
            return "ನಿಮ್ಮ ಆರ್ಡರ್ ಮಾಹಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಲು ನಾನು ಸಹಾಯ ಮಾಡುತ್ತೇನೆ."
        elif intent == "help":
            return "ಖಂಡಿತ, ನಾನು ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತೇನೆ."
        return "ಹೌದು, ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ನಾನು ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇನೆ."

    elif language == "Spanish":
        if intent == "order":
            return "Claro, te ayudaré a comprobar tu pedido."
        elif intent == "help":
            return "Claro, te ayudaré."
        return "Sí, entiendo tu pregunta."

    else:
        if intent == "order":
            return "Sure, I will help you check your order information."
        elif intent == "help":
            return "Sure, I will help you."
        return "Yes, I understand your question."


def chatbot(message):
    global current_language

    language = detect_language(message)

    conversation.append({
        "message": message,
        "language": language
    })

    current_language = language

    return get_response(message, language)


messages = [
    "I need help with my order",
    "Namaste, mujhe apne order ki information chahiye",
    "Namaskara, nanage help beku",
    "Hola, necesito ayuda con mi pedido"
]

print("MULTILINGUAL CHATBOT")
print("--------------------")

for message in messages:
    print("\nUser:", message)
    print("Language:", detect_language(message))
    print("Bot:", chatbot(message))

print("\nConversation Context:")
for item in conversation:
    print(item["language"], ":", item["message"])
