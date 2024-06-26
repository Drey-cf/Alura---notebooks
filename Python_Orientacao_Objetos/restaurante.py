from avaliacao import Avaliacao
from cardapio.item_cardapio import ItemCardapio

class Restaurante:
	restaurantes = []

	def __init__(self, _nome, categoria): # Constructor, a special method that creates and initializes the object when it is created. Python
		self._nome = _nome.title()     # is different, it has a constructor and an initializer. The initializer has a special name, __init__
		self._categoria = categoria.upper() #Esses são os atributos, e uma classe é a abstração de um objeto do mundo real em programação
		self._ativo = False  # colocando como protegido pra nao ser mechido
		self._avaliacao = []
		self._cardapio = []
		Restaurante.restaurantes.append(self)

	def __str__(self):   # sem essa função, ele mostra o lugar na memória
		return f'{self._nome} | {self.categoria}'

	@classmethod  #Para referenciar metodos da classe
	def listar_restaurantes(cls):
		print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'}")
		for restaurante in cls.restaurantes:
			print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

	@property# um decorator do python, modificado como que um atributo é lido. Por exemplo, False como inativo
	def ativo(self):
		return '☒' if self._ativo else '☐'

	def alternar_estado(self):  #Esse metodo é para os objetos, e n da classe
		self._ativo = not self._ativo

	def receber_avaliacao(self, cliente, nota):
		avaliacao = Avaliacao(cliente, nota)
		self._avaliacao.append(avaliacao)

	@property
	def media_avaliacao(self):
		if not self._avaliacao:
			return 'Sem avaliações'
		soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
		quantidade_de_notas = len(self._avaliacao)
		media = round(soma_das_notas/quantidade_de_notas, 1)
		return media

	def adicionar_no_cardapio(self, item):
		if isinstance(item, ItemCardapio):
			self._cardapio.append(item)

	@property
	def exibir_cardapio(self):
		print(f'Cardapio do restaurante {self._nome}\n')
		for i, item, in enumerate(self._cardapio, start = 1):  # começa no indice 1
			if hasattr(item, 'descricao'):
				mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descriçao: {item.descricao}'
				print(mensagem_prato)
			else:
				mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descriçao: {item.tamanho}'
				print(mensagem_bebida)

