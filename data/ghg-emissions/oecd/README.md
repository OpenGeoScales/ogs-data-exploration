
# Data Provider description

The OECD (Organisation for Economic Co-operation and Development) is an intergovernmental economic organisation with 37 member countries, founded in 1961 to stimulate economic progress and world trade.

OECD takes environmental data from UNFCCC's [National Inventory Submissions 2020](https://unfccc.int/process-and-meetings/transparency-and-reporting/greenhouse-gas-data/information-on-data-sources).

# Dataset description

## Data source

The raw data is obtained from [this portal](https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG).
After being processed (the process is shown in the corresponding notebook), the "oecd_processed.csv" file is obtained. This file contains emission data at country level by year and pollutant, giving information of various features.

## Fields

- **oecd_processed.csv**:

| Field | Description |
| ---- | ------------------- |
| id | Identifier of the country and the year |
| COU | Code of the country |
| YEAR | Year of the data |
| CH4__INDEX_1990 | Methane: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| CH4__INDEX_2000 | Methane: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| CH4__TOTAL | Methane: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| Co2__INDEX_1990 | Carbon dioxide 	: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| CO2__INDEX_2000 | Carbon dioxide 	: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| CO2__TOTAL | Carbon dioxide 	: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| GHG__AFOLU | Greenhouse gases: Agriculture, Forestry and Other Land Use (AFOLU) 	[Tonnes of CO2 equivalent] |
| GHG__AGR | Greenhouse gases: 3 - Agriculture 	[Tonnes of CO2 equivalent] |
| GHG__AGR_P | Greenhouse gases: 3 - Agriculture 	[Percentage] |
| GHG__ENER | Greenhouse gases: 1 - Energy 	[Tonnes of CO2 equivalent] |
| GHG__ENER_CO2 | Greenhouse gases: 1C - CO2 from Transport and Storage 	[Tonnes of CO2 equivalent] |
| GHG__ENER_CO2_P | Greenhouse gases: 1C - CO2 from Transport and Storage 	[Percentage] |
| GHG__ENER_FU | Greenhouse gases: 1B - Fugitive Emissions from Fuels 	[Tonnes of CO2 equivalent] |
| GHG__ENER_FU_P | Greenhouse gases: 1B - Fugitive Emissions from Fuels 	[Percentage] |
| GHG__ENER_IND | Greenhouse gases: 1A1 - Energy Industries 	[Tonnes of CO2 equivalent] |
| GHG__ENER_IND_P | Greenhouse gases:  1A1 - Energy Industries 	[Percentage]|
| GHG__ENER_MANUF | Greenhouse gases: 1A2 - Manufacturing industries and construction 	[Tonnes of CO2 equivalent] |
| GHG__ENER_MANUF_P | Greenhouse gases: 1A2 - Manufacturing industries and construction 	[Percentage] |
| GHG__ENER_OSECT | Greenhouse gases: 1A4 - Residential and other sectors 	[Tonnes of CO2 equivalent] |
| GHG__ENER_OSECT_P | Greenhouse gases: 1A4 - Residential and other sectors\t 	[Percentage] |
| GHG__ENER_OTH | Greenhouse gases: 1A5 - Energy - Other 	[Tonnes of CO2 equivalent] |
| GHG__ENER_OTH_P | Greenhouse gases: 1A5 - Energy - Other 	[Percentage] |
| GHG__ENER_P | Greenhouse gases: 1 - Energy [Percentage]|
| GHG__ENER_TRANS | Greenhouse gases: 1A3 - Transport 	[Tonnes of CO2 equivalent] |
| GHG__ENER_TRANS_P | Greenhouse gases: 1A3 - Transport 	[Percentage] |
| GHG__GHG_CAP | Greenhouse gases: Total GHG excl. LULUCF per capita 	[Kilograms per capita] |
| GHG__GHG_GDP | Greenhouse gases: Total GHG excl. LULUCF per unit of GDP 	[Kilograms per 1 000 US dollars] |
| GHG__INDEX_1990 | Greenhouse gases: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| GHG__INDEX_2000 | Greenhouse gases: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| GHG__IND_PROC | Greenhouse gases: 2- Industrial processes and product use 	[Tonnes of CO2 equivalent] |
| GHG__IND_PROC_P | Greenhouse gases: 2- Industrial processes and product use 	[Percentage] |
| GHG__LULUCF | Greenhouse gases: Land use, land-use change and forestry (LULUCF) 	[Tonnes of CO2 equivalent] |
| GHG__OTH | Greenhouse gases: 6 - Other 	[Tonnes of CO2 equivalent] |
| GHG__OTH_P | Greenhouse gases: 6 - Other 	[Percentage] |
| GHG__TOTAL | Greenhouse gases: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| GHG__TOTAL_LULU | Greenhouse gases: Total emissions including LULUCF 	[Tonnes of CO2 equivalent] |
| GHG__WAS | Greenhouse gases: 5 - Waste 	[Tonnes of CO2 equivalent] |
| GHG__WAS_P | Greenhouse gases: 5 - Waste 	[Percentage] |
| HFC__INDEX_1990 | Hydrofluorocarbons: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| HFC__INDEX_2000 | Hydrofluorocarbons: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| HFC__TOTAL | Hydrofluorocarbons: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| HFC_PFC__INDEX_1990 | Unspecified mix of HFCs and PFCs: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| HFC_PFC__INDEX_2000 | Unspecified mix of HFCs and PFCs: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| HFC_PFC__TOTAL | Unspecified mix of HFCs and PFCs: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| N2O__INDEX_1990 | Nitrous oxide: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| N2O__INDEX_2000 | Nitrous oxide: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| N2O__TOTAL | Nitrous oxide: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| NF3__INDEX_1990 | Nitrogen trifluoride: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| NF3__INDEX_2000 | Nitrogen trifluoride: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| NF3__TOTAL | Nitrogen trifluoride: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| PFC__INDEX_1990 | Perfluorocarbons: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| PFC__INDEX_2000 | Perfluorocarbons: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| PFC__TOTAL | Perfluorocarbons: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |
| SF6__INDEX_1990 | Sulphur hexafluoride: Total GHG excl. LULUCF, Index 1990=100 	[Index] |
| SF6__INDEX_2000 | Sulphur hexafluoride: Total GHG excl. LULUCF, Index 2000=100 	[Index] |
| SF6__TOTAL | Sulphur hexafluoride: Total emissions excluding LULUCF 	[Tonnes of CO2 equivalent] |