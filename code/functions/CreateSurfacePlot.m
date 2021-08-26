function CreateSurfacePlot(codeDir,outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data,thr,colourmap_filename)

% Data to plot
%data = load(data_filename);
%data = data(1:1000);
%data = 1 - data
%data_all = load(data_filename,'delimiter',' ');
%data = data_all(1,:);
%data(data<0) = 0; 
%thr = [-2.9 3];
%thr= [1 str2double(thr)];
%thr= [0 2];

%colors = cbrewer('div', 'RdBu', 256);
%%
addpath ('/usr/local/freesurfer/6.0/matlab');
addpath(codeDir);

% Load Stu's Template
load([codeDir,'/fsaverage_surface_data.mat'])
%,'lh_inflated_verts','lh_verts','lh_faces','lh_HCPMMP1','lh_aparc','lh_rand200','lh_sulc')

if exist('colourmap_filename','var')
     % third parameter does not exist, so default it to something
      colors = load(colourmap_filename);
      colors = colors(:,1:3);
end


%%
t = tiledlayout(1,4,'Padding','tight');
t.TileSpacing = 'none';

for h=1:2
    
    if h==1
        hemisphere = 'lh';
        atlas_annot = load(atlas_annot_filename_lh);
        surface.vertices = lh_inflated_verts;
        surface.faces = lh_faces;
        data_tmp = data(1:500); % cortical data only
    elseif h==2
        hemisphere = 'rh';
        atlas_annot = load(atlas_annot_filename_rh);
        surface.vertices = rh_inflated_verts;
        surface.faces = rh_faces;
        data_tmp = data(501:1000); % cortical data only
    end
    
    data_tmp(data_tmp==0) = NaN;
    
    for v=1:2
        nexttile([1 1])       
        % This just plots the ROI ID number for each ROI
        
        [fig] = plotSurfaceROIBoundary(surface,atlas_annot,data_tmp,'midpoint',colors,1,.5,thr);
        
        % The following options set up the patch object to look pretty. This works
        % well for the left hemisphere (medial and lateral). Change the inputs to
        % 'view' to see the brain from different angles ([-90 0] for left and [90 0]
        % for right I find works well)
        
        camlight(80,-10);
        camlight(-80,-10);
        
        if strcmp(hemisphere,'lh') && (v==1)
            angle = 'lateral';
            view([-90 0])
        elseif strcmp(hemisphere,'lh') && (v==2)
            angle = 'medial';
            view([90 0])
        elseif strcmp(hemisphere,'rh') && (v==1)
            angle = 'lateral';
            view([90 0])
        elseif strcmp(hemisphere,'rh') && (v==2)
            angle = 'medial';
            view([-90 0])
        end
        
        %view([90 0]) % -90 lateral, 90 medial
        %view([-90 0]) % -90 lateral, 90 medial (inside)
        
        axis off
        axis equal
        %axis padded
        %axis square


    end
end
    outfile = [outfile_string,'.png'];
    %t.Units = 'inches';
    %saveas(t,outfile)
    %shg    
    exportgraphics(t,outfile,'Resolution','1000')

    %clf('reset')
    %clear fig
end
