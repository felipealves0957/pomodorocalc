def minutes_to_hours(min):
    hours = trunc(min/60)
    minutes = min - hours*60
    return (trunc(hours), trunc(minutes))

def make_lines(nlines):
    print('-'*nlines)

def format_time(time):
    if time < 10:
        return str('0' + str(time))
    else:
        return time
    

from math import trunc
hour = 0
minutes = 0

start_time = str(input('Horário de início: '))
pomodoro_time = int(input('Duração de cada pomodoro (minutos): '))
total_minutes = int(input('Tempo total do pomodoro (minutos): '))
rest_time = int(input('Tempo de descanso (minutos): '))

hour = start_time[:2]
minutes = start_time[3:]

rest_total = ((total_minutes/pomodoro_time) - 1)*rest_time
total_time = rest_total+total_minutes+int(minutes)

make_lines(30)
print(f'Horário inicial: {hour}:{minutes}')
print(f'Horário final: {format_time(int(hour)+minutes_to_hours(total_time)[0])}:{format_time(minutes_to_hours(total_time)[1])}')
make_lines(30)
