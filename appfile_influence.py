import json
import codecs
from pprint import pprint
data = []
with open('/Users/lxb/Desktop/user.json') as f:
    for line in f:
        data.append(json.loads(line))

# print(data.count())

count = len(data);
numOf2 = 0.0
numOf2buy = 0.0
numOf3 = 0.0
numOf3buy = 0.0


for line in data:
    if(line["appfile"].encode("utf8") == '2') :
        numOf2 += 1
        if(line["label"] == 1) :
            numOf2buy += 1
    if(line["appfile"].encode("utf8") == '3') :
        numOf3 += 1
        if(line["label"] == 1) :
            numOf3buy += 1

print data[0]

print "ratio of 2 buy: ", numOf2buy

print "ration of 3 buy: ", numOf3buy

print "ratio of appfile 2 buying the VIP is : ", numOf2buy / count
print "ratio of appfile 2 not buying the VIP is : ", (numOf2 - numOf2buy) / count
print "ratio of appfile 3 buying the VIP is : ", numOf3buy / count
print "ratio of appfile 3 not buying the VIP is : ", (numOf3 - numOf3buy) / count



