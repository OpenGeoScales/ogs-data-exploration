# ogs-data-exploration

Welcome to the ogs-data-exploration repository 👋

This repository is dedicated to the cartography and exploration of greenhouse gas (GHG) emissions data at various geographical scales.
Two main goals are defined for this repository:

- *Documentation*: Build a knowledge base on GHG emissions data (collection methods, concepts, providers...)
- *Data Exploration*: Explore GHG emissions data at various scales in order ot identify relevant data sources, build a complete data catalog and define a data model enabling the integration of explored data.

## Documentation

### Goal
The goal of documentation tasks consists of identifying relevant GHG data and documenting associated knowledge and concepts for understanding its content.

### Outputs

- List of data sources with respective links in [this wiki data-source page](https://github.com/OpenGeoScales/ogs-data-exploration/wiki/Data-sources)
- Feeding wiki with references,  knowledge and concepts related to GHG emissions data

## Exploration

### Goal

The goal of data exploration tasks consists of analyzing the different data sources identified in the documentation tasks in order to provide insights on GHG emissions data.

### Repository structure

The repository structure is splitted into 3 main folders:
- data: contains raw data to explore or links to raw data if the dataset size is bigger than 100MB. 
- notebooks: contains data exploration notebooks (in R or Python)
- data-catalog: contains the json files describing data sources attributes. These json files will be used to build a crelevant data catalog.

We proposed to have a first split of each folder by topic (e.g. ghg-emissions, socio-economic, geo-referential...) and then a second split by data source short name (e.g. ademe, wri (World Resources Institute), eea (European Environmental Agency)...). 

Every data source folder should contains a README file for describing the data source and data provider and files containing datasets.

    project_name/
    ├── README.md                   # overview of the project
    ├── data/                       # notebooks for exploring raw data
   	    ├── ghg-emissions        
	        └── source 1            # folder for data source 1
	    	    └── README.md      # Notebook for exploring data source 1
		    └── dataset      # Notebook for exploring data source 
	        └── source 2            # folder for data source 2
	    	    └── README.md1      # Notebook for exploring data source 1
		    └── dataset      # Notebook for exploring data source 2
	    ├── socio-economic 
	    └── geo-ref 
    ├── notebooks/                  # notebooks for exploring raw data
   	    ├── ghg-emissions        
	       └── source 1            # folder for data source 1
	    	   └── Notebook 1      # Notebook for exploring data source 1
		   └── Notebook 2      # Notebook for exploring data source 
	       └── source 2            # folder for data source 2
	    	   └── Notebook 1      # Notebook for exploring data source 1
		   └── Notebook 2      # Notebook for exploring data source 2
    ├── data-catalog/               # notebooks for exploring raw data
   	    ├── ghg-emissions        
	       └── source 1            # folder for data source 1
	    	   └── data-desc.json  # json file describing data source 1
	       └── source 1            # folder for data source 2
	    	   └── data-desc.json  # json file describing data source 2

### Procedure

Every contributor select one or two data sources to work on. The list of datasets are provided in this [wiki page](https://github.com/OpenGeoScales/ogs-data-exploration/wiki/Data-sources). NB: Some data sources provide several GHG emissions datasets such as the World Resources Institute.

Once you have selected your own datasource, you should clone the repository in your local machine (more informations about git commands are available at the end of this tutorial).

We decided, to make a branch by datasource in order to facilitate independant work at the beginning of this project. So you should have a specific branch for your data source.

In order to work on your branch, do not forget to switch to your branch directly before working on your data (`git checkout NameOfYourBranch`)

#### Data source information
Once you are in your branch, you can start by adding information in the readme file of your datasource. 

#### Data source exploration
Now we can start the exploratory analysis, go to `notebook/ghg-emissions/name of your data source` and create your first notebook there.
After making some analysis you can commit the changes and push it to the remote repository. Do not forget to put the issue number correponding to the data exploratory task in your commit message (`git commit -m "your message #x"`).

After pushing your changes, you shoudl go to Github, select your branch and make a pull request to merge your chnages made in your branch with the main. 
When you make pull request, you can assign the pull request to yourself, define a reviewer, attribute the pull request to a project and milestones.
In order to follow better the backlog evolutio, do not forget to link the pull request to the issue you are working on.

You will receive a message of acceptance when your pull request is merged.
	    
#### Data Catalog description

We want to build a data catalog making the compaison between different data sources easy. Hence, we need some information of data sources you habe just explored!

We ask you to fill a json file containing main dataset atttributes. Once filled, the json file should be stored in `data-catalog/ghg-emissions/data source/data-desc.json`

Here is an exemple of data desription:

```json
{
    "Version": "2021-02-04",
    "DatasourceAttributes": [
        {
            "DataSourceStorageName": "ademe",
			"Topics": ["GHG emissions"],
			"DataProvider": {
				"DataProviderName": "Lou Dupont",
				"DataProviderLink": "https://www.data.gouv.fr/fr/datasets/bilans-demissions-de-ges-publies-sur-le-site-de-lademe-1/",
				"DataProviderDesc": "NA"
			},
			"DataSource": {
				"DataSourceName": "BEGES",
				"DataSourceLink": "https://www.bilans-ges.ademe.fr/fr/bilanenligne/bilans/index/siGras/0",
				"DataSourceOrganism": "ADEME",
				"DataSourceDesc": "NA",
				"DataFormat": "csv",
				"DataAccess": "download"
			},
            "Coverage": {
				"SpatialCoverage":{
					"MainCoverage": "France",
					"NumberOfSpatialEntities": 238,
					"ListOfSpatialEntities": []
				},
				"TemporalCoverage": {
					"MinDate": 2009,
					"MaxDate": 2020,
				}
			},
			"Resolution": {
				"SpatialResolution": ["Communauté Urbaine", "Communauté d'agglomération","Communauté de Commune",
				"Communes", "Départements","Métropole","Régions"],
				"TemporalResolution": "year",
			},
            "Gases": {
				"Included": "All GHG gases",
				"FilterByGase": "False"
			},
            "Scopes": {
				"Included": ["Scope 1", "Scope 2", "Scope 3"],
				"FilterByScope": "True"
			},
			"Sectors": {
				"Included": "All sectors",
				"FilterBySector": "False"
			},
			"Protocol": {
				"ProtocolName": "Base Carbone",
				"ProtocolLink": "https://www.bilans-ges.ademe.fr/fr/accueil/contenu/index/page/decouverte/siGras/1"
			},
			"EstimationMethod": {
				"MethodType": "Bottom-up",
				"MethodDescription": "https://www.bilans-ges.ademe.fr/fr/accueil/contenu/index/page/decouverte/siGras/1"
			}
        }
    ]
}
```

### Outputs

#### Notebooks
Notebooks (Python or R) providing exploratory analysis of raw data

#### Data Catalog

- Feeding a Data Catalog with information about analyzed data stored in json files.

#### Selected datasets

- Selection of datasets to integrate in OGS platform
- Identification of potential transformation necessary for normalizing each data source

## Working with Github Project

We use Github Project to manage backlog. Every task is defined as an **issue**. Every issue is assigned to one contributor and belong to a milestone and a project.

We have 4 stages:
- Backlog: tasks that are identified but we do not know when we will work on
- To do: Task integrated for the current sprint
- In progress: Tasks with contributors working on
- Done: Finished tasks

When we commit changes and make pull request, we should specify the issue number in order to automatize issue stage management.

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
