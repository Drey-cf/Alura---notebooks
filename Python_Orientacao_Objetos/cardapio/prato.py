from cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):  # Estou dizendo que o Prato é um filho da classe ItemCardapio
	def __init__(self, nome, preco, descricao):
		super().__init__(nome, preco)  #super permite que acessemos itens de outra classe
		self.descricao = descricao

	def __str__(self):
		return self._nome

	def aplicar_desconto(self):
		self._preco -= self._preco*.05  # Aqui usamos o conceito de polimorfism, ou seja, um método que se adapta a diferentes classes
		

	