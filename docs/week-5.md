# Week 5: SafeBooru Dataset Preparation

## Objective

The objective of Week 5 was to prepare a labelled full-body anime character dataset from SafeBooru for Conditional GAN training.

## Work Done

The SafeBooru metadata file `all_data.csv` was used to filter suitable anime character images. Since the dataset contained metadata and image URLs instead of direct image files, a filtered subset was created and the selected images were downloaded separately.

Images were filtered using the following conditions:

* Safe-rated images only
* `solo`
* `1girl`
* `full_body`

After filtering, six hair-color labels were selected for conditional generation:

* black_hair
* blonde_hair
* brown_hair
* blue_hair
* pink_hair
* white_hair

A balanced subset was created with images from each class. A smaller test subset was downloaded first to verify the pipeline.

## Dataset Summary

The filtered metadata contained over 100,000 suitable full-body anime image entries. From this, a balanced subset of 3,000 metadata entries was created, with 500 entries per hair-color class.

For initial testing, 600 images were selected and 501 images were successfully downloaded and processed.

## Preprocessing

The downloaded images were:

* Converted to RGB format
* Resized to 64x64
* Normalized to the range `[-1, 1]`
* Loaded using a custom PyTorch Dataset and DataLoader

## Outcome

By the end of Week 5, the SafeBooru dataset pipeline was completed. The filtered dataset can now be used for training a Conditional DCGAN in Week 6.
