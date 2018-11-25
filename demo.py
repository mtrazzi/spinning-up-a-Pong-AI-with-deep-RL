import gym
import random

# code for the two only actions in Pong
UP_ACTION = 2
DOWN_ACTION = 3

# initializing our environment
env = gym.make("Pong-v0")

# beginning of an episode
observation = env.reset()

# main loop
while True:
    # render a frame
    env.render()

    # choose random action
    action = random.randint(UP_ACTION, DOWN_ACTION) 

    #run one step
    observation, reward, done, info = env.step(action)

    # if episode is over, reset to beginning
    if done:
        env.reset()
