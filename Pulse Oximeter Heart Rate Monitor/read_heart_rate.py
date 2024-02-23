import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ecgGUI import ecgGUI
from itertools import count
import serial
from scipy.signal import find_peaks
from RPLCD import CharLCD
import time

# SETUP FOR SERIAL COMMUNICATION
arduino = serial.Serial('COM4', 9600)
arduino.flush()

# SETUP FOR UPDATING DATA
index = count()
x_values = []
y_values = []
#testing_data = []
temp = []
heart_storage = []
x_lim = 200
First_data = 0
waiting_line = 'Waiting...'


def send_data_to_arduino(data):
    arduino.write((data).encode('utf-8'))


def figure_setup():
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='lightyellow')
    ax.set_xlim(left=0, right=x_lim, auto=True)
    return fig, ax


# Function to update the plot in real-time
def update_plot(i):
    global temp, x_values, y_values, heart_storage, First_data
    ecg_signal = arduino.readline().decode('utf-8')
    ecg_signal = int(ecg_signal)
    #print("Received:", ecg_signal)

    x_values.append(next(index))
    y_values.append(ecg_signal)

    plt.cla()
    plt.plot(x_values, y_values)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Real time PPR plot')

    """
    # LOAD DATA INTO CSV FILE
    testing_data.append(ecg_signal)
    df = pd.DataFrame(testing_data)
    file_path = 'testing_output.csv'
    df.to_csv(file_path, index=False)
    """

    if not len(x_values) % x_lim:
        # Ignore the first few data, need to wait for stabilization
        if First_data != 2:
            #send_data_to_arduino(waiting_line)
            print('Waiting for data!')
            First_data += 1
        else:
            peaks, _ = find_peaks(y_values, height=800, distance=10)
            #print(f"peaks are {peaks}")
            for i in range(len(peaks) - 1):
                width = peaks[i + 1] - peaks[i]
                temp.append(width)
            #print(f"temp array are {temp}")
            bpms = np.mean(temp)
            heart_storage.append(bpms)
            if not len(heart_storage) % 2:
                heart_rate = 60 * 1000 / (np.mean(bpms) * 30)
                HR_line = str(round(heart_rate)) + ' BPM'
                #send_data_to_arduino(HR_line)
                print(f"HEART RATE IS : {heart_rate:.1f}")
                heart_storage = []
            else:
                #send_data_to_arduino(waiting_line)
                print('Waiting for data!')
        plt.xlim([len(x_values), len(x_values)+x_lim])
        x_values = []
        y_values = []
        temp = []


fig, ax = figure_setup()
# Set up the animation
# gcf get current function and interval is delay time in miliseconds
ani = FuncAnimation(fig, update_plot, interval=0)

# Show the plot
plt.tight_layout()
plt.show()
