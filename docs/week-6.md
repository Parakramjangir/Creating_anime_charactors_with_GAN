# Week 6: Conditional DCGAN Training on SafeBooru

## Objective

The objective of Week 6 was to train a Conditional DCGAN on the labelled SafeBooru full-body anime character dataset prepared in Week 5.

## Work Done

The SafeBooru subset created in Week 5 was used for model training. Each image was associated with a hair-color label, allowing the model to learn conditional image generation.

The selected classes were:

* black_hair
* blonde_hair
* brown_hair
* blue_hair
* pink_hair
* white_hair

A Conditional DCGAN architecture was implemented by adding label information to both the generator and discriminator.

## Model Architecture

The generator takes two inputs:

* random noise vector
* class label embedding

The discriminator takes:

* image
* class label information

This allows the model to generate images conditioned on a selected hair-color label.

## Training Setup

The model was trained on resized 64x64 RGB images using PyTorch. Binary Cross Entropy loss was used for both generator and discriminator training.

The training process included:

* loading labelled SafeBooru images using a custom PyTorch Dataset
* training the Conditional Generator and Conditional Discriminator
* saving generated samples at different epochs
* plotting generator and discriminator loss curves
* generating final label-wise sample outputs

## Results

The Conditional DCGAN was successfully trained on the SafeBooru subset. Generated outputs were saved for comparison and analysis.

Since full-body anime character generation is significantly harder than face-only generation, the generated images are less sharp than earlier anime face outputs. This is expected due to greater variation in pose, clothing, background, and body structure.

However, the Week 6 model successfully demonstrates the complete pipeline for label-conditioned full-body anime image generation.

## Outcome

By the end of Week 6, the project progressed from dataset preparation to training a Conditional DCGAN on a labelled full-body anime character dataset. The model outputs, loss curve, and final sample grid were saved for further analysis in Week 7.
