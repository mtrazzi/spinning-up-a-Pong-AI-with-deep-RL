# Spinning Up a Pong AI With Deep Reinforcement Learning

<p align="center">
<img src="https://blog.floydhub.com/content/images/2018/11/gif-2.gif" alt="the hard-coded AI that only follows the ball (left) vs. our trained AI">
</p>

[![Run on FloydHub](https://img.shields.io/badge/Run%20on-FloydHub-blue.svg)](https://floydhub.com/run?template=https://github.com/mtrazzi/spinning-up-a-Pong-AI-with-deep-RL)

##### Note: These are the Jupyter Notebooks for my article [Spinning Up a Pong AI With Deep Reinforcement Learning](https://blog.floydhub.com/spinning-up-with-deep-reinforcement-learning/) on FloydHub.

Within a few years, Deep Reinforcement Learning will completely transform robotics, an industry with the potential to [automate](https://www.mckinsey.com/business-functions/operations/our-insights/human-plus-machine-a-new-era-of-automation-in-manufacturing) 64 percent of manufacturing. Hard-to-engineer behaviors will become a piece of cake, so long as there are enough Deep RL practitioners to implement them.

The following notebooks (file ending with .ipynb) detail how to train a model in Keras that plays the game of Pong using simple Policy Gradient techniques:

## Files overview

``` bash

#Main notebooks
  |train.ipynb                             #Main notebook to train the Pong agent in Keras
  |train-with-log.ipynb                    #Same as above but with tensorflow logs and model saving/loading

#Demo notebooks
  |demo.ipynb                              #Simple notebook to generate a gif with a random model
  |demo_black_and_white.ipynb              #Same as above but generate the gif for the pre-processed frame diff

#Utils
  |support.py                              #To support the gif generation
  |easy_tf_log.py                          #Tool to easily plot variable
  |karpathy.py                             #Functions used in karpathy's original RL Pong post

#FloydHub specific  
  |floyd.yml                               #Tells what to execute when launching a job
  |floyd_requirements.txt	                 #Necessary packages to install
  
#Trained weights
  |my_model_weights.h5                     #Saved weights after training
  
```

## Demo of random agent

Gif generated with `demo.ipynb`:

<p align="center">

<img src="https://blog.floydhub.com/content/images/2018/12/gif2.gif" alt="random agent">
</p>

Gif generated with `demo_black_and_white.ipynb`:


<p align="center">

<img src="https://media.giphy.com/media/9V7rafos3IPHs4vO1K/giphy.gif" alt="random agent">
</p>

#### Pre-processed frames in black and white

## **Run the code on FloydHub**
[![Run on FloydHub](https://static.floydhub.com/button/button.svg)](https://floydhub.com/run?template=https://github.com/mtrazzi/spinning-up-a-Pong-AI-with-deep-RL)

Click the above blue button to open a [Workspace](https://blog.floydhub.com/workspaces/) on [FloydHub](https://www.floydhub.com/?utm_medium=readme&utm_source=colornet&utm_campaign=aug_2018) where you will find the same environment.

## Local
``` bash
pip install keras gym jupyter
```
```
git clone https://github.com/mtrazzi/spinning-up-a-Pong-AI-with-deep-RL
cd spinning-up-a-Pong-AI-with-deep-RL
jupyter notebook
```
Go do the desired notebook, files that end with '.ipynb'. To run the model, go to the menu then click on Cell > Run all

## Credits

- Karpathy's [code](https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5) and [blogpost](http://karpathy.github.io/2016/05/31/rl/) for the neural network architecture, pre-processing and training methods
- mrahtz's [easy-tf-log](https://github.com/mrahtz/easy-tf-log) and [tensorflow pong implementation](https://github.com/mrahtz/tensorflow-rl-pong)
- FloydHub's [gym-retro template](https://www.floydhub.com/explore/templates/reinforcement-learning/gym-retro) for the gif generation 
