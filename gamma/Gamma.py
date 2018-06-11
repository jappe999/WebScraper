#!/usr/bin/env python3

import requests, json
from colorama import Fore, Style
from Crawler import Crawler

class Gamma:
    def __init__(self, remote_addr):
        self.remote_addr = remote_addr

    @staticmethod
    def error(err, err_code):
        print(Fore.RED + 'GAMMA error %s:%s' % (err_code, err, ))
        print(Style.RESET_ALL)

    def start(self):
        local_queue = []
        found_urls  = ['https://twitter.com']

        while True:
            local_queue = self.get_url_data(found_urls)

            crawler = Crawler(local_queue)
            crawler.crawl()

            while True:
                if not self.has_threads(crawler):
                    break

            try:
                # Update local found_urls
                found_urls = crawler.found_urls
                print('Found some urls\n')

            except Exception as e:
                Gamma.error(e, '0x1')

    def has_threads(self, crawler):
        if len(crawler.threads) < 1:
            return False

        # Check for dead threads.
        for i in range(len(crawler.threads)):
            if i >= len(crawler.threads):
                break

            if not crawler.threads[i].isAlive():
                del(crawler.threads[i])

        return True

    def get_chunks(self, found_urls):
        chunks        = []
        MAX_CHUNK_LEN = 20

        # Split array in arrays with a max length of MAX_CHUNK_LEN.
        while len(found_urls) > 0:
            chunk = found_urls[:MAX_CHUNK_LEN]
            chunks.append(chunk)

            del found_urls[:MAX_CHUNK_LEN]

        return chunks

    def get_url_data(self, found_urls):
        chunks = self.get_chunks(found_urls)

        try:
            # Send data in chunks to Beta
            for chunk in chunks:
                post_data = json.dumps(chunk)
                requests.post(self.remote_addr, post_data)
        except Exception as e:
            Gamma.error(e, '0x2')

        try:
            # Get new urls from Beta
            response  = requests.get('%s/get' % (self.remote_addr, ))
            urls      = '' if not response.text else response.json()

            print('Got urls back from Beta:')
            print(', '.join(urls))

            return urls
        except Exception as e:
            Gamma.error(e, '0x3')
