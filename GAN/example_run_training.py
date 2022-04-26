import os

basepath =  "../2ddata/"
packedpath =  "../data3d_growing/"

# train the first network
os.system(
    'python multipassGAN-4x.py randSeed 16131119 upRes 8 use_res_net 1 batchNorm 0 pixelNorm 1 out 0 pretrain 0 '
    'pretrainDisc 0 tileSize 16 simSize 64 use_LSGAN 0 use_wgan_gp 1 lambda 1.0 lambda2 0.0 discRuns 1 genRuns 1 '
    'alwaysSave 1 fromSim 1000 toSim 1016 outputInterval 200 genTestImg 1 dropout 0.5 dataDim 2 batchSize 16 '
    'useVelocities 1 useVorticities 0 useK_Eps_Turb 0 useFlags 0 gif 0 genModel gen_resnet '
    f'discModel disc_binclass basePath {basepath} packedSimPath {packedpath} lambda_t 1.0 lambda_t_l2 0.0 '
    'frame_max 120 frame_min 0 data_fraction 0.08 adv_flag 1 adv_mode 0 dataAugmentation 1 premadeTiles 0 rot 1 '
    'minScale 0.85 maxScale 1.15 flip 1 decayLR 1 adam_beta1 0.0 adam_beta2 0.99 learningRate 0.0001 '
    'lossScaling 1 stageIter 40000 decayIter 60000 maxFms 256 startFms 256 filterSize 3 upsamplingMode 2 '
    'upsampledData 0 discRuns 1 load_model_test -1 load_model_no -1 firstNNArch 1 add_adj_idcs 1 '
    'usePixelShuffle 0 addBicubicUpsample 1 startingIter 0 useVelInTDisc 0 upsampleMode 1 gpu 0'
)

# train the second network, note that the input data for the 2nd network has to be generated at first...
os.system(
    'python multipassGAN-4x.py randSeed 9631119 upRes 8 use_res_net 1 batchNorm 0 pixelNorm 1 out 0 pretrain 0 '
    'pretrainDisc 0 tileSize 8 simSize 64 use_LSGAN 0 use_wgan_gp 1 lambda 1.0 lambda2 0.0 discRuns 1 genRuns 1 '
    'alwaysSave 1 fromSim 1000 toSim 1016 outputInterval 100 genTestImg 1 dropout 0.5 dataDim 2 batchSize 16 '
    'useVelocities 1 useVorticities 0 useK_Eps_Turb 0 useFlags 0 gif 0 genModel gen_resnet '
    f'discModel disc_binclass basePath {basepath} packedSimPath {packedpath} lambda_t 1.0 '
    'lambda_t_l2 0.0 frame_max 120 frame_min 0 data_fraction 0.09 adv_flag 1 adv_mode 0 dataAugmentation 1 '
    'premadeTiles 0 rot 1 minScale 0.85 maxScale 1.15 flip 1 decayLR 1 adam_beta1 0.0 adam_beta2 0.99 '
    'learningRate 0.0001 lossScaling 1 stageIter 1 decayIter 250000 maxFms 192 startFms 192 filterSize 5 '
    'outNNTestNo 0 upsamplingMode 1 upsampledData 1 upsampleMode 1 discRuns 1 usePixelShuffle 0 '
    'addBicubicUpsample 1 startingIter 0 useVelInTDisc 0 gpu 0 load_model_test -1 load_model_no -1'
)
