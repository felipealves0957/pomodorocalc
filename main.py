def minutes_to_hours(min):
    hours = trunc(min/60)
    minutes = min - hours*60
    return (trunc(hours), trunc(minutes))

def makelines(nlines):
    print('-'*nlines)

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

makelines(30)
print(f'Horário inicial: {hour}:{minutes}')
print(f'Horário final: {int(hour)+minutes_to_hours(total_time)[0]}:{minutes_to_hours(total_time)[1]}')
makelines(30)
