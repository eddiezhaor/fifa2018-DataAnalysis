#Runhao Zhao (rz6dg) Wenxi Zhao (wz8nx) Shaoran Li (sl4bz) Winfred Hill (whh3rz) Jingnan Yang (jy4fch)
#the following codes scrape Name age rating potential value wage and total from https://sofifa.com/
'''
Runhao Zhao (rz6dg)
Wenxi Zhao (wz8nx)
Shaoran Li (sl4bz)
Winfred Zhao (whh3rz)
Jingnan Yang (jy4fch)
'''
import scrapy;
import os;
from scrapy.selector import Selector
import pandas as pd
class amazonSpider(scrapy.Spider):
    name="fifa"
    #inialize all lists
    player=[]
    age=[]
    rating=[]
    wage=[]
    potential=[]
    value=[]
    total=[]
    page=0
    #if the output file already exists, delete it.
    # url="https://sofifa.com/players?showCol=wi&showCol=hi&showCol=cr&showCol=bl&showCol=ac&showCol=ag&showCol=ba&showCol=ar&showCol=cm&showCol=td"
    url="https://sofifa.com/players?v=18&e=159166&set=true&currency=USD"
    start_urls=[url]
    def parse(self,response):
        count=0
        #find player name
        for i in response.xpath("//a[contains(@href, '/player/')]/text()").extract():
            self.player.append(i)
             #find player age
        for i in response.xpath("//div[@class='col-digit col-ae']/text()").extract():
            self.age.append(i)
             #find player rating
        for i in response.xpath("//div[@class='col-digit col-oa']/span/text()").extract():
            self.rating.append(i)
             #find player potential
        for i in response.xpath("//div[@class='col-digit col-pt']/span/text()").extract():
            self.potential.append(i) 
            #find player value         
        for i in response.xpath("//div[@class='col-digit col-vl']/text()").extract():
            self.value.append(i) 
             #find player wage
        for i in response.xpath("//div[@class='col-digit col-wg']/text()").extract():
            self.wage.append(i)  
             #find player total
        for i in response.xpath("//div[@class='col-digit col-tt']/text()").extract():
            self.total.append(i)    
        self.page+=50
        #find the next page url
        next_page_url=response.xpath("//a[@class='btn pjax']/@href").extract()
        if len(next_page_url)==1:
            next_page_url=next_page_url[0]
        else:
            next_page_url=next_page_url[1]
        if next_page_url is not None and self.page<=18000:
            #go to the next page
            yield scrapy.Request(response.urljoin(next_page_url))
        else:
            finalList=[]
            finalList.append(self.player)
            finalList.append(self.age)
            finalList.append(self.rating)
            finalList.append(self.wage)
            finalList.append(self.potential)
            finalList.append(self.value)
            finalList.append(self.total)
            header=["NAME","AGE","RATING","WAGE","POTENTIAL","VALUE","TOTAL"]
            df=pd.DataFrame(finalList)
            df1=df.T
            #add header
            df1.columns=header
            #output to a csv file
            df1.to_csv("fifa.csv")

#repeat the codes below to scrape different attributes(one attribute each time)
# import scrapy;
# import os;
# from scrapy.selector import Selector
# import pandas as pd
# class amazonSpider(scrapy.Spider):
#     name="fifa"
#     #specify the domain
#     #ask for user input 
#     player=[]
#     age=[]
#     weight=[]
#     height=[]
#     rating=[]
#     wage=[]
#     potential=[]
#     crossing=[]
#     value=[]
#     ballControll=[]
#     acceleration=[]
#     team=[]
#     agility=[]
#     balance=[]
#     aggression=[]
#     composure=[]
#     defending=[]
#     total=[]
#     position=[]
#     page=0
#     #if the output file already exists, delete it.
#     # url="https://sofifa.com/players?showCol=wi&showCol=hi&showCol=cr&showCol=bl&showCol=ac&showCol=ag&showCol=ba&showCol=ar&showCol=cm&showCol=td"
#     url="https://sofifa.com/players?v=18&e=159166&set=true&currency=USD&showCol=td&units=mks"
#     start_urls=[url]
#     def parse(self,response):
#         count=0
#         for i in response.xpath(".//tr"):
#             for b in i.xpath(".//td[6]/div[@class='col-name text-ellipsis rtl']"):
#                 if b.xpath("//a[contains(@href,'/players?')]/@title").extract() is not None:
#                     for e in b.xpath("//a[contains(@href,'/players?')]/@title").extract():
#                         self.team.append(e)
#                 if b.xpath("//a[contains(@href,'/team/')]/text()").extract() is not None:
#                     for d in b.xpath("//a[contains(@href,'/team/')]/text()").extract():
#                         self.team.append(d)
#         # for i in response.xpath("//a[contains(@href, '/player/')]/text()").extract():
#         #     self.player.append(i)
#         # for i in response.xpath("//div[@class='col-digit col-ae']/text()").extract():
#         #     self.age.append(i)
#         # for i in response.xpath("//div[@class='col-digit col-oa']/span/text()").extract():
#         #     self.rating.append(i)
#         # for i in response.xpath("//div[@class='col-digit col-pt']/span/text()").extract():
#         #     self.potential.append(i)        
#         # for i in response.xpath("//div[@class='col-digit col-hi']/text()").extract():
#         #     self.height.append(i)   
#         # for i in response.xpath("//div[@class='col-digit col-wi']/text()").extract():
#         #     self.weight.append(i)    
#         # for i in response.xpath("//div[@class='col-digit col-vl']/text()").extract():
#         #     self.value.append(i) 
#         # for i in response.xpath("//div[@class='col-digit col-wg']/text()").extract():
#         #     self.wage.append(i)  
#         # for i in response.xpath("//div[@class='col-digit col-cr']/span/text()").extract():
#         #     self.crossing.append(i) 
#         # for i in response.xpath("//div[@class='col-digit col-bl']/span/text()").extract():
#         #     self.ballControll.append(i) 
#         # for i in response.xpath("//div[@class='col-digit col-ac']/span/text()").extract():
#         #     self.acceleration.append(i) 
#         # for i in response.xpath("//div[@class='col-digit col-ag']/span/text()").extract():
#         #     self.agility.append(i) 
#         # for i in response.xpath("//div[@class='col-digit col-ba']/span/text()").extract():
#         #     self.balance.append(i)
#         # for i in response.xpath("//div[@class='col-digit col-ar']/span/text()").extract():
#         #     self.aggression.append(i)
#         # for i in response.xpath("//div[@class='col-digit col-cm']/span/text()").extract():
#         #     self.composure.append(i)
#         # for i in response.xpath("//div[@class='col-digit col-td']/text()").extract():
#         #     self.defending.append(i) 
#         # for i in response.xpath(".//div[@class='text-clip rtl']"):
#         #     my=[]
#         #     for a in i.xpath(".//a[contains(@href,'/players?')]/span[contains(@class,'pos')]/text()").extract():
#         #         print(a)
#         #         my.append(a)
#         #     self.position.append(my)
#         # for i in response.xpath("//div[@class='col-digit col-tt']/text()").extract():
#         #     self.total.append(i)    
#         self.page+=50
     
#         next_page_url=response.xpath("//a[@class='btn pjax']/@href").extract()
#         if len(next_page_url)==1:
#             next_page_url=next_page_url[0]
#         else:
#             next_page_url=next_page_url[1]
#         if next_page_url is not None and self.page<=50:
#             yield scrapy.Request(response.urljoin(next_page_url))
#         else:
#             finalList=[]
#             # finalList.append(self.defending)
#             # finalList.append(self.age)
#             finalList.append(self.team)
#             # finalList.append(self.rating)
#             # finalList.append(self.wage))
#             # finalList.append(self.potential)
#             # finalList.append(self.value)
#             # finalList.append(self.total)
#             # finalList.append(self.team)
#             # header=["NAME","AGE","RATING","WAGE","POTENTIAL","VALUE","TOTAL"]
#             header=["Team"]
#             df=pd.DataFrame(finalList)
#             df1=df.T
#             print("hello")
#             df1.columns=header
#             df1.to_csv("team1.csv")