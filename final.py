import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("./pokemon.csv")

df['percentage_male'] = df['percentage_male'].fillna(df['percentage_male'].median())

df['weight_kg'] = df['weight_kg'].fillna(df['weight_kg'].mean())
df['height_m'] = df['height_m'].fillna(df['height_m'].mean())

df = df.assign(for_rock = (df["base_total"]/(df['against_rock']+0.1)) / 100)
df.loc[:, 'for_rock'] = df.for_rock
print('The best six pets for rock: ')
rock_6 =df.sort_values(["for_rock"],ascending=False)[['name','for_rock']].head(6) 
print("len rock_6:", rock_6)


df = df.assign(for_fight = (df["base_total"]/(df['against_fight']+0.1)) / 100) 
df.loc[:, 'for_fight'] = df.for_fight
print('The best six pets for fight: ')
fight_6 =df.sort_values(["for_fight"],ascending=False)[['name','for_fight']].head(6)
print(fight_6)

df = df.assign(for_electric = (df["base_total"]/(df['against_electric']+0.1)) / 100) 
df.loc[:, 'for_electric'] = df.for_electric
print('The best six pets for electric: ')
electric_6 =df.sort_values(["for_electric"],ascending=False)[['name','for_electric']].head(6)
print(electric_6)

df = df.assign(for_fire = (df["base_total"]/(df['against_fire']+0.1)) / 100) 
df.loc[:, 'for_fire'] = df.for_fire
print('The best six pets for fire: ')
fire_6 =df.sort_values(["for_fire"],ascending=False)[['name','for_fire']].head(6)
print(fire_6)

df = df.assign(for_normal = (df["base_total"]/(df['against_normal']+0.1)) / 100) 
df.loc[:, 'for_normal'] = df.for_normal
print('The best six pets for normal: ')
normal_6 =df.sort_values(["for_normal"],ascending=False)[['name','for_normal']].head(6)
print(normal_6)

df = df.assign(for_flying = (df["base_total"]/(df['against_flying']+0.1)) / 100) 
df.loc[:, 'for_flying'] = df.for_flying
print('The best six pets for flying: ')
flying_6 =df.sort_values(["for_flying"],ascending=False)[['name','for_flying']].head(6)
print(flying_6)

df = df.assign(for_psychic = (df["base_total"]/(df['against_psychic']+0.1)) / 100) 
df.loc[:, 'for_psychic'] = df.for_psychic
print('The best six pets for psychic: ')
psychic_6 =df.sort_values(["for_psychic"],ascending=False)[['name','for_psychic']].head(6)
print(psychic_6)

df = df.assign(for_water = (df["base_total"]/(df['against_water']+0.1)) / 100) 
df.loc[:, 'for_water'] = df.for_water
print('The best six pets for water: ')
water_6 =df.sort_values(["for_water"],ascending=False)[['name','for_water']].head(6)
print(water_6)

error = []
for index, row in water_6.iterrows():
    error.append(row["for_water"] - water_6["for_water"].max())
squaredError = []
absError = []
for val in error:
    squaredError.append(val * val)
    absError.append(abs(val))
print("RMSE = ", sqrt(sum(squaredError) / len(squaredError)))
