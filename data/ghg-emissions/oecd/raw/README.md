
# Data Provider description

The OECD (Organisation for Economic Co-operation and Development) is an intergovernmental economic organisation with 37 member countries, founded in 1961 to stimulate economic progress and world trade.

OECD takes environmental data from UNFCCC's [National Inventory Submissions 2020](https://unfccc.int/process-and-meetings/transparency-and-reporting/greenhouse-gas-data/information-on-data-sources).

# Dataset description

## Data source

The raw data is obtained from [this portal](https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG).
After being processed (the process is shown in the corresponding notebook), the "oecd_processed.csv" file is obtained. This file contains emission data at country level by year and pollutant, giving information of various features.

## Fields

- **AIR_GHG_07042021221914030.csv**:

| Field | Description |
| ---- | ------------------- |
| COU | Identifying code of the country |
| Country | Name of the country |
| POL | Identifying code of the pollutant |
| Pollutant | Name of the pollutant |
| VAR | Identifying code of the variable |
| Variable | Name of the variable |
| YEA | Identifying code of the year |
| Year | Name of the year |
| Unit Code | Identifying code of the unit |
| Unit | Name of the unit |
| PowerCode Code | Identifying code of the powercode |
| PowerCode | Power of 10 by which the reported statistics should be multiplied |
| Reference Period Code | Identifying code of the reference period |
| Reference Period | Length of time, for which data are collected |
| Value | Value of the variable |
| Flag Codes | Identifying code of the flag |
| Flags | Attribute of a cell representing qualitative information on the value of that cell |
