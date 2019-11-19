import sys
import pymongo
import scrapy


# db connection
uri = 'mongodb://admin:admin123@ds241298.mlab.com:41298/ds_project?retryWrites=false'
client = pymongo.MongoClient(uri)
db = client.get_default_database()
collection = db['users']


# App


class CNESpider(scrapy.Spider):
    name = "cne"

    def start_requests(self):
        url = 'http://www4.cne.gob.ve/web/registro_electoral/imprimir_datos_elector.php?nacionalidad=V&cedula=20614599'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

# collection.insert_one({
#     "name": "Jhon"
# })

# users = collection.find({})
# for user in users:
#     print('user', user)
