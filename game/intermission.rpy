# # =========================================================================
# # REUSABLE INTERMISSION / TRAVEL NODE
# # =========================================================================

# label travel_intermission(destination_name, custom_text="You press onward down the winding forest path."):
#     scene black with fade
#     play sound "audio/footsteps_gravel.ogg"
    
#     # Display the custom travel description
#     "[custom_text]"
    
#     # Check if the player is currently carrying a physical curse
#     if active_curse != "None":
#         "Your trek is slow and awkward as you struggle under {b}[active_curse]{/b}..."
#     else:
#         "The journey is pleasant, and the fresh air keeps your spirits high."

#     "Your next objective is: {b}[destination_name]{/b}."
    
#     # ---------------------------------------------------------------------
#     # PHYSICAL ARRIVAL CONFIRMATION
#     # ---------------------------------------------------------------------
#     sys "Walk to [destination_name] in real life! Once upi have confirmed you are in the right palce with your Gaurdian Angle, click below to confirm your arrival."

#     menu:
#         "📍 [I have arrived at [destination_name]!]":
#             "You have arrived at [destination_name]! Take a breath and prepare yourself..."
#             $ renpy.pause(0.5)
#             return

# label after_trolls:
#     "With the halfling outpost saved adn the trolsl pacified, you dust the woodchips off your boots."
    
#     # Calls the intermission node
#     call travel_intermission("The Stone Pillar", "You trek deep into the canopy, dodging overgrown roots and mossy stones.") pass

#     # Execution only resumes after they physically walk there and click the button!
#     jump nitwit_start