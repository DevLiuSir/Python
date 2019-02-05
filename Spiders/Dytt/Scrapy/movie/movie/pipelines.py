# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# 设计管道存储爬取的内容
class MoviePipeline(object):

    # 开启爬虫前调用
    def open_spider(self, spider):
        '''
        # 关于open()的mode参数：
        # 'r'：读
        # 'w'：写
        # 'a'：追加
        # 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
        # 'w+' == w+r（可读可写，文件若不存在就创建）
        # 'a+' ==a+r（可追加可写，文件若不存在就创建）
        # 对应的，如果是二进制文件，就都加一个b就好啦：
        # 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
        '''
        self.file = open(r'/Users/liuchuan/Desktop/dytt.txt', 'a+', encoding='utf-8')


    # parse()返回值时调用，一般在这里写入数据
    def process_item(self, item, spider):
        try:
            res = dict(item)
            content = res['download_url']
            print(f"[INFO]: 已保存: {content}")
            self.file.write(content + '\n')             # write: 写入本地, 且只能写入文本
        except:
            pass


    # 关闭爬虫后调用，此处用于关闭文件连接
    def close_spider(self, spider):
        self.file.close()