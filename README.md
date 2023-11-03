# S&P 500 Overnight Random Forest System
## Acknowledgement: Credit to QuantGalore for the original code layout, which I expect will change over time.  His repo can be found at: https://github.com/quantgalore/sp500-overnight-prediction, and check out his blog post: https://quantgalore.substack.com/p/overnight-prediction-of-sp-500.  

Key updates as of writing (11/03/2023) are abstraction of key variables into .env and package locking dependencies, as well as some   

## Overivew
This repo is a collection of python scripts that do the following:
* download SPY spot and options data. 
* calculate overnight returns and volatility
* solve for the greeks of the option contracts (check out feature_functions.py)
* train a random forest model to predict overnight returns
* backtest the model
* calculate the performance metrics of the model
* send an email with the prediction using gmail

## Concepts

We are training a Random Forest model from the scikit-learn library to predict the overnight returns of the S&P 500 index.

This started as a fork of QuantGalore's repo, but I've made some changes to the code and added some features.  I've also added a few more dependencies to the requirements.txt file.  I've also added a .env file to store some of the key variables.  You'll need to create a .env file in the root directory of the project which you can kickstart by copying env.example, then renaming it to .env, and then populating all of the fields with the appropriate variables. the only variable that you don't *need* to update is WORKING_DIR because the python script will automatically create a folder called 'working_dir' if one doesn't exist. 

I'll let the overall purpose of this project go with the flow and welcome community feedback! 


## Installation

1. Clone the repo
2. Use a virtual env , I use Pyenv w/ Python 3.8.10 running on Ubuntu 20.04 
3. pip install -r requirements.txt




## Future Updates

### Quality of Life
* pipenv or poetry
* refactor feature engineering parts
* refactor backtesting parts
* refactor into packages  and modules

### Data
* Use the polygon python client more proactively to speed up some of the ingestion of raw information like options contracts

### Automation
* run_backtest.sh
* run_prod.sh
* some sort of cron job


### Containerization
* Dockerfile
* Orchestrator (Kubernetes, Docker Swarm, etc.) and deployment scripts - also potentially making Automation section redundant



### Processing
By far the slowest part of the process is the feature engineering. While we are ultimately dumping a lot of information about contracts in-memory when running the program, the feature engineering, where 
we calculate the Greeks of the contracts, involves various operations over the dataframes. Some things I'm thinking about and open to suggestions on:
* Polars for faster processing of Dataframes
* GPU acceleration
* PySpark for distributed processing, also use w/ or instead of Polars
* Maybe add and or update the options functions in feature_functions.py to use tf-quant-finance


### Modeling
* Hyperparameter tuning
* Feature selection framework
