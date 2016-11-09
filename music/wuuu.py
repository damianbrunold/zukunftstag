from music import *
from toene import *

samples = []

for i in range(2):
    samples += bereich_saege(c1, e1, 2)
    samples += bereich_saege(e1, c1, 2)

abspielen(samples)
