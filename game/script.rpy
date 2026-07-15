## Main Game Script - Bavarian Pillar Demo

# Declare characters.
# Custom color properties determine the display color of their names in the dialogue box.
define p = Character("You (Barbarian)", color="#e11d48") # Bold red for the Barbarian from Baldur's Gate
define n = Character("Nitwit", color="#22c55e") # Green for the gnome

# Initialize variables to track game state
default roll_modifier = 0 # Modified by failed riddle attempts
default cursed = False # Tracks if Nitwit curses the player

# The game starts here!
label start:

    # 1. Start Ambient looping track
    play sound "audio/ambience_wind.mp3"

    # 2. Start Background Music (BGM)
    play music "audio/bgm_forest.mp3"

    # Begin Story
    scene black with fade
    
    "As you approach the pillar, you see a foreign text that appears to be in a language unlike anything you’ve ever studied back in Baldur's Gate."
    

    label investigate_pillar:
        "Could this text provide valuable information on where to go next?You approach the rock and begin to investigate it closer. Roll 12+ to pass"

        # Manual Investigation Roll Choice (Threshold: 12+)
        menu:
            "Investigation Check (Requires 12+):"
            
            "SUCCESS (12 or higher)":
                jump investigation_success
                
            " FAILURE (Under 12)":
                jump investigation_failure


label investigation_success:
    "You don't find anything valuable about the text, but you do see a red hat popping out from behind the rock that was not there previously "
    
    menu:
        "Call out to the hidden figure":
            jump meet_nitwit_peaceful

        "Ignore it and walk away":
            jump meet_nitwit_surprise


label investigation_failure:
    "You’re unsure if this text is valuable or not, but maybe someone nearby could help?"
    
    menu:
        "Walk away from the monument":
            jump meet_nitwit_surprise


label meet_nitwit_peaceful:
    play sound "audio/nitwit_nap.mp3"
    "The figure slowly moves his way around the monument, and approaches you..."
    n  "You woke me from my afternoon nap. Who dares to disturb nitwit the wise?"
    jump conversation_start


label meet_nitwit_surprise:
    "While walking away, a shadowy figure jumps out from the monument and stands before you"
    play sound "audio/nitwit_surprise.mp3"
    n "STOP RIGHT THERE TRAVELER! I AM NITWIT THE WISE THE ALL KNOWING GUARDIAN OF THIS MONUMENT!"
    jump conversation_start


label conversation_start:
    menu:
        "Ask Nitwit for help reading the text":
            jump ask_for_help

        "Ignore the noisy little gnome":
            jump ignore_nitwit


label ignore_nitwit:
    "He angrily clears his throat"
    play sound "audio/nitwit_ignore.mp3"
    n "HELLO DID YOU NOT HEAR ME?! I AM NITWIT THE WISE IS THERE ANYTHING I CAN DO TO HELP YOU?"
    jump ask_for_help


label ask_for_help:

    "He looks at you with deep disgust"
    play sound "audio/nitwit_language.mp3"
    n "What do you mean you dont know this language? This is bavarian, the best language in the entire world! How dare you!"
    jump riddle_loop


label riddle_loop:
    play sound "audio/nitwit_quiz.mp3"

    n "That explains a lot! Well I do have just the thing to remedy this, but It would be a diservice to you if I did not teach you about our world while i did it! "
    n "If you wish for me to help you, you must first help me with something. Tell me What Prince, is it these angels kneel."

    menu:
        "Prince Karl":
            jump riddle_wrong

        "Prince Bismark":
            jump riddle_wrong

        "Prince Ferdinand":
            jump riddle_correct


label riddle_wrong:
    n "Bah! Wrong! Completely wrong!"
    play sound "audio/nitwit_wrong.mp3"
    $ roll_modifier -= 1
    "* Penalty: You must apply -1 to each roll in this encounter *"
    "Ask to try again"
    jump riddle_loop


label riddle_correct:
    play sound "audio/nitwit_correct.mp3"

    n "Correct!"
    "The gnome smiles at you, and reaches deep into his backpack to pull out a boo"
    n "Here is a dictionary to translate bavarian, I can give it to you for a fee..."
     
    jump get_dictionary


label get_dictionary:
    menu:
        "Grab the dictionary and run! (Barbarian Strength, Threshold: 7+)":
            menu:
                "Strength Check (Current Modifier: [roll_modifier]):"
                
                "SUCCESS (Total is 7 or higher)":
                    jump grab_success
                    
                "FAILURE (Total is under 7)":
                    jump curse

        "Convince him to give it for free (Persuasion, Threshold: 14+)":
            menu:
                "Persuasion Check (Current Modifier: [roll_modifier]):"
                
                "SUCCESS (Total is 14 or higher)":
                    jump persuasion_success
                    
                " FAILURE (Total is under 14)":
                    jump curse

        "Explain you cannot pay him":
            jump curse


label grab_success:
    play sound "audio/nitwit_steal.mp3"
    "You successfully take the dictionary from the gnome, he sighs"
    n "I wish I could have had some money to buy some doner today, but it seems as if you've helped yourself..."
    n "Good luck on the rest of your journey!"
    jump story_ending


label curse:
    play sound "audio/nitwit_time.mp3"

    "The gnome gets mad at you and throws the dictionary at your feet"
    play sound "audio/nitwit_curse.mp3"

    n "Fine! Take the stupid book, but I put a curse upon your head! Now get out of my sight!"
    $ cursed = True
    " **(DM gives you a curse for the next interaction)**"
    jump story_ending


label persuasion_success:
    
    "You fills his ears with praise of Nitwit the Generous, helper of lost travelers and ensure you will sing his praises forever more!"
    "Nitwit blushes, puffing out his chest."
    play sound "audio/nitwit_convince.mp3"
    n "Well... I suppose a legendary sage like myself can spare a book. Here, take it!"
    n "Though I really wanted a doner kebab..."
    jump story_ending




label story_ending:
    stop music fadeout 2.0
    "You flip open the Bavarian dictionary and compare the characters to the writing on the monument."
    "Slowly, the mysterious ancient letters translate in your mind..."
    
    
    "{b}\"Nitwit the Wise is a Fool.\"{/b}"
    
    if cursed:
        "You chuckle, slipping the dictionary into your pocket, ignoring the tiny curse vibrating in your bones."
    else:
        "You laugh out loud and set off into the new world, dictionary in hand."

    "CONGRATULATIONS - You completed the adventure!"
    return