#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):

    # your code should go here

    return True


def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")

