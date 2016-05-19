cat_from_english = {
	'per': 'purr',
	'pear': 'purr',
	'pur': 'purr',
	'prog': 'purr',
	'me': 'meow',
	'now': 'meow',
	'move': 'meow',
	'sat': 'cat',
	'ver': 'fur',
	'mur': 'fur',
	'pos': 'claws',
	'awes': 'claws',
	'mag': 'meow',
	'cast': 'cat',
	'pos': 'paws',
	'pas': 'paws',
	'refer': 'refur',
	'liter': 'litterally',
	'aw': 'claw',
	'kidding': 'kitten',
	'for': 'fur',
	'hys': 'hiss',
	'tal': 'tail',
	'because': 'because',
	'friend': 'furend',
	'princess': 'purrincess',
	'that\'s': 'cats',
	'hys': 'hiss',
	'caut': 'claw',
	'fri': 'fur',
}

shakespeare_quotes = [
	"Be not afraid of greatness: some are born great, some achieve greatness, and some have greatness thrust upon them.",
	"In my stars I am above thee, but be not afraid of greatness. Some are born great, some achieve greatness, and some have greatness thrust upon 'em.",
	"My words fly up, my thoughts remain below: Words without thoughts never to heaven go",
	"The more I give to thee, the more I have, for both are infinite.",
	"To climb steep hills requires slow pace at first.",
	"A friend is one that knows you as you are, understands where you have been, accepts what you have become, and still, gently allows you to grow.",
]

current_quote = shakespeare_quotes[0]
for key in cat_from_english:
	current_quote = current_quote.replace(key, cat_from_english[key])

print(current_quote)
