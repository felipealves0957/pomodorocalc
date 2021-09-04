def minutes_to_hours(min):
    hours = trunc(min/60)
    minutes = min - hours*60
    return (trunc(hours), trunc(minutes))

def make_lines(nlines, mold):
    print(f'{mold}'*nlines)

def format_time(time, ishour = False):
    day = 0
    if ishour and time > 24:
        t = time
        time = t - trunc(t/24)*24
        day = trunc(t/24)

    if time < 10:
        return (str('0' + str(time)), day)

    else:
        return (time, day)

from math import trunc
from time import sleep
hour = 0
minutes = 0
line_mold = '/'
nlines = 60

make_lines(nlines, line_mold)
print('Olá...'.center(nlines))
sleep(1.5)
print('Seja bem-vindo(a) ao PomodoroPlanner'.center(nlines))
make_lines(nlines, line_mold)

start_time = str(input('Horário de início (hh:mm): '))
pomodoro_time = int(input('Duração de cada pomodoro (minutos): '))
total_minutes = int(input('Tempo total do pomodoro (minutos): '))
rest_time = int(input('Tempo de descanso (minutos): '))

hour = start_time[:2]
minutes = start_time[3:]

rest_total = ((total_minutes/pomodoro_time) - 1)*rest_time
total_time = rest_total+total_minutes+int(minutes)

final_hour = int(hour)+minutes_to_hours(total_time)[0]
final_minutes = minutes_to_hours(total_time)[1]

make_lines(nlines, line_mold)
print(f'Horário inicial: {hour}:{minutes}'.center(nlines))
print(f'Horário final: {format_time(final_hour, True)[0]}:{format_time(final_minutes)[0]}'.center(nlines))

if format_time(final_hour, True)[1] > 0:
    print(f'{format_time(final_hour, True)[1]} dia(s) depois da data inicial.'.center(nlines))

make_lines(nlines, line_mold)