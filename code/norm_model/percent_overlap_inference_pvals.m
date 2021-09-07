%% set up
addpath ('/home/asegal/kg98/Ashlea/code/PALM-master');

pval_thr = 0.025;
pval_string = '25';
directions = ["pos", "neg"];

maindir = '/scratch/kg98/Ashlea/parcellation_v2/models/bc_transform/ids/noTopImpact/inference/';
file_string = '_thr26_Nshuf10000';

groups = ["ASD", "MDD",'SCZ', 'ADHD', 'BIPOL','OCD'];
Nrois=1032;
Nperm = 10000;
%% loop over groups

for d=1:2
    
    direction = char(directions(d));


    for g=1:length(groups)

        group = char(groups(g));

        wdir = [maindir,'/',direction,'/',group,'/'];
        cd(wdir)

        % load null and observed
        null = load(['null_distribution',file_string,'.txt']);
        obser = load(['observed_difference',file_string,'.txt']);

        % calculate pvalues
    % calculate pvalues

        % original 
        pvals_tail_1 = zeros(Nrois,1);
        pvals_tail_2 = zeros(Nrois,1);

        for roi=1:Nrois
            G = obser(roi);
            Gdist = null(:,roi);
            pvals_tail_1(roi) = sum(Gdist>=G)/Nperm;
            pvals_tail_2(roi) = sum(Gdist<=G)/Nperm;
        end

        % tail approximation

        pvals_approx_tail_1 = zeros(Nrois,1);
        pvals_approx_tail_2 = zeros(Nrois,1);

        for roi=1:Nrois
            %sprintf('%d',roi)
            G = obser(roi);
            Gdist = null(:,roi);
            Pthr = 0.10;
            G1out = false;
            rev = false;
            pvals_approx_tail_1(roi) = palm_pareto(G,Gdist,rev,Pthr,G1out);
            rev = true;
            pvals_approx_tail_2(roi) = palm_pareto(G,Gdist,rev,Pthr,G1out);
        end

        % FDR correction 
        % Compute FDR-adjusted p-values.
        pval = pvals_approx_tail_1; 
        V = numel(pval);
        [pval,oidx] = sort(pval);
        [~,oidxR]   = sort(oidx);
        padj = zeros(size(pval));
        prev = 1;
        for i = V:-1:1,
            padj(i) = min(prev,pval(i)*V/i);
            prev = padj(i);
        end
        pvals_approx_tail_1_FDR = padj(oidxR);

        pval = pvals_approx_tail_2; 
        V = numel(pval);
        [pval,oidx] = sort(pval);
        [~,oidxR]   = sort(oidx);
        padj = zeros(size(pval));
        prev = 1;
        for i = V:-1:1,
            padj(i) = min(prev,pval(i)*V/i);
            prev = padj(i);
        end
        pvals_approx_tail_2_FDR = padj(oidxR);

        %fdr_tail = mafdr(pvals_tail_twoTail_removed0,'BHFDR', true);



        %%
        % Results
        NSignificant_tail_1 = length(find(pvals_approx_tail_1<pval_thr));
        NSignificant_tail_2 = length(find(pvals_approx_tail_2<pval_thr));
        
        NSignificant_tail_1_FDR = length(find(pvals_approx_tail_1_FDR<pval_thr));
        NSignificant_tail_2_FDR = length(find(pvals_approx_tail_2_FDR<pval_thr));

        sprintf('%s %s one tail uncorr: %d FDR: %d',group, direction, NSignificant_tail_1,NSignificant_tail_1_FDR)

        sprintf('%s %s two tail uncorr: %d FDR: %d',group, direction, NSignificant_tail_2,NSignificant_tail_2_FDR)

        outfile_filname = ['pvals_FDR',file_string,'_PAT.txt'];
        dlmwrite(outfile_filname,pvals_approx_tail_1_FDR);

        outfile_filname = ['pvals_FDR',file_string,'_HC.txt'];
        dlmwrite(outfile_filname,pvals_approx_tail_2_FDR);

        outfile_filname = ['pvals_uncorr',file_string,'_PAT.txt'];
        dlmwrite(outfile_filname,pvals_approx_tail_1);

        outfile_filname = ['pvals_uncorr',file_string,'_HC.txt'];
        dlmwrite(outfile_filname,pvals_approx_tail_2);
    end

end 

% 
% 
% pvals_tail_1 = zeros(Nperm_options,Nrois);
% pvals_tail_2 = zeros(Nperm_options,Nrois);
% 
% for i=1:Nperm_options
%     perm = perm_options(i);
%     null_tmp = null(1:perm,:);
%     Nperm=length(null_tmp);
% 
%     for roi=1:Nrois
%         G = obser(roi);
%         Gdist = null_tmp(:,roi);
%         pvals_tail_1(i,roi) = sum(Gdist>=G)/Nperm;
%         pvals_tail_2(i,roi) = sum(Gdist<=G)/Nperm;
%         
%     end
% end
% 
% 
% Nsignificant_perms = zeros(Nperm_options,1);
% for i=1:Nperm_options
%     Nsignificant_perms(i,1) = length(find(pvals_tail_1(i,:)<=0.025));
% end
% 
% hold on
% plot(perm_options,Nsignificant_perms(:,1));
% ax = gca; % axes handle
% ax.YAxis.Exponent = 0;
% xlabel('Number of Spins');
% ylabel('Number of Significant pvalues');
% 
% hold off
