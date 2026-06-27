# Anime Character Generation using GANs

**Seasons of Code 2026 – IIT Bombay**

**Student:** Parakram Jangir (25B3926)
**Mentor:** Utkarsh Tanwar

---

## Project Overview

This project explores the fundamentals and practical implementation of **Generative Adversarial Networks (GANs)** for anime-style image generation.

Over four weeks, the project progresses from understanding the theoretical foundations of GANs to implementing increasingly advanced architectures including **Vanilla GAN**, **Deep Convolutional GAN (DCGAN)**, and **Conditional GAN (cGAN)**.

The primary objective is to understand how GANs learn image distributions and generate realistic synthetic images while building a strong foundation for future work on high-quality anime character generation.

---

## Repository Structure

```text
dataset/
    dataset_info.md

docs/
    week-1.md
    week-2.md
    week-3.md
    week-4.md

results/
    vanilla_gan/
    dcgan/
    cgan_mnist/

src/
    vanilla_gan/
    dcgan/
    cgan_mnist/

README.md
```

---

## Weekly Progress

### Week 1 – GAN Fundamentals

* Studied the architecture of GANs
* Understood the Generator and Discriminator
* Learned adversarial training and minimax optimization
* Explored GAN variants including DCGAN, WGAN, CycleGAN, and StyleGAN

---

### Week 2 – Vanilla GAN

* Worked with the Anime Face Dataset
* Implemented a Vanilla GAN using PyTorch
* Trained the model to generate anime faces
* Studied GAN training behaviour and convergence

---

### Week 3 – Deep Convolutional GAN (DCGAN)

* Performed dataset preprocessing and normalization
* Implemented a Deep Convolutional GAN (DCGAN)
* Compared DCGAN with Vanilla GAN
* Observed improvements in generated image quality and training stability

---

### Week 4 – Conditional GAN (cGAN)

* Studied the Conditional GAN architecture
* Implemented a Conditional GAN (cGAN) using the MNIST dataset
* Learned label-conditioned image generation using one-hot encoding
* Understood how conditional information is incorporated into both the Generator and Discriminator
* Generated images conditioned on class labels

> **Note:** A simple dataset (MNIST) was used for learning and implementing Conditional GANs before applying similar concepts to more complex datasets such as anime faces.

---

## Datasets

### Anime Face Dataset

Used for Vanilla GAN and DCGAN implementation.

### SafeBooru Dataset

Planned for future experiments involving attribute-conditioned anime face generation.

### MNIST Dataset

Used for implementing and understanding Conditional GANs (cGAN).

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

Generated samples for each implementation are available in the **results/** directory.

* Vanilla GAN
* DCGAN
* Conditional GAN (MNIST)

---

## Future Work

* Train Conditional GANs on anime face datasets
* Improve image quality and training stability
* Experiment with Wasserstein GAN (WGAN)
* Explore StyleGAN and StyleGAN2
* Generate anime faces using user-defined attributes

---

## Acknowledgements

This project was developed as part of **Seasons of Code 2026** at **IIT Bombay** under the guidance of **Utkarsh Tanwar**.
