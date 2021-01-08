# Python-30-Days
## Day 04
### Python for Everybody- Using Python to Access Web Data- Coursera
Today i am learning from python for everybody | Using Python to Access Web Data
Week 1-2 | Coursera Course.
What i **learn** Today:
1. Regular Expressions
2. Raw String

## Week 01 to 02 Completed
All the class code is in [Class_Code.ipynb]('/Class_Code.ipynb') class code file is a notebook file it also includes the **assignments** with output and practice code with nice formating and output.

----

## 1. Regular Expression
A regular expression is the sequence of characters that defines a search pattern. regular expressions are use in searching, validating emails, phone numbers, and web scraping

- lower case letters a to z (a-z) and uppercase case letters A to Z (A-Z)
- Digits 0 to 9 (0-9)
- digits (\d) and non digits (\D)
- Range [] Group () One or more + Escape following character \

***Escaping:*** is a way of treating characters which have a special meaning in regular expressions literally, rather than as special characters

**You can find many more at here** -> [Regular Expressions Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/pdf/)

### Email Validation
```python
patter = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
email = input('Enter your email: ')
if (re.search(patter,email)):
    print('valid')
else:
    print('invalid')
```
### Simple search
```python
handle = open('mbox-short.txt')
for line in handle:
    line.rstrip()
    # Extract line starts with Received:     
    if re.search('^\s\w+, ',line):
        print(line)
```
```python
# Extract email from file
sent = open('mbox-short.txt')
read_sent = sent.read()

# Mails end with .edu domain
mails = re.findall('\w+.\w+@\w+.edu',read_sent)
print('.edu mails',mails)        

# All the mail adress
mails2 = re.findall('^From (\S+@\S+)',read_sent)
print('all mails',mails2)        

# Just domain
mails2 = re.findall('^From .*@([^ ]*)',read_sent)
print('just specific domain',mails2)        
```
***Chechk Class_Code File for more***

----

## 2. Raw Strings:
Raw string is a very powerfull feauture using which we can intruduce raw strings without escaping any character. this treats characters such as '\' as a literal character
A python raw string prefix r or R e.g *r' '*
```python
# \t treat as Tab & \n treat as new line

# Normal String
nor_string = 'hi \t i am \n shahab'
print(f'Normal String -> {nor_string}')

# raw String
raw_string = r'hi \t i am \n shahab'
print(f'Raw String -> {raw_string}')

# Normal String -> hi 	 i am 
# shahab
# Raw String -> hi \t i am \n shahab
```

----

# Assignments
## Week 02
### **Problem Statement:**
- In this assignment you will read through and parse a file with text and numbers.
- You will extractall the numbers in the file and compute the sum of the numbers.

### **Solution:**
```python
file_handle = open('mbox-short.txt')
file_handle_re = file_handle.read()
file_num = re.findall('[0-9]+ ',file_handle_re)

sum_of = 0
count = 0

for num in file_num:
    sum_of += int(num)
    count += 1

print(f'There are total: {count} values AND Sum of the values are: {sum_of}')

# OUTPUT -->  There are total: 1236 values AND Sum of the values are: 3103023
```
----
# Resources:
- [[5 Minute Tutorial] Regular Expressions (Regex) in Python](https://www.youtube.com/watch?v=UQQsYXa1EHs)
- [How to use Python Raw Strings?](https://www.askpython.com/python/string/python-raw-strings#:~:text=A%20Python%20raw%20string%20is,treated%20as%20a%20escape%20character.)
- [Using Python to Access Web Data](https://www.coursera.org/learn/python-network-data)