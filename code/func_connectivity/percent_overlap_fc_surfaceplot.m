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
data_dir = '/scratch/kg98/Ashlea/lesion_networks/data/Level3_Analysis/meants_indivDeviations_union_spinTests/rfMRI_REST1_LR/withSubcortical/'

Nrois = 1032; 
groups = ["HC","MDD","SCZ","ASD","ADHD","BIPOL","OCD"];
directions = ["pos","neg"];
parcel_thresholds = ["50","75"];
overlap_thr = 50;
overlap_thr_string = '50';


for p=1:length(parcel_thresholds)
    
    parcel_thr = char(parcel_thresholds(p));
    
    for d=1:length(directions)

        direction = char(directions(d));

        % Colourmap 
        if strcmp(direction,'neg')
            colourmap_filename = [colourmap_dir, '/colourmap_red_gradient.txt'];
        else
            colourmap_filename = [colourmap_dir, '/colourmap_blue_gradient.txt'];
        end 

        for g=1:length(groups)

            group = char(groups(g));

            file_string = [data_dir,'parc',parcel_thr,'/',direction,'/',group,'/observed_overlap_tfce_tstat_cfwep_c1_thr_parc',parcel_thr,'_bin_TRANSPOSE_union_Nspin10000.txt'];

            data = dlmread([file_string]);
            data = data(1:1000);

            thr = [0 overlap_thr];

            outfile_string = [data_dir,'parc',parcel_thr,'/',direction,'/',group,'/observed_overlap_tfce_tstat_cfwep_c1_thr_parc',parcel_thr,'_bin_TRANSPOSE_union_Nspin10000_ovthr_',overlap_thr_string,'_cortical' ];   
            % Run function to generate plot
            cd(codeDir);
            CreateSurfacePlot(codeDir,outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data,thr,colourmap_filename)

        end

    end 
    
end 