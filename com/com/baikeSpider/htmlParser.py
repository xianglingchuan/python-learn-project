# -*- coding: utf-8 -*-
from bs4 import  BeautifulSoup
import re;
import urlparse;
class HtmlParser(object):

    def _get_new_urls(self, pageUrl, soup):
        new_urls = set();
        #/item/%E7%88%B1%E5%A5%BD%E8%80%85
        links = soup.find_all('a', href=re.compile(r"item"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(pageUrl, new_url)
            new_urls.add(new_full_url);
        return new_urls;

    def _get_new_data(self, pageUrl, soup):
        resData = {}
        resData['url'] = pageUrl;

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>......</h1></dd>
        titleNode = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1');
        resData['title'] = titleNode.get_text();

        #<div class="lemma-summary" label-module="lemmaSummary">.......</div>
        summaryNode = soup.find('div', class_="lemma-summary")
        resData['summary'] = summaryNode.get_text();

        return resData;



    def parse(self, pageUrl, html_cont):
        if pageUrl is None or html_cont is None:
            return
        #print "parse......";
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8");
        newUrls = self._get_new_urls(pageUrl, soup);
        newData = self._get_new_data(pageUrl, soup);
        return newUrls, newData;
