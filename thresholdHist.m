function I_thres = thresholdHist(I, from, to)
% THRESHOLDHIST 
%      I_THRES = THRESHOLDHIST(I, FROM, TO) returns binary image with 
%      pixels in intensity range [FROM, TO]
%
%      Examples 
%
%      TBW

ROI = I > from & I < to;
I_thres= zeros(size(I));
I_thres(ROI) = 1;
