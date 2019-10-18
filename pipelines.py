# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# Scraped data -> Item containers -> Pipeline -> SQL/MongoDB database

import mysql.connection


class QuotetutorialsPipeline(object):
    def __init__(self):
        self.conn= pymongo.MongoClient(
            'localhost',
            27017
        )
        db=self.conn['myquotes']
        self.collection =db['quotes_tb']

    def create_connection(self):
        self.conn= mysql.connector.connect(
            host= 'localhost',
            user='root',
            passwd='12345',
            database='myquotes'
        )
        self.curr= self.conn.cursor()

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
