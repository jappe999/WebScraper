import FileSystem, re
from threading import Thread
from urllib.parse import quote
from Webpage import Webpage
from colorama import Fore, Style

class Crawler(object):
    def __init__(self, urls):
        self.urls       = urls
        self.found_urls = []
        self.threads    = []


    def error(err, err_code):
        print(Fore.RED + 'CRAWLER error %s:%s' % (err_code, err, ))
        print(Style.RESET_ALL)

    def crawl(self):
        if self.urls:
            while len(self.urls) > 0:
                t = Thread(target=self.get_url_contents(self.urls[0]))
                t.deamon = True
                t.start()
                self.threads.append(t)

                del(self.urls[0])

    # Set page in filesystem
    def set_page(self, url, page_contents):
        url = re.sub('^(http://|https://)?', '', url)
        url = quote(url)

        # Creates a directory and paste the contents into a file.
        FileSystem.set_data(url, page_contents)

    def get_url_contents(self, url):
        # Get url contents
        page     = Webpage(url)
        response = page.get_page()

        try:
            if not response == '':
                self.set_page(url, response)
        except Exception as e:
            self.error(e, '0x1')

        if not response == '':
            anchors = page.get_anchors(response)

            # Repeat the crawl function for every anchor found
            for anchor in anchors:
                self.found_urls.append(anchor[0])
