# -*- coding: utf-8 -*-
import urlManager, htmlDownloader, htmlParser, htmlOutputer

class SpiderMain(object):

    def __init__(self):
        self.urls = urlManager.UrlManager();
        self.downloader = htmlDownloader.HtmlDownloader();
        self.parser = htmlParser.HtmlParser();
        self.outputer = htmlOutputer.HtmlOutputer();


    def craw(self, rootUrl):
        count = 1;
        self.urls.add_new_url(rootUrl);
        while self.urls.has_new_url():
            try:
                newUrl = self.urls.get_new_rul();
                print 'craw %d : %s ' % (count, newUrl);
                html_cont = self.downloader.download(newUrl);
                new_urls, new_data = self.parser.parse(newUrl, html_cont)
                self.urls.add_new_urls(new_urls);
                self.outputer.collect_data(new_data);
                if count == 100:
                    break;
                count = count + 1;
            except:
                print "craw failed."
        self.outputer.output_html();



if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313";
    obj_spider = SpiderMain();
    obj_spider.craw(root_url);