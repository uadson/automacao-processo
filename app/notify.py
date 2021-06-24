"""Módulo responsável por emitir notificações relacionadas a
cada processo inscrito na planilha"""


from .controller import Controller

import pyautogui

from time import sleep


class Notify:
	def __init__(self):
		self.objetos = Controller()

	def control_screen(self):
		"""Acessa as telas do sistema para emitir notificações"""

		# Tela 1
		# Clica no campo opção, digita 2 e pressiona enter
		proj_sociais = pyautogui.click(368, 244);pyautogui.typewrite('2');pyautogui.press('enter')
		# Aguarda 0.25 segundos
		sleep(0.25)

		# Tela 2
		# Digita 2 no campo opção e pressiona enter
		fiscalizacao = pyautogui.typewrite('2');pyautogui.press('enter')
		# Aguarda 0.5 segundos
		sleep(0.25)

		# Tela 3
		# Digita 5 no campo opção e pressiona enter
		auto_de_infracao = pyautogui.typewrite('5');pyautogui.press('enter')
		# Aguarda 0.5 segundos
		sleep(0.25)

		# Tela 4
		# Digita 5 no campo opção e pressiona enter
		formularios = pyautogui.typewrite('5');pyautogui.press('enter')
		# Aguarda 0.5 segundos
		sleep(0.25)
		return

	def simple_notify(self, num):
		"""Acessa os campos do sistema de notificação simples
		e realiza as emissões dos documentos"""
		
		processos = self.objetos.read_plan()
		num_not = num
		doc_print = 'pdf' 

		# Tela 5
		# Clica no campo opção, digita 1 e pressiona enter e aguarda 0.25 segundos
		notificacao = pyautogui.click(368, 244);pyautogui.typewrite('1');pyautogui.press('enter')
		sleep(0.25)

		for dado in processos:
			# digita o numero do processo no campo processo e pressiona enter e aguarda 0.25 segundos
			pyautogui.typewrite(str(dado));pyautogui.press('enter')
			sleep(0.25)
			# digita o numero da notificacao e pressiona enter e aguarda 0.25 segundos
			pyautogui.typewrite(str(num_not));pyautogui.press('enter')
			sleep(0.25)
			# digita o numero da impressora e pressiona enter e aguarda 0.25 segundos
			pyautogui.typewrite(str(doc_print));pyautogui.press('enter')
			sleep(0.25)
			num_not += 1

			print(f'Processo {dado} - Notificação {num_not}')

		# retorna para tela inicial
		pyautogui.press('f3')

		return

if __name__ == '__main__':
	teste = Notify()
	print(teste.objetos.read_plan())

	teste.control_screen()
	teste.simple_notify()