# Datasets Information

## Datasets Used

---

## 1. Anime Face Dataset

**Source:**
https://www.kaggle.com/datasets/splcher/animefacedataset

### Description

A dataset containing over 63,000 anime-style face images. It was used to learn and implement generative models capable of synthesizing anime character faces.

### Purpose

* Training the Vanilla GAN
* Training the DCGAN
* Learning image generation using adversarial networks

### Applications

* Anime face generation
* GAN training
* DCGAN training
* Image synthesis experiments

---

## 2. MNIST Handwritten Digits Dataset

**Source:**
https://pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html

### Description

A benchmark dataset containing 70,000 grayscale handwritten digit images (0–9) with corresponding class labels.

### Purpose

Used to implement and understand **Conditional Generative Adversarial Networks (cGANs)**. The labeled nature of the dataset makes it well suited for learning conditional image generation.

### Applications

* Conditional GAN (cGAN) training
* Label-conditioned image generation
* Controlled image synthesis

---

## 3. SafeBooru Dataset

**Source:** 
https://www.kaggle.com/datasets/alamson/safebooru

### Description

An anime-style image dataset containing tagged character images with diverse poses, clothing, and visual attributes. In this project, it is used to create a filtered full-body anime character subset for training a Conditional DCGAN.

### Purpose

For the final stage of the project, the SafeBooru dataset is used for full-body anime character generation using a Conditional DCGAN.

SafeBooru is more challenging than the anime face dataset because it contains:

* Full-body characters
* Different poses
* Varied clothing
* Complex backgrounds
* Greater image diversity



---

## Summary

The project starts with anime face generation using Vanilla GAN and DCGAN. It then moves toward labelled data and Conditional GANs. For the final stage, a filtered SafeBooru subset is used to train a Conditional DCGAN for label-controlled full-body anime character generation.

