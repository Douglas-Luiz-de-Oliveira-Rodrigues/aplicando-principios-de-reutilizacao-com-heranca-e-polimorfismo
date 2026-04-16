class Robo:
    """Classe base que representa um robô genérico"""
    
    def __init__(self, nome: str, tarefa: str):
        """
        Inicializa um robô com nome e tarefa
        
        Args:
            nome: Nome do robô
            tarefa: Tarefa que o robô executa
        """
        self.nome = nome
        self.tarefa = tarefa
    
    def descricao(self) -> str:
        """
        Retorna uma descrição formatada do robô
        
        Returns:
            String formatada: "Robo [nome] executa [tarefa]"
        """
        return f"Robo {self.nome} executa {self.tarefa}"
    
    def __str__(self) -> str:
        """Permite usar print() diretamente no objeto"""
        return self.descricao()


class RoboInteligente(Robo):
    """Robô com inteligência artificial - exemplo de herança"""
    
    def __init__(self, nome: str, tarefa: str, nivel_ia: int):
        """
        Inicializa um robô inteligente
        
        Args:
            nome: Nome do robô
            tarefa: Tarefa que o robô executa
            nivel_ia: Nível de inteligência artificial (1-10)
        """
        super().__init__(nome, tarefa)
        self.nivel_ia = nivel_ia
    
    def descricao(self) -> str:
        """Sobrescreve o método descricao com polimorfismo"""
        return f"Robo {self.nome} executa {self.tarefa} (IA: {self.nivel_ia})"


def main():
    """Função principal que lê entrada e cria um robô"""
    entrada = input().strip()
    partes = entrada.split(maxsplit=1)
    
    if len(partes) != 2:
        print("Entrada inválida")
        return
    
    nome, tarefa = partes
    robo = Robo(nome, tarefa)
    print(robo.descricao())


if __name__ == "__main__":
    main()