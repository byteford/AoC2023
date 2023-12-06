from main import *

def test_make_object():
    obj = line_to_obj("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    print(obj)
    assert obj == {'blue': 6, 'red': 4, 'green': 2}

def test_example():
    assert main("example.txt") == 2286


