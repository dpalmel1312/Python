dic = {
    # --- PRONOMBRES Y CONECTORES (La base de las frases) ---
    'yo': 'i', 'tú': 'you', 'él': 'he', 'ella': 'she', 'nosotros': 'we', 'ellos': 'they',
    'y': 'and', 'o': 'or', 'pero': 'but', 'porque': 'because', 'si': 'if', 'aunque': 'although',
    'mi': 'my', 'tu': 'your', 'su': 'his/her', 'este': 'this', 'ese': 'that',

    # --- VERBOS DE ACCIÓN (Más de 50 verbos) ---
    'aceptar': 'accept', 'abrir': 'open', 'andar': 'walk', 'aprender': 'learn', 'ayudar': 'help',
    'bailar': 'dance', 'beber': 'drink', 'buscar': 'search', 'caer': 'fall', 'cantar': 'sing',
    'cerrar': 'close', 'cocinar': 'cook', 'comer': 'eat', 'comprar': 'buy', 'conducir': 'drive',
    'conocer': 'know', 'correr': 'run', 'crear': 'create', 'creer': 'believe', 'dar': 'give',
    'decir': 'say', 'dejar': 'leave', 'dormir': 'sleep', 'empezar': 'start', 'encontrar': 'find',
    'entender': 'understand', 'escribir': 'write', 'escuchar': 'listen', 'esperar': 'wait',
    'estudiar': 'study', 'hablar': 'speak', 'hacer': 'do', 'ir': 'go', 'jugar': 'play',
    'leer': 'read', 'limpiar': 'clean', 'llamar': 'call', 'llegar': 'arrive', 'llevar': 'carry',
    'mirar': 'look', 'morir': 'die', 'necesitar': 'need', 'oír': 'hear', 'pagar': 'pay',
    'pensar': 'think', 'poder': 'can', 'poner': 'put', 'querer': 'want', 'reír': 'laugh',
    'saber': 'know', 'salir': 'leave', 'sentir': 'feel', 'ser': 'be', 'tener': 'have',
    'tomar': 'take', 'trabajar': 'work', 'traer': 'bring', 'usar': 'use', 'venir': 'come',
    'ver': 'see', 'viajar': 'travel', 'vivir': 'live', 'volar': 'fly', 'volver': 'return',

    # --- ADJETIVOS (Para describir cualquier cosa) ---
    'alto': 'tall', 'bajo': 'short', 'grande': 'big', 'pequeño': 'small', 'largo': 'long',
    'corto': 'short', 'ancho': 'wide', 'estrecho': 'narrow', 'bueno': 'good', 'malo': 'bad',
    'feliz': 'happy', 'triste': 'sad', 'enojado': 'angry', 'cansado': 'tired', 'enfermo': 'sick',
    'fuerte': 'strong', 'débil': 'weak', 'rico': 'rich', 'pobre': 'poor', 'nuevo': 'new',
    'viejo': 'old', 'joven': 'young', 'caliente': 'hot', 'frío': 'cold', 'rápido': 'fast',
    'lento': 'slow', 'fácil': 'easy', 'difícil': 'difficult', 'hermoso': 'beautiful', 'feo': 'ugly',
    'limpio': 'clean', 'sucio': 'dirty', 'caro': 'expensive', 'barato': 'cheap', 'lleno': 'full',
    'vacío': 'empty', 'inteligente': 'smart', 'tonto': 'stupid', 'divertido': 'funny',

    # --- SUSTANTIVOS: NATURALEZA Y TIEMPO ---
    'sol': 'sun', 'luna': 'moon', 'estrella': 'star', 'cielo': 'sky', 'nube': 'cloud',
    'lluvia': 'rain', 'nieve': 'snow', 'viento': 'wind', 'mar': 'sea', 'río': 'river',
    'montaña': 'mountain', 'bosque': 'forest', 'árbol': 'tree', 'flor': 'flower', 'tierra': 'earth',
    'fuego': 'fire', 'aire': 'air', 'clima': 'weather', 'día': 'day', 'noche': 'night',
    'semana': 'week', 'mes': 'month', 'año': 'year', 'hoy': 'today', 'mañana': 'tomorrow',

    # --- SUSTANTIVOS: CIUDAD Y OBJETOS ---
    'casa': 'house', 'puerta': 'door', 'ventana': 'window', 'mesa': 'table', 'silla': 'chair',
    'cama': 'bed', 'cocina': 'kitchen', 'baño': 'bathroom', 'ciudad': 'city', 'calle': 'street',
    'escuela': 'school', 'hospital': 'hospital', 'tienda': 'shop', 'dinero': 'money', 'trabajo': 'job',
    'libro': 'book', 'papel': 'paper', 'computadora': 'computer', 'teléfono': 'phone', 'ropa': 'clothes'
}

frase=input("Dime una frase: ")
frase=frase.split(" ")
frasef=""
for palabra in frase:
    frasef += dic[palabra]
    frasef += (" ") 
print(frasef)

