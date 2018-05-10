def deepSortDictToList(source):
    tmp=[]
    if isinstance(source, dict):
        for k, v in sorted( source.items(), key=lambda pair: (type(pair[1]), pair[0])):     
            tmp.append(k)
            tmp.append( deepSortDictToList( v ) )
    else:
        tmp.append(source)
    return tmp


def deepSortDictToString(source, count=-1):
    tmp = ''    
    if isinstance(source, dict):
        count += 1
        for k, v in sorted( source.items(), key=lambda pair: (type(pair[1]), pair[0])): 
            tmp += '\t'*count              
            tmp += k                         
            if isinstance( v, dict):                
                tmp += '\n'                
            tmp += str( deepSortDictToString( v, count)  )
            
    else: 
        tmp += '='       
        tmp += str(source)
        tmp += '\n'

    return tmp
