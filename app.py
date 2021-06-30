"""1ª Fase do Programa:

a - realiza a leitura dos números do processos descritos na planilha;
b - coleta os dados: código do andamento, tipo de documento e número de notificação;
c - recebe, registra o andamento, emite documento e atualiza o histórico."""


from app.retrieve import Retrieve
from app.phase_register import PhaseRegister
from app.notify import Notify
from app.update_history import Update

from datetime import date

from time import sleep


data = date.today()
data_atual = data.strftime('%d/%m/%Y')


cod = input('Informe o código do andamento: ')


tipos = [
	'NOTIFICACAO'
]


for num, tipo in enumerate(tipos):
	print(num, tipo)


opcao = input('Informe o tipo de documento: ')


if opcao == '0':
	historico = f'* OBS: EXPEDIDA NOTIFICACAO EM {data_atual} AGUARDANDO RETORNO DE AR.&&'


num = int(input('Informe o número da notificação: '))

# receber
app = Retrieve()
app.control_screen()
app.retrieve_doc()
sleep(0.25)

# registrar fase
app = PhaseRegister()
app.control_screen()
app.register(cod)
sleep(0.25)

# notificar
app = Notify()
app.control_screen()
app.simple_notify(num)
sleep(0.25)

# atualizar histórico
app = Update()
app.control_screen()
app.update(historico)
sleep(0.25)