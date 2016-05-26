from app import ShakespeareQuote
import settings
import tweepy


# ------------------------------------------------------------------------------
# Cat From English Dictionary

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
	'ver': 'fur',
	'fer': 'fur',
	'for': 'fur',
	'for': 'fur',
	'full': 'furll',
	'ket': 'cat',
	'My name is': 'My owners call me',
	'users': 'cats',
	'pow': 'paw',
	'fr': 'furr',
	'For': 'Fur',
	'Hi': 'Meow!😸',
	'hi': 'meow!😸',
	'Yo': 'Meow!😸',
	'yo': 'meow!😸',
	'Hello': 'Meow!😸',
	'hello': 'meow!😸',
	'Hey': 'Meow!😸',
	'hey': 'meow!😸',
	'arr': 'purr',
	'awesome': 'clawsome',
	'great': 'great as catnip',
	'good': 'meow-velous',
	'er': 'epurr',
	'ers': 'epurrs',
	'were': 'wrrr',
	'ber': 'purr',
	'per': 'purr',
	'%': 'purrcent',
	'thanks': 'back scratches',
	'thank': 'back scratch',
	'from': 'furom',
	'From': 'Furom',
	'feeling': 'feline',
	'Product': 'Purr-oduct',
	'product': 'purroduct',
	'mou': 'meow',
	'li': 'purr',
	'team': 'litter',
	'followers': 'litter',
	'people': 'cats',
	'wrrr': 'were',
	'pir': 'purr',
	'kidding': 'kitten',
	'kiddin': 'kitten',
	'say': 'meow',
	'saying': 'meowing',
	'said': 'meowed',
	'community': 'cat park',
	'fantastic': 'catastic',
	'podcast': 'podcats',
	'awesomeness': 'pawesomeness',
	'aw': 'paw',
	'getting': 'kitten',
	'yell': 'hiss',
	'food': 'catnip',
	'run': 'pounce',
	'got': 'cat',
	'know': 'meow',
	'now': 'meow',
	'purp': 'purrp',
	'go for it': 'catnip it in the bud meow',
	'to execute': 'catnip it in the bud meow',
	'move': 'mewv',
	'crast': 'cats',
	'pl': 'pawl',
	'amazing': 'ameowsing',
	'marvelous': 'meowvelous',
	'pr': 'purr',
	'por': 'purr',
	'connected': 'catnected',
	'leap': 'pounce',
	'par': 'purr',
	'hows it going': 'whats catalakin',
	'whats up': 'whats catalakin',
	'hope all is well': 'hope you have many more of your 9 lives still',
	'life': 'one of your 9 lives',
	'years old': 'years in my first cat life',
	'garbage': 'litter box',
	'Per': 'Purr',
	'no': 'hiss no',
	'yes': 'yarn right'
}


def calculate_shakespurr_quote():
	shakespeare_quotes = ShakespeareQuote.select().where(ShakespeareQuote.is_tweeted == False)
	for quote in shakespeare_quotes:
		cat_quote = quote.quote
		for key in cat_from_english:
			cat_quote = cat_quote.replace(key, cat_from_english[key], 6)

		# No cat translation possible
		if quote == cat_quote:
			...
			# quote.delete()
		# Don't tweet if len(cat_quote) is > Twitter character limit
		if len(cat_quote) > 140:
			...
		else:
			quote.set_tweeted()
			return cat_quote
	return None

# ------------------------------------------------------------------------------
# Twitter

class TwitterAPI:
    def __init__(self):
        consumer_key = "aaLl3guwRoHztN2TGVrfCEhcA"
        consumer_secret = settings.consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "732567861479120896-9FhyPpPTXhsLJfNsKTDy1O6HrTDsqzW"
        access_token_secret = settings.access_token_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

# ------------------------------------------------------------------------------
# Main

if __name__ == "__main__":
	shakespurr_quote = calculate_shakespurr_quote()

	if shakespurr_quote is not None:
		twitter = TwitterAPI()
		twitter.tweet(shakespurr_quote)
