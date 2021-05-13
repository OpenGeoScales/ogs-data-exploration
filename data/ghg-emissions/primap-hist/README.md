# Data Provider Description

The Potsdam Institute for Climate Impact Research (PIK) is part of the Leibniz Association with 95 other German research institutes in science. The PIK focuses its researches on the climate impact to reach a global sustainability and to bring knowledge and solutions for a more manageable climate in the future. These researches are guided by the integration of the planetary bounderies and the global commons. They are cross-disciplinary and cover Earth System Analysis, Climate Resilience, Transformation Pathways and Complexity Science.

The PIK is funded by the national and regional governments and also external sources.

To spread knowledge, to make it available for all and to make progress the scientific research, the PIK is commited to the Open Science Declaration of the Leibniz Association. Therefore, its pieces of software, models and data are shared at [this preliminary list](http://www.pik-potsdam.de///~hellmann/all-types/). The available data are outputs of models, collected data and combined datasets.

# Dataset Description

The PIK provides the **PRIMAP-HIST dataset**, which combines several published datasets to create a comprehensive set of greenhouse gas emission pathways for every country and Kyoto gas covering the years 1850 to 2018, and all UNFCCC (United Nations Framework Convention on Climate Change) member states, as well as most non-UNFCCC territories.

## Dataset version

It is the 2.2 version used here for the exploration and it dates from January 2021.

## Data source

The data were directly downloaded at this **[link](https://zenodo.org/record/4479172)** or can be found at this **[repository](https://github.com/JGuetschow/PRIMAP-hist)**.

## Files

The PIK provided several files:
- *PRIMAP-hist_v2.2_19-Jan-2021.csv*: With numerical extrapolation of all time series to 2018.
- *PRIMAP-hist_no_extrapolation_v2.2_19-Jan-2021.csv*: Without numerical extrapolation of missing values and not including the country groups mentioned in the data description file.
- *PRIMAP-hist_v2.2_data-description.pdf*: Data description including changelog.
- *PRIMAP-hist_v2.2_updated_figures.pdf*: Updated figures from the PRIMAP-hist paper published in ESSD

The two last files are documentation files and they are placed in the doc folder.

To have the most available and complete data, we only used the *PRIMAP-hist_v2.2_19-Jan-2021.csv* file for the exploration. Indeed, this file contains no missing values thanks to the extrapolation.

Plus, the exploration generated two files:
- *PRIMAP-HISTCR.csv*: Contains only the data with the HISTCR scenario.
- *PRIMAP-HISTTP.csv*: Contains only the data with the HISTTP scenario.

## Fields

The fields are all the same for each csv file.

| Field | Description |
| ---- | ------------------- |
| scenario | Prioritisation made over the different datasource types. |
| country | ISO 3166 three-letter country codes or custom codes for groups. |
| category | IPCC (Intergovernmental Panel on Climate Change) 2006 categories for emissions. Some aggregate sectors have been added to the hierarchy. These begin with the prefix IPCM instead of IPC. |
| entity | Gas categories using global warming potentials (GWP) from either Second Assessment Report (SAR) or Fourth Assessment Report (AR4). |
| unit | Unit is either Gg or GgCO2eq (CO2-equivalent according to the global warming potential used). |
| remaining columns | Years from 1850-2018. |

The field values information and description can be found in the *PRIMAP-hist_v2.2_data-description.pdf* file.
