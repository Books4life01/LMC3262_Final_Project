# Final Boss modifiers
default lion_companion = False
default forest_blessing = False
default cloak_obtained = False
default has_bard_blessing = False

# --- CURSE TRACKING ---
default active_curse = "None"
default active_curses = 0  # Tracks total number of curses accumulated for your final boss modifier!


label start:
    # call lion_bridge_encounter
    # call after_lions
    # call start_troll_encounter
    # call after_trolls
    # call nitwit_start
    # call after_nitwit
    # call bismarck_intro
    # call after_bismarck
    call victory_tunnel_start


# =========================================================================
# REUSABLE PHYSICAL CURSE SELECTION SYSTEM
# =========================================================================

label trigger_curse:
    sys "The curse strikes! Turn to your real-life Guardian Angel. They must choose one physical curse from the menu for you to perform!"
    
    menu:
        "Guardian Angel: Choose 'The Hobbling Goblin' (Hop on one foot)":
            $ active_curse = "Hobbling Goblin"
            $ active_curses += 1
            "The curse takes hold! Your leg feels incredibly heavy. You must hop on one foot whenever you are walking to the next location."
            
        "Guardian Angel: Choose 'The Stone-Arm Hex' (Keep one arm behind back)":
            $ active_curse = "Stone-Arm"
            $ active_curses += 1
            "The curse takes hold! Your dominant arm stiffens and turns to solid oak. You must keep it tucked behind your back for the rest of this journey."
            
        "Guardian Angel: Choose 'The Tongue-Tie Plague' (Whispers/grunts only)":
            $ active_curse = "Tongue-Tie"
            $ active_curses += 1
            "The curse takes hold! Your vocal cords lock up. You can only whisper or grunt until the next encounter."
            
        "Guardian Angel: Choose 'The Paralyzed Glance' (Move torso, not neck)":
            $ active_curse = "Paralyzed Glance"
            $ active_curses += 1
            "The curse takes hold! Your neck freezes completely solid. If you want to look around, you must rotate your entire upper body."

    "Your active physical penalty is now **[active_curse]**. Total accumulated curses: **[active_curses]**."
            
    return