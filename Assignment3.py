import matplotlib.pyplot as plot

FEATURES_FILE = "features.arff"


def main():
    # PART I: VISUALIZATION
    # Initialize the arrays to hold each parameter
    zcr_mean_time_arr = []
    par_mean_time_arr = []
    zcr_std_time_arr = []
    par_std_time_arr = []

    # Main loop to read in ARFF file
    with open(FEATURES_FILE, 'r') as file:
        # Skip the header
        for _ in range(76):
            next(file)

        # Extract the relevant data from each line in the file
        for line in file:
            data_arr = line.split(",")
            zcr_mean_time = float(data_arr[0])
            par_mean_time = float(data_arr[1])
            zcr_std_time = float(data_arr[7])
            par_std_time = float(data_arr[6])

            zcr_mean_time_arr.append(zcr_mean_time)
            par_mean_time_arr.append(par_mean_time)
            zcr_std_time_arr.append(zcr_std_time)
            par_std_time_arr.append(par_std_time)

    print(zcr_mean_time_arr)
    print(par_mean_time_arr)
    print(zcr_std_time_arr)
    print(par_std_time_arr)
    # Plot the graphs using extracted data
    plot_mean(zcr_mean_time_arr, par_mean_time_arr)
    plot_std(zcr_std_time_arr, par_std_time_arr)


# Function to plot zcr mean vs. par mean
def plot_mean(zcr_arr, par_arr):
    plot.plot(zcr_arr, par_arr, 'o')
    plot.title("ZCR Mean Time vs. PAR Mean Time")
    plot.xlabel("ZCR Mean Time")
    plot.ylabel("PAR Mean Time")
    plot.savefig("zcr-par-mean.png")


# Function to plot zcr std vs. par std
def plot_std(zcr_arr, par_arr):
    plot.plot(zcr_arr, par_arr, 'o')
    plot.title("ZCR Mean Time vs. PAR Mean Time")
    plot.xlabel("ZCR Mean Time")
    plot.ylabel("PAR Mean Time")
    plot.savefig("zcr-par-std.png")


main()
