# project_1
Fintech Bootcamp Project 1

Google Earth Engine Crop Area and ETF Time Series Analysise

# Sinan, Jude, Carolina, Chris and Mahtab

Agricultural crops are dramatically changing in North America, in this project we are going to analyzing specific agricultural crop data mainly focusing on Wheat, Soya Bean and Corn. We will be looking into yearly data in specific regions of the US States North Dakota, South Dakota, Montana, Iowa, Illinois, Nebraska and Minnisota. We will be looking at the data collection and trying to see how they correlate ETF Stock.

# Our Approach

The analysis below will showcase the changes in crop land area for 3 agricultural commodities over the last 10 years and will look for correlations with Exchange Traded Fund commodity stocks of the same type.

### 1) Setting up crop data to be visulized on the map.

Using Google Earth Map, we collected the data in order to show the crops.

The following images belows shows how the map had changed over the period of time we had collected the data.

![image](images/1_Google_Map.png)

### 2) Gather ETF Ticker data for CORN, SOYB and WHEAT.

We had imported the dataset from AgriTrieker.py to gather the ETF for Corn, Soy Beans and Wheat from the last 10 years. 

After the data collection was completed we needed to resample the imformation as the pixel data from the map is only available on a yearly basis.

![image](images/2_Google_PctChange.png)

### 3) Gather pixel data that represents crop land cover in the US.

Our goal in this part was to retrieve visual data using Earth Engine and breakdown the information into samples based on Years, US States and Crops 

![image](images/3_Google_CropArea.png)

![image](images/4_Google_CropArea_PctChange.png)

### 4) Compare crop land area changes with ETF stock changes

In this step we had compared the changes in the area in comparision to the ETF Stocks

![image](images/5_Google_Combined_PctChange.png)
![image](images/6_Google_Combined_Correlation.png)

Based on the heatmap, we don’t see a strong correlation between crop land area changes with the ETF returns. Rather, we see correlation between the ETF commodities.

### 5) Compare ETF stock changes with crop land area changes by State.

In this section we had analyzed the data in a state by state basis and how the data that was collected was correlated with ETF stock prices. 

- North Dakota

![image](images/7_Google_CropArea_ND.png)
![image](images/8_Google_Combined_PctChange_ND.png)
![image](images/9_Google_Combined_Correlation_ND.png)

-South Dakota

![image](images/10_Google_CropArea_SD.png)
![image](images/11_Google_Combined_PctChange_SD.png)
![image](images/12_Google_Combined_Correlation_SD.png)

- Montana

![image](images/13_Google_CropArea_MT.png)
![image](images/14_Google_Combined_PctChange_MT.png)
![image](images/15_Google_Combined_Correlation_MT.png)

- Iowa

![image](images/16_Google_CropArea_IA.png)
![image](images/17_Google_Combined_PctChange_IA.png)
![image](images/18_Google_Combined_Correlation_IA.png)

- Illinois

![image](images/19_Google_CropArea_IL.png)
![image](images/20_Google_Combined_PctChange_IL.png)
![image](images/21_Google_Combined_Correlation_IL.png)

- Nebraska

![image](images/22_Google_CropArea_NE.png)
![image](images/23_Google_Combined_PctChange_NE.png)
![image](images/24_Google_Combined_Correlation_NE.png)

- Minnesota

![image](images/25_Google_CropArea_MN.png)
![image](images/26_Google_Combined_PctChange_MN.png)
![image](images/27_Google_Combined_Correlation_MN.png)

4