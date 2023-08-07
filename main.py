import time

t = input("Digite o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada Inválida!")
    quit()

while t:
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(f'\r{timer}', end='')
    time.sleep(1)
    t = t - 1


print("\n""O Tempo Acabou!!!")
