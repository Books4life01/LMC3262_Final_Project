# Declare characters
define n = Character("Nitwit", color="#22c55e")

# Initialize variables to track game state
default roll_modifier = 0
default cursed = False
default dictionary_obtained = False

image bg_pillar = "images/statue.png"
image gnome_pic:
    "images/gnome.png"
    zoom 0.6

label nitwit_start:

    # 1. Start Ambient looping track
    play sound "audio/ambience_wind.mp3"

    # 2. Start Background Music (BGM)
    play music "audio/bgm_forest.mp3"

    # Begin Story - Background is shown here and stays active
    scene black
    show bg_pillar at truecenter:
        rotate 270
        fit "contain"
    with fade
    play sound "audio/NarratorNitwit1.mp3"
    "As you approach the pillar, you see a foreign text that appears to be in a language unlike anything you’ve ever studied back in Baldur's Gate."

label investigate_pillar:
    play sound "audio/NarratorRock.mp3"
    "Could this text provide valuable information on how to defeat the tyrant Nike? You approach the rock and begin to investigate it closer. Roll 12+ to pass."
    
    # Manual Investigation Roll Choice (Threshold: 12+)
    menu:
        "Investigation Check (Requires 12+):"
        
        " SUCCESS (12 or higher)":
            jump investigation_success
            
        " FAILURE (Under 12)":
            jump investigation_failure


label investigation_success:
    play sound "audio/NarratorHat.mp3"
    "You don't find anything valuable about the text, but you do see a red hat popping out from behind the rock that was not there previously."
    
    menu:
        "Call out to the hidden figure":
            jump meet_nitwit_peaceful

        "Ignore it and walk away":
            jump meet_nitwit_surprise


label investigation_failure:
    play sound "audio/NarratorUnsure.mp3"
    "You’re unsure if this text is valuable or not, but maybe someone nearby could help?"
    
    menu:
        "Walk away from the monument":
            jump meet_nitwit_surprise


label meet_nitwit_peaceful:
    play sound "audio/nitwit_nap.mp3"
    "The figure slowly moves his way around the monument, and approaches you..."
    show gnome_pic at truecenter with dissolve
    n "You woke me from my afternoon nap. Who dares to disturb Nitwit the Wise?"
    jump conversation_start


label meet_nitwit_surprise:
    play sound "audio/NarratorSurprise.mp3"
    "While walking away, a shadowy figure calls out from the monument and stands before you."
    play sound "audio/nitwit_surprise.mp3"
    show gnome_pic at truecenter with dissolve
    n "STOP RIGHT THERE TRAVELER! I AM NITWIT THE WISE, THE ALL-KNOWING GUARDIAN OF THIS MONUMENT!"
    jump conversation_start


label conversation_start:
    menu:
        "Ask Nitwit for help reading the text":
            jump ask_for_help

        "Ignore the noisy little gnome":
            jump ignore_nitwit


label ignore_nitwit:
    "He angrily clears his throat."
    play sound "audio/nitwit_ignore.mp3"
    n "HELLO DID YOU NOT HEAR ME?! I AM NITWIT THE WISE! IS THERE ANYTHING I CAN DO TO HELP YOU?"
    jump ask_for_help


label ask_for_help:
    play sound "audio/NarratorDisgust.mp3"
    "He looks at you with deep disgust."
    play sound "audio/nitwit_language.mp3"
    n "What do you mean you don't know this language? This is Bavarian, the best language in the entire world! How dare you!"
    jump riddle_loop


label riddle_loop:
    play sound "audio/nitwit_quiz.mp3"

    n "That explains a lot! Well I do have just the thing to remedy this, but it would be a disservice to you if I did not teach you about our world while I did it!"
    n "If you wish for me to help you, you must first help me with something. Tell me, to what Prince is it these angels kneel?"

    menu:
        "Prince Karl":
            jump riddle_wrong

        "Prince Bismarck":
            jump riddle_wrong

        "Prince Ferdinand":
            jump riddle_correct


label riddle_wrong:
    n "Bah! Wrong! Completely wrong!"
    play sound "audio/nitwit_wrong.mp3"
    $ roll_modifier -= 1
    sys "* Penalty applied: -1 to future rolls in this encounter (Current Penalty: [roll_modifier]) *"
    "Try again..."
    jump riddle_loop


label riddle_correct:
    play sound "audio/nitwit_correct.mp3"

    n "Correct!"
    "The gnome smiles at you, and reaches deep into his backpack to pull out a book."
    n "Here is a dictionary to translate Bavarian, I can give it to you for a fee..."
    jump get_dictionary


label get_dictionary:
    menu:
        "Grab the dictionary and run! (Barbarian Strength, DC 7)":
            sys "🎲 Roll Strength! Target: 7+. Current Modifier: [roll_modifier]"
            menu:
                "SUCCESS (Total is 7 or higher)":
                    jump grab_success
                    
                "FAILURE (Total is under 7)":
                    jump curse

        "Convince him to give it for free (Persuasion, DC 14)":
            "Concoct an argument on why the gnome should give you the dictionary. Based on the argument your angel might give you advantage or disadvantage"

            sys "🎲 Roll Persuasion! Target: 14+. Current Modifier: [roll_modifier]"
            menu:
                "SUCCESS (Total is 14 or higher)":
                    jump persuasion_success
                    
                "FAILURE (Total is under 14)":
                    jump curse

        "Explain you cannot pay him":
            jump curse


label grab_success:
    play sound "audio/nitwit_steal.mp3"
    "You successfully take the dictionary from the gnome. He sighs."
    n "I wish I could have had some money to buy some döner today, but it seems as if you've helped yourself..."
    n "Good luck on the rest of your journey!"
    $ dictionary_obtained = True
    hide gnome_pic with dissolve
    jump story_ending


label curse:
    play sound "audio/nitwit_time.mp3"
    "The gnome gets mad at you and throws the dictionary at your feet."
    play sound "audio/nitwit_curse.mp3"

    n "Fine! Take the stupid book, but I put a curse upon your head! Now get out of my sight!"
    $ cursed = True
    $ dictionary_obtained = True
    " **(Guardian Angel gives you a curse for the next interaction)**"
    hide gnome_pic with dissolve
    
    jump trigger_curse
        
    jump story_ending


label persuasion_success:
    play sound "audio/NitwitPraise.mp3"
    "You fill his ears with praise of Nitwit the Generous, helper of lost travelers, and vow to sing his praises forever more!"
    "Nitwit blushes, puffing out his chest."
    play sound "audio/nitwit_convince.mp3"
    n "Well... I suppose a legendary sage like myself can spare a book. Here, take it!"
    n "Though I really wanted a döner kebab..."
    $ dictionary_obtained = True
    hide gnome_pic with dissolve
    jump story_ending


label story_ending:
    stop music fadeout 2.0
    play sound "audio/NarratorTranslate.mp3"
    "You flip open the Bavarian dictionary and compare the characters to the writing on the monument."
    "Slowly, the mysterious ancient letters translate in your mind..."
    
    play sound "audio/NarratorPhrase.mp3"
    "{b}\"Only the Champions Blade can slay the winged Victory which plagues the land. \"{/b}"
    
    if cursed:
        play sound "audio/NarratorBones.mp3"
        "You commit the cryptic instruction to memory, slipping the dictionary into your pocket while ignoring the tiny curse your companion bestowed upon your bones."
    else:
        play sound "audio/NarratorHand.mp3"
        "You nod solemnly at the revelation, secure the dictionary in your pack, and set off into the  world."

    return # Cleanly returns to your main script loop!