class ProblemaNavegacao:
    def __init__(self, estado_inicial, estados_objetivo):
        self.estado_inicial = estado_inicial
        self.estados_objetivo = estados_objetivo
        self.mapa = {
            "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
            "Zerind": {"Arad": 75, "Oradea": 71},
            "Oradea": {"Zerind": 71, "Sibiu": 151},
            "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
            "Timisoara": {"Arad": 118, "Lugoj": 111},
            "Lugoj": {"Timisoara": 111, "Mehadia": 70},
            "Mehadia": {"Lugoj": 70, "Drobeta": 75},
            "Drobeta": {"Mehadia": 75, "Craiova": 120},
            "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
            "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
            "Fagaras": {"Sibiu": 99, "Bucareste": 211},
            "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucareste": 101},
            "Bucareste": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
            "Giurgiu": {"Bucareste": 90},
            "Urziceni": {"Bucareste": 85, "Vaslui": 142, "Hirsova": 98},
            "Vaslui": {"Urziceni": 142, "Iasi": 92},
            "Iasi": {"Vaslui": 92, "Neamt": 87},
            "Neamt": {"Iasi": 87}
        }

    def eh_estado_objetivo(self, estado):
        return estado in self.estados_objetivo

    def acoes_possiveis(self, estado):
        if estado in self.mapa:
            return list(self.mapa[estado].keys())
        return []

    def custo(self, estado_atual, proximo_estado):
        return self.mapa[estado_atual][proximo_estado]

    def resultado(self, estado, acao):
        return acao
    
# Adicione uma propriedade 'custo_acumulado' ao nó para rastrear o custo acumulado
class Node:
    def __init__(self, state, parent=None, custo_acumulado:int=0)->None:
        self.state = state
        self.parent = parent
        self.custo_acumulado = custo_acumulado

def busca_em_arvore(problema):
    borda = [Node(problema.estado_inicial,0)]  # Inicializa a borda com o estado inicial
    while borda:
        no = borda.pop(0)  # Escolhe o primeiro nó da borda (FIFO)
        
        if problema.eh_estado_objetivo(no.state):
            return solucao(no)  # Se o estado for objetivo, retorna a solução
        
        # Expande o nó escolhido
        acoes_possiveis = problema.acoes_possiveis(no.state)
        for acao in acoes_possiveis:
            novo_estado = problema.resultado(no.state, acao)
            custo_acumulado = no.custo_acumulado + problema.custo(no.state, novo_estado)
            novo_no = Node(novo_estado, no, custo_acumulado)
            borda.append(novo_no)
    
    return "Falha"  # Se a borda estiver vazia e nenhum estado objetivo for alcançado, retorna falha



def solucao(no):
    caminho = []
    while no:
        caminho.append(no.state)
        no = no.parent
    return list(reversed(caminho))

# Exemplo de uso:
estado_inicial = "Arad"
estados_objetivo = ["Bucareste"]
problema = ProblemaNavegacao(estado_inicial, estados_objetivo)
solucao_encontrada = busca_em_arvore(problema)
print("Caminho da solução:", solucao_encontrada)
