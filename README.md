# Rice Datathon 2025

Chevron Track:  
RMSE 7,374  
Submission File in Repo: ChevronDatathon2025_Submission.xlsx

To run this, run notebook.ipynb under src/notebooks

# Description:

In this challenge, we aim to predict the Vehicle Population for different types of cars. Vehicle Population refers to the total inventory of vehicles categorized by features such as model year, fuel type, and vehicle category.

# Data

###  Data Cleaning

To clean the data, we first realized there were missing values in the Model Year column. To combat this, we imputed missing categorical values named "Missing." Since we interpretted this column as categorical, this solution was enough for us. We also added functionality to one-hot encode our predictors throughout our modeling framework, but we ended up not using this feature. 

### Additional Data

We wanted to add some macro data to our analysis. We found there to be sufficient data for our predictions on FRED. We added the Consumer Price Index for All Urban Consumers: Used Cars and Trucks in the US City Average. This alternative data allowed us to see macro impacts to add to other categorical data like Model Year. We will call this CPI in this report. This data was monthly from 1970 to 2024. Since we are predicting on data up till 2026. We simply forecasted the data to fill in this gaps. For "Missing" Model Year, we inputted the mean of the CPI over time.   

SOURCE: https://fred.stlouisfed.org/series/CUSR0000SETA02  


# Our Model:

We use CatBoost models to predict Vehicle Population. Our method involves grouping the data based on key features (referred to as basis columns) and training separate models for each group.

### Basis Columns
Basis columns define how we segment the data before training models. For example, if we choose Fuel Type as a basis column, we train a separate model for each fuel type:
- One model for Electric
- One model for Diesel
- One model for Gasoline

This approach helps us account for clustering and mixed effects in the data, improving the interpretability as well as predictive performance.

### Predictor Columns
Once the data is segmented by the basis column, we use specific features (predictor columns) to train the model. These predictor columns serve as the regressors. For example, if our columns look like:
- basis columns = Fuel Type
- Predictor Columns = Model Year, Vehicle Category, Fuel Technology

Then, to bring it to together, for a car with Electric Fuel Type, we:
1. Subset the data to include only Electric vehicles.
2. Train a model usign Model Year, Vehicle Category, and Fuel Technology as predictors. 
3. Use this model to predict the target variable: Vehicle Population

### Bayesian Optimization
After this method to create our model, we then used Bayesian hyperparameter optimization using the Optuna library. This is what we used to fine-tune our CatBoost models to make our models optimal. To find strong hyperparameters while keeping the time/computational complexity manageable, we quit our parameter tuning process for each basis model after 30 seconds or 20 parameter combinations evaluated - whichever came first.

# Challenges

Using several basis models made overarching model design more complex and significantly increased computational intensity during training. It forced us to fit and store thousands of models which created delays for us computationally. 

# Key Insights

After testing many different basis and prediction column combinations, we found that Vehicle Type was returning the best results and accuracy as the basis. This led us to focusing our tests on this as the basis column. This tells us that much complexity and clustering comes from the Vehicle Type when determining Vehicle Population. 

This led us to optimizing to have Fuel Technology, CPI: Used Cars and Trucks, Number of Vehicles Registered at the Same Address, GVWR Class, Electric Mile Range, Fuel Type, and Model Year as our predictor columns. 

With hyperparameter tuning, this brought our RMSE to 7,374.
