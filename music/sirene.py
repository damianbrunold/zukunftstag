from music import *
from toene import *

samples = []

for i in range(3):
    samples += ton(g1, 0.4)
    samples += ton(d2, 0.4)

abspielen(samples)
