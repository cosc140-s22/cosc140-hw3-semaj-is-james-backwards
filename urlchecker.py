#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

from posixpath import split

def main():
    testurl()

def urlchecker(url):
    urlList = url.split("://")
    if urlList[1].count(':') > 1 or urlList[1].count('?') > 1 or urlList[1].count('#') > 1 or (" " in url):
        return False
    if urlList[0] != "http" and urlList[0] != "https":
        return False
    secondHalf = urlList[1]
    if secondHalf == "" or not("/" in secondHalf):
        return False
    secondHalfList = secondHalf.split("/")
    hostname = secondHalfList[0]
    path = secondHalfList[1]
    if ":" in hostname:
        hostList =  hostname.split(":")
        port = hostList[1]
        name = hostList[0]
        if name == "":
            return False
        if not (port.isdigit() or port == ""):
            return False
    else:
        if hostname == "":
            return False
    if path != "":
        if "#" in url and "?" in url:  
            if url.find("#") > url.find("?"):
                return False
    if ":" in path: #colon can only be in hostname
        return False
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
            print("This " + url + " is not valid, but your function claimed the opposite")
        else:
            print( url + " ok")


if __name__ == "__main__":
    main()

