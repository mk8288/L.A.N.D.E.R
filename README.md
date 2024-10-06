# L.A.N.D.E.R (Leveraging AI Networks for Dynamic Exploration and Reconstruction)

## Overview

### Problem Statement

**Choose Your Own Challenge:**

The goal is to generate a hazard map at 1m grid spacing (1m height resolution) using 5m spatial resolution data for safely navigating a lander to a safe landing site using super-resolution techniques.

We have TMC images that cover nearly 80% of the moon's surface at a 5m resolution, while OHRC data (available at a 25cm resolution) has very limited coverage. Due to this limited OHRC coverage, there are constraints on landing at any arbitrary location on the moon’s surface. The challenge is to create a hazard map using super-resolution techniques from TMC 5m images, considering hazard definitions like:
- Slope > 10 degrees
- Crater/Boulder depth/height > 1m
- Crater distribution, shadow, etc.

This map will be used for safely navigating a lander. The challenge also includes showcasing lander navigation techniques for safe landing in near real time, with TMC 5m datasets as the primary reference.

---

## Walkthrough Filesystem

- **`model.py`** : Contains the model architecture for SRGAN.
- **`train_srgan.py`** : Script to train the SRGAN model from scratch or continue training.
- **`generate_srgan.py`** : Script to generate a 16x superscaled image from a TMC2 image using the trained model.
- **`evaluation.py`** : Script to evaluate the 16x upsampled data using the SSIM evaluation metric with test OHRC data.
- **`srgan_config.py`** : Configuration file for training, generating, and evaluation parameters.
- **`dataset.py`** : Handles creating batches of tensors for training or testing using a DataLoader.
- **`image_quality_assessment.py`** : Contains code for evaluation metrics like SSIM, PSNR, etc.
- **`requirements.txt`** : Lists environment dependencies.
- **`cascade.py`** : An earlier version of the generation script (`generate_srgan.py`).

### Directory Structure

- **`train_data/`** : Directory to store training data.
- **`pretrained_weights/`** : Directory to store pretrained weights.
- **`results/`** : Directory where the best and latest generator and discriminator weights are saved during training.
- **`samples/`** : Directory where logs and per-epoch weights are stored.

---

## Pretrained Weights

- **Generator (g_model)**: `g_last.pth.tar`
- **Discriminator (d_model)**: `d_last.pth.tar`
  
These weights can be used for further training on custom datasets.

- **Best Generator Weights**: `g_best.pth.tar`

---

## Datasets

- **Chandrayaan TMC-2**: Apollo-12 and Apollo-16 from [ISSDC website](https://www.isro.gov.in/chandrayaan2.html)
- **NASA LRO**: Apollo-12 and Apollo-16 from [LROC-NAC website](https://www.lroc.sese.asu.edu/)

---

## How to Train, Generate, and Evaluate

All configurations for training, testing, and evaluation can be modified in the `srgan_config.py` file.

### Generate SuperResolution Images

1. Modify the `srgan_config.py` file:
   - Line 29: Change `mode` to `'generate'`.
   - Line 31: Change `exp_name` to a new experiment name.
   - Line 102: Set `g_model_weights_path` to `./pretrained_models/generate/g_best.pth.tar`.
   
2. The input low-resolution files should have dimensions AxA, where A is a multiple of 24. Store these files in `./generate_data/TMC2/dim_1x`.

3. The corresponding output images will be saved in `./generate_data/TMC2/dim_16x`.

To run the generation process:

```bash
python generate_srgan.py
```

### Evaluation

Modify the `srgan_config.py` file.

- line 29: `mode` change to `evaluate`.

```bash
python evaluation.py
```

- this unzipped folder can also be used to run evaluation over other metrics
- per image size in this folder is 3840x3840 8-bit images


### Installations

```bash
pip install opencv-python numpy tqdm torch torchvision natsort typing scipy
## or
pip install -r requirements.txt
```
