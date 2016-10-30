import random

f = open("stopwords.txt")
lines = f.readlines()

greeting = ['hello', 'hi', 'hey', 'good morning', 'greetings', 'howdy']

question = ['how are you?','how are you doing?', 'you good?', 'hows it going', 'you alright?', 'you okay?']

ai_response = ['im good, you?', 'pretty good, you?', 'great yeah, you?', 'good thanks, you?', 'im fine, you?', 'not too bad, you?', 'rough day actually, you?', 'not too great, you?', 'not good, you?', 'pretty bad really, you?']

positive_responses = ['im good', 'pretty good', 'great yeah', 'good thanks', 'im fine', 'not too bad']

negative_responses = ['rough day actually', 'not too great', 'not good', 'pretty bad really']

positive_feedback = ['thats great', 'good to hear', 'thats nice', 'amazing']

negative_feedback = ['well that sucks', 'sorry to hear that', 'terribly sorry about that']

continued = 

while True:
	userInput = raw_input("/// ")
	if userInput in greeting:
            random_greeting = random.choice(greeting)
            print(random_greeting)
        
        elif userInput in question:
            random_response = random.choice(ai_response)
            print(random_response)
            
        elif userInput in positive_responses:
            positive_response = random.choice(positive_feedback)
            print(positive_response)
            
        elif userInput in negative_responses:
            negative_response = random.choice(negative_feedback)
            print(negative_response)
            
	else:
		print("sorry, but i do not understand what that means")