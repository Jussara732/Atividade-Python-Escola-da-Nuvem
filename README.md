# Atividade Python - Escola da Nuvem

Repositório dedicado aos exercícios de lógica de programação em Python realizados durante o curso da Escola da Nuvem.

## 📂 Estrutura do Projeto

### 🔵 Atividade Prática 1
Exercícios básicos para iniciantes:
* **Questão 1**: Operações matemáticas simples.
* **Questão 2**: Manipulação de textos e variáveis.

### 🔵 Atividade Prática 2
Foco em cálculos e lógica inicial:
* **Questão 1**: Conversor de Moedas (Real para Dólar/Euro).
* **Questão 2**: Calculadora de Desconto de Produtos.
* **Questão 3**: Média Escolar de Notas.
* **Questão 4**: Consumo de Combustível por KM.

### 🔵 Atividade Prática 3
Lógica de decisão e condicionais:
* **01_questao**: Classificador de faixas etárias.
* **02_questao**: Calculadora de IMC com classificações.
* **03_questao**: Conversor de Temperatura (C, F e K).
* **04_questao**: Verificador de Anos Bissextos.
## 🚀 Atividade Prática 04 - Estruturas de Repetição e Tratamento de Erros

Nesta etapa do curso, desenvolvi algoritmos em Python focados em laços de repetição (`for`), lógica condicional avançada e tratamento de exceções com `try/except/finally`.

### 📋 Exercícios Desenvolvidos:

1.  **Calculadora de Soma Acumulada**: Um programa que solicita números ao usuário e realiza a soma total, demonstrando o uso de acumuladores.
2.  **Média de Notas da Turma**: Algoritmo que lê múltiplas notas, calcula a média aritmética e exibe o desempenho geral.
3.  **Verificador de Senha Segura**: Sistema que valida se uma senha possui o comprimento mínimo de 8 caracteres e se contém ao menos um número, utilizando `isdigit()`.
4.  **Analisador de Números Pares e Ímpares**: Código que classifica números inteiros e contabiliza a quantidade de cada tipo. Este exercício inclui tratamento de erro para entradas inválidas e o bloco `finally` para encerramento do processo.

### 🛠️ Tecnologias Utilizadas:
* **Linguagem**: Python 3
* **Ferramentas**: Visual Studio Code, Git e GitHub
* **Conceitos**: Laços `for`, operadores matemáticos (`%`), métodos de string e blocos `try/finally
## 🚀 Atividade Prática 05 - Funções e Bibliotecas em Python

Repositório criado para os exercícios de lógica de programação em Python.

## Questões:
1. **Cálculo de Gorjeta:** Função que calcula porcentagem sobre o valor da conta.
2. **Verificador de Palíndromo:** Uso de `isalnum()` e `slicing [::-1]` para checar frases.
3. **Preço com Desconto:** Cálculo algébrico com formatação de centavos (`:.2f`).
4. **Dias de Vida:** Uso da biblioteca `datetime` para calcular diferença entre datas.

## 🛠️ Tecnologias Utilizadas
* Python 3
* VS Code
* Git & GitHub
# 🚀 **Projeto de Estudos Python - Atividade Prática 6**

Este repositório contém os exercícios desenvolvidos durante o módulo de **Módulos e APIs em Python**. O foco principal foi aprender a consumir dados externos e organizar o código de forma modular.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.13
* **Ambiente:** Visual Studio Code (Windows)
* **Biblioteca Externa:** `requests` (para integração com APIs)

## 📂 Descrição dos Scripts

### 1. Gerador de Senhas Seguras (`01 Senha aleatorias.py`)
Um programa que gera senhas aleatórias utilizando os módulos nativos `random` e `string`.
* **Funcionalidade:** O usuário escolhe o tamanho da senha, e o sistema combina letras, números e símbolos.

### 2. Busca de Usuário Aleatório (`02_buscar_usuario.py`)
Integração com a API **Random User Generator**.
* **Funcionalidade:** Recupera nome, e-mail e país de um perfil fictício para testes de sistemas.

### 3. Consulta de Endereço (`03_consulta_cep.py`)
Consumo da API **ViaCEP**.
* **Funcionalidade:** Ao digitar um CEP, o programa retorna o logradouro, bairro, cidade e estado. Inclui tratamento para CEPs não encontrados.

### 4. Cotação de Moedas em Tempo Real (`04_cotacao_moedas.py`)
Consumo da **AwesomeAPI** de economia.
* **Funcionalidade:** Exibe o valor atual, máxima e mínima de moedas (USD, EUR, BTC, JPY, ARS) em relação ao Real (BRL).
* **Destaque:** Implementação de lógica inteligente para exibir 4 casas decimais em moedas de baixo valor nominal (como o Peso Argentino).

---
## 🚀 Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca necessária:
   ```bash
   pip install requests
---
*Desenvolvido por Jussara Araujo de Souza*