# Customizable-Phone-Interface Capstone Project
This is my Capstone Project. I'm responsible for building a heart rate monitor and hardware device for CPI that can be controlled by a button to make phone calls for people who are physically challenged from a wide array of disabilities (old age, Parkinson’s, MS, Paralysis, etc.).

## 3 Electrodes to collect ECG signal
One of the approaches to monitor the heart rate is collecting ECG signals from 3 electrodes. The analog circuitry is shown below. I used 1 instrumentation amplifier, 1 band-pass filter and 1 summing amplifier to collect signal from 3 electrodes placed on 2 wrists and right leg of my body. 
![IMG_2446](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/bb8a4da5-b94e-434d-9dbd-d42cabda1007)
![SmartSelect_20240405_014020_OneNote](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/fcd62e4e-b570-4f40-8c5c-b5e00b1a0c49)
![IMG_2464](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/c88d67a9-d4d5-4789-b413-94555e9101c0)
![IMG_2444](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/5f0518cf-0e29-4a81-80fb-ef15914ca9c3)


## Pulse Oximeter heart rate monitor
I wrote the code to detect the peaks of the signal, calculate the heartbeat and plotted it in a GUI
Several libraries were used such as numpy, matplotlib, serial, and scipy in Python.
![IMG_1624](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/3dd57526-7145-4873-8fc8-1f247acc32f1)
![IMG_1626](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/3b98a1fe-8550-46a5-a1bb-fa8bc9428d66)
![Picture1](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/32910237-485e-430f-8366-e41ad7ff7e4c)

## 3D design CPI enclosure (SOLIDWORKS)
3D-designed the enclosure of the CPI that perfectly fits the dimensions of the raspberry Pi. One feature of this enclosure is that I can stack up many layers I want on top of it which is neater than the previous design. All the cables and wires will be on one designated layer and LCD display will be on a final layer. The CPI is 3 cm tall, which is a perfect size for a small device.
![CPI_case_assembly](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/5410c7e8-0f17-44a1-b6bb-680b8f8470ea)
![CPI_Case_assembly_1](https://github.com/huykhoi9/Customizable-Phone-Interface/assets/85450944/63da057b-ba70-47d3-b69d-3141ae81e313)
