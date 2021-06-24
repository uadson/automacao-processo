"""Módulo responsável pela coleta dos dados inseridos na planilha"""


from openpyxl import load_workbook

from . settings.base import DATABASE


class Controller:
	def __init__(self):
		self.objetos = list()

	def read_plan(self):
		self.objetos.clear()
		work_book = load_workbook(DATABASE)
		plan = work_book['obj']
		self.objetos = [cell.value if not cell.value else cell.value for cell in plan['A']]
		#for cell in plan['A']:
		#	if not cell.value == None:
		#		self.objetos.append(cell.value)
		return self.objetos


if __name__ == '__main__':
	teste = Controller()

	print(teste.read_plan())