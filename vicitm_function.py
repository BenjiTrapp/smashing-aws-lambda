import time
from random import seed
from random import randint

asimov_quotes = ["The saddest aspect of life right now is that science gathers knowledge faster than society gathers wisdom.",
    "In life, unlike chess, the game continues after checkmate",
    "Your assumptions are your windows on the world. Scrub them off every once in a while, or the light won't come in.",
    "Violence is the last refuge of the incompetent.",
    "Properly read, the Bible is the most potent force for atheism ever conceived.",
    "Self-education is, I firmly believe, the only kind of education there is.",
    "If knowledge can create problems, it is not through ignorance that we can solve them.",
    "Those people who think they know everything are a great annoyance to those of us who do.",
    "The most exciting phrase to hear in science, the one that heralds the most discoveries, is not \"Eureka!\" (I found it!) but 'That's funny...",
    "Life is pleasant. Death is peaceful. It's the transition that's troublesome." ]

def lambda_handler(event, context):
    
    time.sleep(randint(1, 4))
    
    return {
        'statusCode': 200,
        'body': asimov_quotes[randint(0, 10)] + " - Isaac Asimov"
    }
