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
After this method to create our model, we then used Bayesian hyperparameter optimization. This is what we used to fine-tune our CatBoost models to make our models optimal. 
