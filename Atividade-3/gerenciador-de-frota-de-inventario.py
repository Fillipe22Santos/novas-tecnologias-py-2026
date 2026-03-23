wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwclass Equipamento:
    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"
    
    def alugar(self):
        if self.status == "Disponível":
            self.status = "Alugado"
        else:
            print(f"{self.nome} já está alugado.")
    
    def devolver(self):
        self.status = "Disponível"

class Locadora:
    def __init__(self):
        self.inventario = []
        self.faturamento_por_cliente = {}
    
    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)
    
    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for equipamento in self.inventario:
            if equipamento.id_equipamento == id_equipamento:
                if equipamento.status == "Disponível":
                    equipamento.alugar()
                    
                    custo = equipamento.preco_diaria * dias
                    
                    if nome_cliente in self.faturamento_por_cliente:
                        self.faturamento_por_cliente[nome_cliente] += custo
                    else:
                        self.faturamento_por_cliente[nome_cliente] = custo
                    
                    print(f"{equipamento.nome} alugado por {nome_cliente} por {dias} dias. Total: R${custo}")
                    return
                else:
                    print("Equipamento já está alugado.")
                    return
        
        print("Equipamento não encontrado.")
    
    def equipamentos_disponiveis(self):
        disponiveis = []
        for equipamento in self.inventario:
            if equipamento.status == "Disponível":
                disponiveis.append(equipamento.nome)
        return disponiveis

eq1 = Equipamento(1, "Furadeira", 50.0)
eq2 = Equipamento(2, "Serra Elétrica", 80.0)
eq3 = Equipamento(3, "Betoneira", 120.0)

locadora = Locadora()

locadora.cadastrar_equipamento(eq1)
locadora.cadastrar_equipamento(eq2)
locadora.cadastrar_equipamento(eq3)

print("Disponíveis:", locadora.equipamentos_disponiveis())

locadora.realizar_locacao("Felipe", 1, 3)
locadora.realizar_locacao("Maria", 2, 2)

print("Disponíveis:", locadora.equipamentos_disponiveis())
print("Faturamento:", locadora.faturamento_por_cliente)