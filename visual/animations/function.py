# Code to create a basic animation function. #
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# user-defined function
def animate(frame):
    print(frame)


# our figure
fig, ax = plt.subplots(1, 1)


def run():
    # Create an animation using FuncAnimation
    some_animation = animation.FuncAnimation(fig,  # the figure
                                             animate,  # the animation function
                                             frames=10,  # the frame count
                                             interval=1000,  # the time interval between frames in ms
                                             repeat=True)  # boolean value on whether to repeat
    plt.show()


if __name__ == "__main__":
    run()
