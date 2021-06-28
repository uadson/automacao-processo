"""Módulo em estado de construção:

Até o momento ele retorna os objetos com seus atributos e métodos"""

from app.notify import Notify


num = int(input('Informe o número da notificação: '))

app = Notify()
app.control_screen()
app.simple_notify(num)
