# -- coding: utf-8 --
import web
from com.com.mysql.DBUtil import *;
#引入模板
render = web.template.render("templates");

urls = (
    '/index','index',
    '/dview','dview',
    '/layoutIndex', 'layoutIndex',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class index:
    def GET(self):
        #return "index method";
        #页面跳转
        web.seeother("/blog/123?username=xlc&password=111111");

class blog:
    def GET(self):
        print ("获取GET提交数据:")
        print web.input();
        return "blog method";

    def POST(self):
        print "POST提交数据:";
        print web.input();
        print "区取内容的头文件";
        print web.ctx.env;
        return "blog post method";


class hello:
    def GET(self, name):
        return render.index();
        #return open("index.html",'r').read();



class dview:
    def GET(self):
        toUser = "jack";
        fromUser = "mark";
        createTime = "2017-12-27 17:34";


        article = {"title":"文章1","desc":"内容1" };
        article2 = {"title": "文章1", "desc": "内容1"};
        articles = [article,article2];
        articleCnt = len(articles);

        print len(articles);
        return render.dview(toUser,fromUser,createTime,articleCnt,articles);

class layoutIndex:
    def GET(self):
        #查询数据库
        print "=====查询数据库====";
        dbUtil = DBUtil("learn");
        print dbUtil;

        sql = "select * from account";
        dbUtil.getCursor().execute(sql);
        accountList =  dbUtil.getCursor().fetchall();
        #print accountList;
        for account in accountList:
            print account;


        irender = web.template.render("templates", base ="layout");
        return irender.layoutIndex("Lisa", "Hayes",accountList);



if __name__ == "__main__":
    app.run()