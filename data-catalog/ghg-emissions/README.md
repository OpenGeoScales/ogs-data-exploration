
The objective of the data catalog consists of referencing multiple GHG data sources attributes and metadata in order to compare them easily.

Every data source folder should contain a json file *(data source name-desc.json)* describing its attributes as specified in the table below.

The data-catalog.json file combines the different data sources description in one file.

| Field | Type | Description | 
| --- | ---- | ------------------ |
| DataSourceStorageName | String | The name used in github for storing data and related notebooks |
| Topics |  List | List of topics refered by data source. For examples: ghg emissions, socio-economic... |
| DataProvider.DataProviderName | String | The name of the organism providing access to the used data. The data provider doesn't correspond necessarly to the organism collecting data. |
| DataProvider.DataProviderLink| String | Link to the website used for downloading the data. |
| DataProvider.DataProviderDesc | String | A short description of data provider. |
| DataSource.DataSourceName | String | The official name of data source.  |
| DataSource.DataSourceLink | String | Link to the official website of data source. |
| DataSource.Organism | String | The name of the official organism collecting the data. |
| DataSource.DataSourceDesc | String |Short description of the data source.  |
| DataSource.DataFormat| Enum  | The format of downloaded data: `csv`, `json`, `xls`, `geojson`... |
| DataSource.DataAccess | Enum | used method for getting data: `download`, `api`, `ftp` |
| Coverage.SpatialCoverage.MainCoverage | String | The main spatial coverage of the datasource. For example: `World`, `Europe`, `France`... |
| Coverage.SpatialCoverage.NumberOfSpatialEntities| numeric | The number of spatial entities covered by data (number of countries, number of regions...) |
| Coverage.SpatialCoverage.ListOfSpatialEntities| List  | The list of spatial entities' names  |
| Coverage.TemporalCoverage.MinDate | Date | Date of the first recording |
| Coverage.TemporalCoverage.MaxDate | Date | Date of the lst recording |
| Resolution.SpatialResolution | List | List of spatial resolutions convered by the data (dataset may contains multiuple spatial resolutions): `country`, `municipality`, `region`, `grid 1km-1km`  |
| Resolution.TemporalResolution | String  | Temporal resolution of data recording: `year`, `month`... |
| Gases.Included | List | List of gases considered in the datasets: `all ghg gases`, `co2`,`nh4`...   |
| Gases.FilterByGase| Boolean | Indicate if we can filter data by a specific gas  | 
| Scopes.Included | List  | List of considered scopes: `scope 1`, `scope 2`, `scope 3` |
| Scopes.FilterByScope | Boolean | Indicate if we can filter data by a specific scope|
| Sectors.Included | List  |List of considered sectors (e.g. `cement`,`coal`, `flaring`, `gas`, `oil`, `other industries`...)|
| Sectors.FilterBySector| Boolean | Indicate if we can filter data by a specific sector|
| Protocol.ProtocolName | String | GHG emissions inventories are based on specific protocols defining emissions estimations methods. We indicate here the name of the used protocol for the considered dataset. (e.g. `UNFCCC`, `Base carbone`...) |
| Protocol.ProtocolLink | String | Link to wiki page providing description of used protocol |
| EstimationMethod.MethodType | Enum | Indicating whether data is collected based on `Bottom-up` estimation (inventories) or `Top-down` estimation method (`simulation`, `satellite imagery`...)  |
| EstimationMethod.MethodDescription | String | Link to wiki page providing description of estimation method |