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
groups = ["MDD","SCZ","ASD","ADHD","BIPOL","OCD"];
directions = ["pos","neg"];
parcel_thresholds = ["50","75"];
pthr = 0.025;
pthr_string = '25';
correction_method = 'FDR'
grp_directions = ["PAT","HC"];


for c=1:length(grp_directions)
    
    grp_direction = char(grp_directions(c));

    for p=1:length(parcel_thresholds)

        parcel_thr = char(parcel_thresholds(p));

        for d=1:length(directions)

            direction = char(directions(d));

            if strcmp(direction,'pos')
                colourmap_filename = [colourmap_dir, '/colourmap_blue_binary.txt'];
            else
                colourmap_filename = [colourmap_dir, '/colourmap_red_binary.txt'];
            end

            for g=1:length(groups)

                group = char(groups(g));

                file_string = ['pvals_',correction_method,'_tfce_tstat_cfwep_c1_thr_parc',parcel_thr,'_bin_TRANSPOSE_union_Nspin10000_',grp_direction,'.txt'];
                data_corr = dlmread([data_dir,'parc',parcel_thr,'/',direction,'/',group,'/',file_string]);
                file_string = ['pvals_uncorr_tfce_tstat_cfwep_c1_thr_parc',parcel_thr,'_bin_TRANSPOSE_union_Nspin10000_',grp_direction,'.txt'];
                data_uncor = dlmread([data_dir,'parc',parcel_thr,'/',direction,'/',group,'/',file_string]);

                data = zeros(Nrois,1);
                data(data_uncor<pthr) = 1;
                data(data_corr<pthr) = 2;
                data = data(1:1000);

                thr = [1 3];            

                file_string = ['pvals_',correction_method,'_thr26_Nshuf10000_',grp_direction,'_pthr',pthr_string,'_cortical'];
                outfile_string = [data_dir,'parc',parcel_thr,'/',direction,'/',group,'/',file_string ]; 

                % Run function to generate plot
                cd(codeDir);
                CreateSurfacePlot(codeDir,outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data,thr,colourmap_filename)

            end

        end 

    end 
end
