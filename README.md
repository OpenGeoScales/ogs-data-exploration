# ogs-data-exploration
Welcome to the ogs-data-exploration repository!
This repository is dedicated to the cartography and exploration of greenhouse gas (GHG) emissions data at various geographical scales.
Two main goals are defined for this repository:

- *Documentation*: Build a knowledge base on GHG emissions data (collection methods, concepts, providers...)
- *Data Exploration*: Explore GHG emissions data at various scales in order ot identify relevant data sources, build a complete data catalog and define a data model enabling the integration of explored data.

## Documentation

### Goal
The goal of documentation tasks consists of identifying relevant GHG data and documenting associated knowledge and concepts for understanding its content.

### Outputs

- List of data sources with respective links in wiki data-source page
- Feeding wiki with references,  knowledge and concepts related to GHG emissions data

## Exploration

### Goal

The goal of data exploration tasks consists of analyzing the different data sources identified in the documentation tasks in order to provide insights on GHG emissions data.

### Process

- Each contributor is responsible of the analysis of x data sources.
- Each data source has its own git branch.
- We create a folder by data source.
- For each data source, a readme file is needed to describe the content.
- Each data source explorer maintains his/her branch by documenting the data source, providing analysis notebooks and generating a json file describing datasource metadata.
- Contributors are asked to commit changes as frequent as possible by adding issue number in the commit message. 
- When contributor wants to merge new changes in the main branch, he/she should make a pull request by identifying the reviewer and linking the pull request to the issue he/she is working on.
He/she will receive a message of acceptance when your pull request is merged.


### Outputs

#### Notebooks
Notebooks (Python or R) providing exploratory analysis of raw data

#### Data Catalog

- Feeding a Data Catalog with information about analyzed data
```json
{
	"fields": [
	{
			"data_source": "Name of data source",
			"data_provider": "Name of data provider",
			"format": "data format (csv, json, xls)",
			"temporal_resolution": ["year", "month", "day"],
			"spatial_resolution": ["country", "city", "grid-xkm"],
			"temporal_coverage": ["min-date", "max-date"],
			"spatial_coverage": ["Europe", "France"],
			"data_access": ["download", "api"],
			"gases": ["CO2", "CH4"],
			"scopes": ["Scope 1", "Scope 2", "NA"],
			"sectors": ["All sectors", "Industrial", "Agriculture"],
			"protocols": ["kyoto protocol"],
			"estimation_methods": ["Top-Down", "Bottom-Up"]
		}
	]
}
```
#### Selected datasets

- Selection of datasets to integrate in OGS platform
- Identification of potential transformation necessary for normalizing each data source

## Git Tuto

- Install Git
- Using GIT CMD go to the folder where you want to clone the repository (cd file/file)
- Clone the repository
```
git clone https://github.com/OpenGeoScales/ogs-data-exploration.git
```
- Using GIT CMD go to the cloned repository (cd file/file) 
```
cd ogs-data-exploration
```
- By default you are working in the main branch. Change the branch and select the branch associated with the dataset you are working on.
```
git checkout  'name of the branch'
```
For example to switch to the branch 'ademe'
```
git checkout  ademe
```
- Make changes: add notebooks, add data, change readme...
- Track all the changes
```
git add .
```
- Or Track specific files
```
git add data-catalog/ademe/ademe-data-desc.md notebooks/ademe/ademe-notebook.md
```
- Commit the changes by specifying a message and the issue number you are working on after #
```
git commit -m "my message #1"
```
- Push the changes in remote repo by specifying the branch name you want to push on
```
git push origin ademe
```
- When you want to merge changes, go Github, select the branch you changes, and make pull request by assigning a reviewer.
- When the reviewer accept your pull request, your changes will be merged with the main!
