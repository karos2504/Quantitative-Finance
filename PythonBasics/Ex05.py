def process(string, index):
    if index == len(string):
        return
    
    print(string[index])
    
    process(string, index + 1)

process('ABCXYZ', 0)