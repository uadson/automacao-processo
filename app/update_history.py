"""Módulo responsável pelo atualização das informações no histórico
do processo."""


from app.controller import Controller

import pyautogui

from time import sleep

from datetime import date


class Update:
	def __init__(self):
		self.objetos = Controller()

	def control_screen(self):
		"""Acessa as telas do sistema e insere informações no
		histórico do processo"""

		# Tela 1
		# Clica no campo opção, digita 4 e pressiona enter
		sist_eletronico_proc = pyautogui.click(368, 244);pyautogui.typewrite('4');pyautogui.press('enter')
		# Aguarda 0.25 segundos
		sleep(0.25)

		# Tela 2
		# Digita 1 no campo opção e pressiona enter
		processos = pyautogui.typewrite('1');pyautogui.press('enter')
		# Aguarda 0.25 segundos
		sleep(0.25)

		# Tela 3
		# Digita 5 no campo opção e pressiona enter
		atualiza_historico = pyautogui.typewrite('5');pyautogui.press('enter')
		# Aguarda 0.25 segundos
		sleep(0.25)

		return

	def update(self, historico):
		"""Atualiza o histórico do processo"""

		processos = self.objetos.read_plan()

		for dado in processos:
			# digita o numero do processo no campo processo e pressiona enter 2x e aguarda 0.25 segundos
			pyautogui.typewrite(str(dado));pyautogui.press('enter');pyautogui.press('enter')
			sleep(0.25)
			# digita as informações no histórico
			pyautogui.typewrite(historico)
			sleep(0.25)
			
			print(f'Processo {dado} - Atualizado')

			# atualiza os dados
			pyautogui.press('f5')

		print('PROCESSOS ATUALIZADOS!\n')

		# retorna para tela inicial
		pyautogui.press('f3')

		return

if __name__ == '__main__':

	data = date.today()
	data_atual = data.strftime('%d/%m/%Y')

	tipos = [
		'NOTIFICACAO'
	]
	
	for num, tipo in enumerate(tipos):
		print(num, tipo)
	
	opcao = input('Informe o tipo de documento: ')
	
	if opcao == '0':
		historico = f'* OBS: EXPEDIDA NOTIFICACAO EM {data_atual} AGUARDANDO RETORNO DE AR.&&'
	
	print(historico)

	teste = Update()

	print(teste.objetos.read_plan())

	teste.control_screen()

	teste.update(historico)