# Datathon2025

Chevron Challenge.

# Description:

In this challenge, we aim to predict the Vehicle Population for different types of cars. Vehicle Population refers to the total inventory of vehicles categorized by features such as model year, fuel type, and vehicle category.

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

### Model Specifications

To clean the data, We imputed missing categorical values with the category "Missing," which was directly compatible with our CatBoost model. For numerical columns, we simply imputed using the series mean. We also added functionality to one-hot encode our predictors throughout our modeling framework, but we ended up not using this feature. 

## Challenges we ran into

Using several basis models made overarching model design more complex and significantly increased computational intensity during training. It forced us to fit and store thousands of models which created delays for us computationally. 