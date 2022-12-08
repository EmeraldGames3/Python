from modelle.bestellung import Bestellung
from modelle.gekochterGericht import gekochterGericht


def runTypeSafeTyTests():
    testBestellung()
    testGekochterGericht()


def testBestellung():
    b = Bestellung(12, [1, 2, 3], 12.5)
    try:
        b = Bestellung(12, [12], '1')
    except AttributeError:
        del b
        return
    try:
        b = Bestellung(12, 12, 1.6)
    except AttributeError:
        del b
        return
    try:
        b = Bestellung(12.9, [12], 1.8)
    except AttributeError:
        del b
        return

    assert False


def testGekochterGericht():
    g = gekochterGericht(12, 14.0, 6.7)
    try:
        g = gekochterGericht('12', 14.0, 6.7)
    except AttributeError:
        del g
        return
    try:
        g = gekochterGericht(12, '14.0', 6.7)
    except AttributeError:
        del g
        return
    try:
        g = gekochterGericht(12, 14.0, '6.7')
    except AttributeError:
        del g
        return

    assert False


runTypeSafeTyTests()
