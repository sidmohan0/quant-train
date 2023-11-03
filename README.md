# quant-train

## Overview
S&P 500 Overnight Random Forest Systematic Trading Strategy with data ingestion using Polygon API, feature engineering, storage into a MySQL DB, a backtesting framework with visualizations, and code for a production deployment. 

I'll be updating this regularly to add more functionality. Take a peek at the Future Updates section for more details.  Interested in collaborating, contributing, or just want to chat? Please reach out to me direct at sid@datafog.ai. 

## Overivew

This repo is a collection of python scripts that do the following:
* download SPY spot and options data. 
* calculate overnight returns and volatility
* solve for the greeks of the option contracts (check out feature_functions.py)
* train a random forest model to predict overnight returns
* backtest the model
* calculate the performance metrics of the model
* send an email with the prediction using gmail

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

## Acknowledgement: 

Credit to QuantGalore for the original code.  His repo can be found at: https://github.com/quantgalore/sp500-overnight-prediction, and check out his blog post: https://quantgalore.substack.com/p/overnight-prediction-of-sp-500.  


## Changelog

11/3/23
* Added .env
* Added requirements.txt
* Refactoring, file renaming
* Abstracted out MySQL connection
* Source: [SP500 Overnight Prediction](https://quantgalore.substack.com/p/overnight-prediction-of-sp-500)
