"""Módulo em estado de construção:

Até o momento ele retorna os objetos com seus atributos e métodos"""

from app.notify import Notify

app = Notify()
app.control_screen()
num = int(input('Informe o número da notificação: '))
app.simple_notify(num)
