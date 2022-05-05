# Flowers Classification using fastai & wandb

![Imgur](https://i.imgur.com/q7dwrcV.png)

In this repo we will build a simple classifier to distinguish an image into one of 17 possible flower categories using two different loss functions
1. Plain Cross Entropy Loss
2. Poly Loss
and compare the results by logging them to wandb. 

The project contains 3 notebooks as follows
1. `explore_data.ipynb`: This notebook is to understand the nature of problem at hand and the dataset
2. `vanilla_crossentropy.ipynb`: Here we build a classifier using simple cross-entropy loss function in fastai (which is the default loss function)
3. `poly1_loss.ipynb`: In this we build a classifier using poly1-loss which is [introduced here](https://arxiv.org/abs/2204.12511)

The comparison plots for different runs could be [viewed here](https://wandb.ai/vinayak_nayak/oxford_flowers_classification). 

The results of this experiment are explained in this post as well.
