% add relevant paths 
addpath('/project_cephfs/3022017.02/projects/ashseg/toolboxes/cbrewer/cbrewer/');
addpath('/project_cephfs/3022017.02/projects/ashseg/deviation_network_mapping/code/functions');

codeDir = '/project_cephfs/3022017.02/projects/ashseg/toolboxes/plotSurfaceROIBoundary-master';
addpath(codeDir);

% Annot files which tells the function where each ROI is on the brain
atlas_annot_filename_lh = '/project_cephfs/3022017.02/projects/ashseg/atlases/lh_Schaefer2018_1000Parcels_7Networks_order_annot.txt';
atlas_annot_filename_rh = '/project_cephfs/3022017.02/projects/ashseg/atlases/rh_Schaefer2018_1000Parcels_7Networks_order_annot.txt';


% colourmap dir
colourmap_dir = '/project_cephfs/3022017.02/projects/ashseg/deviation_network_mapping/code/cmaps';

% Data directoy where PALM case-control results are saved.
% Directory contains subdirectories for each disorder. 
data_dir = '/project_cephfs/3022017.02/projects/ashseg/models/bc_transform/ids/inference/';

Nrois = 1032; 
groups = ["HC","MDD","SCZ","ASD","ADHD","BIPOL","OCD"];
directions = ["pos","neg"];
overlap_thr = 0.065;
overlap_thr_string = '065';

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

        file_string = 'thr_weight_overlap.txt';   
        data = dlmread([data_dir,direction,'/',group,'/',file_string]);
        data = data(1:1000);

        thr = [0 overlap_thr];

        outfile_string = [data_dir,'inference/',direction,'/',group,'/thr_weight_overlap_',group,'_' ,direction, '_ovthr_',overlap_thr_string,'_cortical' ];   
        % Run function to generate plot
        cd(codeDir);
        CreateSurfacePlot(codeDir,outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data,thr,colourmap_filename)

    end

end 