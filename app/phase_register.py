"""Módulo responsável pelo registro das fases(andamentos)
dos processos."""


from app.controller import Controller

import pyautogui

from time import sleep

from datetime import date


class PhaseRegister:

	dia = date.today().day
	month = date.today()
	mes = month.strftime('%m')
	ano = date.today().year

	def __init__(self):
		self.objetos = Controller()

	def control_screen(self):
		"""Acessa as telas do sistema para efetuar o 
		registro das fases (andamentos)."""

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
		# Digita 8 no campo opção e pressiona enter
		control_andamento = pyautogui.typewrite('8');pyautogui.press('enter')
		# Aguarda 0.5 segundos
		sleep(0.25)

		# Tela 5
		# Digita 1 no campo opção e pressiona enter
		reg_andamento = pyautogui.typewrite('1');pyautogui.press('enter')
		# Aguarda 0.5 segundos
		sleep(0.25)
		return

	def register(self, cod):
		""" Insere os números dos processos, digita o código da fase/andamento
		e data atual."""

		processos = self.objetos.read_plan()

		for dado in processos:
			# digita o numero do processo no campo processo e pressiona enter e aguarda 0.25 segundos
			pyautogui.typewrite(str(dado));pyautogui.press('enter')
			sleep(0.25)
			# digita o código do andamento e pressiona enter e aguarda 0.25 segundos
			pyautogui.typewrite(cod);pyautogui.press('enter')
			sleep(0.25)
			# registrando a data
			pyautogui.typewrite(str(self.dia))
			sleep(0.25)
			pyautogui.typewrite(str(self.mes))
			sleep(0.25)
			pyautogui.typewrite(str(self.ano))
			sleep(0.25)

			pyautogui.press('enter')
			sleep(0.25)
			# salvando registro
			salvar = pyautogui.typewrite('S');pyautogui.press('enter')
			sleep(0.25)

			print(f'Processo {dado} - Código Andamento: {cod}')

		print('ANDAMENTOS REGISTRADOS!\n')
		# retorna para tela inicial
		pyautogui.press('f3')

		return

if __name__ == '__main__':

	cod = input('Informe o código do andamento: ')

	teste = PhaseRegister()

	print(teste.objetos.read_plan())

	teste.control_screen()

	teste.register(cod)