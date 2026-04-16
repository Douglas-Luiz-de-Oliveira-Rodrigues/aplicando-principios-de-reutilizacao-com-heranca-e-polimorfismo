# Aplicando Princípios de Reutilização com Herança e Polimorfismo

# Desafio de Código

## Modelagem de Cliente VIP em Python: Classes e Objetos para Iniciantes

Você foi contratado por uma consultoria de TI para ajudar a modelar o sistema de cadastro de clientes da empresa fictícia **TechBiz**.  
O objetivo é criar uma estrutura que represente clientes utilizando **classes e objetos**, facilitando a manipulação das informações e permitindo identificar clientes VIPs.

### Regras de Negócio
- Implementar a classe **Cliente** com os atributos:
  - `nome`
  - `email`
  - `saldo`
- Criar um objeto da classe com os dados fornecidos.
- Verificar se o saldo é **≥ 1000**:
  - Se sim → imprimir **"VIP"**
  - Caso contrário → imprimir **"REGULAR"**

### Entrada
Três linhas:
1. Nome do cliente (string)  
2. Email do cliente (string)  
3. Saldo do cliente (inteiro não negativo)

### Saída
Uma única linha:
- **"VIP"** se o saldo for igual ou superior a 1000  
- **"REGULAR"** caso contrário  

### Exemplos
| Entrada                                     | Saída    |
|---------------------------------------------|----------|
| Lucas Silva<br>lucas@techbiz.com<br>1500    | VIP      |
| Ana Costa<br>ana@techbiz.com<br>999         | REGULAR  |
| Joao Pedro<br>joao@techbiz.com<br>1000      | VIP      |
| Maria Lima<br>maria@techbiz.com<br>0        | REGULAR  |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica
- **Programação Orientada a Objetos (POO)**: criação de classes e objetos
- **Encapsulamento de dados**: atributos organizados dentro da classe
- **Estruturas condicionais**: para verificar se o cliente é VIP ou REGULAR

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio]()

---

## Cadastro Orientado a Objetos de Robôs Automatizados

Você foi contratado por uma startup de tecnologia que está desenvolvendo um sistema de cadastro de robôs para automatizar tarefas do dia a dia.  
O objetivo é criar um código organizado e escalável, aplicando os pilares da **Programação Orientada a Objetos (POO)**: encapsulamento, herança e polimorfismo.  
Sua missão é criar uma solução reutilizável e clara, que permita cadastrar diferentes tipos de robôs e exibir suas informações de forma padronizada.

### Regras de Negócio
- Implementar uma classe base chamada **Robo** com os atributos:
  - `nome`
  - `tarefa`
- Criar uma função que receba como entrada o nome e a tarefa de um robô.
- Instanciar um objeto da classe **Robo**.
- Retornar uma string formatada no padrão:  
  **"Robo [nome] executa [tarefa]"**
- Estrutura deve permitir fácil extensão para novos tipos de robôs no futuro.

### Entrada
Duas strings separadas por espaço, representando respectivamente:
1. Nome do robô  
2. Tarefa que ele executa  

### Saída
Uma string formatada no padrão:  
**"Robo [nome] executa [tarefa]"**

### Exemplos
| Entrada          | Saída                        |
|------------------|------------------------------|
| Atlas limpeza    | Robo Atlas executa limpeza   |
| Eva jardinagem   | Robo Eva executa jardinagem  |
| WallE reciclagem | Robo WallE executa reciclagem|
| R2D2 vigilancia  | Robo R2D2 executa vigilancia |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica
- **POO (Programação Orientada a Objetos)**: criação de classes e objetos
- **Encapsulamento**: atributos organizados dentro da classe
- **Herança e Polimorfismo**: estrutura preparada para expansão futura

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio]()

---

## Abstração e Interfaces: Padronizando Colaboradores em Python

Você trabalha em uma consultoria de TI que está desenvolvendo um sistema para padronizar o cadastro de diferentes tipos de colaboradores.  
O objetivo é aplicar **abstração e interfaces** para garantir que todos os tipos de colaboradores sigam um mesmo padrão de comportamento, facilitando futuras expansões do sistema.

### Regras de Negócio
- Criar uma classe abstrata chamada **Colaborador** com um método abstrato `exibir_info()`.
- Criar uma classe **Analista** que herda de **Colaborador** e implementa o método `exibir_info()`.
- O método deve retornar a string:  
  **"Analista: [nome]"**
- O programa deve ler o nome do Analista e exibir a saída conforme o padrão.

### Entrada
Uma única linha contendo o nome do Analista (string, pode conter letras e espaços).

### Saída
Uma única linha com a string:  
**"Analista: [nome]"**

### Exemplos
| Entrada      | Saída                 |
|--------------|-----------------------|
| Lucas        | Analista: Lucas       |
| Maria Silva  | Analista: Maria Silva |
| Joao         | Analista: Joao        |
| Ana Paula    | Analista: Ana Paula   |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica
- **Classes Abstratas**: definição de métodos obrigatórios
- **Herança**: classe concreta derivada da abstrata
- **Interfaces e POO**: padronização de comportamento entre colaboradores

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio]()
