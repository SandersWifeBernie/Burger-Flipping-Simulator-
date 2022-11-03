import affinityCalculator as ac
import random

validIngredients = ["lettuce", "tomato", "mustard", "fancy mustard", "ketchup", "cheese", "beef patty", "buns",
                    "onion", "turkey patty", "hot sauce", "bacon", "pickles", "mayo", "relish"]


def inputIngredients():
    ingredientList = []
    invalid = False
    for i in range(5):
        currentIngredient = input("please enter an ingredient")
        currentIngredient.lower()
        if currentIngredient in validIngredients:
            ingredientList.append(currentIngredient)
        else:
            invalid = True
            print("that is not a valid ingredient")
            while invalid:
                currentIngredient = input("please enter a valid ingredient")
                currentIngredient.lower()
                if currentIngredient in validIngredients:
                    ingredientList.append(currentIngredient)
                    invalid = False
    return ingredientList







gameOn = True
screen = "start"
incorrectInput = False
randomNum = random.randint(1, 3)
# initialize the string screens after start screen or else everything will be fucked
while gameOn:
    if screen == "start":
        print("Hello and welcome to Burgee, in this game you'll be playing as a part time burger chef on the weird side of town\n"
              "(don't ask which one cause I don't know either). It's your first day on the job and you're all starry eyed and ready to chef it up in the kitchen.\n"
              "In burgee you'll be approached by one of three random customers and the customer will give you a description of what kind of burger they want,\n"
              "it's up to you to create a burger that fits their taste.\n "
              "You'll have a list of the following ingredients(this isn't bio so need to memorize this): \n"
              "\n"
              "Lettuce\n"
              "Tomato\n"
              "Mustard\n"
              "Fancy Mustard\n"
              "Ketchup\n"
              "Cheese\n"
              "Beef Patty\n"
              "Buns\n"
              "Onion\n"
              "Turkey Patty\n"
              "Hot Sauce\n"
              "Bacon\n"
              "Pickles\n"
              "Mayo\n"
              "Relish\n"
              "\n"
              "You'll get to pick five of these ingredients to make your burger and  your combo will determine \n"
              "the satisfaction of the customer, so basically choose a good combo you get a raise, choose a bad combo and you're dumped onto the street.\n"
              "Well with all that if you're ready to start your first day then press enter, oh and a word of advice try thinking out of the box with your combos.")
        if randomNum == 1:
            screen = "Alistar"
        elif randomNum == 2:
            screen = "Grumpy"
        elif randomNum == 3:
            screen = "Norman"
        getInput = input()
    elif screen == "Alistar":
        print("\n"
              "\n"
              "\n"
              "\n"
              "\n")
        print("It's your first day and the sun is shinning, and you are ready to take on the day and make some scrumptous burgers.\n"
              "After a couple of minutes a slender man walks in. Every aspect of this man can only be described in one way, elegant, from his brimmed\n"
              "top hat to his twirling mustache that twitches every so often, this is the most fancy man you have ever met. The fancy man walks up\n"
              "haughtily to the front counter and you ask for his order.\n"
              "Press enter to continue")
        nextAct = input()
        print("\n"
              "\n"
              "\"Well met my fellow worker, I have come in search for a burger that is truly  worthy of my excellence. I yearn for\n"
              "a patty that is able to rival my very own elegance and make me experience something that will change the very way I view\n"
              "the world. I hope that isn't too much to ask of you.\"\n"
              "Alright bucko you heard the man, introduce some elegance into his life\n")
        ingredients = inputIngredients()
        if ("beef patty" in ingredients) and ("bacon" in ingredients) and ("hot sauce" in ingredients) and ("turkey patty" in ingredients) and ("mayo" in ingredients):
            print("Not gonna lie the burger you made is pretty crude, this does not pass the elegancy test\n"
                  "whatsoever. No matter you serve it up to the fancy man and to your surprise, he doesn't hate it.\n"
                  "\"Incredible I didn't think you'd find the secret desire within my heart. My name is Alistar and\n"
                  "I'm a member of a noble family you see, and because of this I need to keep up the appearance of elegance\n"
                  "at all times, its quite exhausting really. My secret is that I am quite fond of crude things so this burger\n"
                  "was quite the breath of fresh air for me. Thank you for this, genuinely I really appreciate it.\"\n"
                  "Alistar leaves the restaurant with a renewed vigor in his step, ready to continue living is elegant\n"
                  "life.\n"
                  "You've reached the end of the game, to play again enter \"yes\" if not type \"no\" its okay to say no it won't hurt my feelings")
        else:
            alistarAffinity = ac.getAlistarAffinity(ingredients)
            ac.getAlistarResponse(alistarAffinity)
        getInput = input()
        getInput.lower()
        if getInput == "yes":
            screen = "start"
            randomNum = random.randint(1, 3)
            continue
        if getInput == "no":
            gameOn = False

    elif screen == "Grumpy":
        print("\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "The shift starts and your kinda feeling yourself, your fresh and full of excitement for your first day.\n"
              "There then walks in man who seems like a building with feet, he's huge and you are intimated. This mountain of\n"
              "human has thick corded muscles all over his body and has quite a robust jaw. with every steps the ground shakes a\n"
              "little until he reaches the front counter where you then take his order.\n"
              "press enter to continue")
        nextAct = input()
        print("\n"
              "\n"
              "\"Want burger that is strong, something for muscle, put hair on chest, please and thank you.\"\n"
              "You heard him, make something powerful.")
        ingredients = inputIngredients()
        if ("lettuce"in ingredients) and ("onion" in ingredients) and ("mayo" in ingredients) and \
                ("pickles" in ingredients) and ("relish" in ingredients):
            print("You bring out a burger that is not fit for a warrior but regardless you serve it up to the large man.\n"
                  "He goes in for a bit and tears begin to stream down the mans face. \n"
                  "\"Name is Grumpy, since big and strong everybody want Grumpy to be strong, but\n"
                  "Grumpy like cute things and vegetables but scared to order it. Thank you, you gave,\n"
                  "what Grumpy want.\"\n"
                  "Grumpy leaves the restaurant with tears and snot pouring down but you can tell that\n"
                  "at least for now, Grumpy is at peace. You feel like you've made a burger that's powerful in\n"
                  "a different sense.\n"
                  "You've reached the end of the game, to play again enter \"yes\" if not type \"no\" its okay to say no it won't hurt my feelings ")
        else:
            grumpyAffinity = ac.getGrumpyAffinity(ingredients)
            ac.getGrumpyResponse(grumpyAffinity)
        getInput = input()
        getInput.lower()
        if getInput == "yes":
            screen = "start"
            randomNum = random.randint(1, 3)
            continue
        if getInput == "no":
            gameOn = False
    elif screen == "Norman":
        print("\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "The day starts and things feel kinda normal, not to bad but not too good either.\n"
              "In walks in a man that can only be described as what you'd  imagine a normal guy would like.\n"
              "The way he carries himself, his clothes even his scent is scarily normal. Mr. average saunters\n"
              "to the front counter and you take his order.\n"
              "press enter to continue")
        nextAct = input()
        print("\n"
              "\n"
              "\"Hi, would you be able to make me something that's ya know... normal?\n"
              "Like I want the kind of burger that you'd picture in your head when you hear \"burger\"\n"
              "I'd greatly appreciate it.\" \n"
              "Well this isn't so bad try making something normal for the guy.")
        ingredients = inputIngredients()
        if ("lettuce" in ingredients) and ("ketchup" in ingredients) and ("fancy mustard" in ingredients) and \
                ("mustard" in ingredients) and ("mayo" in ingredients):
            print("You end up making a pretty weird burger, you're not really sure if the guy will like it but\n"
                  "it's worth a shot. The normal guy goes in for a bite and something magical happens.\n"
                  "\"Wow, this isn't normal at all but in a weird way this is what I truly wanted\n"
                  "its an abnormal burger but, its the burger for me and that's what matters.\n"
                  "My name is Norman by the way, and even though I try to appear average I'm not actually a normal guy,\n"
                  "I was worried I would be ridiculed for being different so I pretend to be normal. After tasting\n"
                  "this burger you made me realize that I should be true to myself or else I'll never enjoy life to \n"
                  "the fullest. Thank you, I really needed this.\""
                  "Norman exits the establishment a new man, you can tell that he walks with less weight on his shoulders.\n"
                  "Even though the burger itself was weird you felt that you helped someone today and that made this job worth it.\n"
                  "You've reached the end of the game, to play again enter \"yes\" if not type \"no\" its okay to say no it won't hurt my feelings ")
        else:
            normanAffinity = ac.getNormanAffinity(ingredients)
            ac.getNormanResponse(normanAffinity)
        getInput = input()
        getInput.lower()
        if getInput == "yes":
            screen = "start"
            randomNum = random.randint(1, 3)
            continue
        if getInput == "no":
            gameOn = False






