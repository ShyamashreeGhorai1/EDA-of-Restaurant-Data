# -*- coding: utf-8 -*-
"""DataAnalystInternshipTask2@CognifyzTechnology.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jlI4jJP22jNkhasUkuOLZXbyiRjtdO4f

**# DATA ANALYSIS INTERNSHIP TASK 2**

**TASK**
1. Group the dataset by cuisine and calculate the average rating for each cuisine.
2. Calculate the total number of votes for all restaurants.
3. Filter the dataset to include only restaurants that offer online delivery.
4. Count the number of restaurants in each city.
5. Identify the restaurants that have a rating color of "Excellent".
6. Create a bar chart showing the top 10 cities with the most number of restaurants.
7. Calculate the distance between each pair of restaurants using their latitude and longitude coordinates.
8. Create a scatter plot showing the relationship between the average rating and the number of votes for each restaurant.
9. Group the dataset by rating color and calculate the average price range for each rating color.
10. Create a histogram showing the distribution of aggregate ratings.
11. Determine the correlation between the price range and the average rating.
12. Create a heat map showing the density of restaurants across different cities.
13. Use Seaborn to create a scatter plot showing the relationship between the longitude and latitude coordinates of restaurants.
14. Create a box plot using Seaborn to compare the price range distribution for different cuisines.
15. Use Seaborn to create a violin plot showing the distribution of aggregate ratings for restaurants in different cities.

**Importing Libraries**
"""

import pandas as pd
import numpy as np
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

"""**Data Cleansing and Exploratory Data Analysis**"""

# first five record of the dataset
df.head()

# last five record of the dataset
df.tail()

# shape of the dataset
df.shape

# features of the dataset
df.columns

df['Has Table booking'].value_counts()

df['Has Online delivery'].value_counts()

df['Rating text'].value_counts()

# information about the dataset
df.info()

df.dtypes

# summary  statistics of the dataset
df.describe()

# summary statistics of the categorical features
df.describe(include='object')

"""**Missing value treatment**"""

# check null values
df.isnull().sum()

df.dropna(inplace=True)

"""**Treatment of duplicate value**"""

df.duplicated().sum()

"""1. Group the dataset by cuisine and calculate the average rating for each cuisine."""

df.groupby(by=['Cuisines'])['Aggregate rating'].mean()

"""2. Calculate the total number of votes for all restaurants."""

total_votes = df['Votes'].sum()
print("Total number of votes for all restaurants is : ",total_votes)

"""3. Filter the dataset to include only restaurants that offer online delivery."""

df[df['Has Online delivery']=='Yes']

"""4. Count the number of restaurants in each city."""

df.groupby(by=['City'])['Restaurant ID'].count()

"""5. Identify the restaurants that have a rating color of "Excellent"."""

df['Restaurant Name'][df['Rating text']=='Excellent']

"""6. Create a bar chart showing the top 10 cities with the most number of restaurants."""

maxRes = df.groupby(by=['City'])['Restaurant ID'].count().sort_values(ascending=False).head(10)
maxRes.plot(kind='bar',figsize=(10,8),color=['violet','cyan','yellow','powderblue','lightsalmon','lime','slategrey','red','darkslategrey','indigo'])
plt.title('Top 10 cities with most number of restaurants')
plt.xlabel('city')
plt.ylabel('No of restaurants')
plt.show()

"""7. Calculate the distance between each pair of restaurants using their latitude and longitude coordinates."""

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

"""8. Create a scatter plot showing the relationship between the average rating and the number of votes for each restaurant."""

plt.scatter(df['Aggregate rating'],df['Votes'])
plt.title('Scatter plot - Aggregate rating vs No. of votes')
plt.xlabel('Aggregate rating')
plt.ylabel('No. of votes')
plt.show()

"""9. Group the dataset by rating color and calculate the average price range for each rating color."""

df.groupby(by=['Rating color'])['Price range'].mean()

"""10. Create a histogram showing the distribution of aggregate ratings."""

plt.hist(df['Aggregate rating'])
plt.title('Histogram - Aggregate rating')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

"""11. Determine the correlation between the price range and the average rating."""

cor = np.corrcoef(df['Price range'],df['Aggregate rating'])
print('Correlation between the price range and the average rating is : \n',cor)

"""Correlation between the price range and the average rating is 0.43835642"""

plt.scatter(df['Price range'],df['Aggregate rating'])
plt.xlabel("Price range")
plt.ylabel("Aggregate rating")

"""12. Create a heat map showing the density of restaurants across different cities."""

maxRes = df.groupby(by=['City'])['Restaurant ID'].count().sort_values(ascending=False)
maxRes.plot(kind='bar',figsize=(10,8),color='red')
plt.xlabel("City")
plt.ylabel("Restaurant Count")
plt.tight_layout()
plt.show()

"""13. Use Seaborn to create a scatter plot showing the relationship between the longitude and latitude coordinates of restaurants."""

sns.set(style='whitegrid')
sns.scatterplot(x="Latitude",y="Longitude",data=df).set_title("Latitude vs Longitude")

"""14. Create a box plot using Seaborn to compare the price range distribution for different cuisines."""

# Create a box plot using Seaborn
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Price range', y='Cuisines', palette='Set3')

# Set the plot title and labels
plt.title('Price Range Distribution for Different Cuisines')
plt.xlabel('Price Range')
plt.ylabel('Cuisine')

# Adjust the layout and spacing
plt.tight_layout()

# Display the plot
plt.show()

"""15. Use Seaborn to create a violin plot showing the distribution of aggregate ratings for restaurants in different cities."""

sns.set(style="whitegrid")
sns.violinplot(x ='Restaurant Name', y ='Aggregate rating', data = df)
plt.xticks(rotation=45, ha='right')
plt.show()

