# Code to visualise a sine wave. #
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.cla()
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x = range(0, 360)
    y = [math.sin(math.radians(degrees) + (frame / 50)) for degrees in x]
    ax.plot(x, y)


def run():
    global line
    sine_animation = animation.FuncAnimation(fig,  # the figure
                                             animate,  # the animation function
                                             frames=720,  # the frame count
                                             interval=100,  # the time interval between frames in ms
                                             repeat=True)

    plt.show()


run()
