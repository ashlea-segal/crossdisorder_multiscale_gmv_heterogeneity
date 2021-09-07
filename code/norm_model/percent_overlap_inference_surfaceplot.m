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
data_dir = '/scratch/kg98/Ashlea/parcellation_v2/models/bc_transform/ids/noTopImpact/inference/';

Nrois = 1032; 
groups = ["MDD","SCZ","ASD","ADHD","BIPOL","OCD"];
correction_method = 'FDR';
directions = [ "pos", "neg"];
grp_directions = ["PAT","HC"];
pthr = 0.025;
pthr_string = '25';

for d=1:length(directions)
    
    direction = char(directions(d));
    
    if strcmp(direction,'pos')
        colourmap_filename = [colourmap_dir, '/colourmap_blue_binary.txt'];
    else
        colourmap_filename = [colourmap_dir, '/colourmap_red_binary.txt'];
    end

    for c=1:length(grp_directions)
        
        grp_direction = char(grp_directions(c));


        for g=1:length(groups)

            group = char(groups(g));

            % c1 = PAT > HC, c2 = HC > PAT

            file_string = ['pvals_',correction_method,'_thr26_Nshuf10000_',grp_direction,'.txt'];
            data_corr = dlmread([data_dir,direction,'/',group,'/',file_string]);

            file_string = ['pvals_uncorr_thr26_Nshuf10000_',grp_direction,'.txt'];
            data_uncor = dlmread([data_dir,direction,'/',group,'/',file_string]);

            data = zeros(Nrois,1);
            data(data_uncor<pthr) = 1;
            data(data_corr<pthr) = 2;
            data = data(1:1000);

            thr = [1 3];

            file_string = ['pvals_',correction_method,'_thr26_Nshuf10000_',grp_direction,'_pthr',pthr_string];
            outfile_string = [data_dir,direction,'/',group,'/',file_string];

            % Run function to generate plot
            cd(codeDir);
            CreateSurfacePlot(codeDir,outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data,thr,colourmap_filename)

        end

    end
end