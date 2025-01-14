# sort the dict

freq =Frequency = {2: 3, 4: 3, 1: 2, 5: 1, 3: 1}


from functools import cmp_to_key

def compare(x,y):
    if freq[x] > freq[y]:
        return 1
    else:
        return 0
    
sortedfreq = sorted(freq,key=cmp_to_key(compare))
sfreq = sorted(freq)
print("by value: ",sortedfreq)
print("by key: ",sfreq)