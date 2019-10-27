import numpy as np
import math
import matplotlib.pyplot as plt

def get_pareto(points):
    pareto_front = np.empty([0, points.shape[1]])
    not_pareto_front = np.empty([0, points.shape[1]])
    ones_array = np.ones([points.shape[1], 1])
    for i in range(points.shape[0]):
        arr = points[i] <= points
        if np.sum(arr.dot(ones_array) == points.shape[1]) > 1:
            not_pareto_front = np.vstack((not_pareto_front, points[i]))

        else:
            pareto_front = np.vstack((pareto_front, points[i]))

    fig = plt.figure(figsize=[10, 10])
    axs = fig.add_subplot(projection="polar")
    axs.set_yticks([])
    plt.thetagrids(np.arange(0, 360, 360.0 / points.shape[1]), labels=np.arange(0, points.shape[1], 1))

    xpl = np.arange(0, points.shape[1], 1)
    xpl = np.append(xpl, 0)
    xpl = xpl * 2 * math.pi / points.shape[1]

    for x in not_pareto_front:
        ypl = np.append(x, x[0])
        axs.plot(xpl, ypl, color="green")

    for x in pareto_front:
        ypl = np.append(x, x[0])
        axs.plot(xpl, ypl, color="red")

    plt.show()


def main():
    n = int(input())
    m = int(input())
    points = np.random.sample((n, m))
    get_pareto(points)

if __name__ == "__main__":
    main()
