from datetime import datetime

name =input("enter your name:")
# list of items
lists ='''
rice          Rs 50/kg
sugar         Rs 25/kg
tea_powder    Rs 100/kg 
freedom_oil   Rs 105/liter
sprite        RS 90liter
maggi         Rs 55/each
oreo_biscuit Rs 15/each
toothbrush     Rs 1/each
'''
# print(lists)
#declaration
price = 0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist =[]
qlist=[]
plist=[]
items={'rice':50,
'sugar':25,
'tea_powder':100,
'freedom_oil':105,
'sprite':90,'maggi':55,'oreo_biscuit':15,'toothrbush':1}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:") 
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5/100)
            finalamount=gst+totalprice
        else:
                print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp =input("can i bill the items yes or no:")
    if inp =='yes':
        pass
        if finalamount!=0:
            print(25*"=","sai supermarket",25*"=")
            print(28*" ","rajahmundry")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(80*"-")
            print("sno",8*" ",'items',5*" ",'Quantity',5*'',3*'','price')
            for i in range (len(pricelist)):
                print(i,4*' ',5*' ',ilist[i],6*' ',qlist[i],9*' ',plist[i])
            print(80*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*" ",'  Rs',gst)
            print(80*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(40*"-")
            print(60*"","Thanks for visiting")
            print(80*"-")
