#lab 2
films = [{'title': 'Moaalem Ramadan',
  'duration': '1h & 50m',
  'stars': 'Mohammed heninidi'},
  
  {'title': 'Carlitos',
  'duration': '1h & 40m',
  'stars': 'Carlitos'},

  {'title': 'Harry Potter',
  'duration': '14h',
  'stars': 'Harry Potter'},

  {'title': 'Aashor School',
  'duration': '1h & 50m',
  'stars': 'Alaa Waley Al-deen & Ahmed Helmy'},

  {'title': 'Moaalem Ramadan',
  'duration': '1h & 50m',
  'stars': 'Mohammed heninidi'}
   ]

for film in films:
    print(f'Puff the {film["title"]} lasts for {film["duration"]}. Stars: {film["stars"]}')

    # lab 2
Dictionaries = [
    {
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'alreadyRead': True
    },
   {
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'alreadyRead': True
    },
	{
        'title': 'Little woman',
        'author': 'Delan',
        'alreadyRead': False
    },
]
for book in Dictionaries:
	print(f"{book['title']} by {book['author']}")
	if book['alreadyRead'] == True:
		print(f"You already read{book['title']} by {book['author']}")
	else:
		print("not read")