
# Data Provider description

ADEME is a public Environment and Energy Management Agency in France. ADEME is active in the implementation of public policy in the areas of the environment, energy and sustainable development. ADEME makes its expertise and consultancy capacities available to companies, local authorities, public authorities and the general public and helps finance projects in five areas (waste management, soil conservation, efficiency energy and renewable energies, air quality and noise reduction) and to progress in their sustainable development initiatives.

To meet regulatory obligations and support the energy and ecological transition, ADEME has decided to make its data available to businesses, local authorities, public authorities and the general public in order to enable them to progress in their environmental approach by the mean of [an open data portal](https://data.ademe.fr/).

- **Bilan Carbone**

Bilan Carbone® refers to the methods developed by ADEME and Association Bilan Carbone (ABC) to enable organizations and local government authorities (respectively Bilan Carbone® and Bilan Carbone® Territoire) to address, measure and reduce their greenhouse gas emissions. These inventories are published on the [ADEME GES platform](https://www.bilans-ges.ademe.fr/). ADEME publishes the GHG reports entered by organizations via [a search engine](https://www.bilans-ges.ademe.fr/fr/bilanenligne/bilans/index/siGras/0) on its site, but does not publish the consolidated underlying database of all the reports. It is therefore possible to view each report one by one, but not to perform automated processing on this data. 

- **Base Carbone**

The Base Carbone® is a public database of emission factors, necessary for carrying out a greenhouse gas (GHG) emissions assessment and more generally any carbon accounting exercise. A complete documentation of the Base Carbone is provided [here](https://www.bilans-ges.ademe.fr/fr/accueil/contenu/index/page/presentation/siGras/0). The data in the Base Carbone ® can be viewed free of charge by everyone and can be downloaded through [this page](https://www.bilans-ges.ademe.fr/en/accueil/contenu/index/page/downloaddata/siGras/0).

# Dataset description

## Data source

The data is obtained from [this portal](https://www.data.gouv.fr/fr/datasets/bilans-demissions-de-ges-publies-sur-le-site-de-lademe-1/)
The emission.csv file contain emission data at city and company levels based on carbon inventory.

## Fileds

- **assessments.csv**:

| Field | Description |
| ---- | ------------------- |
| id | identifiant numérique du bilan |
| organization_name | nom de l'organisation concernée |
| organization_description | description libre de l'organisation |
| organization_type | type d'organisation |
| collectivity_type | type de collectivité (pour les collectivités territoriales), |
| staff | effectifs, nombre d'agents ou de salariés de l'organisation |
| population  | population de la collectivité (pour les collectivités territoriales) |
| consolidation_method | mode de consolidation du bilan |
| reporting_year | année sur laquelle porte le bilan |
| total_scope_1 | émissions totales (en tonnes équivalent CO2), relatives au Scope 1 (à l'exclusion du CO2 d'origine biogénique), dont le calcul est obligatoire |
| total_scope_2 | émissions totales (en tonnes équivalent CO2), relatives au Scope 2 (à l'exclusion du CO2 d'origine biogénique), dont le calcul est obligatoire |
| total_scope_3 | émissions totales (en tonnes équivalent CO2), relatives au Scope 3 (à l'exclusion du CO2 d'origine biogénique), dont le calcul est facultatif |
| reference_year | année du bilan de référence |
| action_plan | Oui ou Non selon qu'un plan d'action a été saisi en accompagnement du bilan ou pas |
| reductions_scope_1_2 | réduction des émissions (en tonnes équivalent CO2) envisagées d'ici le prochain bilan, pour la somme indifférenciée du Scope 1 et du Scope 2 |
| reductions_scope_1 | réduction des émissions (en tonnes équivalent CO2) envisagées d'ici le prochain bilan, pour le Scope 1 |
| reductions_scope_2 | réduction des émissions (en tonnes équivalent CO2) envisagées d'ici le prochain bilan, pour le Scope 2 |
| reductions_scope_3 | réduction des émissions (en tonnes équivalent CO2) envisagées d'ici le prochain bilan, pour le Scope 3 |
| is_draft |  indique si le bilan est encore en "mode brouillon" sur le site de l'ADEME, ou si l'organisation a effectivement cliqué sur "Publier" pour le rendre accessible via le moteur de recherche (seuls ces bilans sont publiés ici, bien que les autres soient accessibles en ligne) |
| source_url | URL à laquelle est publié le bilan officiel sur le site de l'autorité |