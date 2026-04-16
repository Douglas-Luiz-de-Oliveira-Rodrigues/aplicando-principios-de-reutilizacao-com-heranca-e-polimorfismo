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
