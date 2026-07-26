define lion = Character("Lion", color="#FFD700")

default intimidate_dc = 14
default persuasion_dc = 14
default deception_dc = 13
default intimidate_deceive = True
default asked_nike = False
default asked_why = False
default wisdom = True

label lion_bridge_encounter:

    scene expression "#332211"
    show lion_bridge:
        xalign 0.5
        yalign 0.5
        zoom 0.25

    play sound "narr_journey_begin.mp3"
    "You begin your journey by crossing over a golden bridge."
    stop sound
    play sound "narr_surrounded.mp3"
    "However, the moment you get to the middle, four lions suddenly surround you!"

    stop sound
    play sound "lionroar.mp3"
    show lion_transparent:
        xalign 0.5
        yalign 0.5
        zoom 0.25
    " "
    #TODO lion sound
    play sound "lion_introduction.wav"
    lion "We are the lions of Nike! We will not allow enemies of the Angel to cross!"

    stop sound
    sys "Note: actions that scare the lions raise Intimidation success odds later, but lower Persuasion success odds. Actions that persuade the lions raise persuasion success odds, but lower Intimidation success odds."

label lion_hub:

    menu:
        "Try to talk to the lions":
            jump lion_dialogue   # <--- Changed from 'call' to 'jump'

        "Try to get out (Trigger Climax)":
            jump lion_climax     # <--- Changed from 'call' to 'jump'


label lion_dialogue:
    menu:
        "\"Who is Nike?\"" if not asked_nike:
            play sound "lion_nike_expo.wav"
            lion "Why, Nike is the one who will conquer these lands! 
            She sits in the middle of Tiergarten on her column of victory, 
            ready to conquer the entirety of Berlin! Then the savannas of 
            Berlin will be ours to roam around and hunt in!"
            $asked_nike = True
            jump lion_dialogue   # <--- Loops back to dialogue menu safely

        "(Intimidate) \"This Angel will be no match for the great Nitsche!\"" if intimidate_deceive:
            sys "You are required to brag about your previous accomplishments as a hero. Your guardian angel may give you an advantage if your bragging is convincing, or a disadvantage if it isn't."
            sys "DC: [intimidate_dc]"
            menu:
                "Success >=[intimidate_dc]":
                    play sound "lion_intimidation_pass.wav"
                    lion "W-well as impressive as that sounds, it will be no match for Nike!"
                    sys "The lion's trust in you has gone down! The lion's fear of you has gone up!"
                    $ intimidate_dc -= 3
                    $ persuasion_dc += 1
                    $ intimidate_deceive = False
                "Failure <[intimidate_dc]":
                    #TODO lion dialogue
                    play sound "lion_intimidation_fail.wav"
                    lion "HA! Look how skinny you are! Barbarian??? You look like a humanities professor!
                    How could you defeat Nike? You probably couldn't even defeat a fly! Hahahaha!!!"
                    sys "The lion's trust in you has gone down! The lion's fear of you has gone down!"
                    $ intimidate_dc += 1
                    $ persuasion_dc += 1
                    $ intimidate_deceive = False
            jump lion_hub

        "(Deception) Get on your knees and pretend to be afraid of Nike to earn the trust of the lions" if intimidate_deceive:
            sys "You are required to act afraid in real life. Your guardian angel may give you an advantage if you actually seem scared, or a disadvantage if it seems obviously fake."
            sys "DC: [deception_dc]"
            menu:
                "Success >=[deception_dc]":
                    play sound "lion_deception_pass.wav"
                    lion "Yes! Cower in fear of the glory of our goddess! I like this one"
                    sys "The lion's trust in you has gone up! The lion's fear of you has gone up!"
                    $ intimidate_dc += 1
                    $ persuasion_dc -= 3
                    $ intimidate_deceive = False
                "Failure <[deception_dc]":
                    play sound "lion_deception_fail.wav"
                    lion "You are mocking us! You are not actually afraid! How insulting, 
                    keep acting this way and we shall have your head!"
                    sys "The lion's trust in you has gone down! The lion's fear of you has gone down!"
                    $ intimidate_dc += 1
                    $ persuasion_dc += 1
                    $ intimidate_deceive = False
            jump lion_hub

        "\"Why do you want to conquer Berlin?\"" if not asked_why:
            play sound "lion_lion_king.wav"
            lion "The savannas of Berlin will be our paradise! 
            All that the light touches will be ours! Like in the lion king! 
            And we will spend all day hunting the gazelle of Berlin!"
            $asked_why = True
            menu:
                "(Intelligence) Try to figure out any flaws in the lion's logic. DC: 13" if wisdom:
                    menu:
                        "Success >=[13]":
                            play sound "narr_int_pass.mp3"
                            "You realize that so far you haven't seen any savannas in Berlin. In fact, it seems to be a big city with crowded streets! Not the kind of land the lions are hoping for. You tell the lions this."
                            stop sound
                            play sound "lion_int_pass.wav"
                            lion "What?? That- that can't be right..."
                            stop sound
                            play sound "narr_lions_confused.mp3"
                            "The lions look unsure of themselves, thrown off guard and having to try and consider what you told them."
                            stop sound
                            sys "The lion's trust in you has gone up! The lion's fear of you has gone up!"
                            $ intimidate_dc -= 3
                            $ deception_dc -= 3
                            $ wisdom = False
                        "Failure <[13]":
                            play sound "narr_int_fail.mp3"
                            "You think and think, and you can't find anything wrong with the lion's logic! It seems that the savannas of Berlin really are in danger. The lions watch you think and think that you are scared."
                            stop sound
                            play sound "lion_int_fail.wav"
                            lion "Hahaha! That's right! Be intimidated by our coming reign!"
                            sys "The lion's trust in you has gone down! The lion's fear of you has gone down!"
                            $ intimidate_dc += 1
                            $ deception_dc += 1
                            $ wisdom = False
            jump lion_hub

        "Back to options":
            jump lion_hub


label lion_climax:

    menu:
        "Try to scare the lions away by roaring at them! (Intimidation dc: [intimidate_dc])":
            sys "You are required to roar at the lions in real life. Your guardian angel may give you an advantage if you seem particularly scary, or a disadvantage if you are not at all scary."
            menu:
                "Success >=[intimidate_dc]":
                    play sound "narr_intimidate_pass.mp3"
                    "The lions immediately cower! Frightened, they run away and clear the bridge for you."
                    stop sound
                    play sound "lion_intimidate_pass_2.wav"
                    lion "Clearly you are much more intimidating than Nike. We want to be on your good side, so if you ever need our help, you can summon us."
                    sys "You receive the Lion's call! You can summon a lion to fight for you in the final encounter."
                    $ lion_companion = True
                    return  # <--- Returns to main script/loop

                "Failure <[intimidate_dc]":
                    play sound "narr_intimidate_fail.mp3"
                    "The lions roar back! It seems your roaring has only made them angry."
                    stop sound
                    play sound "narr_attack.mp3"
                    "They attack you, and though you manage to defeat them, you are heavily wounded."
                    stop sound
                    sys "Your guardian angel must pick a curse for you."
                    jump trigger_curse
                    return  # <--- Returns to main script/loop

        "Try to convince the lions to defect from Nike (Persuasion dc: [persuasion_dc])":
            "You are required to actually make a compelling argument and offer something the lions might want instead of conquering the city."
            "Your guardian angel may give you an advantage if you are convincing, or a disadvantage if you are not at all."
            menu:
                "Success >=[persuasion_dc]":
                    play sound "lion_persuade_pass.wav"
                    lion "Wow! I never thought of it like that!"
                    stop sound
                    play sound "narr_persuade_pass.mp3"
                    "One of the lions bows, then slowly clears the path for you out of the bridge."
                    stop sound
                    play sound "lion_persuade_pass_2.wav"
                    lion "From now on, we will no longer fight for Nike. As a show of our gratitude, if you ever need our help, you may summon us. Thank you, friend."
                    stop sound
                    sys "You receive the Lion's call! You can summon a lion to fight for you in the final encounter."
                    $ lion_companion = True
                    return  # <--- Returns to main script/loop

                "Failure <[persuasion_dc]":
                    play sound "narr_persuade_fail.mp3"
                    "The lions only look angry from your attempts to reason with them."
                    stop sound
                    play sound "narr_attack.mp3"
                    "They attack you, and though you manage to defeat them, you are heavily wounded."
                    stop sound
                    sys "Your guardian angel must pick a curse for you."
                    jump trigger_curse
                    return  # <--- Returns to main script/loop