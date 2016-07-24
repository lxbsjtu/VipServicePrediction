import json
import codecs
from pprint import pprint
from collections import OrderedDict
import operator
data = []
with open('/Users/lxb/Desktop/user.json') as f:
    for line in f:
        data.append(json.loads(line))

dict0 = {}
dict1 = {}

for line in data:
    if(line["label"] == 0) :
        label = line["category_id"]
        for elem in label :
            e = elem.encode("utf8")
            if(not dict0.has_key(e)) :
                dict0[e] = 0;

            dict0[e] = dict0[e] + 1

    if (line["label"] == 1):
        label = line["category_id"]
        for elem in label:
            e = elem.encode("utf8")
            if (not dict1.has_key(e)):
                dict1[e] = 0;

            dict1[e] = dict1[e] + 1


order_dict0 = sorted(dict0.items(), key = operator.itemgetter(1), reverse=True)
order_dict1 = sorted(dict1.items(), key = operator.itemgetter(1), reverse=True)

print(order_dict0)
print("-------------------------------------------")
print(order_dict1)








