# Week 4 – Conditional GAN (cGAN)

## Objective

This week focused on understanding and implementing a **Conditional Generative Adversarial Network (cGAN)**. Unlike a standard GAN, a cGAN allows the generation of images conditioned on a given class label, enabling controlled image generation.

---

## Dataset

* **Dataset:** MNIST Handwritten Digits
* **Classes:** 10 (Digits 0–9)
* **Image Size:** 28 × 28 (Grayscale)

A simple dataset was chosen to better understand the concept of conditional image generation before applying it to more complex datasets.

---

## What I Learned

* Difference between GAN, DCGAN, and cGAN.
* One-hot encoding of class labels.
* Conditioning both the Generator and Discriminator using class information.
* Concatenating noise vectors with labels for the Generator.
* Concatenating image tensors with label maps for the Discriminator.
* Training a Conditional GAN using PyTorch.

---

## Model Overview

### Generator

* Takes a random noise vector and a class label as input.
* Concatenates the noise vector with the one-hot encoded label.
* Generates an image corresponding to the specified class.

### Discriminator

* Takes an image and its corresponding class label.
* Concatenates the image with the label map.
* Predicts whether the image is real or generated while considering the provided label.

---

## Training Configuration

* Epochs: 20
* Batch Size: 128
* Learning Rate: 0.0002
* Loss Function: BCEWithLogitsLoss
* Optimizer: Adam

---

## Results

The model successfully learned to generate handwritten digits conditioned on the supplied class labels. Generated sample images are available in the `results/cgan_mnist/` directory.

---

## References

* Conditional Generative Adversarial Nets (Mirza & Osindero, 2014)
* Deep Convolutional GAN (DCGAN) Paper
* PyTorch Documentation
* PyTorch Conditional GAN implementation tutorials

---

## Outcome

By the end of Week 4, I successfully implemented and understood a Conditional GAN (cGAN), gaining practical experience with controlled image generation and conditional deep learning models.
