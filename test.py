from sys import argv
import sys, os
import os.path
import gzip
import subprocess
import re

dataDictionary = {}
minTestCases = 8
testNumber = 0
numRows = 1 #1 to account for Column Header line
numSampleRows = 5
numSampleColumns = 5
checkMark = '&#9989;'
redX = '&#10060;'
complete = True
fail = False


keyFileName = 'testdata.tsv'
testFileName = 'data.tsv'
statusFileName = 'status.md'
downloadFileName = 'download.sh'
installFileName = 'install.sh'
parsePyFileName = 'parse.py'
parseShFileName = 'parse.sh'
keyFilePath = argv[1] + keyFileName
testFilePath = argv[1] + testFileName
statusFilePath = argv[1] + statusFileName
statusFile = open(statusFilePath, 'w')
requiredFiles = [keyFileName, downloadFileName, installFileName, parseShFileName, parsePyFileName]


# Making sure path exists
print('Testing file paths...')
statusFile.write('---\n##### Testing file paths . . .\n\n')
for path in requiredFiles:
    if os.path.exists(argv[1] + path):
        statusFile.write(checkMark + '\t' + path + ' exists.\n\n')
    else:
        statusFile.write(redX + '\t' + path + ' does not exist.\n\n')
        fail = True
if fail:
    print('Fail')
    statusFile.write('###### Results: **FAIL**\n---')
    complete = False
else:
    print('Success')
    statusFile.write('###### Results: PASS\n\n---\n##### Testing user code and test file . . .\n')

    # Run User-generated scripts
    os.chdir(argv[1])
    os.system('chmod +x ./download.sh')
    os.system('chmod +x ./parse.sh')
    os.system('./download.sh')
    os.system('./parse.sh')
    string1 = str(subprocess.check_output(['file', '-b', argv[1] + testFileName + '.gz']))
    if os.path.exists(argv[1] + testFileName + '.gz'):
        if re.search(r"gzip compressed data", string1):
            subprocess.call(['gzip', '-d', argv[1] + testFileName])
            statusFile.write(checkMark + '\t' + testFileName + '.gz was created and zipped correctly.\n\n')
        else:
            statusFile.write(redX + '\t' + argv[1] + testFileName + '.gz is not properly zipped.\n\n')
            fail = True
    else:
        statusFile.write(redX + '\t' + testFileName + '.gz does not exist.\n\n')
        fail = True
    if os.path.exists(testFilePath):
        statusFile.write(checkMark + '\t' + testFileName + ' is the test file.\n\n')
    else:
        statusFile.write(redX + '\t' + testFileName + ' does not exist.\n\n')
        fail = True

    # Open Files
    keyFile = open(keyFilePath, 'r')
    testFile = open(testFilePath, 'r')
    testHeaderData = testFile.readline().rstrip('\n').split('\t')

    # Make Sure key file "testdata.tsv" has enough Tests
    print('Testing key file...')
    numTests = -1 #-1 to not include header line
    for line in keyFile:
        numTests = numTests + 1
    keyFile.close()
    keyFile = open(keyFilePath, 'r')
    keyHeaderData = keyFile.readline().rstrip('\n').split('\t')
    if numTests == 0:
        statusFile.write(redX + '\t' + keyFileName + ' is empty\n\n')
        fail = True
    elif numTests < minTestCases:
        statusFile.write(redX + '\t' + keyFileName + ' does not contain enough test cases. (' + str(numTests) + '; minimum = ' + str(minTestCases) + ')\n\n')
        fail = True
    else:
        statusFile.write(checkMark + '\t' + keyFileName + ' contains enough test cases (' + str(numTests) + '; minimum = ' + str(minTestCases) + ')\n\n')
    if fail:
        print('Fail')
        statusFile.write('###### Results: **FAIL**\n---')
        complete = False
    else:
        print('Success')
        statusFile.write('###### Results: PASS\n---')

    #Print sample of output file and print # of columns and rows in source File
    statusFile.write('\n##### First ' + str(numSampleRows) + ' rows and ' + str(numSampleColumns) + ' columns of test file: \n\n')
    for i in range(numSampleColumns):
        statusFile.write('|\t' + testHeaderData[i])
    statusFile.write('\t|\n')
    for i in range(numSampleColumns):
        statusFile.write('|\t---\t')
    statusFile.write('|\n')
    for line in testFile:
        testData = line.rstrip('\n').split('\t')
        if numRows <= numSampleRows:
            for i in range(numSampleRows):
                statusFile.write('|\t' + testData[i])
            statusFile.write('\t|\n')
        numRows = numRows + 1
        dataDictionary[testData[0]] = testData

    # Make sure first column isn't empty
    if testHeaderData[0] == "":
        statusFile.write('\n**_WARNING:_ First column header is empty. (Should be labeled \"Sample\" in most cases)**\n')
    statusFile.write('**Columns: ' + str(len(testHeaderData)) + ' Rows: ' + str(numRows) + '**\n\n---\n')

    #Begin Tests
    print('Comparing with key file...')
    passedTestCases = True
    statusFile.write('### Test Cases . . .\n\n')
    for line in keyFile:
        testNumber = testNumber + 1
        fail = True
        keyData = line.rstrip('\n').split('\t')
        sample = keyData[0]
        variable = keyData[1]
        value = keyData[2]
        if value == "\"\"":
            value = ""
        compareString = '||\tSample\t|\tColumn\t|\tRow\t|\n|\t---\t|\t---\t|\t---\t|\t---\t|\n|\t**Expected**\t|\t' + sample + '\t|\t' + variable + '\t|\t' + value + '\t|\n'
    #Testing first column
        if (sample not in dataDictionary.keys()):
            failString = '- \"' + sample + '\" is not found in Sample columns'
    #Testing if second column is in Header
        else:
            failString = '- \"' + variable + '\" is not found in Headers'
            for key in dataDictionary.keys():
                if sample in key:
                    for i in range(len(testHeaderData)):
    #Testing if values match
                        if variable == testHeaderData[i] and value == dataDictionary[key][i]:
                            fail = False
                        elif variable == testHeaderData[i] and value != dataDictionary[key][i]:
                            fail = True
                            failString = '\n' + compareString + '|\t**User Generated**\t|\t' + key + '\t|\t' + testHeaderData[i] + '\t|\t' + dataDictionary[key][i] + '\t|\n'
        if fail:
            statusFile.write(redX + '\tTest ' + str(testNumber) + ': Fail\n' + failString + '\n\n')
            complete = False
            passedTestCases = False
        else:
            statusFile.write(checkMark + '\tTest ' + str(testNumber) + ': Success\n\n')
    if passedTestCases:
        print('Success')
        statusFile.write('##### Results: PASS\n---')
    else:
        statusFile.write('##### Results: **FAIL**\n---')
        print('Fail')
        complete = False
    #Close Files
    testFile.close()
    keyFile.close()
statusFile.close()

#Write Status Result to top of Status File
with open(statusFilePath, 'r') as statusFileOriginal: statusContents = statusFileOriginal.read()
with open(statusFilePath, 'w') as statusComplete:
    if complete:
        statusComplete.write('## Status: Complete\n' + statusContents)
        print('Testing Complete: Results = Pass')
    else:
        statusComplete.write('## Status: In Progress\n' + statusContents)
        print('Testing Complete: Results = Fail (See status.md for details)')
