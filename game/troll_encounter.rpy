# =========================================================================
# CHARACTER DEFINITIONS & GAME STATE
# =========================================================================

define sys = Character("System", color="#555555") 

# Troll Character Definitions with custom speech colors
define troll_yellow = Character("Grumble (Yellow Troll)", color="#f1c40f")
define troll_green = Character("Oakhaven (Green Troll)", color="#2ec865")

# Initialize variables specific to this encounter
default playground_passes = 0
default roar_dc = 18

# Track which trolls have been dealt with/scared away
default troll_1_completed = False
default troll_2_completed = False
default duck_shrine_visited = False

# Track player style (violence vs peaceful) to affect the ending
default violent_acts = 0

# =========================================================================
# ENCOUNTER: THE SIEGE OF THE HALFLING SANDBOX
# =========================================================================

label start_troll_encounter:
    scene expression "#332211"
    show halfling_fort at truecenter
    play music "forest_battle_ambient.ogg" fadein 2.0
    stop sound
    play sound "audio/narr_troll_intro.mp3"

    "In the distance, you see a sprawling wooden structure with towers and hand-carved beams and climbing bars and slides for easy escape. Small humanlike figures run about it screaming, looking very childlike."
    "You have come across a vulnerable halfling outpost."
    "Surrounding the fort are two massive, ancient trolls, who seem to be attacking the fort."
    "You can choose how to handle this threat: approach and pacify the trolls individually, or attempt to confront them both at once."
    
    $ playground_passes = 0
    $ violent_acts = 0
    $ troll_1_completed = False
    $ troll_2_completed = False
    $ duck_shrine_visited = False
    
    jump playground_hub


# -------------------------------------------------------------------------
# THE PLAYGROUND HUB (CHOICE MENU)
# -------------------------------------------------------------------------

label playground_hub:
    scene expression "#332211"
    show halfling_fort at truecenter
    "You stand in the center of the wooden outpost, plotting your next move."
    
    menu:
        "Approach the yellow, mushroom-cap troll" if not troll_1_completed:
            jump troll_1_shroom
            
        "Approach the green-skinned, lovesick troll" if not troll_2_completed:
            jump troll_2_lovesick

        "Investigate an overgrown shrine a little away from the outpost" if not duck_shrine_visited:
            jump duck_shrine_subquest

        "Confront all the remaining trolls at once (If the trolls are still at full strength this will be difficult)":
            jump playground_climax


# -------------------------------------------------------------------------
# SHRINE SUBQUEST: THE STONE DUCK BASIN
# -------------------------------------------------------------------------

label duck_shrine_subquest:
    scene expression "#223322"
    show duck_fountain at truecenter
    stop sound
    play sound "audio/narr_duck_intro.mp3"

    "Off to the side of the wooden play structure, half-buried in dry leaves, sits an ancient stone fountain."
    "Four circular basins surround a familiar animal carved into the center. Reflections of the canopy glisten in the standing rain water."
    "This shrine radiates an ancient, quiet magic that could aid your battle... if approached with respect."

    menu:
        "Perform the Offering Trial (Real-Life Physical Check)":
            "You decide to pay respects to the sleeping duck."
            sys "Turn to your real-life Guardian Angel! You must find 4 forest items (twigs, leaves, etc) and gently drop them into the 4 pools of water without splashing or making noise within 30 seconds."
            
            menu:
                "Guardian Angel: Did the player give a suitable and quick offering? (Pass)":
                    $ playground_passes += 1
                    play sound "audio/duck_sucess.mp3"

                    "The water ripples smoothly. A gentle blue light washes over you, soothing your weary limbs."
                    sys "You receive the Blessing of the Forest!"
                    $ forest_blessing = True
                    $ duck_shrine_visited = True

                "Guardian Angel: Did they splash, fumble, or fail the timing? (Fail)":
                    stop sound
                    play sound "audio/duck_fail.mp3"

                    "You drop the offering too heavily, causing a loud splash! The stone duck seems to glare at you in silent judgment."
                    "No blessing will be bestowed today."
                    $ duck_shrine_visited = True

<<<<<<< HEAD
                    "Kick the stone basins to check for hidden loot":
=======
                "Kick the stone basins to check for hidden loot":
>>>>>>> c9c16bf26ca701167b2eff59e4416f392296c2b6
                    $ violent_acts += 1
                    stop sound
                    play sound "audio/duck_aggro.mp3"

            "You give the ancient stone basin a heavy kick."
            "The ancient spirits of the shrine do not take kindly to your vandalism! Heavy, cursed water lashes out at your shins."
            call trigger_curse
            $ duck_shrine_visited = True

        "Return to the halfling Village":
            jump playground_hub

    "You step away from the shrine and return to the main grounds."
    jump playground_hub


# -------------------------------------------------------------------------
# TROLL 1: THE CONFUSED SHROOM-CAP (YELLOW TROLL)
# -------------------------------------------------------------------------

label troll_1_shroom:
    scene expression "#332211"
    show confused_troll at truecenter
    stop sound
    play sound "audio/grumble_01.mp3"

    "You approach the yellow, stump-like figure trembling under its massive mushroom cap."
    "It is frantically shaking and tearing at a thick wooden climbing frame, scaring the halflings inside."
    
    stop sound
    play sound "audio/mushroom_intro.mp3"
    troll_yellow "Urrrgh! Need big timber! Need heavy log! Must build wall to hide from scary stone demon!"
    stop sound  # Cuts audio on click
    play sound "audio/grumble_02.mp3"

    "He points a shaking wooden finger at a small mossy structure sitting a distance away from the halfling village."
    
    stop sound
    play sound "audio/grumble_scared.mp3"
    troll_yellow "Look at it! Sitting right there! Four gaping mouths full of dark swamp water... and a terrifying beast sleeping on top! Grumble shaking! Grumble must break tree fort to protect himself!"
    stop sound  # Cuts audio on click

    hide confused_troll
    show duck_fountain at truecenter 
    play sound "audio/grumble_03.mp3"

    "It seems Grumble's 'attack' on the halfling outpost is actually just a desperate, panicked attempt to hide from the fountain."
    hide duck_fountain
    show confused_troll at truecenter

    menu:
        "Walk over and inspect the 'stone demon' in real life" if not duck_shrine_visited:
            jump duck_shrine_subquest

        "Tell Grumble it's not a demon":
            menu:
                "Tell Grumble: 'That's not a monster, it's a stone DUCK!'" if not troll_1_completed:
                    stop sound
                    play sound "audio/grumble_duck_01.mp3"
                    "Grumble peeks out from behind his mushroom cap, squinting his big yellow eyes at the fountain."
                    stop sound
                    play sound "audio/grumble_duck.mp3"
                    troll_yellow "A... a duck? A little quack-quack bird?"

                    troll_yellow "Ohhh... it not got sharp teeth? It just duck sleeping on water bowls? Haha! Silly Grumble!"
                    troll_yellow "Grumble not need wooden wall no more! Grumble stop shaking fort and go find mushrooms in the bushes. Thank you, sharp-eyed giant!"
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_duck_02.mp3"

                    "The yellow troll rumbles in relief, lets go of the climbing frame, and happily toddles away into the muddy bushes."
                    $ playground_passes += 1
                    $ troll_1_completed = True

                "Tell Grumble: 'That's a giant stone TURKEY!'":
                    stop sound
                    play sound "audio/grumble_turkey.mp3"
                    troll_yellow "A turkey?! With sharp gobbler-teeth?! That even worse!"
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_incorrect_guess.mp3"
                    "Your incorrect guess panics Grumble even further! He violently shakes the frame, unleashing a psychic blast of chaotic energy!"
                    call trigger_curse
                    $ troll_1_completed = True

                "Tell Grumble: 'That's a vicious stone RABBIT!'":
                    stop sound
                    play sound "audio/grumble_rabbit.mp3"
                    troll_yellow "A rabbit?! It gonna call on Grumble's head and bite Grumble's ears!"
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_incorrect_guess.mp3"

                    "Your incorrect guess panics Grumble even further! He violently shakes the frame, unleashing a psychic blast of chaotic energy!"
                    call trigger_curse
                    $ troll_1_completed = True

                "Tell Grumble: 'That's a swamp TOAD!'":
                    stop sound
                    play sound "audio/grumble_toad.mp3"
                    troll_yellow "A toad?! It gonna spit poisonous slime on Grumble!"
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_incorrect_guess.mp3"

                    "Your incorrect guess panics Grumble even further! He violently shakes the frame, unleashing a psychic blast of chaotic energy!"
                    call trigger_curse
                    $ troll_1_completed = True

        "Calm Grumble down with reason without inspecting the fountain (Insight Check, DC 10)":
            sys "Roll a physical d20 for an Insight Check."
            menu:
                "Roll is 10 or higher (Pass)":
                    $ playground_passes += 1
                    stop sound
                    play sound "audio/grumble_pacify_01.mp3"

                    "You mimic his cowering posture to gain his trust, then speak gently to convince him the stone structure is completely dormant."
                    
                    stop sound
                    play sound "audio/grumble_pacify_sucess.mp3"
                    troll_yellow "You... you think stone thing sleeping? Not gonna eat Grumble? Okay... Grumble trust new freind. Grumble go find moss instead."
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_pacify_02.mp3"

                    "Grumble leaves the wooden fort intact and wanders away peacefully."
                    $ troll_1_completed = True
                    
                "Roll is under 10 (Fail)":
                    stop sound
                    play sound "audio/grumble_pacify_fail_01.mp3"

                    "Your attempt to calm him backfires—Grumble thinks you are trying to trick him into getting eaten!"
                    
                    stop sound
                    play sound "audio/grumble_pacify_failure.mp3"
                    troll_yellow "Liarrr! You working with stone demon! Keep away from Grumble!"
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_pacify_fail_02.mp3"

                    "He unleashes a defensive psychic blast before clinging tighter to the timber frame."
                    call trigger_curse
                    $ troll_1_completed = True

        "Attack Grumble to scare him away from the fort (Strength Check, DC 8)":
            $ violent_acts += 1
            sys "Roll a physical d20 for a Strength/Athletics Check."
            menu:
                "Roll is 8 or higher (Pass)":
                    $ playground_passes += 1
                    stop sound
                    play sound "audio/grumble_scare_01.mp3"

                    "You bare your teeth, let out a low snarl, and slam your fist hard against the timber frame!"
                    
                    stop sound
                    play sound "audio/grumble_scare_sucess.mp3"
                    troll_yellow "Eeeek! Loud timber demon! Screaming giant!"
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_scare_02.mp3"

                    "Scared of both you AND the stone monster, Grumble shrieks and flees into the deep woods."
                    $ troll_1_completed = True
                    
                "Roll is under 8 (Fail)":
                    stop sound
                    play sound "audio/grumble_scare_fail_01.mp3"

                    "You lunge forward to strike, but trip over a woodchip and crash face-first into the dirt!"
                    
                    stop sound
                    play sound "audio/grumble_scare_failure.mp3"
                    troll_yellow "Haha! Silly heavy-foot giant fall down!"
                    stop sound  # Cuts audio on click
                    play sound "audio/grumble_scare_fail_02.mp3"

                    "Insulted by your aggression, Grumble retaliates with a curse."
                    call trigger_curse
                    $ troll_1_completed = True

    "You back away to plan your next move."
    jump playground_hub


# -------------------------------------------------------------------------
# TROLL 2: THE LOVESICK FLOWER-BEARER (GREEN TROLL)
# -------------------------------------------------------------------------

label troll_2_lovesick:
    scene expression "#332211"
    show lovesick_troll at truecenter
    stop sound
    play sound "audio/narr_love_intro.mp3"

    "You step up to the green-skinned troll holding a single yellow flower. It is standing at the edge of the woodchips, keeping its distance as it stares with wide, bulging eyes directly at the grand metal slide tower from afar."
    "It sighs a gust of pine-scented wind, trying to woo the structure with a mix of reverence and stage fright."
    stop sound
    play sound "audio/love_intro.mp3"

    troll_green "My shiny-metal goddess... standing so proud, high, and distant... your smooth metal chute shines so brightly in the sun... I brought this beautiful flower for you, yet I dare not step closer... please, break your silence..."
    stop sound
    play sound "audio/slide_poem.mp3"

    "To pacify this lovesick beast, you must compose and recite a romantic limerick out loud toward the distant slide tower on its behalf."
    sys "You have 60 seconds. Once you finish, your real-life Guardian Angel will judge your performance."
    
    menu:
        "Guardian Angel: Did the player deliver a Legendary Performance? (Perfect rhymes, dramatic, funny)":
            stop sound
            play sound "audio/narr_legendary_poem.mp3"

            "The world itself seems to acknowledge your magnificent composition, suddenly you hear the ringing of bells and feel a ryhtmic pulse come over you. You have received the Blessing of the Bard"
            "Your poem is a masterpiece. The green troll sheds a single, sticky tear of sap."
            stop sound
            play sound "audio/legendary_poem.mp3"

            troll_green "Such words... they pierce my wooden bark! My lady of the tower has spoken through your voice! I shall stand here in silent, poetic contemplation..."
            $ playground_passes += 1
            $ has_bard_blessing = True
            
        "Guardian Angel: Did they make a Standard Pass? (Solid attempt)":
            stop sound
            play sound "audio/narr_respectable_poem.mp3"

            "A respectable effort. The green troll rumbles softly and bows its head, pacified by your poetry."
            stop sound
            play sound "audio/ok_poem.mp3"

            troll_green "Your song is strange, giant. But it warms my green heart. I will rest my flower here and admire her beauty from afar."
            $ playground_passes += 1
            
        "Guardian Angel: Did they Fail? (Refused to perform, or didn't rhyme at all)":
            stop sound
            play sound "audio/narr_poem_fail.mp3"

            "The troll is deeply insulted by your mechanical, unfeeling prose."
            stop sound
            play sound "audio/fail_poem.mp3"

            troll_green "Silence, faithless brute! You know nothing of true art! Your words are like dry wood rotting in the rain!"
            stop sound
            play sound "audio/narr_poem_fail_02.mp3"

            "It shrieks a high-pitched wooden scrape, rattling your brain!"
            call trigger_curse
            
    $ troll_2_completed = True
    "You step back to evaluate your next move."
    jump playground_hub


# -------------------------------------------------------------------------
# PLAYGROUND CLIMAX & CONCLUSION
# -------------------------------------------------------------------------

label playground_climax:
    scene expression "#332211"
    show halfling_fort at truecenter
    stop sound
    play sound "audio/resolve.mp3"

    "You gather your resolve to finish this encounter and secure the sandbox once and for all."
    
    if not (troll_1_completed or troll_2_completed):
        "You haven't pacified or scared off a single troll yet! They all stand at full strength, their chaotic magic swirling wildly around the sandbox."
    elif troll_1_completed and troll_2_completed:
        "Both trolls have been dealt with, but you must make one final gesture to permanently seal the area's safety."
    else:
        "One troll has been dealt with, while the remaining one still watches the sandbox with chaotic intent."
        
    # Rebalanced dynamic DC for a maximum of 2 passes instead of 3
    $ roar_dc = 5 if playground_passes >= 2 else (12 if playground_passes == 1 else 18)

    menu:
        "Use Barbarian Roar (Intimidation, Target [roar_dc]+)":
            "You decide to terrify them into submission. Take a deep breath and let out your loudest, most blood-curdling Barbarian war cry right now!"
            sys "Based on how intimidating or pathetic your perforance, your gaurdian angel may give you advantage or disadvantage here"
            sys "Roll Intimidation (d20). Your target DC is [roar_dc]."
            
            menu:
                "Roll is [roar_dc] or higher (Pass)":
                    stop sound
                    play sound "audio/roar_sucess.mp3"

                    "Your roar shakes the very leaves of the Tiergarten. The remaining trolls freeze in absolute terror, instantly hardening into silent, harmless wooden playground decorations."
                    $ playground_passes += 1
                    jump playground_evaluation
                    
                "Roll is under [roar_dc] (Fail)":
                    stop sound
                    play sound "audio/roar_failure.mp3"

                    "You lose your breath halfway through the roar, ending in an awkward cough. The trolls turn and blink at you in silent, wood-carved pity."
                    "They refuse to be intimidated. You must fall back and deal with them the hard way."

                    "Your spectacular failure leaves you open to their combined psychic backfire!"
                    call trigger_curse
                    jump playground_hub


# -------------------------------------------------------------------------
# EVALUATION & ENDING SCENE
# -------------------------------------------------------------------------

label playground_evaluation:
    stop sound
    play sound "audio/troll_completion.mp3"

    "Incredible work. You saved the halfling outpost and brought ancient balance back to the playground."
    
    if violent_acts >= 1:
        stop sound
        play sound "audio/violent_ending.mp3"

        "A heavy silence settles over the playground as you look down at your scuffed knuckles."
        "It wasn't pretty, and those wooden beasts will probably have nightmares about you. But the halflings are safe. You clean yourself up and prepare to move on."
    else:
        stop sound
        play sound "audio/troll_peacfulending.mp3"

        "A warm sense of triumph washes over you."
        "Brilliantly played. You showed the heart of a true hero, balancing power with wisdom. The area feels peaceful once more."

    return