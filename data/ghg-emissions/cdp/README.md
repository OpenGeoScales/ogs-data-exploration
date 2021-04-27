# Documentation of CDP dataset

## Data provider description


CDP is a not-for-profit charity that runs the global disclosure system for investors, companies, cities, states and regions to manage their environmental impacts. The world’s economy looks to CDP as the gold standard of environmental reporting with the richest and most comprehensive dataset on corporate and city action.

CDP provides with a dataset of city/region/country emissions reported yearly by government. We can access every year's dataset (2020 and before).

They provide also with 'corporate data', 'data for investors' and a yearly scores for compagnies/cities but these three datasets are not on free access.

## Dataset description

The data is composed of 3 datasets according to the year of the report (2018, 2019 or 2020).
They can be either downloaded or accessed via API from [this portal](https://data.cdp.net/)


## Fields description

| Field | Description |
|-------|-------------|
| Index | colonne que j'ai ajoutée qui représente l'index de la ligne dans le dataset original (avant de concatener) |
|| Year Reported to CDP | année du rapport |
| Account Number | id de la ligne dans le dataset |
| Organization | entité en charge de la mesure |
| City | ville concernée |
| Country | pays concerné |
| CDP Region | zone géographique (north america, europe , ...) |
| Reporting Authority | ⚠️ présent uniquement pour 2018-2019. authorité responsable (plusieurs valeurs) |
| Access | vaut toujours 'public' |
| City-wide emissions inventory | est-ce que la ville a déja produit ses émissions de GHG ? (oui, en cours, ne compte pas le faire) |
| Accounting year | date de début et de fin de la période mesurée |
| Administrative city boundary | ⚠️ présent uniquement pour 2020. type d'administration (city, city-state, province ...) |
| Inventory boundary (compared to Administrative city boundary) | zone du bilan comparée à la zone administrative |
| Primary Protocol | Protocole utilisé (GPC, ICLEI, ou autres) |
| Primary Protocol Comment | commentaires |
| Common Reporting Framework inventory format (GPC) | correspond ou pas au Common Reporting Format [see documentation](https://www.ghgprotocol.org/sites/default/files/ghgp/standards/GHGP_GPC_0.pdf) |
| Gases Included | gas inclus |
| Direct emissions (metric tonnes CO2e) for Total generation of grid-supplied energy |  |
| Direct emissions (metric tonnes CO2e) for Total emissions (excluding generation of grid-supplied energy) |  |
| Indirect emissions from use of grid supplied energy (metric tonnes CO2e) for Total generation of grid supplied energy |  |
| Indirect emissions from use of grid supplied energy (metric tonnes CO2e) for Total Emissions (excluding generation of grid-supplied energy) |  |
| Emissions occurring outside city boundary (metric tonnes CO2e) for Total Generation of grid supplied energy |  |
| Emissions occurring outside city boundary (metric tonnes CO2e) for Total Emissions (excluding generation of grid-supplied energy) |  |
| TOTAL Scope 1 Emissions (metric tonnes CO2e) |  |
| TOTAL Scope 2 emissions (metric tonnes CO2e) |  |
| TOTAL Scope 3 Emissions |  |
| TOTAL BASIC Emissions (GPC) |  |
| TOTAL BASIC+ Emissions (GPC) |  |
| Change in emissions | changements par rapport au dernière bilan (il y a un bilan/dataset par an) |
| Primary reason for the change in emissions | raisons de ce changement |
| Land area (in square km) | surface de la zone en km2 |
| Population | population |
| Population Year | année de la mesure de population |
| City Location | coordonnées de la ville |
| Last update | dernière mise à jour (tous à la même date, celle de création du dataset soit 2021-04-10) |


