import seasons

def main():
    test_correct_date_True()
    test_correct_date_False()
    test_get_user_date_True()

def test_correct_date_True():
    assert seasons.correct_date("2017-12-12")

def test_correct_date_False():
    assert not seasons.correct_date("20-17-12")

def test_get_user_date_True():
    assert seasons.get_user_date("1999-01-01") == "1999-01-01"