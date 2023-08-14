#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 01:46:38 2023

@author: asegal
"""

import numpy as np
import matplotlib.pyplot as plt

#Adjustable things
directions = ['pos','neg'];
grp_directions = ['PAT','HC']
patientGroups = ['ADHD','ASD','BIPOL','MDD','OCD','SCZ']
#data_dir = '/scratch/kg98/Ashlea/lesion_networks/data/Level3_Analysis/meants_indivDeviations_union_spinTests/rfMRI_REST1_LR/network_withSubcortical/'
data_dir_spin = '/scratch/kg98/Ashlea/lesion_networks/data/Level3_Analysis/meants_indivDeviations_union_spinTests/rfMRI_REST1_LR/network_withSubcortical/'
data_dir_shuff = '/scratch/kg98/Ashlea/lesion_networks/data/Level3_Analysis/meants_indivDeviations_union_shuffleLabels/rfMRI_REST1_LR/network/'
path = '/home/asegal/kg98_scratch/Ashlea/multiscale-heterogeneity-brain-abnormalities/';

for null_type in ['spinnull', 'groupnull']:
    
    for tail in ['PAT','HC']:
        
        for direction in directions:
            
            #wdir = data_dir + direction + '/'
            
            #fig,ax = plt.subplots(len(patientGroups),2,gridspec_kw={'width_ratios':[3,1]})
            #fig,axs = plt.subplots(2,3, figsize=(45,30))
            fig,axs = plt.subplots(3,2, figsize=(30,45))
            
            axs = axs.ravel()
            for i,group in enumerate(patientGroups): 
                
                instring = path + 'figures/nature_neuro_figures/network/' + direction + '/' + group + '_pvals_log10_10network'+tail+'_' + null_type 
                img = plt.imread(instring+".png")
                axs[i].imshow(img)
                axs[i].axis('off')         
            
            #outdir = '/scratch/kg98/Ashlea/deviation_network_mapping/figures/network/'+direction + '/'
            filename = path + '/figures/nature_neuro_figures/network/percentOverlap_significant_'  + direction +'_' + null_type + '_'+tail + 'tail.svg'
            
            #plt.subplots_adjust(wspace=0.1, hspace=0.15)
            plt.subplots_adjust(wspace=0.1, hspace=0.1)
            
            #plt_filename =  outdir + instring+'_combined.png'
            #print(plt_filename)
            plt.savefig(filename, bbox_inches='tight',pad_inches=0.01 ,dpi=300)
            plt.show()