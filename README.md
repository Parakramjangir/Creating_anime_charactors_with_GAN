# Anime Character Generation using GANs

## Seasons of Code 2026 - IIT Bombay

**Student:** Parakram Jangir (25B3926)

**Mentor:** Utkarsh Tanwar

---

## Project Overview

This project aims to generate anime-style character faces using Generative Adversarial Networks (GANs). The project progresses from understanding basic GAN concepts to implementing Deep Convolutional GANs (DCGANs) and Conditional GANs (cGANs) for controlled anime face generation.

The primary objective is to train models capable of learning the distribution of anime face datasets and generating realistic synthetic anime characters.

---

## Project Roadmap

### Week 1: GAN Fundamentals

* Studied GAN architecture
* Understood Generator and Discriminator networks
* Learned adversarial training and minimax optimization
* Explored various GAN architectures including DCGAN, WGAN, StyleGAN, and CycleGAN

### Week 2: Vanilla GAN

* Worked with the Anime Face Dataset
* Implemented and trained a basic GAN
* Generated anime faces from random latent vectors
* Analyzed GAN training behavior

### Week 3: Dataset Preprocessing and DCGAN

* Performed image preprocessing and normalization
* Studied dataset labeling techniques
* Implemented Deep Convolutional GAN (DCGAN)
* Compared performance with Vanilla GAN

### Week 4: Conditional GAN (cGAN)

* Studied Conditional GAN architecture
* Learned label-conditioned image generation
* Prepared datasets for attribute-based generation
* Explored controlled anime face synthesis

---

## Dataset

### Anime Face Dataset

https://www.kaggle.com/datasets/splcher/animefacedataset

### SafeBooru Dataset

https://www.kaggle.com/datasets/alamson/safebooru

---

## Technologies Used

* Python
* PyTorch
* NumPy
* Pandas
* Matplotlib
* OpenCV
* Jupyter Notebook

---

## Results

Training outputs and generated anime face samples will be uploaded in the `results` directory.

---

## Future Work

* Improve image quality and training stability
* Train larger Conditional GAN models
* Generate anime faces using user-defined attributes
* Explore advanced architectures such as StyleGAN

---

## Acknowledgements

This project is being developed under the IIT Bombay Seasons of Code program with guidance from mentor Utkarsh Tanwar.
