"""Módulo responsável por receber no sistema a
cada processo inscrito na planilha"""


from controller import Controller

import pyautogui

from time import sleep


class Retrieve:
	def __init__(self):
		self.objetos = Controller()

	def control_screen(self):
		"""Acessa as telas do sistema para emitir notificações"""

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
		# Digita 6 no campo opção e pressiona enter
		andamentos = pyautogui.typewrite('6');pyautogui.press('enter')
		# Aguarda 0.25 segundos
		sleep(0.25)

		# Tela 4
		# Digita 4 no campo opção e pressiona enter
		receber_inf_num = pyautogui.typewrite('4');pyautogui.press('enter')
		# Aguarda 0.25 segundos
		sleep(0.25)
		return

	def retrieve_doc(self):
		"""Acessa os campos do sistema para receber documentos"""
		
		processos = self.objetos.read_plan() 

		# Tela 5
		# Digita o número do documento/processo e tecla enter para recebê-lo
		for i, dado in enumerate(processos):
			# digita o numero do processo no campo processo e pressiona enter e aguarda 0.25 segundos
			pyautogui.typewrite(str(dado));pyautogui.press('enter')
			sleep(0.25)

			print(f'{i+1:2} - Processo: {dado} - Recebido')

		print('PROCESSOS RECEBIDOS COM SUCESSO!')
		# retorna para tela inicial
		pyautogui.press('f3')

		return		


if __name__ == '__main__':
	teste = Retrieve()
	print(teste.objetos.read_plan())
	teste.control_screen()
	teste.retrieve_doc()
