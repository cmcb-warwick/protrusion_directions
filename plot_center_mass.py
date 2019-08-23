
def uniqueish_color():
	import matplotlib.pyplot as plt
	import numpy as np
	"""There're better ways to generate unique colors, but this isn't awful."""
	return plt.cm.gist_ncar(np.random.random())


def plot_center_mass(filename, image):
    import pandas as pd
    import matplotlib.pyplot as plt
    from get_metadata import get_metadata

    import numpy as np

    frame = pd.read_csv(filename)
    print(frame)
    max_slice = max(frame['Slice'])
    #color=plt.cm.rainbow(np.linspace(0,1,max_slice))
    c_dict = frame['Slice'].map(pd.Series(data=np.arange(max_slice), index=frame['Slice'].values).to_dict())
    print(c_dict)
    fig, ax = plt.subplots()
    plt.scatter(frame['X'], frame['Y'], c=c_dict, cmap=plt.cm.rainbow)
    plt.plot(frame['X'], frame['Y'])
    max_y, max_x, _, _, _ = get_metadata(image)
    ax.set_xlim(0, max_x)
    ax.set_ylim(0, max_y)
    plt.gca().invert_yaxis()
    plt.colorbar()
    #plt.axis('equal')
    
    
    plt.show()
    return


if __name__ == '__main__':
    filename = 'TP_wt_lat/20140205/Results.csv'
    image = 'TP_wt_lat/20140205/new_max_greenchannel_smooth.ome.tif'
    plot_center_mass(filename, image)
