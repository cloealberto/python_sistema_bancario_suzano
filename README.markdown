# 💰 Sistema Bancário - CLOE ALBERTO BANK

Este projeto foi desenvolvido como parte do **Bootcamp Python Developer - Suzano**, com o objetivo de praticar os fundamentos da linguagem Python através da simulação de um sistema bancário simples para pessoa física.

## 🚀 Funcionalidades

A aplicação permite que o usuário realize três operações principais:

- **[1] Depositar**: Aceita valores positivos e adiciona ao saldo da conta.
- **[2] Sacar**: Permite realizar até 3 saques por dia, com limite de R$ 500,00 por saque. Verifica saldo e validade do valor.
- **[3] Extrato**: Exibe todas as movimentações (depósitos e saques) e o saldo atual.
- **[0] Sair**: Encerra o sistema.

## 🧠 Regras de Negócio

- Não é permitido depositar valores negativos ou iguais a zero.
- O saque está limitado a:
  - **3 saques por dia**.
  - **R$ 500,00 por saque**.
  - Saldo disponível na conta.
- O extrato mostra todas as movimentações em ordem e o saldo final.
- Caso não haja movimentações, exibe a mensagem: `Nenhuma movimentação realizada.`

## 🛠️ Tecnologias Utilizadas

- Linguagem: **Python 3**
- IDE sugerida: **VS Code**
- Execução via terminal ou console do Python.

## 📂 Estrutura do Projeto

```bash
sistema_bancario/
├── banco.py       # Arquivo principal com o código-fonte do sistema
├── README.md      # Este arquivo de documentação
