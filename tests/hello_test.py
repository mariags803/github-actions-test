from hello import say_hello, say_good_bye

def test_say_hello():
    assert say_hello() == 'Hello'

def test_say_good_bye():
    assert say_good_bye() == 'Good Bye'
