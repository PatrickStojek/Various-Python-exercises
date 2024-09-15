time_in_sec = int(input('Podaj czas w sekundach: '))

hours = time_in_sec // 3600
minutes = (time_in_sec // 60) - (hours * 60)
seconds = time_in_sec - (hours * 3600) - (minutes * 60) 

print('timer wskazuje na: ' + str(hours) + ':' + str(minutes) + ':' + str(seconds))

