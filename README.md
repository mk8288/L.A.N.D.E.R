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
- **`g.npz`** : Pretrained weight of the models.
- **`generate_srgan.py`** : Script to generate a 16x superscaled image from a TMC2 image using the trained model.
- **`srgan_config.py`** : Configuration file for training, generating, and evaluation parameters.
- **`sam.py`**: Implements the Spectral Angle Mapper (SAM) function to calculate the angular similarity between predicted and original images for evaluating image quality.
- **`requirements.txt`** : Lists environment dependencies.
- **`cascade.py`** : An earlier version of the generation script (`generate_srgan.py`).
- **`utils.py`**: Contains utility functions for loading model state, saving checkpoints, and tracking training progress with metrics such as averages and summaries.


## Pretrained Models

- **Generator Model**: `g.npz`

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
python app.py
```

- this unzipped folder can also be used to run evaluation over other metrics
- per image size in this folder is 3840x3840 8-bit images


### Installations

```bash
pip install opencv-python numpy tqdm torch torchvision natsort typing scipy
## or
pip install -r requirements.txt
```
