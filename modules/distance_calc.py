import pandas as pd
from scipy.spatial.distance import cdist
import pickle



def calculate_distances(new_user_data, data_grouped, scaller_local):
        
    """
    Calcula as distâncias entre um novo usuário e as plantas existentes e retorna o ranking das 4 plantas mais próximas.

    Args:
        new_user_data (dict): Dados do novo usuário no formato de dicionário.
        data_distances (pd.DataFrame): Dados normalizados das plantas existentes.
        data_grouped (pd.DataFrame): Dados agrupados das plantas com informações adicionais.

    Returns:
        pd.DataFrame: Ranking das 4 plantas mais próximas com informações de compatibilidade.
    """
    
    with open(scaller_local, 'rb') as file:
        scaler = pickle.load(file)
   
    new_user = pd.DataFrame([new_user_data])
    new_user_normalized = scaler.transform(new_user)

    data_distances = data_grouped.drop(columns=['kmeans_group', 'name', 'group_name'])

    distances = cdist(new_user_normalized, data_distances, metric='euclidean')


    distances_df = pd.DataFrame(distances.T, columns=['Distance'])
    distances_df['Plant Index'] = data_distances.index
    distances_df['Plant Name'] = data_grouped.loc[data_distances.index, 'name'].values
    distances_df['Group'] = data_grouped.loc[data_distances.index, 'group_name'].values


    distances_df['Compatibility Percentage'] = round(
        100 - (distances_df['Distance'] / distances_df['Distance'].max() * 100), 0
    )


    return distances_df.sort_values(by='Distance').head(4)




"""
# Exemplo de uso da função

new_user_data = {
    'ind_pets': 0,
    'ind_apartment': 0,
    'size_code': 1,
    'experience_level_code': 1,
    'disponibility_level_code': 1
}


data_grouped = pd.read_csv('./datasets/results/plants_grouped.csv') 


ranking = calculate_distances(new_user_data, data_grouped, './pickles/scaler.pkl')
print(ranking)
"""