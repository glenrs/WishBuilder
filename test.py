from sys import argv
#from parse.py import inFilePath
import os.path
import gzip

statusFile = open('status.txt', 'w')

keyFileExtension = '/testdata.tsv'
testFileExtension = '/data.tsv'
keyFilePath = argv[1] + keyFileExtension
testFilePath = argv[1] + testFileExtension

# Making sure path exists
if os.path.exists(keyFilePath):
    if os.path.exists(testFilePath):
        statusFile.write(testFileExtension + ' is the test File.\n')
        statusFile.write(keyFileExtension + ' is the key File.\n\n')
    else:
        statusFile.write(testFileExtension + ' was not created.\n\n')
else:
    statusFile.write(keyFileExtension + ' does not exist.\n\n')

#with gzip
keyFile = open(keyFilePath, 'r')
    #with gzip
testFile = open(testFilePath, 'r')
testHeaderData = testFile.readline().rstrip('\n').split('\t')
keyHeaderData = keyFile.readline().rstrip('\n').split('\t')
dataDictionary = {}
testNumber = 0
numRows = 1 #1 to account for Column Header line
numSampleRows = 5
numSampleColumns = 5

#Print sample of output file and print # of columns and rows in source File
statusFile.write('First ' + str(numSampleRows) + ' rows and ' + str(numSampleColumns) + ' columns of test file: \n\n')
for i in range(numSampleColumns):
    statusFile.write(testHeaderData[i] + '\t')
statusFile.write('\n')
for line in testFile:
    testData = line.rstrip('\n').split('\t')
    if numRows <= numSampleRows:
        for i in range(numSampleRows):
            statusFile.write(testData[i] + '\t')
        statusFile.write('\n')
    numRows = numRows + 1
    dataDictionary[testData[0]] = testData
statusFile.write('\nColumns: ' + str(len(testHeaderData)) + ' Rows: ' + str(numRows) + '\n\n')

#Begin Tests
for line in keyFile:
    testNumber = testNumber + 1
    statusFile.write('Test ' + str(testNumber) + ': ')
    fail = True
    keyData = line.rstrip('\n').split('\t')
    sample = keyData[0]
    variable = keyData[1]
    value = keyData[2]
    if value == "\"\"":
        value = ""
    compareString = sample + '\t' + variable + '\t' + value
#Testing first column
    if (sample not in dataDictionary.keys()):
        failString = '\"' + sample + '\" is not found in Sample column'
#Testing if second column is in Header
    else:
        failString = '\"' + variable + '\" is not found in Headers'
        for key in dataDictionary.keys():
            if sample in key:
                for i in range(len(testHeaderData)):
#Testing if values match
                    if variable == testHeaderData[i] and value == dataDictionary[key][i]:
                        fail = False
                    elif variable == testHeaderData[i] and value != dataDictionary[key][i]:
                        fail = True
                        failString = "Expected Output: \t" + compareString + "\nGenerated Output: \t" + key + ' ' + testHeaderData[i] + ' ' + dataDictionary[key][i]
    if fail:
        statusFile.write('fail\n' + failString + '\n')
    else:
        statusFile.write('success\n')
