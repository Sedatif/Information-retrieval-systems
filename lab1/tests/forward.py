import os

def forwardIndex():
    wordsAdded = {}
    keywords = {}
    with open('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\keywords.txt', 'r') as KeywordsFile:
        keywords = KeywordsFile.read()
        KeywordsFile.close()
    #print(keywords)
    cwd = os.getcwd()
    os.chdir('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\test_text_files')
    fileList = os.listdir(os.getcwd())
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            wordsAdded[f.name] = []
            for word in words:
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word in keywords and word not in wordsAdded[f.name]:
                    wordsAdded[f.name] += [word]
    return wordsAdded

def createDictionary():
    wordsAdded = {}
    keywords = {}
    with open('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\keywords.txt', 'r') as KeywordsFile:
        keywords = KeywordsFile.read()
    
    cwd = os.getcwd()
    os.chdir('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\test_text_files')
    fileList = os.listdir(os.getcwd())
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            wordsAdded[f.name] = []
            for word in words:
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word in keywords and word not in wordsAdded[f.name]:
                    wordsAdded[f.name] += [word]
    return wordsAdded, cwd

def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\forward_index_file.txt', 'w') as indexFile:
        for file, files in words.items():
            indexFile.write(file[:file.find(".txt")] + " ")
            for word in files:
                indexFile.write(word + " ")
            indexFile.write('\n')
    return words
            
#writeToFile(*createDictionary())