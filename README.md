# Google Earth Engine Crop Area and ETF Time Series Analysis


# Table of contents:

- [Prerequisites](#prerequisites)
    - [How to set up the Google Earth Engine API](#how-to-set-up-the-google-earth-engine-api)

- [The Project ](#the-project)
	- [Project Goals](#project-goals)

    - [Data](#data)

	- [Our Approach](#our-approach)	
	- [In Conclusion](#in-conclusion)
	

# Prerequisites

### Libraries Utilized:

```shell
 - requests
 - pandas
 - alpaca_trade_api
 - MCSimulation
 - Numpy
 - seaborn
 - geemap
 - ee 
 - panel 
 - hvplot.pandas
 - dotenv
 - os
```

### How to set up the Google Earth Engine API

##### A Google account and an Earth Engine account is required to run the API. 

##### Earth Engine - https://signup.earthengine.google.com/

#### 1) Setup a new GEEMap environment.

```shell
conda create -n geenv python=3.7 anaconda -y

conda activate geenv

```
#### 2) We need to install some libraries

```shell
conda install mamba -c conda-forge

mamba install geemap -c conda-forge

mamba install jupyter_contrib_nbextensions -c conda-forge

```

#### 3) And Finally run Jupyter Notebook

```shell
jupyter notebook
```



# The Project
The agricultural crop landscape is dramatically changing in North America, in this project we are going to analyze specific agricultural crop data focused on Wheat, Soybean and Corn.
 We will be looking into yearly data of these commodities in specific regions of the United States, the states of focus are as follow;
 - North Dakota
 - South Dakota
 - Montana 
 - Iowa 
 - Illinois
 - Nebraska 
 - Minnesota



## Project Goals


The goals for this project is to see the correlation, if any between the commodities, the price of the commodites and their yield and the land area in which they are planted.

##### *** The Earth Engine jupyter notebook can be accessed [here](GOOGLECROP.ipynb).

## Data

We used Alpaca API to gather the information on the ETFs. 

For the visuals displayed on  Geemap we used a package from the USDA facilitated by GEE as well as resources from [**Geemap**](https://geemap.org)

We complemented the data by using [**Kaggle**](https://www.kaggle.com/ainslie/usda-wasde-monthly-corn-soybean-projections)
for the corn and wheat prices as well as more data from the USDA  for the [**wheat  prices**](https://www.ers.usda.gov/data-products/wheat-data/).


![image](images/Data_sources.png)
                                                                                                                                                   

## Our Approach

The study conducted will showcase the changes in crop land area for 3 agricultural commodities over the last 10 years. Data will then be analyzed to understand the correlations with ETF commodity stocks of the same type.

#### 1) Setting up crop data to be visulized on the map.

Using Google Earth Engine, we were able to visualize the data priorly collected, we were able to apply differet keys for different crops to make the graphical presentation more clear.

The following image below shows how the map has changed over the period of time based on the data found.

![image](images/1_Google_Map.png)

#### 2) Gathering ETF Ticker data for CORN, SOYB and WHEAT.

We imported the dataset from Alpaca API to gather the ETF for Corn, Soybean and Wheat from the last 10 years. 

After the data was collected, we needed to resample the information (clean up data) as the pixel data from the map is only available on a yearly intervals.

![image](images/2_Google_PctChange.png)

Our study shows Wheat yeilded the highest return among the produced crops in the current year, however soybean used to yeild the best returns during 2012 to 2018. Since 2019 corn has been on a steady decline. 

#### 3) Gathering pixel data that represents crop land cover in the US.

Our goal in this section was to retrieve visual data using Google Earth Engine of how much land is used to farm the 3 different crops (soybean, wheat, corn) and breakdown the information into samples based on the years, crops, area used in the different states.


![image](images/3_Google_CropArea.png)

As our study shows corn has used up the most plantation area. Soy Bean is the second most cultivated crop, between 2016 to 2018 there was an increase in porduction and the land used that it overtook corn, however that was short lived and soon the cultivation declined early 2018. Wheat has always remained low and constant.

![image](images/4_Google_CropArea_PctChange.png)

#### 4) Comparing cropland area changes with ETF 

In this step we compared the changes in the croplands area with the changes in the ETFs prices

![image](images/5_Google_Combined_PctChange.png)
![image](images/6_Google_Combined_Correlation.png)

Based on the heatmap, we don’t see a strong correlation between cropland area changes with the ETF returns. Rather, we see correlation amongst the ETFs.

#### 5)Comparing cropland area changes with ETF by State.

In this section we had analyzed the data in a state by state basis and how the data that was collected was correlated with ETF stock prices. 

- ##### North Dakota

![image](images/7_Google_CropArea_ND.png)
![image](images/8_Google_Combined_PctChange_ND.png)
![image](images/9_Google_Combined_Correlation_ND.png)

- ##### South Dakota

![image](images/10_Google_CropArea_SD.png)
![image](images/11_Google_Combined_PctChange_SD.png)
![image](images/12_Google_Combined_Correlation_SD.png)

- ##### Montana

![image](images/13_Google_CropArea_MT.png)
![image](images/14_Google_Combined_PctChange_MT.png)
![image](images/15_Google_Combined_Correlation_MT.png)

- ##### Iowa

![image](images/16_Google_CropArea_IA.png)
![image](images/17_Google_Combined_PctChange_IA.png)
![image](images/18_Google_Combined_Correlation_IA.png)

- ##### Illinois

![image](images/19_Google_CropArea_IL.png)
![image](images/20_Google_Combined_PctChange_IL.png)
![image](images/21_Google_Combined_Correlation_IL.png)

- ##### Nebraska

![image](images/22_Google_CropArea_NE.png)
![image](images/23_Google_Combined_PctChange_NE.png)
![image](images/24_Google_Combined_Correlation_NE.png)

- ##### Minnesota

![image](images/25_Google_CropArea_MN.png)
![image](images/26_Google_Combined_PctChange_MN.png)
![image](images/27_Google_Combined_Correlation_MN.png)


### In Conclusion

When comparing state by state we notice that wheat as a whole has historically experienced the most significant fluctuations in its cropland size while soybean has been the ETF with the highest growth amongst the compared commodities.

Giving the steady growth of the commodity price and the little diminish in it's cultivation area, we can asume that soybean would be the best option to allocate a higher portion of funds when adding the said commodity to a portfolio in a long term investment, corn being second and wheat third. 

##### *** The ETF portfolio jupyter notebook can be accessed [here](WEATCORNSOYB.ipynb).

