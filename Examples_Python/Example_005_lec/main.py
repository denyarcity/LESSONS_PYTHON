# в терминале прописываем "python3 -m venv .folder" создается папка в которой будут храниться все библиотеки.
# устанавливаем библиотеку "pip install isOdd"

# from isOdd import isOdd

# print(isOdd(1)) #=> true
# print(isOdd(4)) #=> false


# Прогрессбар "pip install progCollecting progress"
# from progress.bar import Bar
# import time # импортируем системный таймер

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1) # Делаем секундную задержку для имитации процесса загрузки
#     bar.next()
# bar.finish()

# Смайлики (Первая попавшаяся библиотека со смайликами)

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# matplotlib - библиотека для визуализации

# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('_mpl-gallery')

# # make data:
# np.random.seed(3)
# x = 0.5 + np.arange(8)
# y = np.random.uniform(2, 7, len(x))

# # plot
# fig, ax = plt.subplots()

# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

# самостоятельный простейший пример

# list = [1, 2, 3, 2, 7, 2, 4, 4]
# plt.plot(list)
# plt.show()

# Telegram-bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5521002894:AAF_WYZLABePovHAPyg7XTtPmq_mYw9AYoo").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()
