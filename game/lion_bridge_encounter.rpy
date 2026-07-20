define lion = Character("YLion", color="#FFD700")

default intimidate_dc = 13
default persuasion_dc = 13
default deception_dc = 13
default intimidate_deceive = True
default wisdom = True

label lion_bridge_encounter:

    scene black
    # TODO: transition to bridge background

    "You begin your journey by crossing over a golden bridge."
    "However, the moment you get to the middle, four lions suddenly surround the bridge!"

    lion "We are the lions of Nike! We will not allow enemies of the Angel to cross!"

    "Note: actions that scare the lions raise Intimidation success odds later, but lower Deception success odds. Actions that persuade the lions raise Deception success odds, but lower Intimidation success odds."

label lion_hub:

    menu:
        "Try to talk to the lions":
            jump lion_dialogue   # <--- Changed from 'call' to 'jump'

        "Try to get out (Trigger Climax)":
            jump lion_climax     # <--- Changed from 'call' to 'jump'


label lion_dialogue:
    menu:
        "\"Who is Nike?\"":
            lion "Why, Nike is the one who will conquer these lands! She sits in the middle of Tiergarten on her column of victory, ready to conquer the entirety of Berlin! Then the savannas of Berlin will be ours to roam around and hunt in!"
            jump lion_dialogue   # <--- Loops back to dialogue menu safely

        "(Intimidate) \"This Angel will be no match for the great Nitsche!\"" if intimidate_deceive:
            "You are required to brag about your previous accomplishments as a hero. Your guardian angel may give you an advantage if your bragging is convincing, or a disadvantage if it isn't."
            "DC: [intimidate_dc]"
            menu:
                "Success":
                    lion "W-well as impressive as that sounds, it will be no match for Nike!"
                    "The lion's trust in you has gone down! The lion's fear of you has gone up!"
                    $ intimidate_dc -= 1
                    $ persuasion_dc += 1
                    $ intimidate_deceive = False
                "Failure":
                    lion "HA! I would tell you to go back to preschool, but you couldn't even defeat the kids there! Hahahaha!!!"
                    "The lion's trust in you has gone down! The lion's fear of you has gone down!"
                    $ intimidate_dc += 1
                    $ persuasion_dc += 1
                    $ intimidate_deceive = False
            jump lion_hub

        "(Deception) Get on your knees and pretend to be afraid of Nike" if intimidate_deceive:
            "You are required to act afraid in real life."
            "Your guardian angel may give you an advantage if you actually seem scared, or a disadvantage if it seems obviously fake."
            "DC: [deception_dc]"
            menu:
                "Success":
                    lion "Yes! Cower in fear of the glory of our goddess!"
                    "The lion's trust in you has gone up! The lion's fear of you has gone up!"
                    $ intimidate_dc += 1
                    $ persuasion_dc -= 1
                    $ intimidate_deceive = False
                "Failure":
                    lion "You are mocking us! You are not actually afraid! How insulting, we shall have your head for this!"
                    "The lion's trust in you has gone down! The lion's fear of you has gone down!"
                    $ intimidate_dc += 1
                    $ deception_dc += 1
                    $ intimidate_deceive = False
            jump lion_hub

        "\"Why do you want to conquer Berlin?\"":
            lion "The savannas of Berlin will be our paradise! All that the light touches will be ours! Like in the lion king! And we will spend all day hunting the gazelle of Berlin!"

            menu:
                "(Intelligence) Try to figure out any flaws in the lion's logic. DC: 13" if wisdom:
                    menu:
                        "Success":
                            "You realize that so far you haven't seen any savannas in Berlin. In fact, it seems to be a big city with crowded streets! Not the kind of land the lions are hoping for."
                            "You tell the lions this."
                            lion "What?? That- that can't be right..."
                            "The lions look unsure of themselves, thrown off guard and having to try and consider what you told them."
                            "The lion's trust in you has gone up! The lion's fear of you has gone up!"
                            $ intimidate_dc -= 1
                            $ deception_dc -= 1
                            $ wisdom = False
                        "Failure":
                            "You think and think, and you can't find anything wrong with the lion's logic! It seems that the savannas of Berlin really are in danger."
                            "The lions watch you think and think that you are scared."
                            lion "Hahaha! That's right! Be intimidated by our coming reign!"
                            "The lion's trust in you has gone down! The lion's fear of you has gone down!"
                            $ intimidate_dc += 1
                            $ deception_dc += 1
                            $ wisdom = False
            jump lion_hub

        "Back to options":
            jump lion_hub


label lion_climax:

    menu:
        "Try to scare the lions away by roaring at them! (Intimidation dc: [intimidate_dc])":
            "You are required to roar at the lions in real life."
            "Your guardian angel may give you an advantage if you seem particularly scary, or a disadvantage if you are not at all scary."
            menu:
                "Success":
                    "The lions immediately cower! Frightened, they run away and clear the bridge for you."
                    lion "Clearly you are much more intimidating than Nike. We want to be on your good side, so if you ever need our help, you can summon us."
                    "You receive the Lion's call! You can summon a lion to fight for you in the final encounter."
                    $ lion_companion = True
                    return  # <--- Returns to main script/loop

                "Failure":
                    "The lions roar back! It seems your roaring has only made them angry."
                    "They attack you, and though you manage to defeat them, you are heavily wounded."
                    "Your guardian angel must pick a curse for you."
                    call trigger_curse
                    return  # <--- Returns to main script/loop

        "Try to convince the lions to defect from Nike (Persuasion dc: [persuasion_dc])":
            "You are required to actually make a compelling argument and offer something the lions might want instead of conquering the city."
            "Your guardian angel may give you an advantage if you are convincing, or a disadvantage if you are not at all."
            menu:
                "Success":
                    lion "Wow! I never thought of it like that!"
                    "One of the lions bows, then slowly clears the path for you out of the bridge."
                    lion "From now on, we will no longer fight for Nike. As a show of our gratitude, if you ever need our help, you may summon us. Thank you, friend."
                    "You receive the Lion's call! You can summon a lion to fight for you in the final encounter."
                    $ lion_companion = True
                    return  # <--- Returns to main script/loop

                "Failure":
                    "The lions only look angry from your attempts to reason with them."
                    "They attack you, and though you manage to defeat them, you are heavily wounded."
                    "Your guardian angel must pick a curse for you."
                    call trigger_curse
                    return  # <--- Returns to main script/loop