from models.CookedDish import CookedDish

"""
Here we test how the assignment of ids works
"""

def test_id():
    d1 = CookedDish(None, "Fish", 1, 1, 1)
    d2 = CookedDish(None, "Fish", 1, 1, 1)
    d3 = CookedDish(None, "Fish", 1, 1, 1)
    d4 = CookedDish(None, "Fish", 1, 1, 1)

    print(d1.id)
    print(d2.id)
    print(d3.id)
    print(d4.id)

    assert d4.id == 3
    assert d3.id == 2
    assert d1.id == 0
    assert d2.id == 1

test_id()
