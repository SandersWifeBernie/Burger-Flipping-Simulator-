def getAlistarAffinity (food):
    affinity = 0
    for item in food:
        item = item.lower()
        if "lettuce" in item:
            affinity = affinity + 20
        elif "tomato" in item:
            affinity = affinity + 25
        elif "mustard" in item:
            affinity = affinity + 15
        elif "fancy mustard" in item:
            affinity = affinity + 25
        elif "ketchup" in item:
            affinity = affinity - 10
        elif "cheese" in item:
            affinity = affinity + 15
        elif "beef patty" in item:
            affinity = affinity - 10
        elif "buns" in item:
            affinity = affinity + 15
        elif "onions" in item:
            affinity = affinity - 30
        elif "turkey patty" in item:
            affinity = affinity + 30
        elif "hot sauce" in item:
            affinity = affinity - 5
        elif "bacon" in item:
            affinity = affinity - 10
        elif "pickles" in item:
            affinity = affinity - 5
        elif "mayo" in item:
            affinity = affinity + 25
        elif "relish" in item:
            affinity = affinity - 15
    return affinity


def getGrumpyAffinity(food):
    affinity = 0
    for item in food:
        item = item.lower()
        if "lettuce" in item:
            affinity = affinity - 10
        elif "tomato" in item:
            affinity = affinity - 20
        elif "mustard" in item:
            affinity = affinity + 5
        elif "fancy mustard" in item:
            affinity = affinity - 25
        elif "ketchup" in item:
            affinity = affinity + 15
        elif "cheese" in item:
            affinity = affinity + 15
        elif "beef patty" in item:
            affinity = affinity + 30
        elif "buns" in item:
            affinity = affinity + 15
        elif "onions" in item:
            affinity = affinity - 30
        elif "turkey patty" in item:
            affinity = affinity + 15
        elif "hot sauce" in item:
            affinity = affinity + 20
        elif "bacon" in item:
            affinity = affinity + 30
        elif "pickles" in item:
            affinity = affinity - 5
        elif "mayo" in item:
            affinity = affinity - 15
        elif "relish" in item:
            affinity = affinity - 15
    return affinity


def getNormanAffinity(food):
    affinity = 0
    for item in food:
        item = item.lower()
        if "lettuce" in item:
            affinity = affinity + 20
        elif "tomato" in item:
            affinity = affinity + 10
        elif "mustard" in item:
            affinity = affinity + 20
        elif "fancy mustard" in item:
            affinity = affinity - 25
        elif "ketchup" in item:
            affinity = affinity + 20
        elif "cheese" in item:
            affinity = affinity + 20
        elif "beef patty" in item:
            affinity = affinity + 30
        elif "buns" in item:
            affinity = affinity + 20
        elif "onions" in item:
            affinity = affinity + 15
        elif "turkey patty" in item:
            affinity = affinity - 20
        elif "hot sauce" in item:
            affinity = affinity - 5
        elif "bacon" in item:
            affinity = affinity + 10
        elif "pickles" in item:
            affinity = affinity + 15
        elif "mayo" in item:
            affinity = affinity - 15
        elif "relish" in item:
            affinity = affinity - 30
    return affinity

endGame = "You've reached the end of the game, to play again enter \"yes\" if not type \"no\" its okay to say no it won't hurt my feelings"
# basically remember to use the get affinity methods before using response methods


def getAlistarResponse(affinity):
    if affinity < 30:
        print("\"My word I don't think I've ever had the displeasure of experiencing such a rubbish patty before.\n" 
               "The fact that you've squandered the privilege of burger cooking is nothing sort of a disgrace, I hope I never see you again\n"
              "good day to you sir\" Alistar spits in your face and walks away in a disheveled dimeaneor. You've seemed to have really pissed the guy off\n"
              "but you brush it off and try to finish off the rest of the shift strong.")
        input("Press enter to continue")
        print("A few days pass and you wake up to a string of text messages from your boss\n"
              "with all of them reading \"NEVER COME BACK AGAIN\", its safe to say he heard about the fancy man,\n"
              " so now you're out of a job and rent's due tomorrow so goodluck with that pal.\n"
              "\n"
              "\n"
               + endGame)

    elif 30 <= affinity <= 50:
        print("The elegant man takes a bite of whatever you concocted in the kitchen.\n "
              "\" Eh well it's below satisfactory but it will have to do, thank you? \n"
              "Alistar saunters out of the store clutching his stomach you think you might've served a health and safety violation."
              "Either way you pay it no mind and close off the rest of your shift without any problems.\n"
              "\n"
              "\n"
              + endGame)
    elif 50 < affinity < 70:
        print("The fancy looking man begins eating what looks like a pretty decent burger \n"
              "\" I must say this is quite an enjoyable patty my good sir, keep up the good work\"\n"
              "He smirks and flips you a quarter, Alistar begins to exit the restaurant with a satisfied look on his face.\n"
              "Looks like you did a pretty decent job for your first day. \n"
              "\n"
              "\n"
              + endGame)
    elif 70 <= affinity< 90:
        print("The fancy mans goes in for an elegant bite and you can see there's an expression of elation drawn all over his face.\n"
              "\"What an exquisite experience, I do think I'll be coming hear again, thank yiou kind sir and here treat your self\"\n"
              "He hands you a five dollar bill and exits with a bit of a spring in his step.\n"
              "\n"
              "\n"
               + endGame)
    elif affinity >= 90:
        print("You come out with what looks like a burger that has been crafted for only individual's with the finest taste\n"
              "in every form of the word this is a burger that can only be described as elegant. The elegant man gazes upon\n"
              "this elegant burger not totally convinced yet. He goes in for a bite and the scene that unfolds after can only be\n"
              "described as a scene from tom and jerry, the fancy man is jumping in joy with tears streaming down his eyes.\n"
              "\" My word, I don't think I've ever had such a magnificent patt-no that was no mere patty that was a true burger.\n"
              "My name is Alistar and by god I cannot thank you enough for such a wonderful burger.\"\n"
              "Alistar takes your hand and shakes it profusely while pulling out a seemingly endless string of bills from his wallet and gives it you.\n"
              "Afterwards he exits the establishment looking as if he has just experienced something spiritual. It's safe to say\n"
              "your first day went off without a hitch.\n"
              "\n"
              "\n"
              + endGame)


def getGrumpyResponse(affinity):
    if affinity < 30:
        print("\"Do not like this, not enough meat\" The large man hulks out of the establishment looking very dejected, he really didn't like that burger.\n"
              "You go on with your shift but you can't get your mind off of that order, you still remember the mopey face that poor man wore while he left\n "
              "and your filled with guilt and shame. After you finished your shift you head home with your head hung low after doing such a poor job.\n"
              "\n"
              "\n"
              + endGame)
    elif 30 <= affinity <= 50:
        print("The hulking man takes the little burger from your hands and takes a bite. His expression seems...Neutral?\n"
              "\"This...burger\""
              "The large man begins to leave the establishment with a neutral expression, you think that the order went well?\n"
              "\n"
              "\n"
              + endGame)
    elif 50 < affinity < 70:
        print("You serve up what looks like a decently powerful burger and give it up for the large man to devour.\n"
              "\"Hey this pretty good\"\n"
              "The customer leaves the restauranty looking pretty good so you think that you did a pretty good job today.\n"
              "\n"
              "\n"
              + endGame)
    elif 70 <= affinity < 90:
        print("You bust out of the kitchen with a smug demeanor knowing you made a powerful burger,\n "
              "you serve it up for the hulking man to gorge on.\n"
              "\"This power, this good\"\n"
              "The large man gives a hearty fist pump in the air and gives a *crisp* slap on the back and exits victorious.\n"
              "Today went well and while your back may sting at least you served a powerful burger.\n"
              "\n"
              "\n"
              + endGame)
    elif affinity >= 90:
        print("After chefing it up in the kitchen you end up with a burger so mighty it can't even be described with mortal langauge,\n"
              "this is a burger worthy of warriors. The big man perks up upon the sight of such a dominant burger.\n"
              "He goes in for a bite and when he's done he looks like he's just been through a battle described in myths.\n"
              "\"Burger very good, much hair on chest, name is Grumpy\"\n"
              "The large man that proceeds to go onto a rampage because of the delight of the patty that you made, he destroys tables,\n"
              "chair and eventually the whole building is torn down in a matter of minutes. After the dust settles, Grumpy is\n"
              "nowhere to be seen. What you can see is your boss with steam coming out of his ears, looks like your first day might\n"
              "also be your last.\n"
              "\n"
              "\n"
              + endGame)


def getNormanResponse(affinity):
    if affinity < 30:
        print("\"That was not normal at all, I'm gonna have to normally talk to the manager and have a normal argument with him\"\n"
              "The average man storms past the desk your working at and has what sounds like a normal and stern conversation with your boss.\n"
              "In the matter of five minutes you lose your job and now have to very normally leave the restaurant and find a new job.\n"
              "\n"
              "\n"
              + endGame)
    elif 30 <= affinity <= 50:
        print("The burger you made is kinda normal, hopefully the average man likes it. He goes in for a bite and upon tasing the bruger has a decently\n"
              "normal expression on his face.\n"
              "\"Well it's kinda average I guess, I'll be on my way now\" He thanks you for the food and calmly exits.\n"
              "All things considered you'd say that things went... kinda normal.\n"
              "\n"
              "\n"
              + endGame)
    elif 50 < affinity < 70:
        print("You exit the kitchen with a pretty normal looking burger, hopefully this\n"
              "meets the average man's standards. He goes in for a bite and reception is... pretty average.\n"
              "\"That's a pretty normal burger, thanks.\" He exits the establishment in an average fashion.\n"
              "You'd say that the order went pretty well, it was somewhat average at least.\n"
              "\n"
              "\n"
              + endGame)

    elif 70 <= affinity < 90:
        print("You come out of the kitchen and this is one normal looking burger, you'd swear it would be a quarter pounder.\n"
            "The burger gets served and the normal man goes in for a bite, he seems pleased.\n"
            "\"Hey now this is one normal burger, I appreciate this, thank you\" The average man exits without any flare.\n"
            "You'll feel accomplished in yourself since you made one normal lookin burger.\n"
            "\n"
            "\n"
            + endGame)

    elif affinity >= 90:
        print("The burger you just made was so normal that there is no dramatic flair on it at all, its literally just a big mac.\n"
              "Like seriously it's just a regular burger, it's kinda sad really. You serve it up with a blank expression to the normal man\n"
              "The average man calmly eats his burger, like any normal person would, then proceeds to thank you.\n"
              "\"Finally, an average burger that promotes family values. My name's Norman by the way, and I can't thank you enough for this.\"\n"
              "Norman exits the restaurant like he entered, normally and you finish off the rest of your shift.\n"
              "You know you did a great job today but you can't help but feel like it was just so...average.\n"
              "\n"
              "\n"
              + endGame)




