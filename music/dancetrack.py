from music import *
from toene import *

beat = 0.5

basedrum_takt = bumm(beat) * 4

hihat_takt = stille(beat) + rauschen(0.02) + \
             stille(beat-0.02) + stille(beat) + \
             rauschen(0.02) + stille(beat-0.02)

bass_takt1 = ton(c0,   beat) + stille(beat) + \
             ton(e0,   beat / 2) + stille(beat / 2) + \
             ton(h0/2, beat / 2) + stille(beat / 2)
bass_takt2 = ton(f0,   beat) + stille(beat) + \
             ton(a0,   beat / 2) + stille(beat / 2) + \
             ton(c0,   beat / 2) + stille(beat / 2)
bass_takt3 = ton(g0/2, beat) + stille(beat) + \
             ton(h0/2, beat / 2) + stille(beat / 2) + \
             ton(d0,   beat / 2) + stille(beat / 2)

bass = bass_takt1 + bass_takt1 + bass_takt2 + bass_takt3 + bass_takt1

first = mix3(ton_saege(c1, beat * 4),
             ton_saege(e1, beat * 4),
             ton_saege(g1, beat * 4))
fourth = mix3(ton_saege(f1, beat * 4),
              ton_saege(a1, beat * 4),
              ton_saege(c2, beat * 4))
fifth = mix3(ton_saege(g1, beat * 4),
             ton_saege(h1, beat * 4),
             ton_saege(d2, beat * 4))

melody = first + first + fourth + fifth + first

samples = mix4(basedrum_takt, hihat_takt, bass, melody)

abspielen(samples * 3)
