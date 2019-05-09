import json
# with open("items.jl", "r") as read_file:
#     for l in read_file:
#         d = json.loads(l)
#         print(type(d['link']))

# dt = ['Brand', 'Operating System Type', 'Display Resolution', 'Storage Capacity', 'Depth', 'Width', 'FM Radio', 'Number Of SIM', 'Product weight', 'Mobile Phone Type', 'Cellular Network Technology', 'Number of Cores', 'Chipset manufacturer', 'Model Number', 'EAN-13', ' Battery Capacity in mAh', 'External Product ID Type', 'External Product ID', 'Item EAN', 'Rear Camera Resolution', '3.5 mm Audio Jack', 'Display Size (Inch)', 'Bluetooth version', 'Bluetooth', 'NFC', 'Front Camera', 'Front Flash', 'Color', 'Fast Charge', 'Height', 'Memory RAM']
# dd = ['HUAWEI', 'Android', '1440 x 3120', '128 GB', '176 millimeters', '96 millimeters', False, 'Dual SIM', '540 grams', 'Smartphone', '4G LTE', '8', 'Huawei Kirin', 'Mate 20 PRO', '6901443260690', '4000 - 5000 mAH', 'EAN-13', '6901443260690', '2724678270456', '40MP + 20MP + 8MP', False, '6.3 Inch', '5', True, True, '24MP\xa0', False, 'Emerald Green', True, '60 millimeters', '6 GB']
#
# print(len(dt))
# print(len(dd))
# # for t,d in enumerate(dt),enumerate(dd):
# #     print(t + ": "+ d)
# str="{"
# for (t,d) in zip(dt,dd):
#     str += "'"+t +"':'"+d + "',"
# str[:-1]
# str+='}'
# print(str)
# d=[]
# print(len(d)==0)
#
# res = dict(zip(dt, dd))
# # valu = 'fi-x'
# # res = False if valu == 'fi-x' else True
# print(res)

#
# d = {'link': {'Brand': 'HUAWEI', 'Operating System Type': 'Android', 'Display Resolution': '1440 x 3120', 'Storage Capacity': '128 GB', 'Depth': '176 millimeters', 'Width': '96 millimeters', 'FM Radio': False, 'Number Of SIM': 'Dual SIM', 'Product weight': '540 grams', 'Mobile Phone Type': 'Smartphone', 'Cellular Network Technology': '4G LTE', 'Number of Cores': '8', 'Chipset manufacturer': 'Huawei Kirin', 'Model Number': 'Mate 20 PRO', 'EAN-13': '6901443260690', ' Battery Capacity in mAh': '4000 - 5000 mAH', 'External Product ID Type': 'EAN-13', 'External Product ID': '6901443260690', 'Item EAN': '2724678270456', 'Rear Camera Resolution': '40MP + 20MP + 8MP', '3.5 mm Audio Jack': False, 'Display Size (Inch)': '6.3 Inch', 'Bluetooth version': '5', 'Bluetooth': True, 'NFC': True, 'Front Camera': '24MP\xa0', 'Front Flash': False, 'Color': 'Emerald Green', 'Fast Charge': True, 'Height': '60 millimeters', 'Memory RAM': '6 GB'}}
# print(type(d))
# print(type(d['link']))
# print(len(list(d['link'].keys())))
# print((list(d['link'].values())))

#print(json.dump([{t,d} for (t,d) in zip(dt,dd)]))
# from scrapy import Selector
#
# val = Selector(text="""
#    <ul class = "list">
#       <li class="attr">one</li>
#       <li>one</li>
#
#    </ul>
#
#    <ul class = "list">
#       <li>four</li>
#       <li>five</li>
#       <li>six</li>
#    </ul>""")
# res = lambda x: val.xpath(x).extract()
# print(res("//li[@class='attr']"))
# print(res("//li[@class='attr']/following-sibling::li[1]/text()"))

# jstr = """
# (function() {
# 		var getProducts = function() {
# 			var products = [{"variant_id":"5501214-4082203991","list_price":"4499.00","catalog_id":"5501214-40959303921-cat","final_price":"3499.00","brand":"SAMSUNG ","catalog_options":[" Blue","512GB"],"sku":"MOSGHN960FZBHKSA","currency":"SAR","title":"SAMSUNG GALAXY NOTE 9 DUAL SIM,  blue, 512gb","category_ids":["ho04780711","ho04780711_mobi","ho04780711_mobi_sams"],"categories":["Home","Mobiles","Samsung"],"discount":22},{"variant_id":"5501214-62162891193","list_price":"4499.00","catalog_id":"5501214-40959303921-cat","final_price":"3499.00","brand":"SAMSUNG ","catalog_options":[" Black","512GB"],"sku":"MOSGHN960FZKHKSA","currency":"SAR","title":"SAMSUNG GALAXY NOTE 9 DUAL SIM,  black, 512gb","category_ids":["ho04780711","ho04780711_mobi","ho04780711_mobi_sams"],"categories":["Home","Mobiles","Samsung"],"discount":22},{"variant_id":"5501214-62468547737","list_price":"4499.00","catalog_id":"5501214-40959303921-cat","final_price":"3499.00","brand":"SAMSUNG ","catalog_options":[" Purple\t","512GB"],"sku":"MOSGHN960FZPHKSA","currency":"SAR","title":"SAMSUNG GALAXY NOTE 9 DUAL SIM,  purple , 512gb","category_ids":["ho04780711","ho04780711_mobi","ho04780711_mobi_sams"],"categories":["Home","Mobiles","Samsung"],"discount":22},{"variant_id":"5501214-65183174362","list_price":"3599.00","catalog_id":"5501214-40959303921-cat","final_price":"2999.00","brand":"SAMSUNG ","catalog_options":[" Black","128GB"],"sku":"MOSGHN960FZKDKSA","currency":"SAR","title":"SAMSUNG GALAXY NOTE 9 DUAL SIM,  black, 128gb","category_ids":["ho04780711","ho04780711_mobi","ho04780711_mobi_sams"],"categories":["Home","Mobiles","Samsung"],"discount":17},{"variant_id":"5501214-74080109059","list_price":"3599.00","catalog_id":"5501214-40959303921-cat","final_price":"2999.00","brand":"SAMSUNG ","catalog_options":[" Blue\t","128GB"],"sku":"MOSGHN960FZBDKSA","currency":"SAR","title":"SAMSUNG GALAXY NOTE 9 DUAL SIM,  blue , 128gb","category_ids":["ho04780711","ho04780711_mobi","ho04780711_mobi_sams"],"categories":["Home","Mobiles","Samsung"],"discount":17},{"variant_id":"5501214-79673154578","list_price":"3599.00","catalog_id":"5501214-40959303921-cat","final_price":"2999.00","brand":"SAMSUNG ","catalog_options":[" Purple\t","128GB"],"sku":"MOSGHN960FZPDKSA","currency":"SAR","title":"SAMSUNG GALAXY NOTE 9 DUAL SIM,  purple , 128gb","category_ids":["ho04780711","ho04780711_mobi","ho04780711_mobi_sams"],"categories":["Home","Mobiles","Samsung"],"discount":17}];
# 			return $.map(products, function(product, i) {
# 				return{"name":product.title,
# 							 "id":product.sku,
# 							 "price":product.final_price,
# 							 "brand":product.brand,
# 							 "category":product.categories ? product.categories.join("/") : "",
# 							 "variant":product.catalog_options ? product.catalog_options.join(",") : ""
# 							};
# 			});
# 		};
# 		window.dataLayer = window.dataLayer || [];
# 		window.dataLayer.push({"ecommerce":{"detail":{"products":getProducts()}}});
# 		window.dataLayer.push({"page_type": "product"});
# 	})();
#
#
#
#
#
#
# """

# jsonstr = jstr[jstr.find("[{"):jstr.find("}];")+2]
# print(jsonstr)
# jm=json.loads(jsonstr,strict =False)
# print(type(jm))
# print(len(jm))
# print((jm[0]['list_price']))
# str1=[1,2,3]
# str2= [4,5,6]
# str1 = str1 + str2
# print(str1)

# l = [{'variant_id': '5501214-14125528698', 'list_price': '899.00', 'catalog_id': '5501214-75957230369-cat', 'final_price': '799.00', 'brand': 'NOKIA ', 'catalog_options': [' Black'], 'sku': 'MONK11DRGBW1A04', 'currency': 'SAR', 'title': 'NOKIA 6.1 PLUS 64GB 4G DUAL SIM,  black', 'category_ids': ['ho04780711', 'ho04780711_mobi', 'ho04780711_mobi_noki'], 'categories': ['Home', 'Mobiles', 'Nokia'], 'discount': 11}, {'variant_id': '5501214-72179301974', 'list_price': '899.00', 'catalog_id': '5501214-75957230369-cat', 'final_price': '799.00', 'brand': 'NOKIA ', 'catalog_options': [' Blue'], 'sku': 'MONK11DRGLW1A04', 'currency': 'SAR', 'title': 'NOKIA 6.1 PLUS 64GB 4G DUAL SIM,  blue', 'category_ids': ['ho04780711', 'ho04780711_mobi', 'ho04780711_mobi_noki'], 'categories': ['Home', 'Mobiles', 'Nokia'], 'discount': 11}, {'variant_id': '5501214-99484552435', 'list_price': '899.00', 'catalog_id': '5501214-75957230369-cat', 'final_price': '799.00', 'brand': 'NOKIA ', 'catalog_options': [' White'], 'sku': 'MONK11DRGWW1A04', 'currency': 'SAR', 'title': 'NOKIA 6.1 PLUS 64GB 4G DUAL SIM,  white', 'category_ids': ['ho04780711', 'ho04780711_mobi', 'ho04780711_mobi_noki'], 'categories': ['Home', 'Mobiles', 'Nokia'], 'discount': 11}]
# for i in l :
#     print(i['final_price'])
#     print(i['currency'])
#     print(i['title'])
#     print(i['brand'])
#     print((i['catalog_options'][0].strip()))
#     try:
#         print(i['catalog_options'][1])
#     except:
#         pass
#


# i.xpath('following-sibling::dd[1]/text()').extract()
import unicodedata
# import re
#
#
#
#
#
# s = 'https://saudi.souq.com/sa-ar/D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%D8%AC-%D8%AC%D8%A7%D9%84%D8%A7%D9%83%D8%B3%D9%8A-%D9%86%D9%88%D8%AA-8-%D8%B4%D8%B1%D9%8A%D8%AD%D8%AA%D9%8A%D9%86-%D8%A7%D8%AA%D8%B5%D8%A7%D9%84-64-%D8%AC%D9%8A%D8%AC%D8%A7-6-%D8%AC%D9%8A%D8%AC%D8%A7-%D8%B1%D8%A7%D9%85-%D8%AC%D9%8A%D9%84-%D8%A7%D9%84%D8%B1%D8%A7%D8%A8%D8%B9-%D8%A7%D9%84-%D8%A7%D9%8A-%D8%AA%D9%8A-%D8%A7%D8%B3%D9%88%D8%AF-23879228/i/>'
#
# print(s.split("/")[-3])
# to_be_arabic = s.split("/")[-3]
# out = re.sub("%", "\\x", to_be_arabic)
# print(out)
# print(out.encode(encoding='utf-8'))
# print(out.decode("utf-8"))
#
# print(out[out.rfind("\\x")])
#
# # out = re.sub("%", "\\x", s)
# # print(out)
# #
# # s=out.encode()
# # print(s)
# # for i in s:
# #     print(i)
# # # print(s.decode("utf-8"))
# # # print(type(s))
# # # i = b'\xD8\xB3'
# # # print(type(i))
# # # print(i.decode("utf-8"))

# st = '\nproducts of 678';
# import re
# d=re.findall(r'\d+', st)
# print(int(d[0]))
# import math
# a=40
# t = 678
# print(math.floor(t/a))
#
# lis = ['Internal', '\n32GB', 'External', '\nMicroSD Up to 128GB', 'RAM', '\n3GB', 'Processor', '\nQuad-Core 2.7GHz Krait 450', 'SIM', '\nSingle SIM', 'SIM Slot', '\nMicro SIM', 'OS', '\nAndroid 4.4 KitKat', 'Weight', '\n174g', 'Other Features', '\nFingerprint sensor, S Pen stylus, Document viewer, S-Voice natural language commands and dictation, Air gestures', 'Size', '\n5.6 inches', 'Display Type', '\nSuper AMOLED Capacitive Touchscreen', 'Resolution', '\n1600 x 2560 pixels', 'Primary', '\n16MP', 'Secondary', '\n3.7MP', 'Video Recording', '\n2160p 30fps', 'Flash', '\nLED flash', 'Network', '\n4G', 'WiFi', '\nYes', 'Bluetooth', '\nYes', 'NFC', '\nYes', 'Port', '\nMicroUSB v2.0']
# print(lis[1].strip())
# lin = 'https://www.luluhypermarket.com'
# ima =  ['/medias/sys_master/images/images/h81/h31/9154003402782/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-01.jpg', '/medias/sys_master/images/images/h7c/hbe/9154003992606/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-02.jpg', '/medias/sys_master/images/images/h73/hd6/9154004582430/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-03.jpg', '/medias/sys_master/images/images/h14/h69/9154005172254/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-04.jpg']
# ima = [ lin + i for i in ima]
# print(ima)

# img = [{'url': 'https://www.luluhypermarket.com/medias/sys_master/images/images/h81/h31/9154003402782/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-01.jpg', 'path': 'full/e1c0efaeab0b00978d8ba708d9049e071069c462.jpg', 'checksum': 'ad95ea5931931641f86352b45d58d266'}, {'url': 'https://www.luluhypermarket.com/medias/sys_master/images/images/h7c/hbe/9154003992606/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-02.jpg', 'path': 'full/0825c049d3b9d9b6e8d8ce2af5890374499ac9e3.jpg', 'checksum': '5e6f4fa205ad74bbb9c154822648ba63'}, {'url': 'https://www.luluhypermarket.com/medias/sys_master/images/images/h73/hd6/9154004582430/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-03.jpg', 'path': 'full/bc7342c717268ed9c524b9eea58ae2b64a47f191.jpg', 'checksum': '1fc78310007d9723ba66fd441da77076'}, {'url': 'https://www.luluhypermarket.com/medias/sys_master/images/images/h14/h69/9154005172254/Samsung-Galaxy-Note-Edge-SM-N915F-Black-1025320-04.jpg', 'path': 'full/2db132595a9d8217277bd37c7ac51c0f74562499.jpg', 'checksum': '89e2ea382b32f2870cec01774341dce8'}]
# print(img[3]['path'])

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3=[]
# for x,y in zip(list1, list2):
#     list3.append(x)
#     list3.append(y)
#
# print(list3)

# url = 'https://saudi.souq.com/sa-en/honor-8x-dual-sim-128gb-4gb-ram-4g-lte-blue-38827518/i/'
# print(url.replace("sa-en","sa-ar"))

ll=[]
l = ['https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-32gb-4g-lte-black-11526680/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-32gb-4g-lte-gold-11526690/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-32gb-4g-lte-rose-gold-11526666/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-32gb-4g-lte-silver-11526713/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-32gb-4g-lte-silver-11526713/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-32gb-4g-lte-silver-11526713/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-128gb-4g-lte-silver-11526727/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-256gb-4g-lte-silver-11526671/i/', 'https://saudi.souq.com/sa-en/apple-iphone-7-with-facetime-32gb-4g-lte-silver-11526713/i/']
for i in l :
    ll.append(i)
    ll.append(i.replace("sa-en","sa-ar"))

print(ll)