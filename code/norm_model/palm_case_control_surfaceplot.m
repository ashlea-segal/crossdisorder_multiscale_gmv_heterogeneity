% add relevant paths 
addpath ('/usr/local/freesurfer/6.0/matlab');
addpath('/scratch/kg98/Ashlea/deviation_network_mapping/code/functions');

codeDir = '~/kg98/Ashlea/code/plotSurfaceROIBoundary-master';
addpath(codeDir);

% Annot files which tells the function where each ROI is on the brain
atlas_annot_filename_lh = '/scratch/kg98/Ashlea/parcellation_v2/atlases/lh_Schaefer2018_1000Parcels_7Networks_order_annot.txt';    
atlas_annot_filename_rh = '/scratch/kg98/Ashlea/parcellation_v2/atlases/rh_Schaefer2018_1000Parcels_7Networks_order_annot.txt'; 

% colourmap dir
colourmap_dir = '/scratch/kg98/Ashlea/deviation_network_mapping/code/cmaps';

% Data directoy where PALM case-control results are saved.
% Directory contains subdirectories for each disorder. 
data_dir = '/scratch/kg98/Ashlea/parcellation_v2/models/bc_transform/ids/case_control/';


groups = ["MDD","SCZ","ASD","ADHD","BIPOL","OCD"];
correction_method = 'cfwe';
pthr = 0.025;
pthr_string = '25';

for g=1:length(groups)

    group = char(groups(g));

    % c1 = PAT > HC, c2 = HC > PAT
    file_string = ['palm_dat_tstat_',correction_method,'p_c1.csv'];
    data_corr_c1 = dlmread([data_dir,group,'/',file_string]);

    file_string = ['palm_dat_tstat_uncp_c1.csv'];
    data_uncor_c1 = dlmread([data_dir,group,'/',file_string]);

    file_string = ['palm_dat_tstat_',correction_method,'p_c2.csv'];
    data_corr_c2 = dlmread([data_dir,group,'/',file_string]);

    file_string = ['palm_dat_tstat_uncp_c2.csv'];
    data_uncor_c2 = dlmread([data_dir,group,'/',file_string]);

    data = zeros(Nrois,1);
    data(data_uncor_c1<pthr) = 1;
    data(data_corr_c1<pthr) = 2;
    data(data_uncor_c2<pthr) = -1;
    data(data_corr_c2<pthr) = -2;
    data = data(1:1000);

    thr = [-3 4];

    file_string = ['palm_dat_tstat_',correction_method,'p_pthr',pthr_string];
    outfile_string = [data_dir,group,'/',file_string];
    colourmap_filename = [colourmap_dir, '/colourmap_RdBu_binary.txt'];

    % Run function to generate plot
    cd(codeDir);
    CreateSurfacePlot(codeDir,outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data,thr,colourmap_filename)
    
end

