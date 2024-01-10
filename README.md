<h3 align="center"> 
	🚧  Projeto em construção... 🚀 🚧
</h3><br>

<p align="center">
 <a href="#introdução">Introdução</a> •
  <a href="#dados">Dados</a> • 
 <a href="#objetivo">Objetivo</a> • 
 <a href="#autor">Autor</a>
</p>

<h1 align="center">Modelo de Classificação de risco de crédito</h1>

## Introdução

Atualmente, as instituições financeiras disponibilizam recursos de crédito para pessoas físicas ou empresas. Esses recursos podem ser, por exemplo, na forma de empréstimo ou financiamento.

No caso do empréstimo, o cliente pode usar o dinheiro como quiser, no caso do financiamento, o dinheiro é para a compra de um bem especificado em contrato. Além das diferenças de prazos, taxas, entre outros.

No Brasil, de acordo com o [relatório de Economia Bancária de 2022](https://www.bcb.gov.br/content/publicacoes/relatorioeconomiabancaria/reb2022p.pdf) publicado pelo Banco central do Brasil, o ano de 2022 encerrou, pelo terceiro ano consecutivo, com forte crescimento da carteira de crédito do sistema financeiro nacional.

Para essa liberação de crédito, é feita uma análise de crédito, onde é avaliado a capacidade de pagamento da pessoa física ou jurídica que deseja os recursos.

Cada vez mais instituições financeiras têm utilizado técnicas de análise de dados e aprendizado de máquina em suas operações, ajudando na determinação do risco de crédito do cliente.

## Dados

Os dados utilizados nesse projeto foram coletados na plataforma [Kaggle](https://www.kaggle.com/datasets/uciml/german-credit/data), popular por suas competições de Machine Learning. 

O dataset possui informações a respeito de pessoas que pediram crédito bancário, tendo o risco classificados em 'good' ou 'bad' de acordo com as features.

O dataset original possui 1000 linhas e 20 colunas, no entanto o autor no Kaggle diz ser impossível de entender o dataset original devido ao complicado sistema de categorias e símbolos. Dessa maneira, ele coletou apenas as features as quais achava importantes, ou que a descrição não era obscura, e disponibilizou 10 features em um arquivo CSV.

- Age (idade)
- Sex (sexo)
    - male (masculino)
    - female (feminino)
- Job (emprego)
    - 0: unskilled and non-resident (não qualificado e não residente)
    - 1: unskilled and resident (não qualificado e residente)
    - 2: skilled (qualificado)
    - 3: highly skilled (altamente qualificado)
- Housing (casa)
    - own (própria)
    - rent (aluguel)
    - free (de favor)
- Saving accounts (conta poupança)
    - little (pouco)
    - moderate (moderado)
    - rich (rico)
    - quite rich (muito rico)
- Checking accounts (conta-corrente)
    - little (pouco)
    - moderate (moderado)
    - rich (rico)
- Credit amount (valor do limite de crédito liberado)
- Duration (tempo do contrato de crédito em meses)
- Purpose (propósito do crédito)

## Objetivo

Neste projeto, a meta é entender as relações existente entre as features disponibilizadas no dataset, como por exemplo se o valor de crédito liberado tem relação com idade ou sexo, entre outras hipóteses que serão levantadas durante o projeto, com o objetivo de entender como essas features influenciam na categorização do risco de crédito do cliente.

Além disso, após a análise exploratória dos dados, o objetivo é criar um modelo de classificação, que consiga definir em bom ou ruim o risco de crédito de novos clientes.

## Autor

Feito por Dafne Piovesan.

[![Linkedin Badge](https://img.shields.io/badge/-Dafne-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/dafnefp/)](https://www.linkedin.com/in/dafnefp/) 
[![Email Badge](https://img.shields.io/badge/-dafnefp@uol.com.br-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:dafnefp@uol.com.br)](mailto:dafnefp@uol.com.br)
