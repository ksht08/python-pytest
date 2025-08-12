def test_sum():
    a = 5
    b = 10
    c = a + b
    assert a != b, "a and b should not be equal"
    assert c == 15, "Expected sum of a and b to be 15"
    #assert a == b, "error"