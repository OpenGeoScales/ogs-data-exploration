
# Data Provider description

The OECD (Organisation for Economic Co-operation and Development) is an intergovernmental economic organisation with 37 member countries, founded in 1961 to stimulate economic progress and world trade.

OECD takes environmental data from UNFCCC's [National Inventory Submissions 2020](https://unfccc.int/process-and-meetings/transparency-and-reporting/greenhouse-gas-data/information-on-data-sources).

# Dataset description

## Data source

The raw data is obtained from [this portal](https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG).
After being processed (the process is shown in the corresponding notebook), the "oecd_processed.csv" file is obtained. This file contains emission data at country level by year and pollutant, giving information of various features.

## Fileds

- **assessments.csv**:

| Field | Description |
| ---- | ------------------- |
| id | identifier of the country and the year |
| COU | code of the country |
| year | year of the data |
| GHG__AFOLU | Greenhouse gases:  |
| GHG__AGR | Greenhouse gases:  |
| GHG__AGR_P | Greenhouse gases:  |
| GHG__ENER | Greenhouse gases:  |
| GHG__ENER_CO2 | Greenhouse gases:  |
| GHG__ENER_CO2_P | Greenhouse gases:  |
| GHG__ENER_FU | Greenhouse gases:  |
| GHG__ENER_FU_P | Greenhouse gases:  |
| GHG__ENER_IND | Greenhouse gases:  |
| GHG__ENER_IND_P | Greenhouse gases:  |
| GHG__ENER_MANUF | Greenhouse gases:  |
| GHG__ENER_MANUF_P | Greenhouse gases:  |
| GHG__ENER_OSECT | Greenhouse gases:  |
| GHG__ENER_OSECT_P | Greenhouse gases:  |
| GHG__ENER_OTH | Greenhouse gases:  |
| GHG__ENER_OTH_P | Greenhouse gases:  |
| GHG__ENER_P | Greenhouse gases:  |
| GHG__ENER_TRANS | Greenhouse gases:  |
| GHG__ENER_TRANS_P | Greenhouse gases:  |
| GHG__GHG_CAP | Greenhouse gases:  |
| GHG__GHG_GDP | Greenhouse gases:  |
| GHG__INDEX_1990 | Greenhouse gases:  |
| GHG__INDEX_2000 | Greenhouse gases:  |
| GHG__IND_PROC | Greenhouse gases:  |
| GHG__IND_PROC_P | Greenhouse gases:  |
| GHG__LULUCF | Greenhouse gases:  |
| GHG__OTH | Greenhouse gases:  |
| GHG__OTH_P | Greenhouse gases:  |
| GHG__TOTAL | Greenhouse gases:  |
| GHG__TOTAL_LULU | Greenhouse gases:  |
| GHG__WAS | Greenhouse gases:  |
| GHG__WAS_P | Greenhouse gases:  |



['COU', 'Year', 'CH4__TOTAL', 'CH4__INDEX_2000', 'CH4__INDEX_1990',
       'CO2__TOTAL', 'CO2__INDEX_2000', 'CO2__INDEX_1990', 'GHG__TOTAL',
       'GHG__INDEX_1990', 'GHG__GHG_CAP', 'GHG__WAS', 'GHG__IND_PROC',
       'GHG__ENER', 'GHG__AGR', 'GHG__OTH', 'GHG__GHG_GDP', 'GHG__ENER_IND',
       'GHG__LULUCF', 'GHG__ENER_OSECT', 'GHG__ENER_OTH', 'GHG__ENER_FU',
       'GHG__ENER_MANUF', 'GHG__ENER_TRANS', 'GHG__TOTAL_LULU',
       'GHG__INDEX_2000', 'GHG__ENER_CO2', 'GHG__AFOLU', 'GHG__ENER_IND_P',
       'GHG__ENER_OTH_P', 'GHG__AGR_P', 'GHG__ENER_P', 'GHG__ENER_MANUF_P',
       'GHG__ENER_OSECT_P', 'GHG__WAS_P', 'GHG__IND_PROC_P',
       'GHG__ENER_TRANS_P', 'GHG__ENER_FU_P', 'GHG__OTH_P', 'GHG__ENER_CO2_P',
       'HFC__TOTAL', 'HFC__INDEX_2000', 'HFC__INDEX_1990', 'HFC_PFC__TOTAL',
       'HFC_PFC__INDEX_2000', 'HFC_PFC__INDEX_1990', 'N2O__TOTAL',
       'N2O__INDEX_2000', 'N2O__INDEX_1990', 'NF3__TOTAL', 'NF3__INDEX_2000',
       'NF3__INDEX_1990', 'PFC__TOTAL', 'PFC__INDEX_2000', 'PFC__INDEX_1990',
       'SF6__TOTAL', 'SF6__INDEX_2000', 'SF6__INDEX_1990'],