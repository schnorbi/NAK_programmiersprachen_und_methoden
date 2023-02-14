personen = [
      {'name'     : 'Leo Lustiglaune',
       'alter'    : 23,
       'hobbies'  : [ 'Fahrrad fahren',
                      'Lesen'
                    ],
       'isStudent': True,
      },
      {'name'     : 'Lea Lambrecht',
       'alter'    : 24,
       'hobbies'  : [],
       'isStudent': False,
      }
]
#Aufgabe 1.1:
print('Anzahl der Hobbies der ersten Personen: ' + str(len(personen[0]['hobbies'])))

#Aufgabe 1.2:
print(personen[1]['name'].split()[0])

#Aufgabe 1.3:
print(personen[0]['alter'] > 25 and personen[0]['isStudent'] == True)

#Aufgabe 1.4:
print(personen[1]['hobbies'] != [])