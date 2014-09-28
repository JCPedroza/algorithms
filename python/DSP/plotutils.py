import matplotlib.pyplot as plt

def plot_all(*args):
    length = len(args)
    for arg in range(length):
        plt.plot(args[arg])
        if arg < length - 1:
            plt.figure()
    plt.show()
