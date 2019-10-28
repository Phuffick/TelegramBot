import telebot
from UsersHolder import DBGroupWorker
from ScheduleHolder import ScheduleHolder
from NamesHolder import NamesHolder

bot = telebot.TeleBot('915489580:AAGL6FuGgOs-7OIx3Itw_88KMye2tPnlU-g')


@bot.message_handler(commands=['set_group'])
def start_message(message):
    group = message.text.split(' ')[1]
    DBGroupWorker.set_user_group(message.chat.id, group)
    bot.send_message(message.chat.id, 'Так, ты добавлен в группу: ' + group)
    #bot.reply_to(message.chat.id, "Введите группу: /set_group номер_группы ")


@bot.message_handler(commands=['get_times'])
def start_message(message):
    bot.send_message(message.chat.id, "Время пар: " )
    times = ScheduleHolder.get_times()
    output = ''
    num = 1

    for number, time in times.items():
        output += str(num) + ")  " + time + "\n"
        num += 1
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Хммммм, ну чекай тогда: \n\n' +
                     '/help - помощь (если опять все забудешь)\n\n' +
                     '/set_group номер_группы - первое, что нужно сделать, то есть установить твою группу.'
                     'Можно ввести только 11, 12, 14, 15, 17, 18\n\n' +
                     '/get_schedule_today - расписание на сегодня\n\n' +
                     '/get_schedule_next - расписание на ближайший день\n\n' +
                     '/get_times - только если нужно время пар\n\n' +
                     '/get_all_schedule - все расписание выбранной группы\n\n' +
                     '/get_theorem - не попробуешь - не узнаешь\n\n' +
                     '/get_names - ну это конечно... Преподов знать нужно. Чтобы завтра знал!!!\n\n' +
                     'Ну пока все')


@bot.message_handler(commands=['get_schedule_today'])
def start_message(message):
    group = DBGroupWorker.get_user_group(message.chat.id)
    schedule = ScheduleHolder.get_schedule_today(group)
    time = ScheduleHolder.get_times()

    if schedule:
        output = ''
        for number, subject in schedule.items():
            output += str(time[number]) + '   ' + str(subject) + '\n'
        bot.send_message(message.chat.id, output)
    else:
        bot.send_message(message.chat.id, 'Елси чо, в этот день спать можешь спокойно.')


@bot.message_handler(commands=['get_schedule_next'])
def start_message(message):
    group = DBGroupWorker.get_user_group(message.chat.id)
    schedule = ScheduleHolder.get_schedule_next(group)
    time = ScheduleHolder.get_times()

    if schedule:
        output = ''
        for number, subject in schedule.items():
            output += str(time[number]) + '   ' + str(subject) + '\n'
        bot.send_message(message.chat.id, output)
    else:
        bot.send_message(message.chat.id, 'Если чо, в этот день можешь спать спокойно')


@bot.message_handler(commands=['get_all_schedule'])
def start_message(message):
    group = DBGroupWorker.get_user_group(message.chat.id)
    schedule = ScheduleHolder.get_all_schedule(group)
    time = 1

    if schedule:
        output = ''
        Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for n, schedules in schedule.items():
            output += str(Week[int(n)]) + '\n\n'
            for j, subj in schedules.items():
                output += str(time) + ')   ' + str(subj) + '\n'
                time += 1
            time = 1
            output += '\n'
        bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['get_names'])
def start_message(message):
    group = DBGroupWorker.get_user_group(message.chat.id)
    names = NamesHolder.get_names(group)
    output = ''

    for name, subj in names.items():
        output += str(name) + '  conducts  ' + str(subj) + '\n\n'
    bot.send_message(message.chat.id, output)



@bot.message_handler(commands=['get_theorem'])
def start_message(message):
    photo = open('Photo/theorem.png', 'rb')
    bot.send_photo(message.chat.id, photo)

bot.polling()