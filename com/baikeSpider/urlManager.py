# -*- coding: utf-8 -*-

class UrlManager(object):

    def __init__(self):
        self.newUrls = set();
        self.oldUrls = set();

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url);

    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url);


    def has_new_url(self):
        return len(self.newUrls) != 0

    def get_new_rul(self):
        newUrl = self.newUrls.pop();
        self.oldUrls.add(newUrl);
        return newUrl;
