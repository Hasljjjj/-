import telebot
import time

bot_token = "هنا تحط توكن بوتك"
bot = telebot.TeleBot(bot_token)

# Create a function to respond to incoming messages
@bot.message_handler(func=lambda message: True)
def on_chat_message(message):
    # If the recipient did not call the "/start" command
    if message.text != "/start":
        # Ignore the message
        return

    # Send welcome message with photo
    photo = open('hacker.jpg', 'rb') # Replace with the name of your photo file
    bot.send_photo(message.chat.id, photo, caption='مرحبا بك في الجحيم  انتضر شوي ورح يتم ازعاجك👿!')

    time.sleep(3)
    sent_count = 0
    while True:
        for i in range(99):
            bot.send_message(message.chat.id,
                             "⠀⢀⡴⠋⠉⢉⠍⣉⡉⠉⠉⠉⠓⠲⠶⠤⣄⠀⠀⠀\n⠀⢀⠎⠀⠪⠾⢊⣁⣀⡀⠄⠀⠀⡌⠉⠁⠄⠀⢳⠀⠀\n⠀⣰⠟⣢⣤⣐⠘⠛⭕️⠻⠭⠇⠀⠟⭕️⠛⠂⠀⢌⢷⡀\n⢸⢈⢸⠠⡶⠬⣉⡉⠁⠀⣠⢄⡀⠀⠳⣄⠑⠚⣏⠁⣪⠇\n⠀⢯⡊⠀⠹⡦⣼⣍⠛⢲⠯⢭⣁⣲⣚⣁⣬⢾⢿⠈⡜⠀\n⠀⠀⠙⡄⠀⠘⢾⡉⠙⡟⠶⢶⣿⣶⣿⣶⣿⣾⣿⠀⡇⠀\n⠀⠀⠀⠙⢦⣤⡠⡙⠲⠧⠀⣠⣇⣨⣏⣽⡹⠽⠏⠀⡇⠀\n⠀⠀⠀⠀⠈⠙⠦⢕⡋⠶⠄⣤⠤⠤⠤⠤⠂⡠⠀⡇⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠦⠤⣄⣀⣀⣀⣠⠔⠁      Hacked  👿 👿 👿 👿 👿 👿  👿BY https://t.me/Digital_killer1")
            time.sleep(0.01)

        sent_count += 1
        bot.send_message(
            message.chat.id,
            "كيف حالك اخوي انتضر شوي بس 😂 😂 😂 "
        )
        time.sleep(5)

        if sent_count == 10:
            break
        else:
            sent_count += 1

# Start the bot
bot.polling()