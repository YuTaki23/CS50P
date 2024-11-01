from numb3rs import validate

def main():
    test_validate_True()
    test_validate_False()

def test_validate_True():
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")

def test_validate_False():
    assert not validate("512.512.512.512")
    assert not validate("1.2.3.1000")
    assert not validate("cat")