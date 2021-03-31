# ogs-data-exploration
This repository is dedicated to the cartography and exploration of greenhouse gas (GHG) emissions data at various geographical scales.

## Documentation

### Goal
The goal of documentation tasks consists of identifying relevant GHG data and documenting associated knowledge and concepts for understanding its content.

### Outputs

- List of data sources with respective links in wiki data-source page
- Feeding wiki with references,  knowledge and concepts related to GHG emissions data

## Exploration
### Goal
The goal of data exploration tasks consists of exploring and analyzing the different data sources identified in the documentation tasks.

### Process

- Each contributor is responsible of the analysis of x data sources.
- We create a branch by data source in the github repo.
- We create a folder by data source.
- For each data source, a readme file is needed to describe the content.
- Each data source explorer maintains his/her branch by documenting the data source, providing analysis notebooks and generating a json file describing datasource metadata.
- Contributors are asked to commit changes as frequent as possible by adding issue number in the commit message. 
- When you want to merge your changes in the main branch, make a pull request by identifying the reviewer and linking the pull request to the issue you are working on.
You will receive a message of acceptance when your pull request is merged.


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
