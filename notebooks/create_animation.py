import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn')

# Create a figure for depicting the information
fig, ax = plt.subplots(1, 2, figsize = (10,3))
ax1, ax2 = ax

# Create a figure for the original CE Loss
x = np.linspace(1e-2,1,1001)
y = -np.log(x)

ax1.plot(x, y, lw = 2)
ax1.set_title("Original CE Loss")
ax1.set_xlim([0,1])

# Create a placeholder for the second figure to plot upon
line, = ax2.plot([], [], lw=3, c = "r")

def init():
    line.set_data([], [])
    return line,

# Define the logic of animation
def animate(i):
    x = np.linspace(1e-2, 1, 1001)
    y = np.zeros(1001)
    for p in range(1, i + 1):
        y += (1 - x) ** p / p 
    rmse = ((-np.log(x) - y) ** 2).sum() ** 0.5
    ax1.set_title(f"Original CE Loss\nRMSE from approximation: {rmse:.3f}", fontsize = 10)
    line.set_data(x, y)
    ax2.set_title(f"Approximate CE Loss considering first {i + 1} terms\n in the expansion", fontsize = 10)
    ax2.set_xlim([0, 1]); ax2.set_ylim([0,4]);
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames = 20, interval = 1000, blit=True)

anim.save('ce_taylor_series.gif', writer='imagemagick')
