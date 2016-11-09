def lese_daten(dateiname):
    result = []
    with open(dateiname, "r") as inp:
        s = inp.readline().strip()
        while s:
            if s == "briefstart":
                brief = {}
                brief['zeilen'] = []
                s = inp.readline().strip()
                while s != "briefend":
                    name = s[0:s.find(",")]
                    wert = s[s.find(",")+1:]
                    if name == "text":
                        brief["zeilen"].append(wert)
                    else:
                        brief[name] = wert
                    s = inp.readline().strip()
                result.append(brief)
            s = inp.readline().strip()
    return result

if __name__ == '__main__':
    daten = lese_daten("daten.txt")
    for brief in daten:
        if brief['sprache'] == 'deutsch':
            print brief

                    
