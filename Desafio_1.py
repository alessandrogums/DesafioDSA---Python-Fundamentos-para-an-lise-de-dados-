# primeira forma 

def Caracteres_unicos(string):
    string_fin=''
    if string is None :
        return False 
    else: 
        for carac in string:
            if carac  in string_fin:
                return False
            string_fin+=carac
        return True 

      
# segunda forma 

def Caracteres_unicos(string):
    if string is None:
        return False
    else:
        for k,v in enumerate(string):
            if string.index(v) != k:
                return False
        return True 

#terceira forma 

def Caracteres_unicos(string):
  if string is None:
    return False
  else:
    uni=set(string)
    if len(string) - len(uni)  == 0:
        return True
    return False 
