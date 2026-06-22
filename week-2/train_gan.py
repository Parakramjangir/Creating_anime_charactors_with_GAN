import torch
import torch.nn as nn
import torch.optim as optim

from models import Generator, Discriminator
from dataset import get_dataloader

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

latent_dim = 100
epochs = 20
batch_size = 64

dataloader = get_dataloader("anime_data")

G = Generator(latent_dim).to(device)
D = Discriminator().to(device)

criterion = nn.BCELoss()

optimizer_G = optim.Adam(
    G.parameters(),
    lr=0.0002,
    betas=(0.5, 0.999)
)

optimizer_D = optim.Adam(
    D.parameters(),
    lr=0.0002,
    betas=(0.5, 0.999)
)

for epoch in range(epochs):

    for imgs, _ in dataloader:

        imgs = imgs.to(device)

        real_labels = torch.ones(
            imgs.size(0), 1
        ).to(device)

        fake_labels = torch.zeros(
            imgs.size(0), 1
        ).to(device)

        # Train Discriminator

        optimizer_D.zero_grad()

        real_loss = criterion(
            D(imgs),
            real_labels
        )

        noise = torch.randn(
            imgs.size(0),
            latent_dim
        ).to(device)

        fake_imgs = G(noise)

        fake_loss = criterion(
            D(fake_imgs.detach()),
            fake_labels
        )

        d_loss = real_loss + fake_loss
        d_loss.backward()
        optimizer_D.step()

        # Train Generator

        optimizer_G.zero_grad()

        g_loss = criterion(
            D(fake_imgs),
            real_labels
        )

        g_loss.backward()
        optimizer_G.step()

    print(
        f"Epoch [{epoch+1}/{epochs}] "
        f"D Loss: {d_loss.item():.4f} "
        f"G Loss: {g_loss.item():.4f}"
    )
