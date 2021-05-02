This readme file sums up information available on the JRC's official description of the GHS Urban Centre Database 2015 (see PDF file) and on the [organisation website](https://ghsl.jrc.ec.europa.eu/). It was not written by a JRC member.
Additial information written by the author are written in *italics*.
# UCDB : origins

There is no such thing as a worldwide consistant definition of a city.
The criteria used to identify urban areas vary from country to country 
and may not be consistent even between different data sources within a given country.

Many countries use a threshold of 5,000 ihabitants or less, but in some countries,
the threshold can be 10 to 20 times higher.

To address this issue, the European Union, the Organisation for Economic Cooperation 
and Development (OECD) and the World Bank launched a voluntary commitment to 
develop a global, people-based definition of cities and settlements in October 2016.

# Urban Centers Criteras

The UC (Urban Centers, i.e "cities") as implemented in the current GHSL settlement model (SMOD) formulation is defined as: 
“the spatially-generalized high-density clusters of contiguous grid cells of 1 km2 with a 
density of at least 1,500 inhabitants per km2 of land surface or at least 50% built -up 
surface share per km2 of land surface, and a minimum population of 50,000.”

# UCDB's genral charasteristics

## Quality control

The quality control code is the result of the quality check procedure performed over the 
full dataset of Urban Centres, which relays on visual assessment. The assessment was 
performed in two steps: automatic and manual.

Each Urban Centre was visually validated using a VHR map 
(Google Maps1 6 or Bing Maps1 7), and assessed as true positive if within the polygon of the 
Urban Centre a high density settlement is present

- True positives: there is a high density settlement present;
- False positive: there is no presence of a high density settlement;
- Uncertainty: the expert was not sure or there was disagreement between 
experts.

The attributes related to control codes are:
- **ID_HDC_G0**: unique ID of the Urban Centre
- **QA2_1V**: quality code (0 – false positive, 1 – true positive, >1 uncertain).

## Extension (EPSG:4326)

- **BBX_LATMN** : latitude of the low left corner of the bounding box;
- **BBX_LONMN** : longitude of the low left corner of the bounding box;
- **BBX_LATMX** : latitude of the top right corner of the bounding box;
- **BBX_LONMX** : longitude of the top right corner of the bounding box.

## Location (EPSG:4326)

- **GCPNT_LAT**: Latitude of the geometric centroid;
- **GCPNT_LON**: Longitude of the geometric centroid;
- **XBRDR**: cross border (the value 1 indicates if it is a cross border Urban Centre, 
while value 0 is assigned to Urban Centres which whole polygon lays within 
borders of only one country);
- **XCTR_NBR**: number of the countries with which the Urban Centre polygon 
crosses;
- **XC_ISO_LST**: list of ISO-3 codes of the countries with which the Urban Centre
polygon crosses (separation char: ‘;’);
- **CTR_MN_ISO**: the ISO 3 code of the main country, i.e., the country within which 
borders the majority of the area of the Urban Centre is located;
- **CTR_MN_NM**: the name of the main country, i.e., the country within which 
borders the majority of the area of the Urban Centre is located; 
- **GRGN_L1**: Major Geographical Region (UNDESA, 2018b), according to the 
classification of the main country;
- **GRGN_L2**: Geographical Region (UNDESA, 2018b), according to the classification 
of the main country.

*## Geometry (EPSG:4326)

- **geometry** : The UC represented as a polygon*

## Names

The name(s) assigned to the Urban Centres are calculated using available open source 
placename databases.

**These names shall be used only for visualisation purpose and shall not be understand as an official position of EC in any case**.

This means that when there are cities whose naming is subject to international or cultural dispute, then one name is chosen over the other,
however this does not mean the JRC nor the EU officially endorces this name.

When a UC is made of mutiple cities (ex : Paris and Boulogne-Billancourt, Saint-Denis, and Montreuil ; Dakar and Guédiawaye, Parcelles Assainies, Rufisque, Pikine),
then they are all listed between bracets, ordered by population.

- **UC_NM_MN**: the main name of the Urban Centre (the country ISO 3 is declared 
within ‘[]’, to support the cross border entities);
- **UC_NM_LST**: full list of assigned names of the Urban Centre;
- **UC_NM_SRC**: source of the list of names per each country (WUP, GRUMP, NE, 
GN, WM – online mapping services, OTHER – web user feedback and other 
manual revisions). 

***Not every UC name is in latin character (ex: 威宁县; رودبار; 청하역; আলীখালী; Весенний)***

***You should know that there are many possible ways to romanized (i.e write in latin alphabet) a non-latin culture's city name (ex for japanese : Hepburn, Nihon-Shiki, Kunrei-shiki).
The romanization method is NOT indicated in the USBD. Keep this in mind when using names as an merging index***

