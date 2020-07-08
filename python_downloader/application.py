import re
import urllib3
http = urllib3.PoolManager()

class App(object):

    def __init__(self):
        pass

    def download(self,):
        urls = []
        filenames = []
        for url in urls:
            filename = re.sub("https://.*?/files/","",url)
            print("filename:  " + filename)
            filenames.append(filename)

        N = 0 
        for url in urls:
            r = http.request('GET',url)
            Name = filenames[N]
            N += 1
            with open(Name, "wb") as fcont:
                fcont.write(r.data)
