import re

ifile = 'example.txt'
ofile = 'output.txt'


with open(ifile, 'r') as f:
  lines = f.readlines()

target = open(ofile, 'w')

correct_id = ""
line_number = 0
for line in lines:
  match = True
  while(match):
    match = re.search(r'(\d{4})-(\d{4})', line)
    if match:
      line = re.sub(r'(\d{4})-(\d{4})', match.group(1) + '/' + match.group(2), line, 1)
  match= True
  while(match):
    match = re.search(r'(\d{2})/(\d{2})/(\d{4})', line)
    if match:
      print(match.groups())
      line = re.sub(r'(\d{2})/(\d{2})/(\d{4})', match.group(3) + '-' + match.group(1) + '-' + match.group(2), line, 1)  
  target.write(line)

target.close()