import pandas as pd
from scipy.spatial.distance import cdist
import pickle
from dataclasses import dataclass


@dataclass
class PlantRanking:
    distance: float
    plant_index: int
    plant_name: str
    group: str
    compatibility: float



def calculate_distances(new_user_data, data_complete, scaller_local):     
    with open(scaller_local, 'rb') as file:
        scaler = pickle.load(file)
    
    data = data_complete[['ind_pets', 'ind_apartment', 'size_code', 'experience_level_code', 'disponibility_level_code']]
    
    new_user = pd.DataFrame([new_user_data])
    new_user_normalized = scaler.transform(new_user)


    distances = cdist(new_user_normalized, data, metric='euclidean')

    distances_df = pd.DataFrame(distances.T, columns=['Distance'])
    distances_df['Plant Index'] = data.index
    distances_df['Plant Name'] = data_complete.loc[data_complete.index, 'name'].values
    distances_df['Group'] = data_complete.loc[data_complete.index, 'group_name'].values

    distances_df['Compatibility Percentage'] = round(100 - (distances_df['Distance'] / distances_df['Distance'].max() * 100), 0)
    distances_df = distances_df.sort_values(by='Compatibility Percentage', ascending=False).head(4)

    ranking  = []
    for i in range(len(distances_df)):
        if distances_df['Compatibility Percentage'].iloc[i] > 0:
            plants = PlantRanking(
                distance=distances_df['Distance'].iloc[i],
                plant_index=distances_df['Plant Index'].iloc[i],
                plant_name=distances_df['Plant Name'].iloc[i],
                group=distances_df['Group'].iloc[i],
                compatibility=distances_df['Compatibility Percentage'].iloc[i]
            )
            ranking.append(plants)


    return plants




""""
Exemplo de uso da função

new_user_data = {
    'ind_pets': 0,
    'ind_apartment': 0,
    'size_code': 1,
    'experience_level_code': 1,
    'disponibility_level_code': 1
}


data_grouped = pd.read_csv('./datasets/results/plants_complete.csv') 
pickle_file = './pickles/scaler.pkl'

ranking = calculate_distances(new_user_data, data_grouped, pickle_file)
print(ranking)
"""