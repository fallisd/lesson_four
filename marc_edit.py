import re

ifile = 'des_libris_records_unedited.txt'
ofile = 'des_libris_records_edited.txt'


with open(ifile, 'r') as f:
  lines = f.readlines()

target = open(ofile, 'w')

correct_id = ""
line_number = 0
for line in lines:
  line_number = line_number + 1
  
  if line.startswith('=LDR'):
    correct_id = ""
  
  if line.startswith('=530'):
    if 'celarc' in line:
      match = re.match(r'.*celarc.ca/.*/.*/(.*).[pdf|jpg]', line)
      if match:
        correct_id = match.group(1)
      else:
        print('Line:' + str(line_number) + ' Does not math the regular expression.')
    elif 'deslibris' in line:
      match = re.match(r'.*deslibris.ca/.*/(.*)\b', line)
      if match:
        correct_id = match.group(1)
      else:
        print('Line:' + str(line_number) + ' Does not match the regular expression' )
    else:
      target.write(line)
      print('Line:' + str(line_number) + ' Does not contain "celarc" or "deslibris" url.' )
    continue
  
  if line.startswith('=856') and (correct_id != ""):
    target.write('=856  40$uhttp://deslibris.ca/ID/' + correct_id)
  else:
    target.write(line)
  

  
    
  
