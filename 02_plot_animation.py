import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# function generates random number
def number_random():
    return np.random.randint(300)

# Create figure for plotting
fig, ax = plt.subplots()
xs = []
ys = []

def animate(i, xs:list, ys:list):
    flt = number_random()
    
    # Add x to lists
    ys.append(flt)

    # Limit x lists to 10 items
    ys = ys[-20:]
    print(ys)

    # Draw x and y lists
    ax.clear()
    ax.plot(ys)
    
    # Format plot
    ax.set_ylim([0,301])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.20)
    ax.set_title('Plot of random numbers')
    ax.set_xlabel('Scala')
    ax.set_ylabel('Random Number')

# Set up plot to call animate() function every 1000 milliseconds
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=500)

plt.show()