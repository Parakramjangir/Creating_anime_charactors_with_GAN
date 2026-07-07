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

##3. SafeBooru Dataset
   Source: Kaggle SafeBooru Dataset

Description
A large anime-style image dataset containing tagged character illustrations from SafeBooru. Unlike the Anime Face Dataset, this dataset includes more diverse images such as full-body characters, different poses, clothing styles, backgrounds, and visual attributes. The tags available with the images can be used to create labelled data for Conditional GAN training.

Purpose
Creating a labelled full-body anime character dataset
Training the Conditional GAN / Conditional DCGAN
Generating anime characters based on selected labels
Moving from face-only generation to full-body character generation

Applications
Full-body anime character generation
Conditional GAN training
Label-controlled image synthesis
Anime image generation experiments
Dataset filtering using tags
# Dataset Information

This project uses anime image datasets for training different GAN models. The dataset usage gradually moves from simple anime face generation to labelled full-body anime character generation for the final Conditional GAN model.

---

## 3. SafeBooru Dataset

**Source:** SafeBooru Dataset
**Platform:** Kaggle

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

