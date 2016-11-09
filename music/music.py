import StringIO
import math
import random
import wave
import audioop
import winsound

pi2 = 2 * math.pi
framerate = 44100

def interpolate_linear(a, b, p):
    return a + (b - a) * p

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def interpolate_logistic(a, b, p):
    return a + (b - a) * sigmoid(-5.0 + 16.0 * p)

def stille(dauer):
    samples = int(dauer * framerate)
    return [0] * samples

def rauschen(dauer, amplitude=1.0):
    samples = int(dauer * framerate)
    return [random.uniform(-1, 1) * amplitude
            for i in range(samples)]

def ton_sinus(frequenz, dauer, amplitude=1.0):
    samples = int(dauer * framerate)
    return [math.sin((pi2 * frequenz * i / framerate) % pi2) * amplitude
            for i in range(samples)]
    
def bereich_sinus(freq1, freq2, dauer, amplitude=1.0):
    samples = int(dauer * framerate)
    result = []
    for i in range(samples):
        frequenz = int(interpolate_logistic(freq1, freq2, 1.0 * i / samples) * 1000) / 1000
        result.append(math.sin((pi2 * frequenz * i / framerate) % pi2) * amplitude)
    return result
    
def ton_saege(frequenz, dauer, amplitude=1.0):
    samples = int(dauer * framerate)
    return [(((2.0 * frequenz * i / framerate) % 2.0) - 1.0) * amplitude
            for i in range(samples)]

def bereich_saege(freq1, freq2, dauer, amplitude=1.0):
    samples = int(dauer * framerate)
    result = []
    for i in range(samples):
        frequenz = int(interpolate_logistic(freq1, freq2, 1.0 * i / samples) * 1000) / 1000
        result.append(((1.0 * frequenz * i / framerate) % 1.0) * amplitude)
    return result
    
def bumm(dauer, amplitude=1.0):
    data = ton_saege(25, dauer, amplitude)
    data = [math.exp(-i * 10 / len(data)) * data[i] for i in range(len(data))]
    return normalize(data)

def form(samples, envelope):
    # todo
    return data

def mix2(track1, track2, renormalize=True):
    len1 = len(track1)
    len2 = len(track2)
    result = [0] * max(len1, len2)
    factor = 1
    for i in range(max(len1, len2)):
        result[i] = track1[i % len1] + track2[i % len2]
        if renormalize:
            if result[i] < -1.0: factor = min(factor, -1.0 / result[i])
            if result[i] > 1.0: factor = min(factor, 1.0 / result[i])
        else:
            if result[i] < -1.0: result[i] = -1.0
            if result[i] > 1.0: result[i] = 1.0
    return [factor * result[i] for i in range(max(len1, len2))]

def mix3(track1, track2, track3, renormalize=True):
    return mix2(track1, mix2(track2, track3, renormalize), renormalize)

def mix4(track1, track2, track3, track4, renormalize=True):
    return mix2(mix2(track1, track2, renormalize),
                mix2(track3, track4, renormalize),
                renormalize)

def ton(frequenz, dauer=1.0, amplituden=[1, 0.7, 0.5, 0.4]):
    return mix4(ton_sinus(frequenz, dauer, amplituden[0]),
                ton_sinus(frequenz * 2, dauer, amplituden[1]),
                ton_sinus(frequenz * 3, dauer, amplituden[2]),
                ton_sinus(frequenz * 4, dauer, amplituden[3]))

def normalize(samples, amplitude=1.0):
    maxsample = max(samples)
    return [sample / maxsample * amplitude for sample in samples]

def stereo(links, rechts):
    result = []
    for i in range(min(len(links), len(rechts))):
        result += [links[i], rechts[i]]
    return result
    
def verpacken16bit(samples):
    result = ""
    for i in range(len(samples)):
        sample = int(samples[i] * 32767)
        low = sample & 0xff
        high = (sample >> 8) & 0xff
        result += chr(low) + chr(high)
    return result

def abspielen(samples, stereo=False):
    samples = verpacken16bit(samples)

    result = StringIO.StringIO()
    out = wave.open(result, "w")
    out.setnchannels(2 if stereo else 1)
    out.setsampwidth(2)
    out.setframerate(framerate)
    out.writeframes(samples)
    out.close()

    winsound.PlaySound(result.getvalue(), winsound.SND_MEMORY)

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

def klang_anzeigen(liste):
    master = Tk()
    w = Canvas(master, width=1000, height=1000)
    w.pack()
    maxlen = min(max([len(samples) for samples in liste]),
                 5000)
    for j, samples in enumerate(liste):
        x0 = None
        y0 = None
        w.create_line(0, 120 * (j + 1), 1000, 120 * (j + 1), fill = "#00f")
        for i, sample in enumerate(samples):
            x = 1000 * i / maxlen
            y = 120 * (j + 1) - 50 * sample
            if x0 and y0:
                w.create_line(x0, y0, x, y, fill = "#000", width = 1)
            x0 = x
            y0 = y
    mainloop()
    

    
