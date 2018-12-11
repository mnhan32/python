def getUpdateNestedDict(ori, update, matchType=0, addNonExisted=True):
    '''
    return a updated dictionary, original dictionary remain untouched.
    '''
    oriCopy=ori.copy()
    for k in update.keys():
        if k in oriCopy.keys():
            if oriCopy[k] != update[k]:            
                if isinstance(oriCopy[k], dict) and isinstance(update[k], dict):                
                    oriCopy[k] = getUpdateNestedDict(oriCopy[k], update[k], matchType=matchType, addNonExisted=addNonExisted)
                else:
                    if not matchType:
                        pass#print('In non match type mode, key %s has differnt value type than target dictionary, overwrite.'%k, 3)
                        oriCopy[k] = update[k]
                    else:
                        if type(oriCopy[k]) == type(update[k]):
                            pass#print('Update key %s value, was %s now %s.'%(k, oriCopy[k], update[k]))
                            oriCopy[k] = update[k]
            else:
                pass#print('key %s has the same value, skip.'%k)                
        else:            
            if addNonExisted:
                pass#print('In add non existed mode, key %s not exist in target dictionary, add it to target dictionary.'%k, 3)
                oriCopy[k] = update[k]
            else:
                pass#pLog('key %s not exist in target dictionary, skip.'%(pKey+':'+k), 3)
    return oriCopy

def updateNestedDict(ori, update,  matchType=1, addNonExisted=False):
    '''
    update original input dictionary
    '''
    for k in update.keys():
        if k in ori.keys():
            if ori[k] != update[k]:            
                if isinstance(ori[k], dict) and isinstance(update[k], dict):                
                    updateNestedDict(ori[k], update[k], matchType=matchType, addNonExisted=addNonExisted)
                else:
                    if not matchType:
                        pass#print('In non match type mode, key %s has differnt value type than target dictionary, overwrite.'%k, 3)
                        ori[k] = update[k]
                    else:
                        if type(ori[k]) == type(update[k]):
                            pass#print('Update key %s value, was %s now %s.'%(k, ori[k], update[k]))
                            ori[k] = update[k]
            else:
                pass#print('key %s has the same value, skip.'%k)                
        else:            
            if addNonExisted:
                pass#print('In add non existed mode, key %s not exist in target dictionary, add it to target dictionary.'%k, 3)
                ori[k] = update[k]
            else:
                pass#pLog('key %s not exist in target dictionary, skip.'%(pKey+':'+k), 3)

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

