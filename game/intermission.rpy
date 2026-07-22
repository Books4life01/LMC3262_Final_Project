# =========================================================================
# REUSABLE INTERMISSION / TRAVEL NODE
# =========================================================================

label travel_intermission(destination_name, custom_text="You press onward down the winding forest path."):
    scene black with fade
    play sound "audio/footsteps_gravel.ogg"
    show traveling at truecenter
    
    # Display the custom travel description
    "[custom_text]"
    
    # Check if the player is currently carrying a physical curse
    if active_curse != "None":
        "Your trek is slow and awkward as you struggle under {b}[active_curse]{/b}..."
    else:
        "The journey is pleasant, and the fresh air keeps your spirits high."

    "Your next objective is: {b}[destination_name]{/b}."
    
    # ---------------------------------------------------------------------
    # PHYSICAL ARRIVAL CONFIRMATION
    # ---------------------------------------------------------------------
    sys "Walk to [destination_name] in real life! Once you have confirmed you are in the right place with your Guardian Angel, click below to confirm your arrival."

    menu:
        "📍 I have arrived at [destination_name]!":
            "You have arrived at [destination_name]! Take a breath and prepare yourself..."
            $ renpy.pause(0.5)
            return


# =========================================================================
# GAME SEQUENCE: LIONS -> TROLLS -> NITWIT -> BISMARCK
# =========================================================================

# -------------------------------------------------------------------------
# ROUTE 1: AFTER LIONS (Node 1) -> HALFLING SANDBOX / TROLLS (Node 2)
# -------------------------------------------------------------------------
label after_lions:
    "With the lions on the bridge dealt with, you leave the golden structure behind and dust off your boots. Their talk of Nike was troubling, and you feel your purpose in this land is to free this land from Nike's rule."
    "Your gaurdian angel reccomends you travel North to learn more about the land before you confront the winged monarch."

    call travel_intermission("The Halfling Outpost", "You follow the woodland path north filled with determination towards a know Halfling Outpost")
    return


# -------------------------------------------------------------------------
# ROUTE 2: AFTER TROLLS (Node 2) -> STONE PILLAR / NITWIT (Node 3)
# -------------------------------------------------------------------------
label after_trolls:
    "With the halfling outpost saved and the trolls pacified, you wave goodbye to the little folk and venture deeper into the woods."
    "Your gaurdian angel mentions an ancient text carved in stone, that may hold the secret to defeating Victory herself."
    
    call travel_intermission("The Stone Pillar", "You trek deep into the canopy, dodging overgrown roots and mossy stones.")
    return


# -------------------------------------------------------------------------
# ROUTE 3: AFTER NITWIT (Node 3) -> BISMARCK MONUMENT (Node 4)
# -------------------------------------------------------------------------
label after_nitwit:
    "Your gaurdian angel mentions the sword of victory is held by the King, who holds court with his attendants not to far ahead"
    "Leaving the ancient pillar behind, you push through the thick brush toward the edge of the forest clearing."
    
    call travel_intermission("The Bismarck Monument", "A wide stone plaza begins to emerge through the treeline as grand monuments appear ahead.")
    return


# -------------------------------------------------------------------------
# ROUTE 4: FINAL DEPARTURE / END OF CHAPTER
# -------------------------------------------------------------------------
label after_bismarck:
    "With the Champions Blade in hand and the trials completed, you turn towards the final challenge. Onwards, to Victory herself"
    
    call travel_intermission("Nike's Perch", "You make your way to the hidden tunnels")

    return