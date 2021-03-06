import time
# WEEK 1
# Week 1 Assignment1
'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the
number at the end of the line below. Convert the extracted value to a floating
point number and print it out.
'''
text = "X-DSPAM-Confidence:    0.8475"
numf = text[text.find('0'):text.find('5')]
# print(float(numf))

# WEEk 3
# Week 3 Assignment # 1
'''
7.1 Write a program that prompts for a file name, then opens that file and reads
through the file, and print the contents of the file in upper case. Use the file
words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt
'''
def inputCheck():
    file = input("Enter the file name: ")
    # Exceptional handling     
    try:    
        txt = open(file,'r')
        return txt
    except:
        print('File Not found')
        return inputCheck()

# txt = inputCheck()
# readable_txt = txt.read()
# print(readable_txt.upper())

# Week 3 Assignment # 2
'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below. Do
not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''
def check_input():
    file = input(' Enter the file name: ')
    # Control over user input
    try:
        txt = open(file)
        return txt
    except:
        print('File does not exists')
        return check_input()

txt = check_input()
no_items = 0
sum_items = 0

for line in txt:
    if line.startswith("X-DSPAM-Confidence:"):
        no_items += 1
        start = line.find('X-DSPAM-Confidence: ')
        end = line.find('/n')
        # Bcz start line is same so i add the length of the start. and start after that
        found = line[start+20:end]
        sum_items += float(found)

avg = sum_items / no_items 

print(f'Total number of items: {no_items}')
print(f'Sum of the items: {sum_items}')
print(f'Average of the items: {avg}')