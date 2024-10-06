import random
import numpy as np
import torch
from torch.backends import cudnn
from utils import make_directory
import os

# Random seed to maintain reproducible results
random.seed(0)
torch.manual_seed(0)
np.random.seed(0)

# Use GPU for training by default
device = torch.device(device="cpu")  # For switching on GPU
# Turning on when the image size does not change during training can speed up training
cudnn.benchmark = True

# When evaluating the performance of the SR model, whether to verify only the Y channel image data
only_test_y_channel = True

# Model architecture name
d_arch_name = "discriminator"
g_arch_name = "srresnet_x4"

# Model arch config
in_channels = 3
out_channels = 3
channels = 64
num_rcb = 16

# Test upscale factor
upscale_factor = 4

# Current configuration parameter method
mode = "generate"

# Experiment name, easy to save weights and log files
exp_name = "SRGAN_11x"

# Set BASE_DIR to the directory where the code is running
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

if mode == "train":
    # Dataset address
    train_gt_images_dir = os.path.join(DATA_DIR, 'train_data', 'train', 'TMC2NAC_dataset', 'high')
    train_lr_images_dir = os.path.join(DATA_DIR, 'train_data', 'train', 'TMC2NAC_dataset', 'low')

    test_gt_images_dir = os.path.join(DATA_DIR, 'train_data', 'test', 'high')
    test_lr_images_dir = os.path.join(DATA_DIR, 'train_data', 'test', 'low')

    gt_image_size = 96
    lr_image_size = 24
    batch_size = 64
    num_workers = 6

    # The address to load the pretrained model
    pretrained_d_model_weights_path = os.path.join(DATA_DIR, 'pretrained_weights', 'train', 'd_last.pth.tar')
    pretrained_g_model_weights_path = os.path.join(DATA_DIR, 'pretrained_weights', 'train', 'g_last.pth.tar')

    # Incremental training and migration training
    resume_d_model_weights_path = os.path.join(DATA_DIR, 'pretrained_weights', 'train', 'd_last.pth.tar')
    resume_g_model_weights_path = os.path.join(DATA_DIR, 'pretrained_weights', 'train', 'g_last.pth.tar')

    # Total num epochs
    epochs = 1

    # Loss function weight
    pixel_weight = 1.0
    content_weight = 1.0
    adversarial_weight = 0.001

    # Feature extraction layer parameter configuration
    feature_model_extractor_node = "features.35"
    feature_model_normalize_mean = [0.485, 0.456, 0.406]
    feature_model_normalize_std = [0.229, 0.224, 0.225]

    # Optimizer parameter
    model_lr = 1e-4
    model_betas = (0.9, 0.999)
    model_eps = 1e-8
    model_weight_decay = 0.0

    # Dynamically adjust the learning rate policy [100,000 | 200,000]
    lr_scheduler_step_size = epochs // 2
    lr_scheduler_gamma = 0.1

    # How many iterations to print the training result
    train_print_frequency = 1
    valid_print_frequency = 1

if mode == "generate":
    # Test data address
    stp0_lr_dir = os.path.join(DATA_DIR, 'generate_data', 'TMC2', 'singletest_1x')
    stp1_sr_dir = os.path.join(DATA_DIR, 'generate_data', 'TMC2', 'singletest_4x')
    stp2_sr_dir = os.path.join(DATA_DIR, 'generate_data', 'TMC2', 'singletest_16x')
    dim24_dir = os.path.join(DATA_DIR, 'generate_data', 'TMC2', 'dim24')
    dim96_dir = os.path.join(DATA_DIR, 'generate_data', 'TMC2', 'dim96')

    make_directory(dim24_dir)
    make_directory(dim96_dir)
    make_directory(stp1_sr_dir)
    make_directory(stp2_sr_dir)

    g_model_weights_path = os.path.join(DATA_DIR, 'pretrained_weights', 'generate', 'g_best.pth.tar')

if mode == "evaluate":
    # Evaluate data address
    test_ohrc_path = os.path.join(DATA_DIR, 'figure', 'ohrc_test2.png')
    gen_data_dir = os.path.join(DATA_DIR, 'generate_data', 'TMC2', 'dim_16x')

