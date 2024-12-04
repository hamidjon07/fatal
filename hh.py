

import telebot

# Telegram bot tokeningizni kiriting
TOKEN = "7788712794:AAGsko3wKnTO3Nd_YyHgQvZLz83R60P8OHI"
bot = telebot.TeleBot(TOKEN)


# Lotin-Kirill o'girish uchun funksiyalar
def to_cyrillic(text):
    letters = {
        "A": "А", "B": "Б", "D": "Д", "E": "Э", "F": "Ф", "G": "Г",
        "H": "Ҳ", "I": "И", "J": "Ж", "K": "К", "L": "Л", "M": "М",
        "N": "Н", "O": "О", "P": "П", "Q": "Қ", "R": "Р", "S": "С",
        "T": "Т", "U": "У", "V": "В", "X": "Х", "Y": "Й", "Z": "З",
        "a": "а", "b": "б", "d": "д", "e": "э", "f": "ф", "g": "г",
        "h": "ҳ", "i": "и", "j": "ж", "k": "к", "l": "л", "m": "м",
        "n": "н", "o": "о", "p": "п", "q": "қ", "r": "р", "s": "с",
        "t": "т", "u": "у", "v": "в", "x": "х", "y": "й", "z": "з",
        "'": "ъ", "ʼ": "ъ"
    }
    for latin, cyrillic in letters.items():
        text = text.replace(latin, cyrillic)
    return text


def to_latin(text):
    letters = {
        "А": "A", "Б": "B", "Д": "D", "Э": "E", "Ф": "F", "Г": "G",
        "Ҳ": "H", "И": "I", "Ж": "J", "К": "K", "Л": "L", "М": "M",
        "Н": "N", "О": "O", "П": "P", "Қ": "Q", "Р": "R", "С": "S",
        "Т": "T", "У": "U", "В": "V", "Х": "X", "Й": "Y", "З": "Z",
        "а": "a", "б": "b", "д": "d", "э": "e", "ф": "f", "г": "g",
        "ҳ": "h", "и": "i", "ж": "j", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "қ": "q", "р": "r", "с": "s",
        "т": "t", "у": "u", "в": "v", "х": "x", "й": "y", "з": "z",
        "ъ": "'", "Ъ": "ʼ"
    }
    for cyrillic, latin in letters.items():
        text = text.replace(cyrillic, latin)
    return text


# Xabarlarni qayta ishlash
@bot.message_handler(func=lambda message: True)
def transliterate_message(message):
    text = message.text
    if text.isascii():  # Agar matn lotin alifbosida bo'lsa
        translated_text = to_cyrillic(text)
    else:  # Agar matn kirill alifbosida bo'lsa
        translated_text = to_latin(text)

    bot.reply_to(message, translated_text)


# Botni doimiy ishga tushirish
print("Bot ishga tushdi...")
bot.polling()