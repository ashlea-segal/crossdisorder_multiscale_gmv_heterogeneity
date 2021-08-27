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
data_dir = '/scratch/kg98/Ashlea/parcellation_v2/models/bc_transform/ids/noTopImpact/';

Nrois = 1032; 
groups = ["HC"]%"MDD","SCZ","ASD","ADHD","BIPOL","OCD"];
directions = ["pos","neg"];
overlap_thr = 5;
overlap_thr_string = '5';

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

        file_string = ['percent_overlap_',group,'_',direction,'.txt'];
        data = dlmread([data_dir,file_string]);
        data = data(1:1000);

        thr = [0 overlap_thr];

        outfile_string = [data_dir,'inference/',direction,'/',group,'/percent_overlap_',group,'_' ,direction, '_ovthr_',overlap_thr_string,'_cortical' ];   
        % Run function to generate plot
        cd(codeDir);
        CreateSurfacePlot(codeDir,outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data,thr,colourmap_filename)

    end

end 