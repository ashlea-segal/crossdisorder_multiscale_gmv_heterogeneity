#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 07:40:12 2023

@author: asegal
"""

# Group disorder maps together
import matplotlib.pyplot as plt

path = '/home/asegal/kg98_scratch/Ashlea/crossdisorder_multiscale_gmv_heterogeneity/';
directions = ['pos','neg']
regional_thrs = ['thr26', 'thrweight']
circuit_thrs = ["parc50", "parc75"]
pval_tails = ['HC', 'PAT']
groups = ['HC','ADHD','ASD','BIPOL','MDD','OCD','SCZ']
disorders = ['ADHD', 'ASD', 'BIPOL', 'MDD', 'OCD','SCZ']

#-----------------------------------------------------------------------------
# Regional
#-----------------------------------------------------------------------------

# percent overlap

for direction in directions:
    for regional_thr in regional_thrs:

        while regional_thr is not 'thrweight' and direction is not 'pos':
    
            _, axs = plt.subplots(7, 1, figsize=(12, 12))
            axs = axs.flatten()
            for group, ax in zip(groups, axs):
                print(group)
                img_filename = path + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/percent_overlap_' + group + '_' + direction + '_thr26.png'
                img = plt.imread(img_filename)
                ax.imshow(img)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['bottom'].set_visible(False)
                ax.spines['left'].set_visible(False)
                ax.get_xaxis().set_ticks([])
                ax.get_yaxis().set_ticks([])
            #plt.show()
            plt.tight_layout()
            filename = path + '/figures/nature_neuro_figures/regional/percentOverlap_' + direction + '.svg'
            plt.savefig(filename, dpi=300)
             
            plt.cla()   # Clear axis
            plt.clf()   # Clear figure

# # signifcant rois
 
for direction in ['pos','neg']:
    
    for regional_thr in regional_thrs:
        
        while regional_thr is not 'thrweight' and direction is not 'pos':

            for tail in ['PAT','HC']:
                
                _, axs = plt.subplots(2, 3, figsize=(12, 6))
                axs = axs.flatten()
                for group, ax in zip(disorders, axs):
                        print(group)
                        img_filename = path + '/figures/nature_neuro_figures/regional/' + direction + '/' + group + '/pvals_FDR_' + regional_thr + '_Nshuf10000_' + tail + '.png';
                        img = plt.imread(img_filename)
                        ax.imshow(img)
                        ax.spines['top'].set_visible(False)
                        ax.spines['right'].set_visible(False)
                        ax.spines['bottom'].set_visible(False)
                        ax.spines['left'].set_visible(False)
                        ax.get_xaxis().set_ticks([])
                        ax.get_yaxis().set_ticks([])
                #plt.show()
                plt.tight_layout()
                filename = path + '/figures/nature_neuro_figures/regional/percentOverlap_significant_' + regional_thr + '_' + direction + '_'+tail + 'tail.svg'
                plt.savefig(filename,dpi=300)
                plt.cla()   # Clear axis
                plt.clf()   # Clear figure

#-----------------------------------------------------------------------------
# Circuit
#-----------------------------------------------------------------------------

# percent overlap

for direction in directions:
    for circuit_thr in circuit_thrs:

        _, axs = plt.subplots(7, 1, figsize=(12, 12))
        axs = axs.flatten()
        for group, ax in zip(groups, axs):
            print(group)
            img_filename = path + '/figures/nature_neuro_figures/circuit/' + direction + '/' + group + '/percent_overlap_' + group + '_' + direction + '_' + circuit_thr + '.png'
            img = plt.imread(img_filename)
            ax.imshow(img)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.get_xaxis().set_ticks([])
            ax.get_yaxis().set_ticks([])
        #plt.show()
        plt.tight_layout()
        filename = path + '/figures/nature_neuro_figures/circuit/percentOverlap_' + direction + '_' + circuit_thr + '.svg'
        plt.savefig(filename, dpi=300)
         
        plt.cla()   # Clear axis
        plt.clf()   # Clear figure

# # signifcant rois
 
for direction in ['pos','neg']:
    for null_type in ['spinnull', 'groupnull']:
        
        if null_type is 'groupnull':
            perm = 'Nshuf10000'
        else:
            perm = 'Nspin10000'
        for circuit_thr in circuit_thrs:
            for tail in ['PAT','HC']:
                
                _, axs = plt.subplots(2, 3, figsize=(12, 6))
                axs = axs.flatten()
                for group, ax in zip(disorders, axs):
                        print(group)
                        img_filename = path + '/figures/nature_neuro_figures/circuit/' + direction + '/' + group + '/pvals_FDR_' + circuit_thr + '_' + null_type + '_' + perm + '_' + tail + '.png';
                        img = plt.imread(img_filename)
                        ax.imshow(img)
                        ax.spines['top'].set_visible(False)
                        ax.spines['right'].set_visible(False)
                        ax.spines['bottom'].set_visible(False)
                        ax.spines['left'].set_visible(False)
                        ax.get_xaxis().set_ticks([])
                        ax.get_yaxis().set_ticks([])
                #plt.show()
                plt.tight_layout()
                filename = path + '/figures/nature_neuro_figures/regional/percentOverlap_significant_' + circuit_thr + '_' + direction +'_' + null_type + '_'+tail + 'tail.svg'
                plt.savefig(filename,dpi=300)
                plt.cla()   # Clear axis
                plt.clf()   # Clear figure
# # #-----------------------------------------------------------------------------
# # # Edge
# # #-----------------------------------------------------------------------------

# #for direction in ['pos','neg']:
# for direction in ['pos']:

#     _, axs = plt.subplots(2, 3, figsize=(12, 12))
#     axs = axs.flatten()
#     for disorder, ax in zip(disorders, axs):
#         print(disorder)
#         img_filename = path + '/results/figures/edges/Schaefer100_7netANDTianS2/' + direction + '/' + disorder + '/group_edges_empirical_Schaefer100_7netANDTianS2_minclustthr10_streamthr10_normsubjthr50_connectivity_mat.png'
#         img = plt.imread(img_filename)
#         ax.imshow(img)
#         ax.spines['top'].set_visible(False)
#         ax.spines['right'].set_visible(False)
#         ax.spines['bottom'].set_visible(False)
#         ax.spines['left'].set_visible(False)
#         ax.get_xaxis().set_ticks([])
#         ax.get_yaxis().set_ticks([])
#     #plt.show()
#     plt.tight_layout()
#     filename = path + '/results/figures/edges/Schaefer100_7netANDTianS2/percentOverlap_' + direction + '_horizontal.svg'
#     plt.savefig(filename, dpi=600)

#     plt.cla()   # Clear axis
#     plt.clf()   # Clear figure

# for direction in ['pos','neg']:
    
#     for tail in ['right','left']:
        
#         _, axs = plt.subplots(2, 3, figsize=(12, 12))
#         axs = axs.flatten()
#         for disorder, ax in zip(disorders, axs):
#             print(disorder)
#             img_filename = path + '/results/figures/edges/Schaefer100_7netANDTianS2/' + direction + '/' + disorder + '/grpnull_pval_Schaefer100_7netANDTianS2_minclustthr10_streamthr10_normsubjthr50_' + tail +'tail_connectivity_mat.png'
#             img = plt.imread(img_filename)
#             ax.imshow(img)
#             ax.spines['top'].set_visible(False)
#             ax.spines['right'].set_visible(False)
#             ax.spines['bottom'].set_visible(False)
#             ax.spines['left'].set_visible(False)
#             ax.get_xaxis().set_ticks([])
#             ax.get_yaxis().set_ticks([])
#         #plt.show()
#         plt.tight_layout()
#         filename = path + '/results/figures/edges/Schaefer100_7netANDTianS2/percentOverlap_significant_' + direction + '_'+tail + 'tail_horizontal.svg'
#         plt.savefig(filename,dpi = 600)
   
#         plt.cla()   # Clear axis
#         plt.clf()   # Clear figure


# #-----------------------------------------------------------------------------
# # Node
# #-----------------------------------------------------------------------------

# for direction in ['pos','neg']:
#     _, axs = plt.subplots(2, 3, figsize=(12, 12))
#     axs = axs.flatten()
#     for disorder, ax in zip(disorders, axs):
#         print(disorder)
#         img_filename = path + '/results/figures/nodes/Schaefer100_7netANDTianS2/' + direction + '/' + disorder + '/group_nodes_empirical_Schaefer100_7netANDTianS2_minclustthr10_streamthr10_normsubjthr50.png'
#         img = plt.imread(img_filename)
#         ax.imshow(img)
#         ax.spines['top'].set_visible(False)
#         ax.spines['right'].set_visible(False)
#         ax.spines['bottom'].set_visible(False)
#         ax.spines['left'].set_visible(False)
#         ax.get_xaxis().set_ticks([])
#         ax.get_yaxis().set_ticks([])
#     #plt.show()
#     plt.tight_layout()
#     filename = path + '/results/figures/nodes/Schaefer100_7netANDTianS2/percentOverlap_' + direction + '.svg'
#     plt.savefig(filename, dpi=600)

#     plt.cla()   # Clear axis
#     plt.clf()   # Clear figure

# for direction in ['pos','neg']:
    
#     for tail in ['right','left']:
        
#         _, axs = plt.subplots(2, 3, figsize=(12, 12))
#         axs = axs.flatten()
#         for disorder, ax in zip(disorders, axs):
#             print(disorder)
#             img_filename = path + '/results/figures/nodes/Schaefer100_7netANDTianS2/' + direction + '/' + disorder + '/grpnull_group_nodes_Schaefer100_7netANDTianS2_minclustthr10_streamthr10_normsubjthr50_nperm5000_pval_approx_'+tail+'.png'
#             img = plt.imread(img_filename)
#             ax.imshow(img)
#             ax.spines['top'].set_visible(False)
#             ax.spines['right'].set_visible(False)
#             ax.spines['bottom'].set_visible(False)
#             ax.spines['left'].set_visible(False)
#             ax.get_xaxis().set_ticks([])
#             ax.get_yaxis().set_ticks([])
#         #plt.show()
#         plt.tight_layout()
#         filename = path + '/results/figures/nodes/Schaefer100_7netANDTianS2/percentOverlap_significant_' + direction + '_'+tail + 'tail_horizontal.svg'
#         plt.savefig(filename,dpi = 600)
#         plt.cla()   # Clear axis
#         plt.clf()   # Clear figure
# #-----------------------------------------------------------------------------
# # Network
# #-----------------------------------------------------------------------------



# #for direction in ['pos','neg']:
# for direction in ['pos']:

#     _, axs = plt.subplots(2, 3, figsize=(12, 12))
#     axs = axs.flatten()
#     for disorder, ax in zip(disorders, axs):
#         print(disorder)
#         img_filename = path + '/results/figures/networks/Schaefer100_7netANDTianS2/' + direction + '/' + disorder + '/group_networks_empirical_Schaefer100_7netANDTianS2_minclustthr10_streamthr10_normsubjthr50.png'
#         img = plt.imread(img_filename)
#         ax.imshow(img)
#         ax.spines['top'].set_visible(False)
#         ax.spines['right'].set_visible(False)
#         ax.spines['bottom'].set_visible(False)
#         ax.spines['left'].set_visible(False)
#         ax.get_xaxis().set_ticks([])
#         ax.get_yaxis().set_ticks([])
#     #plt.show()
#     plt.tight_layout()
#     filename = path + '/results/figures/networks/Schaefer100_7netANDTianS2/percentOverlap_' + direction + '.svg'
#     plt.savefig(filename, dpi=600)
#     plt.cla()   # Clear axis
#     plt.clf()   # Clear figure
    
# #for direction in ['pos','neg']:
# for direction in ['pos']:

    
#     _, axs = plt.subplots(2, 3, figsize=(12, 12))
#     axs = axs.flatten()
#     for disorder, ax in zip(disorders, axs):
#         print(disorder)
#         img_filename = path + '/results/figures/networks/Schaefer100_7netANDTianS2/' + direction + '/' + disorder + '/group_networks_empirical_Schaefer100_7netANDTianS2_minclustthr10_streamthr10_normsubjthr50_nperm5000_pval_approx.png'
#         img = plt.imread(img_filename)
#         ax.imshow(img)
#         ax.spines['top'].set_visible(False)
#         ax.spines['right'].set_visible(False)
#         ax.spines['bottom'].set_visible(False)
#         ax.spines['left'].set_visible(False)
#         ax.get_xaxis().set_ticks([])
#         ax.get_yaxis().set_ticks([])
#     #plt.show()
#     plt.tight_layout()
#     filename = path + '/results/figures/networks/Schaefer100_7netANDTianS2/percentOverlap_significant_' + direction + '_horizontal.svg'
#     plt.savefig(filename,dpi = 600)
#     plt.cla()   # Clear axis
#     plt.clf()   # Clear figure