

Data provider | Description | Geoscale | Data sources | Access |
---|---------|---|---| ---| 
Technical Reference for Air Pollution and Climate Change (CITEPA) | Citepa officially estimates greenhouse gas and air polluant emissions each year on behalf of the French Ministry of the Environment. | `Country scale`<br /> `City scale`| `Citepa` | [Get data](https://www.citepa.org/fr/telechargements/) |

# CITEPA description

Created in 1961, [CITEPA (Technical Reference for Air Pollution and Climate Change)](https://www.citepa.org/en/about/) quantifies, identifies, expertises and reports atmospheric emissions data, explanatory variables and efficiency indicators, as well as methods for monitoring, quantifying, projecting and modeling emissions, policies and measures of mitigation and adaptation.

As a non-profit organisation and State operator for the French Environment Ministry, the Citepa meets reporting requirements for air pollutants and greenhouse gas emissions from France in different inventory formats, such as UNFCCC, EMEP, and Kyoto Protocol.


**National inventory data**

Citepa officially estimates greenhouse gas and air polluant emissions each year on behalf of the Ministry of the Environment. his inventory is carried out as part of France’s international commitments, mainly under the United Nations Framework Convention on Climate Change (as well as the Kyoto Protocol and the Paris Agreement) for greenhouse gases, and the United Nations Economic Commission for Europe for pollutants (LRTAP Convention).

All produced data and official reports can be download [from this page](https://www.citepa.org/fr/telechargements/).

**IGT (Inventaire GES territorialisé)**

The Ministry in charge of the Environment has entrusted the Interprofessional Technical Center for Atmospheric Pollution Studies (CITEPA) with a mission of “territorialization” or a “spatialization” of the national GHG inventory. The spatial resolution is the municipality level, and then aggeregated by EPCI. It is established from botha breakdown of national GHG emissions at municipal level and already spatialized information and can be downloaded through:

- [ADEME Open Data Portal](https://data.ademe.fr/datasets/igt-pouvoir-de-rechauffement-global)
- [Datagouv Open Data Portal](https://www.data.gouv.fr/fr/datasets/inventaire-de-gaz-a-effet-de-serre-territorialise/)



Inventory file for GHG by municipality in 2016 (35797 municipalities)

The file contain quantity of GHG in Teq CO2 (Ton CO2 equivalent) with the six main gas (CO2, CH4, N2O, CFC, HFC, SF6) taken into account by the kyoto potocol.
(farming, others transports, international others transports, CO2 biomass out of total, wastes, energy, non-energy industry, Residential, Road, Tertiary)


fields: 
INSEE commune => municipality code (uri-reference) 
Commune ==> municipality name (string)

Tous les champs suivant sont des secteurs stockant la quantité de GES en Teq CO2 (number):
All the followings fields are sectors with quantity of GHG in Teq CO2 (number):

farming
others transports
international others transports
CO2 biomass out of total
wastes
energy
non-energy industry
Residential
Road
Tertiary
lat (number) => geographical coordinate that allow to locate depending equator
lon (number) => geographical coordinate that allow to locate depending Greenwich meridian
