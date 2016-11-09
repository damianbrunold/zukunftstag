from music import *
from toene import *

samples1 = ton(c1, 0.5)
samples2 = ton_sinus(c1, 0.5)
samples3 = ton_saege(c1, 0.5)
samples4 = rauschen(0.5)

abspielen(samples1 + samples2 + samples3 + samples4)
klang_anzeigen([samples1, samples2, samples3, samples4])
