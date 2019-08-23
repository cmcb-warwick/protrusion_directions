def visualise_angles(angles):
    import numpy as np
    import matplotlib.pyplot as plt
    
    bottom = 0
    max_height = 20
    bins_number = 8  # the [0, 360) interval will be subdivided into this
    # number of equal bins
    bins = np.linspace(0.0, np.pi, bins_number + 1,endpoint=True)
    print(bins)
    #theta = np.linspace(-0.0001,  1.0001 * np.pi, N+1, endpoint=True)
    #print(theta)
    #radii = np.zeros(N)
    n, _, _ = plt.hist(angles, bins)
    print(n)
    #for angle in angles:
        #this_theta = math.atan2(-vector[1],vector[0])
        # print(this_theta)
        #radii[np.digitize(angle, theta)] += 1
        # print(np.digitize(this_theta, theta))
    #print(radii)
    #width = (np.pi) / N
    plt.clf()
    width = np.pi / bins_number
    ax = plt.subplot(111, polar=True)
    ax.set_thetamin(0)
    ax.set_thetamax(180)
    ax.set_theta_zero_location("N")
    bin_pos = bins[:bins_number] + bins[1:]
    bin_pos = bin_pos / 2
    print(bin_pos)
    bars = ax.bar(bin_pos, n, width=width, bottom=bottom)
    plt.show()

    return



if __name__ == '__main__':
    angles = [0.33,1.88,2.17,0.56,0.93,2.97,2.04,0.99,0.48,1.97,1.39,2.8,1.81,2.67,1.78,2.3,0.55,2.13,1.03,1.91,2.64,2.11,2.79,3.09,1.76,2.97,1.57,0.1,2.63,2.55,1.03,0.16,0.2,0.21,2.22,1.16,1.73,1.74,0,2.5,0.07,1.36,1.69,1.09,0.59,0.79,1.9,0.44,0.15,1.25]
    visualise_angles(angles)