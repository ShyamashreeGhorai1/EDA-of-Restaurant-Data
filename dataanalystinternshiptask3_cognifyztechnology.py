# -*- coding: utf-8 -*-
"""DataAnalystInternshipTask3@CognifyzTechnology.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aBOQ4Ms6I7S1N2dIxecWdBgRd6bXB0UC

**Importing Libraries**
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""**Loading the Dataset**"""

import io
import pandas as pd
from google.colab import files

uploaded = files.upload()

df = pd.read_csv(io.BytesIO(uploaded.get('Task_1_data_analysis (1).csv')))

df

pd.pandas.set_option('Display.max_columns',None)
pd.pandas.set_option('Display.max_rows',None)

"""**Basic Information about the Dataset**"""

# first five record from the dataset
df.head()

# last five record from the dataset
df.tail()

# shape of the dataset
df.shape

df.info()

# summary statistics of the numerical dataset
df.describe()

# summary statistics of the categorical featrures
df.describe(include='object')

df.dtypes

# features of the dataset
df.columns

df['Has Online delivery'].value_counts()

df['Has Table booking'].value_counts()

df['Is delivering now'].value_counts()

df['Rating color'].value_counts()

df['Rating text'].value_counts()

"""**Data Cleaning**"""

# Treatment of missing value

df.isnull().sum()

df.dropna(inplace=True)
print(df.isnull().sum())

# Treatment of duplicate value

df.duplicated().sum()

# Treatment of inconsistent value

# Removing useless characters from the column, city
Spec_chars = ["�","_"]
for char in Spec_chars:
  df['City'] = df['City'].str.replace(char,' ')

df['City']

# Removing useless characters from the column, cuisines
Spec_chars = ["�","_"]
for char in Spec_chars:
  df['Cuisines'] = df['Cuisines'].str.replace(char,' ')

df['Cuisines']

# Removing useless characters from the column, Restaurant Name
Spec_chars = ["�","_"]
for char in Spec_chars:
  df['Restaurant Name'] = df['Restaurant Name'].str.replace(char,' ')

df['Restaurant Name']

# Removing useless characters from the column, Address
Spec_chars = ["�","_"]
for char in Spec_chars:
  df['Address'] = df['Address'].str.replace(char,' ')

df['Address']

# Removing useless characters from the column, Locality
Spec_chars = ["�","_"]
for char in Spec_chars:
  df['Locality'] = df['Locality'].str.replace(char,' ')

df['Locality']

# Removing useless characters from the column, Locality Verbose
Spec_chars = ["�","_"]
for char in Spec_chars:
  df['Locality Verbose'] = df['Locality Verbose'].str.replace(char,' ')

df['Locality Verbose']

# Removing useless characters from the column, Currency
Spec_chars = ["�","_"]
for char in Spec_chars:
  df['Currency'] = df['Currency'].str.replace(char,' ')

df['Currency']

"""**Exploratory Data Analysis**"""

plt.figure(figsize=(10,6))
plt.hist(df['Average Cost for two'],color='lime')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Distribution of the feature, Average cost for two')

plt.figure(figsize=(10,6))
plt.hist(df['Restaurant ID'],color='purple')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Distribution of the feature, Restaurant ID')

plt.figure(figsize=(10,6))
plt.hist(df['Country Code'],color='yellow')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Distribution of the feature, Country Code')

plt.figure(figsize=(10,6))
plt.hist(df['Longitude'],color='lightcoral')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Distribution of the feature, Longitude')

plt.figure(figsize=(10,6))
plt.hist(df['Latitude'],color='darkcyan')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Distribution of the feature, Latitude')

a = df['Price range'].value_counts()
price_range = a.index
freq = a.values
plt.figure(figsize=(8,6))
plt.bar(price_range,freq,color= ['violet','cyan','yellow','powderblue'])
plt.xlabel("Price range")
plt.ylabel("Count of price range")
plt.show()

plt.figure(figsize=(8,6))
plt.hist(df['Votes'],bins=[0,500,1000,1500,2000],color='pink')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Distribution of the feature ,votes')

## Observation:-  Most of the value of the observation of the feature, votes lies between 0 and 500.

plt.figure(figsize=(8,6))
plt.hist(df['Aggregate rating'],color='indigo')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Distribution of the feature, aggregate rating")
plt.show()

df['Aggregate rating'].max()

## Restaurants with highest rating
df[['Restaurant Name','City']][df['Aggregate rating']==4.9]

## Top 10 restaurant with highest vote
ResNam = df.groupby(by='Restaurant Name')['Votes'].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(22,8))
plt.bar(ResNam.index, ResNam.values,color=['violet','cyan','yellow','powderblue','lightsalmon','lime','slategrey','red','darkslategrey','indigo'])

plt.figure(figsize=(22,12))
a = df['Has Online delivery'].value_counts()
b = df['Rating text'].value_counts()
c = df['Rating color'].value_counts()
plt.subplot(1,3,1)
plt.bar(a.index, a.values,color=['violet','cyan'])
plt.xlabel('Has online delivery')
plt.ylabel('Count of each class')
plt.subplot(1,3,2)
plt.bar(b.index, b.values,color=['hotpink','lightgreen','purple','violet','yellow','red'])
plt.xlabel('Rating text')
plt.ylabel('Count of each class')
plt.subplot(1,3,3)
plt.bar(c.index, c.values, color=['orangered','lightcoral','lightgreen','olive','lime','slategrey'])
plt.xlabel('Rating color')
plt.ylabel('Count of each class')

## Correlation between the features
matplotlib.rcParams['figure.figsize'] = (15,8)
sns.heatmap(df.corr(),cmap = 'YlGnBu', annot = True)
plt.show()

## Top 10 cuisines with highest vote
df.groupby(by='Cuisines')['Votes'].max().sort_values(ascending=False).head(10)

# which currency is used by which city
df[['City','Currency']].groupby(['City','Currency']).size().reset_index()

plt.figure(figsize = (15, 4))
plt.subplot(1,3,1)
sns.boxplot(x = 'Has Online delivery', y = 'Aggregate rating', data = df)
plt.subplot(1,3,2)
sns.boxplot(x = 'Has Table booking', y = 'Aggregate rating', data = df)
plt.show()

plt.figure(figsize = (20, 4))
plt.subplot(1,3,1)
sns.violinplot(x = 'Rating text', y = 'Average Cost for two', data = df)
plt.subplot(1,3,2)
sns.violinplot(x = 'Price range', y = 'Votes', data = df)

sns.set_style('whitegrid')
sns.pairplot(df,hue='Rating text')
plt.show()

"""1. Count the number of restaurants in each city."""

df.groupby(by=['City'])['Restaurant ID'].count()

"""2. Create a bar chart showing the top 10 cities with the most number of restaurants."""

maxRes = df.groupby(by=['City'])['Restaurant ID'].count().sort_values(ascending=False).head(10)
maxRes.plot(kind='bar',figsize=(10,8),color=['violet','cyan','yellow','powderblue','lightsalmon','lime','slategrey','red','darkslategrey','indigo'])
plt.title('Top 10 cities with most number of restaurants')
plt.xlabel('city')
plt.ylabel('No of restaurants')
plt.show()

"""3. Calculate the distance between each pair of restaurants using their latitude and longitude coordinates."""

!pip install haversine

import haversine as hs

# Define a function to calculate the distance between two points using Haversine formula
def calculate_distance(lat1,lon1,lat2,lon2):
  distance = hs.haversine((lat1,lon1),(lat2,lon2))
  return distance

# Input function to get restaurant name from tha user
def get_restaurant_names():
  restaurant1 = input("Enter the name of the first restaurant: ").strip()
  restaurant2 = input("Enter the name of the second restaurant: " ).strip()
  return restaurant1, restaurant2

def calculate_distance_between_restaurants():
  restaurant1, restaurant2 = get_restaurant_names()
  #Convert restaurant names to lowercase for case-insensitive matching
  restaurant1_lower = restaurant1.lower()
  restaurant2_lower = restaurant2.lower()
# Find the latitude and longitude coordinates of the two restaurants
  restaurant1_data = df[df["Restaurant Name"].str.lower() == restaurant1_lower]
  restaurant2_data = df[df["Restaurant Name"].str.lower() == restaurant2_lower]

  if len(restaurant1_data) == 0:
    print(f"Restautrant '{restaurant1}' not found in the dataset")
  if len(restaurant2_data) ==0:
    print(f"Restautrant '{restaurant2}' not found in the dataset")

  lat1, lon1 = restaurant1_data[['Latitude','Longitude']].values[0]
  lat2, lon2 = restaurant2_data[['Latitude','Longitude']].values[0]

   # calculate distance between two restaurants
  distance = calculate_distance(lat1, lon1, lat2, lon2)

  # print the distance between the two restaurants
  print(f"The distance between {restaurant1} and {restaurant2} is approximately {distance:.2f} kilometers.")

# call the main function
calculate_distance_between_restaurants()

"""4. Identify the unique cuisines available in the dataset."""

unique_cuisines = df['Cuisines'].unique()
for cuisin in unique_cuisines:
  print(cuisin)

"""5. Sort the dataset based on the aggregate rating in descending order."""

df.sort_values(by='Aggregate rating',ascending=False)

"""6. Identify the restaurants that have a rating color of "Excellent"."""

df['Restaurant Name'][df['Rating text']=='Excellent']

"""7. Use Seaborn to create a violin plot showing the distribution of aggregate ratings for restaurants in different cities."""

plt.figure(figsize=(30,20))
sns.set(style="whitegrid")
sns.violinplot(x ='Restaurant Name', y ='Aggregate rating', data = df)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

