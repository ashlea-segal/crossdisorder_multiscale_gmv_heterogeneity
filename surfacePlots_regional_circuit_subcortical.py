#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 04:54:10 2023

@author: asegal
"""

# In bash

# $ module load virtualgl
# $ vglrun spyder
import os
import sys
import numpy as np
import pyvista as pv
from numpy import inf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

def CreateSubcorticalPlot(mesh_lh_filename, mesh_rh_filename, data, nsubROIs, thr, cmap, outfile_string,gridFlag):

    # get subcortical data
    data_subcortical = data[-nsubROIs:]
    
    for h in range(2):
        
        if h is 0:
            hemisphere = 'lh';
            current_mesh =  pv.read(mesh_lh_filename)
            current_position = [1.5, 0.5, -1]
            #current_data = data_subcortical[:int(len(data_subcortical)/2)] # ERROR TIAN RH-LH
            current_data = data_subcortical[int(len(data_subcortical)/2):]
            current_outname = outfile_string + '_lh.png'
    
        elif h is 1:
            hemisphere = 'rh';
            current_mesh =  pv.read(mesh_rh_filename)
            current_position = [-10, 4, -6]
            #current_data = data_subcortical[int(len(data_subcortical)/2 ):]
            current_data = data_subcortical[:int(len(data_subcortical)/2)]

            current_outname = outfile_string + '_rh.png'
        
        # settings     
        meshSmooth = current_mesh.smooth(n_iter=200) # Smooth
        
         # Get scalars
        cells = meshSmooth.active_scalars
        unique_elements, counts_elements = np.unique(cells, return_counts=True)   
        
        hemisphere_degree = current_data
        scalarsDegree = np.repeat(hemisphere_degree, counts_elements, axis=0)
        
         # Create plotting object
        pv.rcParams['transparent_background'] = True
        plotter = pv.Plotter(border=False,border_color='w',off_screen=True)
        plotter.add_mesh(meshSmooth,scalars=scalarsDegree, cmap=cmap , clim = [0,thr])
        plotter.camera_position = current_position
        #plotter.window_size = 1150, 860
        if gridFlag == 'line':
            plotter.window_size = 805, 602
        else:
            plotter.window_size = 1150, 860
        #plotter.border_color = False
        #plotter.remove_scalar_bar(title=None)
        plotter.remove_scalar_bar()

        plotter.image_scale = 2
        #plotter.add_scalar_bar()
        plotter.show(screenshot=current_outname) # doesn't work
        #plotter.show() # doesn't work

#                #plotter.screenshot(outfile_img)

# #    # can open into matplotlib
#         plt.figure(figsize=(30,15))
#         plt.imshow(plotter.image)
#         plt.axis('off')
#         plt.show()
 
def plotCorticalandSubcorticalTogether(surface_filename,subcort_lh_filename,subcort_rh_filename, gridFlag):
    
    fig, ax = plt.subplots()
    
    surface = plt.imread(surface_filename) 
    subcort_lh = plt.imread(subcort_lh_filename) 
    subcort_rh = plt.imread(subcort_rh_filename) 
    
    subcort_lh_plot = ax.imshow(subcort_lh, zorder = 10)
    subcort_rh_plot = ax.imshow(subcort_rh, zorder = 10)
    ax.imshow(surface, zorder = 1)
    
    # shuffle subcortical plot positions 
    if gridFlag == 'line':
        transform = mpl.transforms.Affine2D().translate(1270, 165)
        subcort_lh_plot.set_transform(transform + ax.transData)
        transform = mpl.transforms.Affine2D().translate(3400, 165)
        subcort_rh_plot.set_transform(transform + ax.transData) 
    else:
        #transform = mpl.transforms.Affine2D().translate(380, 3000)
        transform = mpl.transforms.Affine2D().translate(200, 1420)
        subcort_lh_plot.set_transform(transform + ax.transData)
        transform = mpl.transforms.Affine2D().translate(1680, 1420)
        subcort_rh_plot.set_transform(transform + ax.transData) 
    ax.axis('off')
    #plt.tight_layout()
    #plt.show() 
    
    return fig
        
pathDir = '/home/asegal/kg98_scratch/Ashlea/crossdisorder_multiscale_gmv_heterogeneity/';
groups = ['HC', 'ADHD', 'ASD', 'BIPOL', 'MDD', 'OCD', 'SCZ']
directions = ['pos','neg']
regional_thrs = ['thr26', 'thr_weight']
pval_tails = ['HC', 'PAT']
parcellation = 'Schaefer100_7netANDTianS2'
mesh_lh_filename = '/scratch/kg98/Ashlea/crossdisorder_multiscale_wmv_heterogeneity/data/tian_lh.vtk'
mesh_rh_filename = '/scratch/kg98/Ashlea/crossdisorder_multiscale_wmv_heterogeneity/data/tian_rh.vtk'
level = 'regional'
nsubROIs = 32
thr_bin = 2.5
thr = 5
for direction in directions:
    
    print(direction)
    
    if direction == 'neg':
        cmap = np.loadtxt('/scratch/kg98/Ashlea/crossdisorder_multiscale_wmv_heterogeneity/data/cmap/colourmap_red_gradient.txt')
        cmap_binary = np.loadtxt('/scratch/kg98/Ashlea/crossdisorder_multiscale_wmv_heterogeneity/data/cmap/colourmap_red_binary.txt')
    else:
        cmap = np.loadtxt('/scratch/kg98/Ashlea/crossdisorder_multiscale_wmv_heterogeneity/data/cmap/colourmap_blue_gradient.txt')
        cmap_binary = np.loadtxt('/scratch/kg98/Ashlea/crossdisorder_multiscale_wmv_heterogeneity/data/cmap/colourmap_blue_binary.txt')
    
    cmap = mpl.colors.ListedColormap(cmap)
    cmap.set_under(color=(0.7, 0.7, 0.7))
    
    cmap_binary = np.insert(cmap_binary,0,np.array((1,1,1,1)),0)
    cmap_binary = mpl.colors.ListedColormap(cmap_binary)
    cmap_binary.set_under(color=(0.7, 0.7, 0.7))


    for group in groups:
        
        print(group)
        
        # Regional 
        if level == 'regional':
            
            for regional_thr in regional_thrs:

                if regional_thr == 'thrweight':
                    thr = 0.065
                else:
                    thr = 5
                
                if regional_thr == 'thrweight':
                     regional_thr_str = 'thr_weight'
                else:
                     regional_thr_str = 'thr26'
                # overlap maps 
                data_filename = pathDir + '/data_figures/regional/' + direction + '/' + group + '/percent_overlap_' + regional_thr + '_' + group + '_' + direction + '.txt';
                data = np.loadtxt(data_filename)
                outfile_string = pathDir + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/percent_overlap_' + regional_thr + '_' + group + '_' + direction + '_subcortical.png';
                CreateSubcorticalPlot(mesh_lh_filename, mesh_rh_filename, data, nsubROIs, thr, cmap, outfile_string,'line')
                
                # plot cortical and subcortical together 
                surface_filename = pathDir + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/percent_overlap_' + regional_thr + '_' + group + '_' + direction + '_cortical.png';
                subcort_lh_filename = outfile_string+'_lh.png' # insert local path of the image.
                subcort_rh_filename = outfile_string+'_rh.png' # insert local path of the image.
        
                surfaceAndSubcortical_filename = pathDir + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/percent_overlap_' + regional_thr + '_' + group + '_' + direction + '.png'
                fig = plotCorticalandSubcorticalTogether(surface_filename,subcort_lh_filename,subcort_rh_filename,'line')
                fig.tight_layout()
                fig.savefig(surfaceAndSubcortical_filename, dpi=300,bbox_inches='tight')
                
                if group is not 'HC':
            
                    for pval_tail in pval_tails:
                        
                        # significant maps 
                        
                        data_filename = pathDir + '/data_figures/regional/' + direction + '/' + group + '/pvals_FDR_' + regional_thr +'_Nshuf10000_' + pval_tail + '.txt';
                        data_FDR = np.loadtxt(data_filename)
                        data_filename = pathDir + '/data_figures/regional/' + direction + '/' + group + '/pvals_uncorr_' + regional_thr +'_Nshuf10000_' + pval_tail + '.txt';
                        data_uncorr = np.loadtxt(data_filename)      
                        
                        data = np.zeros((np.shape(data_FDR)))
                        data[data_uncorr<0.025] = 1
                        data[data_FDR<0.025] = 2
                        
                        outfile_string = pathDir + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/pvals_FDR_' + regional_thr + '_Nshuf10000_' + pval_tail + '_subcortical.png';
                        CreateSubcorticalPlot(mesh_lh_filename, mesh_rh_filename, data, nsubROIs, thr_bin, cmap_binary, outfile_string, 'square')
                        
                        # plot cortical and subcortical together                             
                        surface_filename = pathDir + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/pvals_FDR_' + regional_thr_str + '_Nshuf10000_' + pval_tail + '_cortical.png';
                        subcort_lh_filename = outfile_string+'_lh.png' # insert local path of the image.
                        subcort_rh_filename = outfile_string+'_rh.png' # insert local path of the image.
                        
                        surfaceAndSubcortical_filename = pathDir + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/pvals_FDR_' + regional_thr + '_Nshuf10000_' + pval_tail + '.png';
                        fig = plotCorticalandSubcorticalTogether(surface_filename,subcort_lh_filename,subcort_rh_filename,'square')
                        fig.savefig(surfaceAndSubcortical_filename, dpi = 300,bbox_inches='tight')

        # # Circuit - no subcortical but run it so it is the same size as above
        # elif level == 'circuit':

        #     for circuit_thr in ['parc50','parc75']:
                
        #         # overlap map
        #         surface_filename = pathDir + '/figures/nature_neuro_figures/circuit/' + direction + '/' + group + '/percent_overlap_' +  circuit_thr + '_' + group + '_' + direction +  '.png'
        #         fig, ax = plt.subplots()
        #         surface = plt.imread(surface_filename) 
        #         ax.imshow(surface, zorder = 1)
        #         ax.axis('off')
        #         #plt.tight_layout()
        #         #plt.show() 
        #         surface_filename = pathDir + '/figures/nature_neuro_figures/circuit/' + direction + '/' + group + '/percent_overlap_' + circuit_thr + '_' + group + '_' + direction + '.png'
        #         fig.tight_layout()
        #         fig.savefig(surface_filename, dpi=300,bbox_inches='tight')
                
        #         # significance 
        #         if group is not 'HC':

        #             for pval_tail in pval_tails:
        #                 for null in ['spinnull_Nspin10000','groupnull_Nshuf10000']:
        #                     surface_filename = pathDir + '/figures/nature_neuro_figures/circuit/' + direction + '/' + group + '/pvals_FDR_' + circuit_thr + '_' + null + '_' + pval_tail + '.png'
        #                     fig, ax = plt.subplots()
        #                     surface = plt.imread(surface_filename) 
        #                     ax.imshow(surface, zorder = 1)
        #                     ax.axis('off')
        #                     #plt.tight_layout()
        #                     #plt.show() 
        #                     surface_filename = pathDir + '/figures/nature_neuro_figures/circuit/' + direction + '/' + group + '/pvals_FDR_' + circuit_thr + '_' + null + '_' + pval_tail + '.png'
        #                     fig.tight_layout()
        #                     fig.savefig(surface_filename, dpi=300,bbox_inches='tight')
            
        
        
        
        