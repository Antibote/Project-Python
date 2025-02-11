from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
import datetime
from database import db_fetchall
from telebot import types

scheduler = BackgroundScheduler()
scheduler.start()

def send_reminder(chat_id, task_id, bot):
    """Функция для отправки напоминания пользователю."""
    task = db_fetchall("SELECT Task FROM Adds WHERE Id = ?", (task_id,))
    if task:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("Удалить запись", callback_data=f'delete_task_{task_id}'),
            types.InlineKeyboardButton("Вернуться в главное меню", callback_data='main_menu')
        )
        bot.send_message(chat_id, f'⏰ Напоминание: {task[0][0]}!', reply_markup=markup)

def schedule_reminder(chat_id, task_id, reminder_time, bot):
    """Функция для добавления напоминания в планировщик."""
    try:
        job_id = f'reminder_{task_id}'
        scheduler.add_job(
            send_reminder,
            'date',
            run_date=reminder_time,
            args=[chat_id, task_id, bot],
            id=job_id
        )
    except JobLookupError as e:
        print(f"Ошибка при добавлении напоминания: {e}")
