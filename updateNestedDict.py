def getUpdateNestedDict(ori, update, matchType=0, addNonExisted=True):
    '''
    return a updated dictionary, original dictionary remain untouched.
    '''
    oriCopy=ori.copy()
    for k in update.keys():
        if k in oriCopy.keys():
            if isinstance(oriCopy[k], dict) and isinstance(update[k], dict):              
                updateNestedDict(oriCopy[k], update[k], matchType=matchType, addNonExisted=addNonExisted)
            else:
                if not matchType:
                    oriCopy[k] = update[k]
                else:
                    if type(oriCopy[k]) == type(update[k]):
                        oriCopy[k] = update[k] 
        else:
            if addNonExisted:
                oriCopy[k] = update[k]
    return oriCopy


def updateNestedDict(ori, update, matchType=0, addNonExisted=True):
    '''
    update original input dictionary
    '''
    for k in update.keys():
        if k in ori.keys():
            if isinstance(ori[k], dict) and isinstance(update[k], dict):              
                updateNestedDict(ori[k], update[k], matchType=matchType, addNonExisted=addNonExisted)
            else:
                if not matchType:
                    ori[k] = update[k]
                else:
                    if type(ori[k]) == type(update[k]):
                        ori[k] = update[k] 
        else:
            if addNonExisted:
                ori[k] = update[k]
    #return ori


//Test script
import json 
a={
    'aa':{
        'aa1':5,
        'aa2':{
            'aa2a':4,
            'aa2b':5,
            'aa2c':{}
        },
        'aa3':{
            'aa3a':4,
            'aa3b':{}
        }
    },
    'bb':5,
    'cc':{
    }
}

b = {
    'bb':3,
    'cc':{
        'cc1':{
            'cc1a':5,
            'cc1b':{},
            'cc1c':3
        }
    },
    'aa':{
        'aa2':{
            'aa2a':3,
            'aa2c':{
                'aa2c1':1
            }
        },
        'aa3':{
            'aa3a': {},
            'aa3b': 555
        },
        'aa4':8,
        'aa5':{
            'aa5a':4,
            'aa5b':3
        }
    },
    'ee':{}
}


p = getUpdateNestedDict(a, b, matchType=1, addNonExisted=True)
updateNestedDict(a, b, matchType=1, addNonExisted=True)

print json.dumps(a, indent=4)
print json.dumps(p, indent=4)

