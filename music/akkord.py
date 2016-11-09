from music import *
from toene import *

ton1 = ton(c1, 1.5)
ton2 = ton(e1, 1.5)
ton3 = ton(g1, 1.5)

samples = mix3(ton1, ton2, ton3)

abspielen(samples)
