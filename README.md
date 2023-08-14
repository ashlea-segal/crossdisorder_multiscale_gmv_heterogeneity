# crossdisorder_multiscale_gmv_heterogeneity

Code and data to generate the figures in the manuscript "Regional, circuit, and network heterogeneity of brain abnormalities in psychiatric disorders"

The main analysis is divided into three sections
1) Heterogeneity at the level of brain regions
2) Heterogeneity at the level of functional circuits
3) Heterogeneity at the level of extended functional networks

## File descriptions

Directories: 
- `data_figures/`: folder containing the figure source data
- `functions/`: folder containing various utility analysis and visualisation functions

Code
1. `regional_circut_surfacePlots_cortical.m` generates the cortical surface plots for each disorder (% overlap and significant ROIs)
2. `regional_circut_surfacePlots_subcortical.py` generates the subcortical surface plots and combines it to the surface cortical plots for each disorder  (% overlap and significant ROIs)
3. `regional_circut_surfacePlots_allTogether.py` combines the surface plots for all disorders 
4. `regional_circuit_histogramPlots.py` generates the histograms showing the distribution of % overlap across brain regions for each disorder 
5. `network_plots.py` generates the figures showing significant networks 
