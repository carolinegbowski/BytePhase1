# Testing

* How many tests will pass and fail in the following code? (Please don't copy/paste and execute to find out)
```Python
L = []
@pytest.fixture(params=[1,2,3,4,5])
def populate_list(request):
  L.append(request.param)
  return L
  
@pytest.fixture(params=[1,2,3,4,5])
def get_num(request):
  return request.param
  
def test_L(populate_list, get_num):
  assert get_num in populate_list
```

* Read on [PyTest](http://doc.pytest.org/en/latest/skipping.html#id1) features and write a function `test_version` in `test_version.py` that asserts True, but only runs on Python versions 3.x or later
  * The test only **runs** on Python versions later than 3.x. If an earlier version is used, the test should should be skipped, it should never fail
  * Hint: Look into skip/skipif
  * To test, run `python2 test_version.py` and `python3 test_version.py`

* Write unit tests for the FizzBuzzer class using the python pytest module.
* You should have as many tests as you deem appropriate, but explain the reasoning behind why you have as many tests as you do
  * Hint: Do not combine two tests into one (ie. testing an input value & testing an if condition)
  
