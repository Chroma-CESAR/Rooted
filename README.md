# Indoor Plants Analysis

Este projeto tem como objetivo analisar e classificar plantas de interior com base em diferentes características, como origem, clima, frequência de rega, toxicidade e adequação para apartamentos. A análise foi realizada utilizando um conjunto de dados de plantas, com etapas de tratamento, visualização e classificação.

---

## Estrutura do Projeto

- **Tratamento de Dados**: Limpeza e preparação dos dados para análise.
- **Análises Realizadas**: Visualizações e insights sobre as características das plantas.
- **Classificações**: Categorizações específicas, como tamanho, toxicidade e adequação para apartamentos.
- **Notebooks**:
  - `base.ipynb`: Realiza o pré-processamento e a análise exploratória dos dados.
  - `model.ipynb`: Complementa o `base.ipynb`, aplicando técnicas de machine learning para agrupar e classificar as plantas.

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
   - Seleção de plantas originárias de países populares, como Brasil, México, Venezuela, entre outros, com base em referências confiáveis.

3. **Classificações**:
   - **Solo**: Classificação em `Loamy soils`, `Peat soils`, `Sandy soils`, e `Silty and clay soils`.
   - **Luz Solar**: Classificação em `Full sun`, `Partial shade`, e `Full sun or partial shade`.
   - **Frequência de Rega**: Classificação em `weekly`, `7-10 days`, e `2-4 weeks`.

4. **Níveis de Experiência e Disponibilidade**:
   - Determinação do nível de experiência necessário para cuidar de cada planta.
   - Classificação da disponibilidade com base nas necessidades de rega e luz solar.

---

## Resultados

- **Distribuições**:
  - Gráficos de distribuição para categorias como frequência de rega, tamanhos, toxicidade, adequação para apartamentos, solo ideal, e luz solar necessária.

- **Exportação**:
  - Os dados tratados e classificados foram exportados para o arquivo `plants_cleaned.csv`.

---

## Notebooks

### `base.ipynb`

Este notebook realiza o pré-processamento e a análise exploratória dos dados. Ele é responsável por:

- Carregar os dados brutos do arquivo `plants.csv`.
- Realizar a limpeza e transformação dos dados.
- Gerar visualizações iniciais para entender as distribuições e padrões nos dados.

### `model.ipynb`

Este notebook complementa o `base.ipynb` ao aplicar técnicas de machine learning para agrupar e classificar as plantas. Ele inclui:

- Mapeamento de dificuldades de solo, luz solar e rega.
- Criação de variáveis categóricas para níveis de experiência e disponibilidade.
- Normalização dos dados para uso em algoritmos de clustering.
- Aplicação do método K-Means para agrupar as plantas em clusters.
- Visualização dos clusters utilizando PCA.
- Cálculo do Silhouette Score para avaliar a qualidade dos clusters.

---

## Codificações Importantes

| Coluna                     | Valores Possíveis       | Descrição                              |
|----------------------------|-------------------------|----------------------------------------|
| `ind_apartment`            | 0 ou 1                 | Indica se a planta é adequada para apartamentos (0 = Não, 1 = Sim). |
| `ind_pet`                  | 0 ou 1                 | Indica se a planta é segura para pets (0 = Não, 1 = Sim).           |
| `size_code`                | 0, 1, 2, 3             | Tamanho da planta (0 = Small, 1 = Medium, 2 = Big, 3 = Very Big).   |
| `experience_level_code`    | 0, 1, 2                | Nível de experiência necessário (0 = Beginner, 1 = Amateur, 2 = Experienced). |
| `disponibility_level_code` | 0, 1, 2                | Nível de disponibilidade necessário (0 = Low, 1 = Medium, 2 = High). |




## Como Executar

1. Certifique-se de ter o Python instalado.
    - Recomenda-se o uso do ambiente virtual (venv).
    ```bash
    py -m venv .venv
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute os notebooks na seguinte ordem:
    - Primeiro, execute o `base.ipynb` para realizar o pré-processamento e salvar os dados tratados.
    - Em seguida, execute o `model.ipynb` para aplicar os modelos de machine learning e gerar os clusters.

---

## Referências

- [Kaggle - Plant Dataset](https://www.kaggle.com/datasets/iottech/plant/data)
- [ASPCA - Toxic and Non-Toxic Plants](https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants)
- [Pet Poison Helpline](https://www.petpoisonhelpline.com/poisons/)
- [NCBI - Toxicity of Plants Containing Calcium Oxalate Crystals](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10220692/)
- [RHS - Potentially Harmful Garden Plants](https://www.rhs.org.uk/advice/profile?pid=524)
- [PictureThis - Plant Identification and Care](https://www.picturethisai.com/)