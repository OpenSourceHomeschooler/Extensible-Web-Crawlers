import re, urllib, Queue

class WebCrawler:
    """A Simple Web Crawler That Is Readily Extensible"""
    #Declare the variable to hold the name of the file
    fileName = "UrlList.txt"
    urlsCrawled = {}
    
    # Crawler constructor method
    def __init__(self, urlFileName):
        self.fileName = urlFileName
        size = 1
        
    # This attempts to see if the URL is valid as is
    def isUrl(self, url):
        if re.findall("http://", url, re.I):
		        return True
	      else:
		        return False
    
    # This method tests to see if the specified URL has
    # been crawled. If not it adds it the hash table.
    def notCrawled(self, test ):
        try:
            self.urlsCrawled[test]
        except:
            self.urlsCrawled.update({test: 1})
            return True
        return False
    
    # This is the heart of the crawler and will crawl forever
    def crawlUrls(self, url, depth):
        textfile = file(self.fileName, 'wt')
        urlList = Queue.Queue()
        urlList.put(url)
        while not urlList.empty():
            currentUrl = urlList.get()
            if self.isUrl(currentUrl):
                try:
                    webpage = urllib.urlopen(currentUrl).read()
                except:
                    print "Following URL failed!"
                    print currentUrl
                    #break
                for urlsFound in re.findall('''href=["'](.[^"']+)["']''',webpage, re.I):
                    if self.notCrawled(urlsFound):
                        print urlsFound
                        urlList.put(urlsFound)
                        textfile.write(urlsFound+'\n')

# The following are not part of the class but they rather test it
myCrawler = WebCrawler('CrawledUrls.txt')

myCrawler.crawlUrls("http://wordsmakeworlds.com/", 2)
