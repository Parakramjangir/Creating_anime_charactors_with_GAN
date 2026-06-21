# Dataset Information

## Dataset Used

### Anime Face Dataset

Source:
https://www.kaggle.com/datasets/splcher/animefacedataset

The Anime Face Dataset was used as the primary dataset for training the GAN models in this project. The dataset contains anime-style character face images collected for generative modeling tasks.

## Dataset Purpose

The dataset is used to train Generative Adversarial Networks (GANs) capable of generating realistic anime character faces. It serves as the foundation for Vanilla GAN, DCGAN, and Conditional GAN experiments conducted during the project.

## Dataset Characteristics

* Image Type: Anime character faces
* Format: JPG/PNG images
* Color Space: RGB
* Domain: Anime face generation

## Preprocessing Performed

The following preprocessing steps were applied before training:

1. Image loading and verification.
2. Resizing images to a fixed resolution suitable for training.
3. Conversion to RGB format where necessary.
4. Normalization of pixel values to the range [-1, 1].
5. Removal of corrupted or unreadable images.
6. Organization of images into a structured dataset directory.

## Dataset Labeling

For Conditional GAN experiments, images may be labeled using simple visual attributes such as:

* Hair Color

  * Black Hair
  * Blonde Hair
  * Brown Hair
  * Blue Hair
  * Pink Hair

* Eye Color

  * Blue Eyes
  * Green Eyes
  * Brown Eyes
  * Red Eyes

These labels enable controlled image generation using Conditional GANs.

## Future Improvements

* Expand the labeled dataset.
* Improve label quality and balance.
* Introduce additional attributes such as hair length and facial expressions.
* Explore automated label extraction techniques.
