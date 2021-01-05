# Python-30-Days
## Day 3
### Python for Everybody- Python data structure - Coursera
Today i am learning from python for everybody | python data structure | Coursera Course.
What i **learn** Today:
- List [ ]
- Dictionaries { }
- Tuples ()
- List Comprehension

## Week 4 to 6 Completed
All the class code is in [Class_Code.ipynb]('/Class_Code.ipynb') class code file is a notebook file it also includes the **assignments** with output.
# Week 4 
## Assignment # 8.4
### **Problem Statement:**
- Open the file [romeo.txt](/romeo.txt) and read it line by line. For each line, 
- split the line into a list of words using the split() method. 
- The program should build a list of words. For each word on each line check to see if the word is already
    in the list and if not append it to the list. 
- When the program completes,sort and print the resulting words in alphabetical order
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

### **Solution:**
```python
file = open('romeo.txt')
read_file = file.read()
words_list = read_file.split()
unique_words = list()
for word in words_list:
    if word in unique_words: continue
    unique_words.append(word)
unique_words.sort()
for word in unique_words:
    print(word)
```
## Assignment # 8.5
### **Problem Statement:**
- Open the file [mbox-short.txt](/mbox-short.txt) and read it line by line. 
- When you find a line that starts with 'From ' like the following line: *From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008*
- You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
- Then print out a count at the end.
**Hint:** make sure not to include the lines that start with 'From:
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
### **Solution:**
```python
file = open('mbox-short.txt')
count = 0;
for line in file:
    if line.startswith('From '): 
        line_itm = line.split()
        print(line_itm[1])
        count += 1
print(f'total number of times addresses appears: {count}')
```
----
# Week 5
## Assignment # 9.4
### **Problem Statement:**
- Write a program to read through the [mbox-short.txt](/mbox-short.txt) and figure out who has the sent the greatest number of mail messages. 
- The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
- The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
- After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

### **Solution:**
```python
handle = open('mbox-short.txt')
mails = list()
for line in handle:
    if line.startswith('From '):
        line_piece = line.split()
        mails.append(line_piece[1])

mail_count = dict()
for mail in mails:
    mail_count[mail] = mail_count.get(mail,0) + 1

most_mail_by = ''
count = 0
for user,times in mail_count.items():
#     print(user,'->',times)
    if most_mail_by == '' or times > count:
        most_mail_by = user
        count = times
print(f'Mails histogram: {mail_count}')
print(f'Most mails are from: {most_mail_by}')
print(f'Total number of mails are: {count}')
```
----
# Week 6
## Assignment # 10.2
### **Problem Statement:**
- Write a program to read through the [mbox-short.txt](/mbox-short.txt) and figure out the distribution by hour of the day for each of the messages.
- You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. <br/> *From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008*
- Once you have accumulated the counts for each hour, print out the counts,
- sorted by hour as shown below.

### **Solution**
```python
file_handle = open('mbox-short.txt')
hour_count = dict()
# from_lines[aa ]
for line in file_handle:
    if line.startswith('From '):
        msg_pieces = line.split()
        time = msg_pieces[5].split(":")
        hour_count[time[0]] = hour_count.get(time[0],0) + 1

hr_tuple_rev = sorted( [ (v,k) for (k,v) in hour_count.items() ] , reverse= True )
hr_tuple = [ (k,v) for (v,k) in hr_tuple_rev ]
```