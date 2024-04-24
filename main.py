import os 
import art
print(art.logo)
#os.system("cls")

print("Welcome to the secret auction program.")
 
tally = {}

tally_count = True

while tally_count:
    username = input("\nWhat is your name?: ").lower()
    amount_bid = input("What's your bid?: ")
    tally[username] = amount_bid
#or key,value in tally.items():
    #key = input("What is your name?: ").lower()
    #value = input("What's your bid?: ")
    #tally[key] = value
    #print(key, value)

    question = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if question == 'no':
        tally_count = False

for key, value in tally.items():
    print(f"{key.capitalize()} has the bid of {value}.")
    


#print(max(tally, key=tally.get))

#key_max = max(tally.keys(), key=(lambda k: tally[k]))
#print(tally[key_max])

#print(tally)        
#print(max(tally.values()))       



    
#name = input("What is your name?: ").lower()
#bid = input("What's your bid?: ")
#question = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

 
                


