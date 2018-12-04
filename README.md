# Spinning Up a Pong AI With Deep Reinforcement Learning

<p align="center">
<img src="https://blog.floydhub.com/content/images/2018/11/gif-2.gif" alt="the hard-coded AI that only follows the ball (left) vs. our trained AI">
</p>

[![Run on FloydHub](https://img.shields.io/badge/Run%20on-FloydHub-blue.svg)](https://floydhub.com/run?template=https://github.com/mtrazzi/spinning-up-a-Pong-AI-with-deep-RL)

##### Note: These are the Jupyter Notebooks for my article "Spinning Up a Pong AI With Deep Reinforcement Learning" on FloydHub.

Within a few years, Deep Reinforcement Learning will completely transform robotics, an industry with the potential to [automate](https://www.mckinsey.com/business-functions/operations/our-insights/human-plus-machine-a-new-era-of-automation-in-manufacturing) 64 percent of manufacturing. Hard-to-engineer behaviors will become a piece of cake, so long as there are enough Deep RL practitioners to implement them.

Fortunately, OpenAI just released [Spinning Up in Deep RL](https://blog.openai.com/spinning-up-in-deep-rl/): an aggregate of resources, code, and advice to help the rest of us get started with Deep Reinforcement Learning.

Among their recommendations for surviving the initial hurdles of Deep RL is the advice to start with Vanilla Policy Gradient algorithms.

The following notebooks (file ending with .ipynb) detail how to train a model in Keras that plays the game of Pong.

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
