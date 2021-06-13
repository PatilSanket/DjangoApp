from django.shortcuts import render
from GOT.utils import get_col_handle
from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import urlparse

col_handle = get_col_handle()

# Create your views here.
def AllBattles(self):
    res = col_handle.find({}, {'name':1})

    #print(res.next())
    
    return HttpResponse(res)
    #return render(self, "Wars/index.html", {'Wars': res})

def Battle_by_ID(self, ID):
    #ID = str(ID)
    res = col_handle.find({ 'battle_number' : ID })

    return HttpResponse(res)

def Aggregates(self):
    ###For getting count by battle_type
    pipeline1 = [{"$group":
         {
           "_id": "$battle_type",
           "WarCount": { "$sum": 1 }
         }} ]  

    ###Aggregate Functions i.e. min, max and avg 
    aggr = [{ "$group": {
        "_id": "",
        "count": { "$sum": 1 },
        "max": { "$max": "$defender_size" },
        "min": { "$min": "$defender_size" },
        "avg": { "$avg": "$defender_size" }
        }}]
               
    res1 = col_handle.aggregate(pipeline1)
    print(res1)

    return HttpResponse(res1)

    


