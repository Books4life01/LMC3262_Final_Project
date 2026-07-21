# Character Definitions
define nike = Character("Nike")

# Track stealth performance modifier from GA
default stealth_modifier = 0

label victory_tunnel_start:
    scene bg_dark_tunnel with fade
    play music "audio/bgm_dungeon_dread.mp3"
    
    "Armed with the Champions's blade, you slip into the shadows at the mouth of the pedestrian tunnel leading beneath the roundabout to the tyrant perch."
    show tunnel at truecenter
    "Nike's golden light pulses heavily from above. To approach unseen, you must tread with absolute silence..."

    # Check for Unseen Cloak from Siegfried
    if cloak_obtained:
        "You wrap Siegfried's enchanted cloak around your shoulders. Its weave distorts light and muffles your footsteps, granting you supernatural stealth! + 5 stealth bonus"

    # =========================================================================
    # STEALTH PERFORMANCE & PHYSICAL STEALTH ROLL (DC 15)
    # =========================================================================
    sys "STEALTH CHECK: The player must tip-toe in real life through the tunnel/area with complete stealth!"

    menu:
        "Guardian Angel Judge: Perfect silent tiptoeing! (+3 Roll Bonus)":
            $ stealth_modifier = 3
            "You move like a ghost, your steps making no sound against the damp subterranean stone."

        "Guardian Angel Judge: Clumsy or noisy tiptoeing! (+0 Roll Bonus)":
            $ stealth_modifier = 0
            "Your boot clips a loose rock, but you freeze before the sound echoes too far."

    # Determine calculation string & value for system prompt
    $ cloak_bonus = 5 if cloak_obtained else 0
    $ total_stealth_mod = stealth_modifier + cloak_bonus

    # Physical d20 Stealth Roll
    sys "🎲 PHYSICAL ROLL: Roll a d20 for Stealth! Add your Stealth Modifier (+[total_stealth_mod]). Target DC is 15."

    menu:
        "🎲 Total Stealth Roll was 15 or HIGHER (SUCCESS)":
            play sound "audio/stealth_success.mp3"
            $ stealth_buff = 5
            "**[STEALTH SUCCESS]** You reach the end of the tunnel completely undetected! You gain the **Shadow Ambush Buff (+5)**!"

        "🎲 Total Stealth Roll was LESS than 15 (FAIL)":
            play sound "audio/stealth_fail.mp3"
            $ stealth_buff = 0
            "**[STEALTH FAILED]** A flock of tunnel birds scatters, alerting Nike above! You lose the opportunity for a stealth ambush (+0)."
            
    hide tunnel
    call victory_column_climax


# =========================================================================
# THE CLIMAX & BUFF TALLY (NIKE DC 30)
# =========================================================================
label victory_column_climax:
    scene bg_victory_column with fade
    show victory at truecenter
    play music "audio/bgm_final_boss.mp3"
    
    "You burst out of the tunnel at the base of the massive Victory Column!"
    "High above on her golden pillar, Nike stands tall, her spear radiating blinding celestial power!"

    # --- CALCULATE TOTAL MODIFIERS ---
    $ total_modifier = 0

    "As you draw your sword, the power of your journey surges through you:"

    # Default knowledge from translated dictionary
    $ total_modifier += 5
    "📖 **Bavarian Knowledge (+5):** Armed with translations from the ancient texts, you spot the vulnerable rune etched at the joint of her golden wings!"

    if forest_blessing:
        $ total_modifier += 5
        "🌊 **Blessing of the Forest (+5):** Ancient spring water magic wraps around you, shielding your mind from Nike's blinding radiance!"

    if bard_blessing:
        $ total_modifier += 5
        "🎵 **Bard's Blessing (+5):** A lingering heroic rhythm echoes in your pulse, steadying your hand and sharpening your focus!"

    if lion_companion:
        $ total_modifier += 5
        "🦁 **Lion Companion (+5):** Your spectral lion companion prowls at your side, letting out a roar that draws Nike's celestial gaze away from you!"

    if stealth_buff > 0:
        $ total_modifier += 5
        "🥷 **Shadow Ambush (+5):** Your silent approach through the tunnel gives you the element of surprise!"

    if active_curses > 0:
        $ total_modifier -= active_curses
        "💀 **Active Curses (-[active_curses]):** The lingering weight of your past failures pulls at your limbs!"

    # =========================================================================
    # GA SPEAR THROW PERFORMANCE & FINAL PHYSICAL d20 ROLL (DC 30)
    # =========================================================================
    nike "MORTAL! YOU DARE STAND BENEATH MY COLUMN OF VICTORY?"
    "You raise Bismarck's sword, preparing to hurl it toward the sky to shatter her golden perch!"

    sys "⚔️ GA PERFORMANCE CHECK: The player must physically mime throwing their sword/spear straight up at the statue with a dramatic battle cry!"

    menu:
        "Guardian Angel Judge: Majestic spear throw & epic battle cry! (+5 Performance Bonus)":
            $ total_modifier += 5
            "Your form is flawless as you hurl the blade into the heavens!"

        "Guardian Angel Judge: Standard or weak throw! (+0 Performance Bonus)":
            "You launch the blade skyward with all the strength you can muster!"

    # Display Total Modifiers to Player
    "Your current total Attack Modifier is: **+[total_modifier]**"
    sys "🎲 PHYSICAL ROLL: Roll a d20! Add your total modifier (+[total_modifier]). Target DC to defeat Nike is 30."

    menu:
        "🎲 Total d20 Roll + Modifiers equaled 30 or HIGHER (CRITICAL HIT!)":
            play sound "audio/nike_shatter.mp3"
            "**CRITICAL HIT!**"
            "Bismarck's blade streaks through the air like a bolt of lightning, striking the core of Nike's golden pedestal!"
            "With a deafening crack, her divine shield shatters and Nike tumbles from her high column, crashing onto the stone courtyard below!"
            call finish_or_spare

        "🎲 Total d20 Roll + Modifiers was LESS than 30 (MISSED)":
            play sound "audio/attack_fail.mp3"
            "Your blade grazes her divine armor, but her holy aura deflects the blow!"
            "Nike's blinding light washes over you, forcing a temporary retreat... (Try gathering remaining blessings or making a more epic throw!)"
            call victory_column_climax


# =========================================================================
# FINAL MORAL CHOICE: FINISH HER OR SPARE HER
# =========================================================================
label finish_or_spare:
    play music "audio/bgm_climax_decision.mp3"
    
    "Nike lies weakened upon the cobblestones, her golden armor cracked and her spear broken."
    nike "You... a mere mortal... have defeated victory itself..."
    
    "You step forward, picking up Bismarck's sword. The realm awaits your final decision."

    menu:
        "⚔️ Finish Her: Strike down the goddess and rid Tiergarten of her tyrant rule forever!":
            play sound "audio/sword_strike.mp3"
            "You deliver the final blow. Nike dissolves into a brilliant burst of golden starlight, dispersing harmlessly across the canopy of Tiergarten."
            "The oppressive weight over Berlin vanishes instantly. You stand as the undisputed conqueror of the realm."
            call game_ending_home

        "🕊️ Spare Her: Offer your hand and show mercy to the fallen goddess.":
            play sound "audio/magic_chime.mp3"
            "You lower your blade and extend a hand."
            "Nike gazes at you in shock, her harsh expression softening into awe."
            nike "Mercy... a true virtue greater than victory."
            "She bows her head in respect, swearing to protect Tiergarten as a peaceful guardian rather than a tyrant."
            call game_ending_home


label game_ending_home:
    play music "audio/bgm_victory_fanfare.mp3"
    
    "A glowing dimensional portal opens at the base of the tower, humming with sweet, familiar air."
    "With your quest complete, you step through the rift, returning home as a true hero of the realm."

    "{b}THE END — THANK YOU FOR PLAYING!{/b}"
    return