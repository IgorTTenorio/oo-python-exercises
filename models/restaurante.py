class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '🗹'
    
    def alternar_status(self):
        self._ativo = not self._ativo
    

restaurante_praca = Restaurante('Restaurante da Praça', 'Comida Caseira')
restaurante_praca.alternar_status()
restaurante_pizza = Restaurante('Pizzaria do Zé', 'Pizza')

Restaurante.listar_restaurantes()