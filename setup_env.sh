# Only enable external GPU
export CUDA_VISIBLE_DEVICES=1

export DATA_ROOT=.
export IHANNES_PCD_PRED_DATA=${DATA_ROOT}/pcd_data/pred_depth
export IHANNES_PCD_RS_DATA=${DATA_ROOT}/pcd_data/rs_depth
export IHANNES_PCD_DEPTH_ANY_DATA=${DATA_ROOT}/pcd_data/depth_anything