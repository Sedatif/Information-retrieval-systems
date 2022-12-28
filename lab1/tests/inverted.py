import os

def invertedIndex():
    wordsAdded = {}
    cwd = os.getcwd()
    os.chdir('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\test_text_files')
    fileList = os.listdir(os.getcwd())
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            for word in words:
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word not in wordsAdded.keys():
                    wordsAdded[word] = [f.name]
                else:
                    if file not in wordsAdded[word]:
                        wordsAdded[word] += [f.name]
    return wordsAdded

def createDictionary():
    wordsAdded = {}
    cwd = os.getcwd()
    os.chdir('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\test_text_files')
    fileList = os.listdir(os.getcwd())
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            for word in words:
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word not in wordsAdded.keys():
                    wordsAdded[word] = [f.name]
                else:
                    if file not in wordsAdded[word]:
                        wordsAdded[word] += [f.name]
    return wordsAdded, cwd

def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\inverted_index_file.txt', 'w') as indexFile:
        for word, files in words.items():
            indexFile.write(word + " ")
            for file in files:
                indexFile.write(file[:file.find(".txt")] + " ")
            indexFile.write('\n')
    return words

def writeToTestFile(words):
    with open('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\inverted_index_file.txt', 'w') as indexFile:
        for word, files in words.items():
            indexFile.write(word + " ")
            for file in files:
                indexFile.write(file[:file.find(".txt")] + " ")
            indexFile.write('\n')
    return words
            
writeToFile(*createDictionary())