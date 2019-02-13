import matplotlib.pyplot as plt

FEATURES_FILE = "features.arff"


def main():
    # PART I: VISUALIZATION
    # Initialize the arrays to hold each parameter
    zcr_mean_music_arr = []
    par_mean_music_arr = []
    zcr_std_music_arr = []
    par_std_music_arr = []
    zcr_mean_speech_arr = []
    par_mean_speech_arr = []
    zcr_std_speech_arr = []
    par_std_speech_arr = []

    # Main loop to read in ARFF file
    with open(FEATURES_FILE, 'r') as file:
        # Skip the header
        for _ in range(76):
            next(file)

        # Extract the relevant data from each line in the file
        for line in file:
            data_arr = line.split(",")

            par_mean_time = float(data_arr[1])
            zcr_mean_time = float(data_arr[2])
            par_std_time = float(data_arr[6])
            zcr_std_time = float(data_arr[7])

            data_type = data_arr[72].strip()
            if data_type == "music":
                zcr_mean_music_arr.append(zcr_mean_time)
                par_mean_music_arr.append(par_mean_time)
                zcr_std_music_arr.append(zcr_std_time)
                par_std_music_arr.append(par_std_time)
            else:
                zcr_mean_speech_arr.append(zcr_mean_time)
                par_mean_speech_arr.append(par_mean_time)
                zcr_std_speech_arr.append(zcr_std_time)
                par_std_speech_arr.append(par_std_time)

    # plot the graphs using extracted data
    plot_mean(zcr_mean_music_arr, par_mean_music_arr, zcr_mean_speech_arr, par_mean_speech_arr)
    plot_std(zcr_std_music_arr, par_std_music_arr, zcr_std_speech_arr, par_std_speech_arr)


# Function to plot zcr mean vs. par mean
def plot_mean(zcr_music, par_music, zcr_speech, par_speech):
    plt.plot(zcr_music, par_music, 'bo', label='Music')
    plt.plot(zcr_speech, par_speech, 'go', label="Speech")
    plt.title("ZCR Mean Time vs. PAR Mean Time")
    plt.xlabel("ZCR Mean Time")
    plt.ylabel("PAR Mean Time")
    plt.legend()
    plt.savefig("zcr-par-mean.png")
    plt.clf()


# Function to plot zcr std vs. par std
def plot_std(zcr_music, par_music, zcr_speech, par_speech):
    plt.plot(zcr_music, par_music, 'bo', label="Music")
    plt.plot(zcr_speech, par_speech, 'go', label="Speech")
    plt.title("ZCR Std Time vs. PAR Std Time")
    plt.xlabel("ZCR Std Time")
    plt.ylabel("PAR Std Time")
    plt.legend()
    plt.savefig("zcr-par-std.png")
    plt.clf()


main()
