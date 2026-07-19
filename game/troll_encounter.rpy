# =========================================================================
# CHARACTER DEFINITIONS & GAME STATE
# =========================================================================

define sys = Character("System", color="#555555") 

# Troll Character Definitions with custom speech colors
define troll_yellow = Character("Grumble (Yellow Troll)", color="#f1c40f")
define troll_green = Character("Oakhaven (Green Troll)", color="#2ec865")

# Initialize variables specific to this encounter
default modifier_bonus = 0
default active_curse = "None"
default has_bard_blessing = False
default playground_passes = 0
default roar_dc = 18

# Track which trolls have been dealt with/scared away
default troll_1_completed = False
default troll_2_completed = False

# Track player style (violence vs peaceful) to affect the ending
default violent_acts = 0

# =========================================================================
# ENCOUNTER: THE SIEGE OF THE HALFLING SANDBOX
# =========================================================================

label start_troll_encounter:
    scene expression "#332211"
    show halfling_fort at truecenter
    play music "forest_battle_ambient.ogg" fadein 2.0

    "In the distance, you see a sprawling wooden structure with towers and hand-carved beams and climbing bars and slides for easy escape. Small humanlike figures run about it screaming, looking very childlike."
    "You have come across a vulnerable halfling outpost."
    "Surrounding the fort are two massive, ancient wooden trolls, who seem to be attacking the fort."
    "You can choose how to handle this threat: approach and pacify the trolls individually, or attempt to confront them both at once."
    
    $ playground_passes = 0
    $ violent_acts = 0
    $ troll_1_completed = False
    $ troll_2_completed = False
    
    jump playground_hub


# -------------------------------------------------------------------------
# THE PLAYGROUND HUB (CHOICE MENU)
# -------------------------------------------------------------------------

label playground_hub:
    scene expression "#332211"
    show halfling_fort at truecenter
    "You stand in the center of the wooden playground outpost, plotting your next move."
    
    menu:
        "Approach the yellow, mushroom-cap troll" if not troll_1_completed:
            jump troll_1_shroom
            
        "Approach the green-skinned, lovesick troll" if not troll_2_completed:
            jump troll_2_lovesick
            
        "Confront all the remaining trolls at once (Trigger Climax)":
            jump playground_climax


# -------------------------------------------------------------------------
# TROLL 1: THE CONFUSED SHROOM-CAP (YELLOW TROLL)
# -------------------------------------------------------------------------

label troll_1_shroom:
    scene expression "#332211"
    show confused_troll at truecenter
    "You approach the yellow, stump-like figure scratching its wooden head under a massive mushroom cap."
    "It is leaning heavily against a thick wooden climbing frame, shaking it violently as if trying to uproot an actual pine tree."
    
    troll_yellow "Urrrgh... tree got square branches? Why logs so smooth and straight? Grumble shake, but no pinecones fall... Grumble hungry..."
    
    menu:
        "Inspect the troll and try to guide it away (Insight Check, DC 10)":
            sys "Roll a physical d20 for an Insight Check."
            menu:
                "Roll is 10 or higher (Pass)":
                    $ playground_passes += 1
                    "You scratch your head in confusion to match its energy, then gently point toward the dense, muddy bushes nearby."
                    troll_yellow "Ohhh! Dark soil! Squishy moss! Grumble thank giant buddy. Grumble go find mushrooms there!"
                    "The yellow troll rumbles in appreciation, wandering away from the log climbing frame."
                    $ troll_1_completed = True
                "Roll is under 10 (Fail)":
                    "You try to gesture, but your movements are clumsy. The yellow troll startles!"
                    troll_yellow "Aaargh! Keep away from Grumble's mushroom cap!"
                    "It unleashes a sudden psychic backfire of clumsy, disoriented energy before resuming its shaking of the wooden logs."
                    call trigger_curse
                    $ troll_1_completed = True

        "Attack the troll and try to scare it off (Strength Check, DC 8)":
            $ violent_acts += 1
            sys "Roll a physical d20 for a Strength/Athletics Check."
            menu:
                "Roll is 8 or higher (Pass)":
                    $ playground_passes += 1
                    "You bare your teeth, let out a low snarl, and slam your fist hard against the thick timber frame, making the heavy wood thud with a deep, echoing boom."
                    troll_yellow "Eeeek! Loud timber demon! Screaming giant! Grumble leaving, Grumble sorry!"
                    "Terrified by your brute strength, the yellow troll cowers and retreats into the background."
                    $ troll_1_completed = True
                "Roll is under 8 (Fail)":
                    "You lunged to strike, but your foot caught on a stray woodchip! You crash face-first into the dirt."
                    troll_yellow "Haha! Silly heavy-foot giant fall down."
                    "Insulted by the attack, it unleashes a sudden psychic blast of energy, inflicting a curse before resuming its shaking of the frame."
                    call trigger_curse
                    "You hurt your pride and your shins. Grumble stands his ground, still blocking the climbing frame."

    "You back away to plan your next move."
    jump playground_hub


# -------------------------------------------------------------------------
# TROLL 2: THE LOVESICK FLOWER-BEARER (GREEN TROLL)
# -------------------------------------------------------------------------

label troll_2_lovesick:
    scene expression "#332211"
    show lovesick_troll at truecenter
    "You step up to the green-skinned troll holding a single yellow flower. It is standing at the edge of the woodchips, keeping its distance as it stares with wide, bulging eyes directly at the grand wooden slide tower from afar."
    "It sighs a gust of pine-scented wind, trying to woo the structure with a mix of reverence and stage fright."
    
    troll_green "My timber-limbed goddess... standing so proud, high, and distant... your smooth metal chute shines so brightly in the sun... I brought this beautiful flower for you, yet I dare not step closer... please, break your silence..."
    
    "To pacify this lovesick beast, you must compose and recite a romantic limerick out loud toward the distant slide tower on its behalf."
    "You have 60 seconds. Once you finish, your real-life Guardian Angel will judge your performance."
    
    menu:
        "Guardian Angel: Did the player deliver a Legendary Performance? (Perfect rhymes, dramatic, funny)":
            "Your poem is a masterpiece. The green troll sheds a single, sticky tear of sap."
            troll_green "Such words... they pierce my wooden bark! My lady of the tower has spoken through your voice! I shall stand here in silent, poetic contemplation..."
            $ playground_passes += 1
            
        "Guardian Angel: Did they make a Standard Pass? (Solid attempt)":
            "A respectable effort. The green troll rumbles softly and bows its head, pacified by your poetry."
            troll_green "Your song is strange, giant. But it warms my green heart. I will rest my flower here and admire her beauty from afar."
            $ playground_passes += 1
            
        "Guardian Angel: Did they Fail? (Refused to perform, or didn't rhyme at all)":
            "The troll is deeply insulted by your mechanical, unfeeling prose."
            troll_green "Silence, faithless brute! You know nothing of true art! Your words are like dry wood rotting in the rain!"
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
    "You gather your resolve to finish this encounter and secure the sandbox once and for all."
    
    if not (troll_1_completed or troll_2_completed):
        "You haven't pacified or scared off a single troll yet! They all stand at full strength, their chaotic magic swirling wildly around the sandbox."
    elif troll_1_completed and troll_2_completed:
        "Both trolls have been dealt with, but you must make one final gesture to permanently seal the area's safety."
    else:
        "One troll has been dealt with, while the remaining one still watches the sandbox with chaotic intent."
        
    # Rebalanced dynamic DC for a maximum of 2 passes instead of 3
    $ roar_dc = 5 if playground_passes == 2 else (12 if playground_passes == 1 else 18)

    menu:
        "Use Barbarian Roar (Intimidation, Target [roar_dc]+)":
            "You decide to terrify them into submission. Take a deep breath and let out your loudest, most blood-curdling Barbarian war cry right now!"
            
            sys "Roll Intimidation (d20). Your target DC is [roar_dc]."
            
            menu:
                "Roll is [roar_dc] or higher (Pass)":
                    "Your roar shakes the very leaves of the Tiergarten. The remaining trolls freeze in absolute terror, instantly hardening into silent, harmless wooden playground decorations."
                    $ playground_passes += 1
                    jump playground_evaluation
                    
                "Roll is under [roar_dc] (Fail)":
                    "You lose your breath halfway through the roar, ending in an awkward cough. The trolls turn and blink at you in silent, wood-carved pity."
                    "Your spectacular failure leaves you open to their combined psychic backfire!"
                    call trigger_curse
                    "They refuse to be intimidated. You must fall back and deal with them the hard way."
                    jump playground_hub


# -------------------------------------------------------------------------
# EVALUATION & ENDING SCENE
# -------------------------------------------------------------------------

label playground_evaluation:
    # Adjusted metrics for evaluation to match the 2-troll threshold
    if playground_passes >= 2:
        "Incredible work. You saved the halfling outpost and brought ancient balance back to the playground."
        "The heavy, stagnant magic lifts, replaced by a warm, emerald glow that flows into your muscles."
        sys "You receive the Blessing of the Forest! You gain a +2 modifier to all rolls in the next encounter."
        $ modifier_bonus += 2
        
        # Guardian Angel final reaction depends on your methods
        if violent_acts >= 1:
            "Through your mental link, you feel your Guardian Angel's presence. They look down at your scuffed knuckles and sigh."
            "GA: 'Well... it wasn't pretty, and those wooden beasts will probably have nightmares about you. But the halflings are safe. Clean yourself up, Barbarian.'"
        else:
            "Through your mental link, you feel your Guardian Angel's presence. They radiate a warm, golden approval."
            "GA: 'Brilliantly played. You showed the heart of a true hero, balancing power with wisdom. The Weave smiles upon us. Let us move on.'"
            
    elif playground_passes == 0:
        "That was an utter disaster. The outpost is in ruins, the kids are crying, and you are heavily weighed down by ancient curses."
        "GA: 'We must flee. You fought poorly and listened even worse. Let us hope your luck improves before our next trial.'"
    else:
        "The playground is quiet once more. You dust off the woodchips, wipe the sweat from your brow, and prepare to move on."
        "GA: 'A messy skirmish, but a victory nonetheless. Let us keep moving before any more forest spirits awaken.'"
        
    "Consult your map. It is time to head to your next destination."
    return


# =========================================================================
# REUSABLE PHYSICAL CURSE SELECTION SYSTEM
# =========================================================================

label trigger_curse:
    sys "The curse strikes! Turn to your real-life Guardian Angel. They must choose one physical curse from the menu for you to perform!"
    
    menu:
        "Guardian Angel: Choose 'The Hobbling Goblin' (Hop on one foot)":
            $ active_curse = "Hobbling Goblin"
            "The curse takes hold! Your leg feels incredibly heavy. You must hop on one foot whenever you are walking to the next location."
            
        "Guardian Angel: Choose 'The Stone-Arm Hex' (Keep one arm behind back)":
            $ active_curse = "Stone-Arm"
            "The curse takes hold! Your dominant arm stiffens and turns to solid oak. You must keep it tucked behind your back for the rest of this journey."
            
        "Guardian Angel: Choose 'The Tongue-Tie Plague' (Whispers/grunts only)":
            $ active_curse = "Tongue-Tie"
            "The curse takes hold! Your vocal cords lock up. You can only whisper or grunt until the next encounter."
            
        "Guardian Angel: Choose 'The Paralyzed Glance' (Move torso, not neck)":
            $ active_curse = "Paralyzed Glance"
            "The curse takes hold! Your neck freezes completely solid. If you want to look around, you must rotate your entire upper body."
            
    return