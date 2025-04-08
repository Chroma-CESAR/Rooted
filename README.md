# Indoor Plants Analysis

Este projeto tem como objetivo analisar e classificar plantas de interior com base em diferentes características, como origem, clima, frequência de rega, toxicidade e adequação para apartamentos. A análise foi realizada utilizando um conjunto de dados de plantas, com etapas de tratamento, visualização e classificação.

---

## Estrutura do Projeto

- **Tratamento de Dados**: Limpeza e preparação dos dados para análise.
- **Análises Realizadas**: Visualizações e insights sobre as características das plantas.
- **Classificações**: Categorizações específicas, como tamanho, toxicidade e adequação para apartamentos.

---

## Tratamento de Dados

1. **Leitura dos Dados**:
   - Os dados foram carregados a partir do arquivo `plants.csv`.
   - Colunas desnecessárias foram removidas, como `Unnamed: 0`.

2. **Limpeza**:
   - Remoção de espaços em branco nas colunas `family`, `categories`, `origin`, `climate` e `img_url`.
   - Exclusão de valores duplicados na coluna `common_name`.
   - Preenchimento de valores ausentes:
     - `common_name`: Removidos.
     - `origin`: Preenchidos com "Unknown".

3. **Transformações**:
   - Extração do primeiro nome da coluna `common_name` para criar a coluna `name`.
   - Criação de categorias de rega (`water_category`) com base no clima e na categoria da planta.

---

## Análises Realizadas

1. **Distribuições**:
   - Visualizações das distribuições de famílias, categorias, climas e origens das plantas.

2. **Plantas Populares**:
   - Seleção de plantas originárias de países populares, como Brasil, México, Venezuela, entre outros.

3. **Imagens**:
   - Exibição de imagens das plantas populares utilizando URLs fornecidas no dataset.

4. **Frequência de Rega**:
   - Classificação das plantas em categorias de rega:
     - `weekly`: Plantas tropicais e tropicais úmidas.
     - `7-10 days`: Outros climas.
     - `2-4 weeks`: Cactos e suculentas.

5. **Plantas Venenosas**:
   - Identificação de plantas tóxicas para pets com base nas famílias conhecidas por toxicidade:
     - `Araceae`, `Euphorbiaceae`, `Liliaceae`, `Amaryllidaceae`, `Apocynaceae`.

---

## Classificações

1. **Tamanho das Plantas**:
   - Classificação das plantas em:
     - `small`, `medium`, `big`, `very big`.
   - Baseada em pesquisas e listas pré-definidas.

2. **Adequação para Apartamentos**:
   - Plantas pequenas e médias foram classificadas como adequadas (`ind_apartment = 1`).

3. **Codificação de Categorias**:
   - Codificação das categorias `water_category` e `size` para facilitar análises e uso em Machine Learning.

---

## Resultados

- **Distribuições**:
  - Gráficos de distribuição para categorias como frequência de rega, tamanhos, toxicidade e adequação para apartamentos.

- **Exportação**:
  - Os dados tratados e classificados foram exportados para o arquivo `plants_cleaned.csv`.

---

## Referências

- [Kaggle - Plant Dataset](https://www.kaggle.com/datasets/iottech/plant/data)
- [ASPCA - Toxic and Non-Toxic Plants](https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants)
- [Pet Poison Helpline](https://www.petpoisonhelpline.com/poisons/)
- [NCBI - Toxicity of Plants Containing Calcium Oxalate Crystals](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10220692/)
- [RHS - Potentially Harmful Garden Plants](https://www.rhs.org.uk/advice/profile?pid=524)

---

## Como Executar

1. Certifique-se de ter o Python instalado.
    - Recomenda-se o uso do ambiente virtual (venv).
    ```bash
   py -m venv .venv
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt