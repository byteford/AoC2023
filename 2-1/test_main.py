from main import *

def test_make_object():
    obj = line_to_obj("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    print(obj)
    assert obj == {'blue': 6, 'red': 20, 'green': 13}

def test_example():
    assert main("example.txt") == 8


