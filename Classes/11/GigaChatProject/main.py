import telebot
from gigachat import GigaChat
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем токены из переменных окружения
TELEGRAM_TOKEN = '7273842183:AAH6welz9AScmnjIRwN5quu1qmBps8jVazQ'
GIGACHAT_TOKEN = 'OTY2N2QzM2ItOGE2Yy00ZjBhLTlmYWUtNDg5YjRkMTFkN2UzOjc5N2E1ZDBkLTJkNjEtNDk2YS05ZDFlLWFiMjNiNTI0YjI2Yg=='

# Инициализируем бота и GigaChat
bot = telebot.TeleBot(TELEGRAM_TOKEN)
giga = GigaChat(credentials=GIGACHAT_TOKEN, verify_ssl_certs=False)

# # # Обработчик команды /start
# # @bot.message_handler(commands=['start'])
# # def send_welcome(message):
# #     # Получаем информацию о пользователе
# #     user_name = message.from_user.first_name
    
# #     welcome_text = f"""
# #     👋 Здравствуйте, {user_name}!
    
# #     Я бот-помощник, работающий на базе GigaChat.
# #     Я могу ответить на любые ваши вопросы и помочь с различными задачами.
    
# #     🤖 Что я умею:
# #     • Отвечать на вопросы
# #     • Помогать с задачами
# #     • Объяснять сложные темы
# #     • Давать рекомендации
    
# #     Просто напишите свой вопрос, и я постараюсь помочь!
# #     Используйте /help для получения дополнительной информации.
# #     """
    
#     # Отправляем приветственное сообщение
#     bot.send_message(message.chat.id, welcome_text)
    
#     # Создаем клавиатуру с командами
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#     start_button = telebot.types.KeyboardButton('/start')
#     help_button = telebot.types.KeyboardButton('/help')
#     markup.add(start_button, help_button)
    
#     # Отправляем сообщение с клавиатурой
#     bot.send_message(message.chat.id, "Выберите команду или просто напишите свой вопрос:", reply_markup=markup)

# # Обработчик команды /help
# @bot.message_handler(commands=['help'])
# def send_help(message):
#     help_text = """
#     🤖 Вот что я умею:
    
#     - Отвечать на ваши вопросы
#     - Помогать с решением задач
#     - Объяснять сложные темы
    
#     Просто напишите свой вопрос, и я отвечу!
    
#     Команды:
#     /start - Начать общение
#     /help - Показать это сообщение
#     """
#     bot.reply_to(message, help_text)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Получаем ответ от GigaChat
        response = giga.chat(message.text)
        answer = response.choices[0].message.content
        
        # Отправляем ответ пользователю
        bot.reply_to(message, answer)
    except Exception as e:
        error_message = "Извините, произошла ошибка. Попробуйте позже."
        bot.reply_to(message, error_message)
        print(f"Error: {e}")

# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    # Отправляем сообщение о запуске в консоль
    # print("Доступные команды:")
    # print("/start - Начать общение")
    # print("/help - Показать справку")
    bot.polling(none_stop=True)
