
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import soundfile as sf

dataset_path = Path("Noise")

files = list(dataset_path.glob("*.wav"))

print(f"Найдено файлов: {len(files)}")

for file in files:
    audio, sr = sf.read(file)
    fft = np.fft.rfft(audio)
    frequencies = np.fft.rfftfreq(len(audio), 1 / sr)

    amplitude = np.abs(fft)

    plt.figure(figsize=(10, 4))

    plt.plot(frequencies, amplitude)

    plt.xlabel("Frequency, Hz")
    plt.ylabel("Amplitude")

    plt.xlim(0, 5000)

    plt.show()

