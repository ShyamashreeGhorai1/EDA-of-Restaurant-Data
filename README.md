# EDA-of-Restaurant-Data
Restaurant data analysis is a process of converting the data points into meaningful insights
and extract patterns from it through analysis which can help to make business related decision.
To operate any restaurant , there may arise many questions like , why some cuisines get more 
order than the other or how they can  improve customer experience  or how they can reduce cost
for employees etc. To get answer of these questions, restaurant data analysis may take important role.
EDA of restaurant data analysis can boost the performance of business by increasing the revenue.
## Dataset and Features
We perform our analysis on restaurant dataset which contain 9551 rows and 21 columns.
Features of the dataset are : 1) Restaurant ID 2) Restaurant Name 3) Country Code
4) City 5) Address 6) Locality 7) Locality Verbose 8) Longitude 9) Latitude 10) Cuisines
11) Average Cost for two 12) Currency 13) Has Table booking 14) Has Online delivery 15) Is 
delivering now 16) Switch to order menu 17) Price range 18) Aggregate rating 19) Rating color
20) Rating text 21) Votes.
![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/448ea2c0-a290-4b68-a652-979f62b4bbfb)
## Data Cleaning
We  cleaned our data through following steps:
Treatment of missing value : There are 9 missing values in cuisines feature, which we removed by 
deleting the observations.
Treatment of duplicate value : There is no duplicate value in our dataset.
Treatment of inconsistent value : We removed special characters from city, cuisines, restaurant name, 
address, locality, locality verbose and currency column.
## Result of Analysis
Distribution of the features:

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/ae038400-1e0b-4bd5-ad7c-5b3796ecbcd5)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/556c4a5a-47fa-45f7-91a4-f741ea55c410)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/50e5d4b5-60dc-412f-a01f-989e84b34c42)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/a8c609a4-eee4-44a3-819c-586c275a6843)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/df1fbe4d-73a1-4dd3-889e-23290af1f482)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/84be32c3-5a03-4363-8f71-cd43b54d4205)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/fcd09cf2-fe1e-43fd-9b8e-a2ce8fae7c82)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/dee61f8f-ed7f-4925-b7d4-06bcf7713c0c)

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/1d4b95fc-07d7-4ec9-9da7-856831c38a27)

Correlation between the features:

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/93d27dd9-90d0-4868-ab79-05db1ed7f029)

Top 10 restaurant with highest vote

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/5bb5447e-7a28-4929-8fa5-ab02886851c1)

Top 10 cities with most number of restaurants 

![image](https://github.com/ShyamashreeGhorai1/EDA-of-Restaurant-Data/assets/131132617/3e29e1ef-eebb-4919-ae85-1e742dbbf0a1)

Top 10 cuisines with highest vote:

Cuisines Italian, American, Pizza -> 10934
American, Burger, Café -> 9667
Continental, American, Asian, North Indian  ->7931
Continental, North Indian -> 7574 
European, Mediterranean, North Indian -> 6907 
North Indian, Chinese -> 5966 
Finger Food, North Indian, Italian, Continental, Thai, South Indian -> 5705 
North Indian, European, Mediterranean -> 5385 
Chinese, North Indian 5288 South Indian -> 5172

## Conclusion
We analysed various restaurant across various city. It helps us to extract patterns which further helps 
us to analyse various components of the dataset. Restaurant data analysis is a crucial step to operate 
any restaurant because it uncover patterns through analysis which can help to make business related 
decision.
















