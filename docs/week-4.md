# Week 4 - Conditional GAN (cGAN)

## Idea

A Conditional GAN allows controlled generation by adding label information.

Instead of:
G(z) → image

We use:
G(z, y) → image

Where:
- z = noise vector
- y = condition (hair color, eye color, etc.)

Discriminator also becomes:
D(x, y) → real or fake

## Why this is useful

Unlike vanilla GANs, cGAN allows:
- Controlled image generation
- Better structured outputs
- More realistic attribute consistency

 ## Architecture Change

### Generator
Input:
- Noise vector (z)
- Label vector (y)

Output:
- Generated image conditioned on y

### Discriminator
Input:
- Image (x)
- Label (y)

Output:
- Probability real/fake

## Dataset Preparation Idea

To train a cGAN, images must have labels such as:

- hair_color: black, blonde, pink, blue
- eye_color: brown, green, red

Example:
image_001 → blue_hair + green_eyes
image_002 → black_hair + brown_eyes

These labels allow conditional generation.
