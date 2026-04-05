%% IBEHS 4F04 - Lab Data Acquisition System
%MATLAB requirements:
%Data Acquisition Toolbox
%NI-DAQmx Support from Data Acquisition Toolbox
%NI-DAQmx drivers
%
%Instructions: Plug NI USB-6216 module into computer, set the duration on
%line 20, then click run to collect data using input channel ai0. After the
%data is done recording, a plot of time domain data and the frequency
%response will be displayed


clear;
close all;

%configure DAQ for analog input
d = daq("ni"); %using NI USB-6216

%Set sampling rate (Hz) - Optional - If this line is not included then it
%defaults to 1000Hz (max of 400kHz)
d.Rate = 1000;

%Set duration (seconds)
duration = 5;

addinput(d, "Dev1", "ai0", "Voltage"); %using analog input channel 0
% addinput(d, "Dev1", "ai1", "Voltage"); %uncomment to add channel ai1
numinputs = length(d.Channels);

%AC coupling removes any DC offset in the signals
ac_coupling = true; 

%read analog input(s) for specified duration
data = read(d, seconds(duration), "OutputFormat", "Matrix");


%Remove DC offset if ac_coupling is true
if ac_coupling
    for i = 1:numinputs
        data(:,i) = data(:,i)-mean(data(:,i));
    end
end


%Calculate FFT to analyze frequency content
Fs = d.Rate;
T = 1/Fs;
L = duration*Fs;
t = (0:L-1)*T;
f = Fs*(0:(L/2))/L;

%Generate time vector
time = (0:1/Fs:duration-1/Fs)';

%Initialize variable to store all FFT data
FFTdata = zeros(L/2+1, numinputs);
for i = 1:numinputs
    %Calculate FFT
    Y = fft(data(:,i));
    
    %Calculate single and double sided spectrums
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1);
    P1(2:end-1) = 2*P1(2:end-1);
    
    %Save single sided spectrum to FFTdata
    FFTdata(:,i) = P1;    
end

%Plot results
figure
subplot(2,1,1)
for i=1:numinputs
    plot(time, data(:,i))
    hold on
end
hold off
ylabel("Amplitude (V)")
xlabel("Time (s)")
title("Signal(s) in Time Domain")
legend(d.Channels.ID)


subplot(2,1,2)
for i=1:numinputs
    plot(f, FFTdata(:,i))
    hold on
end
hold off
ylabel("Magnitude")
xlabel("Frequency (Hz)")
title("Single Sided Magnitude Spectrum(s)")
legend(d.Channels.ID)
clear d;


