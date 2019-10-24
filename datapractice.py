dict={'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
#print(dict['Dec'])
for month in dict:
    if month.startswith('M'):
        print(month)
  
naomiDict={'name':'Naomi', 'age':16, 'classes':{'0':'The Farm', '1st': 'APUSH', '2nd':'DSW', '3rd':'APES', '4th':'English', '5th':'Math', '6th':'Cross Country'}, 'height':'5 feet 1 inch'}
  
if '6th' in naomiDict['classes']:
    print('has a 6th')
else:
    print('does not have a 6th')
    
joyDict={'name':'Joy', 'age':16, 'classes':{'1st': 'English', '2nd':'DSW', '3rd':'Jazz Band', '4th':'Math', '5th':'APES', '6th':'Marching Band', '7th':'Dumline'}, 'height':'5 feet 4 inches'}
if '6th' in naomiDict['classes']:
    print('has a 6th')
else:
    print('does not have a 6th')
    
karleighDict={'name':'Karleigh', 'age':16, 'classes':{'1st': 'English', '2nd':'DSW', '3rd':'APES', '4th':'Math', '5th':'Marine Biology', '6th':'Swim Team'}, 'height':'5 feet 3 inches'}
if '6th' in naomiDict['classes']:
    print('has a 6th')
else:
    print('does not have a 6th')
    
classData=[naomiDict, joyDict, karleighDict]
print(classData[2]['height'])