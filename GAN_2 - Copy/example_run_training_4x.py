import os

basepath = "../3ddata_gan_sliced_2/"
packedpath = "../3ddata_sim/"

# train the first network
os.system(f'python multipassGAN-4x.py randSeed 16131119 upRes 4 batchNorm 0 out 0 pretrain 0 pretrainDisc 0 tileSize 16 simSize 32 lambda 1.0 lambda2 0.0 discRuns 1 genRuns 1 alwaysSave 1 fromSim 1000 toSim 1000 outputInterval 200 genTestImg 1 dropout 0.5 dataDim 2 batchSize 16 useVelocities 1 useVorticities 0 useK_Eps_Turb 0 useFlags 0 gif 0 genModel gen_resnet discModel disc_binclass basePath {basepath} packedSimPath {packedpath} lambda_t 1.0 lambda_t_l2 0.0 frame_max 120 frame_min 0 data_fraction 0.08 adv_flag 1 dataAugmentation 1 premadeTiles 0 rot 1 minScale 0.85 maxScale 1.15 flip 1 decayLR 1 adam_beta1 0.0 learningRate 0.0001 upsampledData 0 discRuns 1 load_model_test -1 load_model_no -1')

# train the second network, note that the input data for the 2nd network has to be generated at first...
# os.system('python multipassGAN-8x.py randSeed 96031119 upRes 8 use_res_net 1 batchNorm 0 pixelNorm 1 out 0 pretrain 0 pretrainDisc 0 tileSize 8  simSize 32 use_LSGAN 0 use_wgan_gp 1 lambda 1.0 lambda2 0.0 discRuns 1 genRuns 1 alwaysSave 1 fromSim 1000 toSim 1000 outputInterval 100 genTestImg 1 dropout 0.5 dataDim 2 batchSize 16 useVelocities 1 useVorticities 0 useK_Eps_Turb 0 useFlags 0 gif 0 genModel gen_resnet discModel disc_binclass basePath ../2ddata/ packedSimPath ../data3d_growing/ lambda_t 1.0 lambda_t_l2 0.0 frame_max 120 frame_min 0 data_fraction 0.09 adv_flag 1 adv_mode 0 dataAugmentation 1 premadeTiles 0 rot 1 minScale 0.85 maxScale 1.15 flip 1 decayLR 1 adam_beta1 0.0 adam_beta2 0.99 learningRate 0.0001 lossScaling 1 stageIter 1     decayIter 250000 maxFms 192 startFms 192 filterSize 5 upsamplingMode 1 upsampledData 1 upsampleMode 1 discRuns 1 usePixelShuffle 0 addBicubicUpsample 1 startingIter 0 useVelInTDisc 0 load_model_test -1 load_model_no -1 gpu 0 outNNTestNo 0 ')
