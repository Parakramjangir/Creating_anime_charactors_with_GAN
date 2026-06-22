# Week 2 - Vanilla GAN on Anime Face Dataset

## Objective

Implement and train a basic Generative Adversarial Network (GAN) on an anime face dataset to understand the adversarial training process.

## Dataset

Dataset Used:
https://www.kaggle.com/datasets/splcher/animefacedataset

Total Images: 63,565

## Preprocessing

- Loaded anime face images using a custom PyTorch Dataset class.
- Resized images to 64 × 64.
- Converted images to RGB format.
- Normalized pixel values to the range [-1, 1].
- Created DataLoader with batch size 64.

## GAN Architecture

### Generator

- Input: 100-dimensional latent vector
- Fully connected layers:
  - 100 → 256
  - 256 → 512
  - 512 → 1024
  - 1024 → 64×64×3
- Activation:
  - ReLU
  - Tanh

### Discriminator

- Input: 64×64×3 image
- Fully connected layers:
  - 64×64×3 → 1024
  - 1024 → 512
  - 512 → 256
  - 256 → 1
- Activation:
  - LeakyReLU
  - Sigmoid

## Training

Loss Function:
- Binary Cross Entropy Loss (BCELoss)

Optimizer:
- Adam
- Learning Rate = 0.0002

Training Epochs:
- 5

### Training Logs

Epoch 1:
D Loss = 0.0305
G Loss = 5.9383

Epoch 2:
D Loss = 0.3800
G Loss = 2.7611

Epoch 3:
D Loss = 0.0366
G Loss = 4.1899

Epoch 4:
D Loss = 0.6249
G Loss = 2.0049

Epoch 5:
D Loss = 1.1666
G Loss = 2.4351

## Outcomes

- Successfully implemented a Vanilla GAN using PyTorch.
- Trained on the Anime Face Dataset.
- Generated synthetic anime face samples.
- Observed adversarial training behavior between Generator and Discriminator.

## Challenges

- Understanding dataset structure on Kaggle.
- Implementing a custom dataset loader.
- Interpreting GAN training losses.
