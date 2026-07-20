# =========================================================================
# REUSABLE INTERMISSION / TRAVEL NODE
# =========================================================================

label travel_intermission(destination_name, custom_text="You press onward down the winding forest path."):
    scene black with fade
    play sound "audio/footsteps_gravel.ogg"
    
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
    "With the lions on the bridge dealt with, you leave the golden structure behind and dust off your boots."
    
    call travel_intermission("The Halfling Sandbox", "You follow the woodland path toward a commotion near a wooden playground in the distance.")

    jump start_troll_encounter


# -------------------------------------------------------------------------
# ROUTE 2: AFTER TROLLS (Node 2) -> STONE PILLAR / NITWIT (Node 3)
# -------------------------------------------------------------------------
label after_trolls:
    "With the halfling outpost saved and the trolls pacified, you wave goodbye to the little folk and venture deeper into the woods."
    
    call travel_intermission("The Stone Pillar", "You trek deep into the canopy, dodging overgrown roots and mossy stones.")

    jump nitwit_start


# -------------------------------------------------------------------------
# ROUTE 3: AFTER NITWIT (Node 3) -> BISMARCK MONUMENT (Node 4)
# -------------------------------------------------------------------------
label after_nitwit:
    "Leaving the ancient pillar behind, you push through the thick brush toward the edge of the forest clearing."
    
    call travel_intermission("The Bismarck Monument", "A wide stone plaza begins to emerge through the treeline as grand monuments appear ahead.")

    jump bismarck_intro


# -------------------------------------------------------------------------
# ROUTE 4: FINAL DEPARTURE / END OF CHAPTER
# -------------------------------------------------------------------------
label after_bismarck:
    "With Siegfried's legendary blade in hand and the trials completed, you turn away from the grand monument."
    
    call travel_intermission("The Sanctuary Gates", "With your task complete, you make your victorious return trip back to the sanctuary.")

    "You step back through the sanctuary threshold. Your journey in this realm is complete!"
    return