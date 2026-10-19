# Notebook cell 3
#@title Setup (run once)
# Supplied support code and images are embedded: no separate files are needed.
import os, sys, time, io, base64, zipfile, hashlib
from pathlib import Path
_cs180_started = time.perf_counter()
IN_COLAB = 'google.colab' in sys.modules
IN_KAGGLE = Path('/kaggle/working').is_dir()
PART = 'partb'
_work = Path('/content/cs180-hw3') if IN_COLAB else (Path('/kaggle/working') if IN_KAGGLE else Path.cwd())
_work.mkdir(parents=True,exist_ok=True)
_support = base64.b64decode('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')
assert hashlib.sha256(_support).hexdigest() == 'ba2fae2d7267a416d94cd581fd0ac5eadf93d641618063a782d0dffdc36d31cd', 'Damaged notebook support data'
with zipfile.ZipFile(io.BytesIO(_support)) as _archive:
    for _entry in _archive.infolist():
        _target=(_work/_entry.filename).resolve()
        if _work.resolve() not in _target.parents: raise ValueError('Unsafe embedded path')
    _archive.extractall(_work)
os.chdir(_work)
if str(_work) not in sys.path: sys.path.insert(0,str(_work))
from colab_setup import configure
configure(PART,install_dependencies=IN_COLAB or IN_KAGGLE)
print('Setup complete. Continue with the notebook below.')

# Notebook cell 5
# Install requirements-partb.txt in the active environment before running.
# No automatic package changes to an existing GPU environment.
import sys
assert sys.version_info >= (3,9), 'Use Python 3.9 or newer.'

# Notebook cell 6
import os, json, time, random
from pathlib import Path
from typing import Optional
import numpy as np
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torchvision.utils import make_grid
import matplotlib.pyplot as plt

SEED = 180
random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)
torch.set_num_threads(4)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
torch.backends.cudnn.benchmark = True
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True
GROUP = os.environ.get('PARTB_GROUP','all')
assert GROUP in ('all','denoise','time','class','no_scheduler')
OUT = Path('results/partb') / GROUP
OUT.mkdir(parents=True, exist_ok=True)
metrics = {'seed':SEED,'group':GROUP,'torch':torch.__version__,
           'device':str(device),'gpu':torch.cuda.get_device_name() if device.type=='cuda' else None,
           'visible_devices':os.environ.get('CUDA_VISIBLE_DEVICES'),
           'precision':'float32 with TF32 convolution/matmul enabled'}
print(metrics)
train_dataset = MNIST('data', train=True, download=True, transform=ToTensor())
test_dataset = MNIST('data', train=False, download=True, transform=ToTensor())
assert len(train_dataset)==60000 and len(test_dataset)==10000

def show_grid(images, title, filename, nrow=10):
    images = images.detach().float().cpu()
    grid = make_grid(images.clamp(0, 1), nrow=nrow, padding=2)
    fig, ax = plt.subplots(figsize=(12, max(2, len(images)/nrow*1.15)))
    ax.imshow(grid.permute(1, 2, 0)); ax.set_title(title); ax.axis('off')
    fig.tight_layout(); fig.savefig(OUT / filename, dpi=120)
    plt.show(); plt.close(fig)


def loss_plot(losses, name):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(losses, alpha=.4, linewidth=.5)
    window = min(100, len(losses))
    smooth = torch.tensor(losses).unfold(0, window, 1).mean(1)
    ax.plot(range(window-1, len(losses)), smooth, linewidth=1)
    ax.set(xlabel='Optimizer step', ylabel='Mean squared error', title=name)
    fig.tight_layout(); fig.savefig(OUT / (name+'_loss.png'), dpi=120)
    plt.show(); plt.close(fig)


def make_loader(batch_size, seed=180):
    # Decode/normalize once; augmentation noise is still drawn fresh in each step.
    dataset = torch.utils.data.TensorDataset(train_dataset.data[:, None].float()/255,
                                             train_dataset.targets)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=0,
                      pin_memory=device.type == 'cuda',
                      generator=torch.Generator().manual_seed(seed))

# Notebook cell 11
class Conv(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, 1, 1),
            nn.BatchNorm2d(out_channels),
            nn.GELU(),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====

        # ===== end of code ====
        return self.net(x)


class DownConv(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, 2, 1),
            nn.BatchNorm2d(out_channels),
            nn.GELU(),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====
        return self.net(x)
        # ===== end of code ====


class UpConv(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            nn.ConvTranspose2d(in_channels, out_channels, 4, 2, 1),
            nn.BatchNorm2d(out_channels),
            nn.GELU(),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====
        return self.net(x)
        # ===== end of code ====


class Flatten(nn.Module):
    def __init__(self):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            nn.AvgPool2d(7),
            nn.GELU(),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====
        return self.net(x)
        # ===== end of code ====


class Unflatten(nn.Module):
    def __init__(self, in_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            nn.ConvTranspose2d(in_channels, in_channels, 7, 7, 0),
            nn.BatchNorm2d(in_channels),
            nn.GELU(),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====

        # ===== end of code ====
        return self.net(x)


class ConvBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            Conv(in_channels, out_channels),
            Conv(out_channels, out_channels),
        )

        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====

        # ===== end of code ====
        return self.net(x)


class DownBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            DownConv(in_channels, out_channels),
            ConvBlock(out_channels, out_channels),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====

        # ===== end of code ====
        return self.net(x)


class UpBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            UpConv(in_channels, out_channels),
            ConvBlock(out_channels, out_channels),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====

        # ===== end of code ====
        return self.net(x)

# Notebook cell 13
class UnconditionalUNet(nn.Module):
    def __init__(
        self,
        in_channels: int,
        num_hiddens: int,
    ):
        super().__init__()
        # ===== your code here! ====
        D = num_hiddens

        self.conv = ConvBlock(in_channels, D)

        self.down1 = DownBlock(D, D)
        self.down2 = DownBlock(D, 2 * D)

        self.flatten = Flatten()
        self.unflatten = Unflatten(2 * D)

        self.up1 = UpBlock(4 * D, D)
        self.up2 = UpBlock(2 * D, D)

        self.final_block = ConvBlock(2 * D, D)
        self.output = nn.Conv2d(D, in_channels, 3, 1, 1)
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        assert x.shape[-2:] == (28, 28), "Expect input shape to be (28, 28)."
        # ===== your code here! ====
        x0 = self.conv(x)
        x1 = self.down1(x0)
        x2 = self.down2(x1)

        bottleneck = self.flatten(x2)
        u0 = self.unflatten(bottleneck)

        u1 = self.up1(torch.cat([u0, x2], dim=1))
        u2 = self.up2(torch.cat([u1, x1], dim=1))

        features = self.final_block(
            torch.cat([u2, x0], dim=1)
        )
        return self.output(features)
        # ===== end of code ====

# Notebook cell 15
# Visualize images at different noisy level
# ===== your code here! ====
images = []

for digit in range(10):
    index = (test_dataset.targets == digit).nonzero()[0].item()
    image, _ = test_dataset[index]
    images.append(image)

images = torch.stack(images)

noise = torch.randn_like(images)

for sigma in [0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0]:
    noisy_images = images + sigma * noise

    show_grid(
        noisy_images,
        f"Noise level σ = {sigma} — digits 0–9",
        f"noising_sigma_{sigma}.png",
        nrow=10,
    )
# ===== end of code ====

# Notebook cell 18
# Complete the recommended denoising hyperparameters from Section 1.2.1.
batch_size = 256
learning_rate = 1e-4
noise_level = 0.5
hidden_dim = 128
num_epochs = 5

# Notebook cell 19
# MNIST train_dataset/test_dataset were loaded in setup.
# Build shuffled training and non-shuffled test DataLoaders.
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True,
)

test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    shuffle=False,
)

# Notebook cell 20
# Define your model, optimizer, and loss
# ===== your code here! ====
model = UnconditionalUNet(1, hidden_dim).to(device)

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=learning_rate,
)

criterion = nn.MSELoss()
# ===== end of code ====

# Notebook cell 21
testimgs = []
for digit in range(10):
  index = (test_dataset.targets == digit).nonzero()[0].item() #how i got first valid index
  validimage, _ = test_dataset[index]
  testimgs.append(validimage)

testimgs = torch.stack(testimgs).to(device)
testnoise = torch.randn_like(testimgs)
testnoisy = testimgs + 0.5 * testnoise

# Notebook cell 22


# Notebook cell 23
# The training loops
from tqdm.auto import tqdm
train_losses = []
for epoch in range(num_epochs):
    model.train()
    for i, (images, _) in enumerate(tqdm(train_loader)):

        # ===== your code here! ====
        images = images.to(device)
        noisy = images + noise_level * torch.randn_like(images)
        outputs = model(noisy)

        # ===== end of code ====

        loss = criterion(outputs, images)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        train_losses.append(loss.item())

    if epoch + 1 in [1,5]:
      model.eval()

      with torch.no_grad():
        results = model(testnoisy)
      show_grid(
          torch.cat([testimgs, testnoisy, results]),
          f"Epoch {epoch + 1}: clean / noisy / denoised — digits 0–9",
          f"denoiser_epoch_{epoch + 1}.png",
          nrow=10,
      )

      torch.save(
          model.state_dict(),
          OUT / f"denoiser_epoch_{epoch + 1}.pt",
      )

# Notebook cell 24
# Visualize your training curve
# ===== your code here! ====
loss_plot(train_losses, "denoiser")

torch.save(
    train_losses,
    OUT / "denoiser_losses.pt",
)
# ===== end of code ====

# Notebook cell 26
# Visualize OOD testing
# ===== your code here! ====
model.eval()

for sigma in [0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0]:
    noisy_images = testimgs + sigma * testnoise

    with torch.no_grad():
        predictions = model(noisy_images)

    show_grid(
        torch.cat([
            testimgs,
            noisy_images,
            predictions,
        ]),
        (
            f"OOD σ={sigma}, trained at σ=0.5 — "
            "rows: original / noisy / denoised; columns: 0–9"
        ),
        f"ood_sigma_{sigma}.png",
        nrow=10,
    )
# ===== end of code ====

# Notebook cell 28
# Section 1.2.3: train a fresh D=128 UNet for 5 epochs, Adam lr=1e-4,
# batch size 256. Input is independent Gaussian noise, target is a clean digit.
# Plot losses, show held-out results at epochs 1 and 5, and explain averaging.

freshmodel=UnconditionalUNet(1,128).to(device)
freshopt=torch.optim.Adam(freshmodel.parameters(),lr=1e-4)
lossfn=nn.MSELoss()
losses=[]
freshnoise=torch.randn_like(testimgs)
for epoch in range(5):
    freshmodel.train()
    for images,label in train_loader:
        images=images.to(device)
        noise=torch.randn_like(images)

        outputs=freshmodel(noise)
        loss=lossfn(outputs,images)

        freshopt.zero_grad()
        loss.backward()
        freshopt.step()
        losses.append(loss.item())
    print("Finished epoch",epoch+1)
# Display and save the loss curve across the entire training run.

    if epoch+1 in [1,5]:
        freshmodel.eval()
        with torch.no_grad():
            results=freshmodel(freshnoise)
        show_grid(
            torch.cat([freshnoise,results]),
            f"Epoch {epoch+1}: pure noise / prediction",
            f"pure_noise_epoch_{epoch+1}.png",
            nrow=10,
        )
        torch.save(freshmodel.state_dict(),OUT/f"pure_noise_epoch_{epoch+1}.pt")
loss_plot(losses,"pure_noise")



# Notebook cell 31
class FCBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        # ===== your code here! ====
        self.net = nn.Sequential(
            nn.Linear(in_channels, out_channels),
            nn.GELU(),
            nn.Linear(out_channels, out_channels),
        )
        # ===== end of code ====

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # ===== your code here! ====
        return self.net(x)
        # ===== end of code ====



class TimeConditionalUNet(nn.Module):
    def __init__(
        self,
        in_channels: int,
        num_classes: int,
        num_hiddens: int,
    ):
        super().__init__()
        # ===== your code here! ====
        Ddims = num_hiddens

        self.conv = ConvBlock(in_channels, Ddims)
        self.down1 = DownBlock(Ddims, Ddims)
        self.down2 = DownBlock(Ddims, 2 * Ddims)

        self.flatten = Flatten()
        self.unflatten = Unflatten(2 * Ddims)

        self.up1 = UpBlock(4 * Ddims, Ddims)
        self.up2 = UpBlock(2 * Ddims, Ddims)

        self.final_block = ConvBlock(2 * Ddims, Ddims)
        self.output = nn.Conv2d(Ddims, in_channels, 3, 1, 1)

        self.fc1 = FCBlock(1, 2 * Ddims)
        self.fc2 = FCBlock(1, Ddims)
        # ===== end of code ====

    def forward(
        self,
        x: torch.Tensor,
        t: torch.Tensor,
    ) -> torch.Tensor:
        """
        Args:
            x: (N, C, H, W) input tensor.
            t: (N,) normalized time tensor.

        Returns:
            (N, C, H, W) output tensor.
        """
        assert x.shape[-2:] == (28, 28), "Expect input shape to be (28, 28)."
        # ===== your code here! ====
        compatibletforlinearblock = t.reshape(-1, 1)
        compatibleforunflatten = self.fc1(compatibletforlinearblock)[:, :, None, None]
        compatibleforupblock = self.fc2(compatibletforlinearblock)[:, :, None, None]

        x0 = self.conv(x)
        x1 = self.down1(x0)
        x2 = self.down2(x1)

        bottleneck = self.flatten(x2)
        u0 = self.unflatten(bottleneck)
        u0 = u0 * compatibleforunflatten

        u1 = self.up1(torch.cat([u0, x2], dim=1))
        u1 = u1 * compatibleforupblock

        u2 = self.up2(torch.cat([u1, x1], dim=1))

        features = self.final_block(
            torch.cat([u2, x0], dim=1)
        )
        return self.output(features)
        # ===== end of code ====

# Notebook cell 33
def time_fm_forward(
    unet: TimeConditionalUNet,
    x_1: torch.Tensor,
    num_ts: int,
) -> torch.Tensor:
    """Algorithm 1

    Args:
        unet: TimeConditionalUNet
        x_1: (N, C, H, W) input tensor.
        num_ts: int, number of timesteps.
    Returns:
        (,) loss.
    """
    unet.train()
    # ===== your code here! ====

    noise = torch.randn_like(x_1)
    t = torch.rand(x_1.shape[0], device=x_1.device)
    time = t[:, None, None, None]
    mixed = (1 - time) * noise + time * x_1
    prediction = unet(mixed, t)
    return ((prediction - (x_1 - noise)) ** 2).mean()
    # ===== end of code ====


# Notebook cell 34
@torch.inference_mode()
def time_fm_sample(
    unet: TimeConditionalUNet,
    img_wh: tuple[int, int],
    num_ts: int,
    seed: int = 0,
) -> torch.Tensor:
    """Algorithm 2

    Args:
        unet: TimeConditionalUNet
        img_wh: (H, W) output image width and height.
        num_ts: int, number of timesteps.
        seed: int, random seed.

    Returns:
        (N, C, H, W) final sample.
    """
    unet.eval()
    # ===== your code here! ====
    device = next(unet.parameters()).device
    generator = torch.Generator(device=device).manual_seed(seed)
    images = torch.randn(
        40, 1, *img_wh,
        device=device,
        generator=generator,
    )
    for step in range(num_ts):
        # have to create a tensor full of the timsteps -- images.shape[0] times
        t = torch.full(
            (images.shape[0],),
            step / num_ts,
            device=device,
        )
        images = images + unet(images, t) / num_ts #this is the euler integration -- divided by num_ts
    return images
    # ===== end of code ====


# Notebook cell 35
class TimeConditionalFM(nn.Module):
    def __init__(
        self,
        unet: TimeConditionalUNet,
        num_ts: int = 50,
        img_hw: tuple[int, int] = (28, 28),
    ):
        super().__init__()

        self.unet = unet
        self.num_ts = num_ts
        self.img_hw = img_hw


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (N, C, H, W) input tensor.

        Returns:
            (,) flow-matching loss.
        """
        return time_fm_forward(
            self.unet, x, self.num_ts
        )


    @torch.inference_mode()
    def sample(
        self,
        img_wh: tuple[int, int],
        seed: int = 0,
    ):
        return time_fm_sample(
            self.unet, img_wh, self.num_ts, seed
        )

# Notebook cell 37
# Feel free to use code from part 1.2.1
# as they should be very similar
# ===== your code here! ====

timeloader = DataLoader(train_dataset, batch_size=64, shuffle=True)
timeunet = TimeConditionalUNet(1, 10, 64).to(device)
timemodel = TimeConditionalFM(timeunet).to(device)
timeopt = torch.optim.Adam(timemodel.parameters(), lr=1e-2)
scheduler = torch.optim.lr_scheduler.ExponentialLR(
    timeopt, gamma=0.1 ** (1 / 10)
)
timelosses = []

for epoch in range(10):
    timemodel.train()
    for images, labels in tqdm(timeloader):
        images = images.to(device)
        loss = timemodel(images)
        timeopt.zero_grad()
        loss.backward()
        timeopt.step()
        timelosses.append(loss.item())

    scheduler.step()
    print("Finished epoch", epoch + 1)

    if epoch + 1 in [1, 5, 10]:
        torch.save(
            timemodel.state_dict(),
            OUT / f"time_epoch_{epoch + 1}.pt",
        )
        samples = timemodel.sample((28, 28), seed=0)
        show_grid(
            samples,
            f"Time-conditioned generation: epoch {epoch + 1}",
            f"time_epoch_{epoch + 1}.png",
            nrow=10,
        )

loss_plot(timelosses, "time_conditioned")
torch.save(timelosses, OUT / "time_losses.pt")
# ===== end of code ====

# Notebook cell 39
# Sampling from the UNet
# ===== your code here! ====
for epoch in [1, 5, 10]:
    timemodel.load_state_dict(
        torch.load(
            OUT / f"time_epoch_{epoch}.pt",
            map_location=device,
            weights_only=True,
        )
    )
    samples = timemodel.sample((28, 28), seed=0)
    show_grid(
        samples,
        f"Time-conditioned generation: epoch {epoch}",
        f"time_epoch_{epoch}.png",
        nrow=10,
    )
# ===== end of code ====

# Notebook cell 41
class ClassConditionalUNet(nn.Module):
    def __init__(
        self,
        in_channels: int,
        num_classes: int,
        num_hiddens: int,
    ):
        super().__init__()
        # ===== your code here! ====
        D = num_hiddens
        self.numclasses = num_classes

        self.conv = ConvBlock(in_channels, D)
        self.down1 = DownBlock(D, D)
        self.down2 = DownBlock(D, 2 * D)
        self.flatten = Flatten()
        self.unflatten = Unflatten(2 * D)
        self.up1 = UpBlock(4 * D, D)
        self.up2 = UpBlock(2 * D, D)
        self.final_block = ConvBlock(2 * D, D)
        self.output = nn.Conv2d(D, in_channels, 3, 1, 1)

        self.time1 = FCBlock(1, 2 * D)
        self.time2 = FCBlock(1, D)
        self.class1 = FCBlock(num_classes, 2 * D)
        self.class2 = FCBlock(num_classes, D)
        # ===== end of code ====

    def forward(
        self,
        x: torch.Tensor,
        c: torch.Tensor,
        t: torch.Tensor,
        mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        Args:
            x: (N, C, H, W) input tensor.
            c: (N,) int64 condition tensor.
            t: (N,) normalized time tensor.
            mask: (N,) mask tensor. If not None, mask out condition when mask == 0.

        Returns:
            (N, C, H, W) output tensor.
        """
        assert x.shape[-2:] == (28, 28), "Expect input shape to be (28, 28)."
        # ===== your code here! ====
        c = torch.nn.functional.one_hot(c, self.numclasses).float()

        if mask is not None:
          c = c * mask[:,None]

        t = t.reshape(-1, 1)
        t1 = self.time1(t)[:, :, None, None]
        t2 = self.time2(t)[:, :, None, None]
        c1 = self.class1(c)[:, :, None, None]
        c2 = self.class2(c)[:, :, None, None]

        x0 = self.conv(x)
        x1 = self.down1(x0)
        x2 = self.down2(x1)

        u0 = self.unflatten(self.flatten(x2))
        u0 = c1 * u0 + t1

        u1 = self.up1(torch.cat([u0, x2], dim=1))
        u1 = c2 * u1 + t2

        u2 = self.up2(torch.cat([u1, x1], dim=1))
        features = self.final_block(torch.cat([u2, x0], dim=1))
        return self.output(features)
        # ===== end of code ====


# Notebook cell 42


# Notebook cell 43
def class_fm_forward(
    unet: ClassConditionalUNet,
    x_1: torch.Tensor,
    c: torch.Tensor,
    p_uncond: float,
    num_ts: int,
) -> torch.Tensor:
    """Algorithm 3

    Args:
        unet: ClassConditionalUNet
        x_1: (N, C, H, W) input tensor.
        c: (N,) int64 condition tensor.
        p_uncond: float, probability of unconditioning the condition.
        num_ts: int, number of timesteps.

    Returns:
        (,) loss.
    """
    unet.train()
    # ===== your code here! ====
    noise = torch.randn_like(x_1)
    t = torch.rand(x_1.shape[0], device=x_1.device)
    time = t[:, None, None, None]
    mixed = (1 - time) * noise + time * x_1
    mask = (torch.rand(x_1.shape[0], device=x_1.device) >= p_uncond).float()
    prediction = unet(mixed, c, t, mask)
    return ((prediction - (x_1 - noise)) ** 2).mean()
    # ===== end of code ====


# Notebook cell 44
@torch.inference_mode()
def class_fm_sample(
    unet: ClassConditionalUNet,
    c: torch.Tensor,
    img_wh: tuple[int, int],
    num_ts: int,
    guidance_scale: float = 5.0,
    seed: int = 0,
) -> torch.Tensor:
    """Algorithm 4

    Args:
        unet: ClassConditionalUNet
        c: (N,) int64 condition tensor. Only for class-conditional
        img_wh: (H, W) output image width and height.
        num_ts: int, number of timesteps.
        guidance_scale: float, CFG scale.
        seed: int, random seed.

    Returns:
        (N, C, H, W) final sample.
        (N, T_animation, C, H, W) caches.
    """
    unet.eval()
    # ===== your code here! ====
    device = next(unet.parameters()).device
    c = c.to(device)
    generator = torch.Generator(device=device).manual_seed(seed)
    images = torch.randn(
        len(c), 1, *img_wh,
        device=device,
        generator=generator,
    )
    mask = torch.zeros(len(c), device=device)
    caches = [images.clone()]

    for step in range(num_ts):
        t = torch.full((len(c),), step / num_ts, device=device)
        unconditional = unet(images, c, t, mask)
        conditional = unet(images, c, t)
        velocity = unconditional + guidance_scale * (
            conditional - unconditional
        )
        images = images + velocity / num_ts

        if (step + 1) % 10 == 0 or step + 1 == num_ts:
            caches.append(images.clone())

    return images, torch.stack(caches, dim=1)
    # ===== end of code ====


# Notebook cell 45
class ClassConditionalFM(nn.Module):
    def __init__(
        self,
        unet: ClassConditionalUNet,
        num_ts: int = 300,
        p_uncond: float = 0.1,
    ):
        super().__init__()
        self.unet = unet
        self.num_ts = num_ts
        self.p_uncond = p_uncond

    def forward(self, x: torch.Tensor, c: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (N, C, H, W) input tensor.
            c: (N,) int64 condition tensor.

        Returns:
            (,) loss.
        """
        return class_fm_forward(
            self.unet, x, c, self.p_uncond, self.num_ts
        )

    @torch.inference_mode()
    def sample(
        self,
        c: torch.Tensor,
        img_wh: tuple[int, int],
        guidance_scale: float = 5.0,
        seed: int = 0,
    ):
        return class_fm_sample(
            self.unet, c, img_wh, self.num_ts, guidance_scale, seed
        )

# Notebook cell 47
# Train a fresh class-conditioned D=64 UNet for 10 epochs, batch size 64,
# Adam initial lr=1e-2, class dropout probability .1, exponential gamma=.1**(1/10).
# Save checkpoints at epochs 1,5,10. Then train an independent no-scheduler
# comparison; choose/document a constant learning rate and compare results.

loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

model = ClassConditionalFM(ClassConditionalUNet(1, 10, 64)).to(device)
opt = torch.optim.Adam(model.parameters(), lr=0.01)
scheduler = torch.optim.lr_scheduler.ExponentialLR(opt, gamma=0.1**(1/10))
losses = []

for epoch in range(10):
    model.train()
    for imgs, labels in tqdm(loader):
        imgs = imgs.to(device)
        labels = labels.to(device)
        loss = model(imgs, labels)
        opt.zero_grad()
        loss.backward()
        opt.step()
        losses.append(loss.item())

    scheduler.step()
    print("With scheduler: finished epoch", epoch+1)
    if epoch+1 in [1, 5, 10]:
        torch.save(model.state_dict(), OUT/f"class_epoch_{epoch+1}.pt")

loss_plot(losses, "class")
torch.save(losses, OUT/"class_losses.pt")

model2 = ClassConditionalFM(ClassConditionalUNet(1, 10, 64)).to(device)
opt2 = torch.optim.Adam(model2.parameters(), lr=0.001)
losses2 = []

for epoch in range(10):
    model2.train()
    for imgs, labels in tqdm(loader):
        imgs = imgs.to(device)
        labels = labels.to(device)
        loss = model2(imgs, labels)
        opt2.zero_grad()
        loss.backward()
        opt2.step()
        losses2.append(loss.item())

    print("Without scheduler: finished epoch", epoch+1)
    if epoch+1 in [1, 5, 10]:
        torch.save(
            model2.state_dict(),
            OUT/f"class_no_scheduler_epoch_{epoch+1}.pt"
        )

loss_plot(losses2, "class_no_scheduler")
torch.save(losses2, OUT/"class_no_scheduler_losses.pt")

# Notebook cell 48
loss_plot(losses2, "class_no_scheduler")
torch.save(losses2, OUT/"class_no_scheduler_losses.pt")

# Notebook cell 50
# At epochs 1,5,10, generate four instances of each digit (40 images),
# with 300 Euler steps and guidance scale 5.0. Keep seeds fixed for comparisons.
# Also visualize the no-scheduler model and describe the tradeoff.
labels = torch.arange(10, device=device).repeat(4)

for epoch in [1, 5, 10]:
    model.load_state_dict(torch.load(
        OUT/f"class_epoch_{epoch}.pt",
        map_location=device,
        weights_only=True
    ))
    imgs, frames = model.sample(labels, (28, 28), guidance_scale=5, seed=0)
    show_grid(
        imgs,
        f"With scheduler: epoch {epoch}",
        f"class_epoch_{epoch}.png",
        nrow=10
    )

    model2.load_state_dict(torch.load(
        OUT/f"class_no_scheduler_epoch_{epoch}.pt",
        map_location=device,
        weights_only=True
    ))
    imgs, frames = model2.sample(labels, (28, 28), guidance_scale=5, seed=0)
    show_grid(
        imgs,
        f"Without scheduler: epoch {epoch}",
        f"class_no_scheduler_epoch_{epoch}.png",
        nrow=10
    )