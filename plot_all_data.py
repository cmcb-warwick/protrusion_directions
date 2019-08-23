def plot_all_data(folder):
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    from visualise_angles import visualise_angles
    from visualise_results import generate_histogram

    files = os.listdir(folder)
    # print(files)
    frame = pd.DataFrame()
    for file in files:
        if file.endswith('csv'):
            # print(file)
            frame = frame.append(pd.read_csv(os.path.join(folder,file)), ignore_index=True)

    visualise_angles(frame['angle(rad)'])
    x, y = frame['vec_x'].values, frame['vec_y'].values
    vectors = zip(x,y)
    print(vectors)
    generate_histogram(vectors)
    # print(frame)
    return


if __name__ == '__main__':
    folder = '/home/erick/Nextcloud/CMCB/Michael_protrusions/alldata'
    plot_all_data(folder)
