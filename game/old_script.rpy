# ## Main Game Script - Branching Story & Audio Integration Demo

# # Declare characters. 
# # Custom color properties determine the display color of their names in the dialogue box.
# define p = Character("Player", color="#38bdf8")
# define g = Character("Guardian Echo", color="#c084fc")
# define n = Character(None, kind=nvl) # NVL narrator fallback if needed

# # Initialize variables to track game state
# default has_key = False
# default clues_found = 0

# # The game starts here!
# label start:

#     # 1. Start Ambient looping track
#     # The 'ambience' channel is our custom channel configured in options.rpy. 
#     # Since loop is True by default for it, it will loop indefinitely.
#     play sound "audio/ambience_drip.mp3"

#     # 2. Start Background Music (BGM)
#     # The 'music' channel is a standard Ren'Py looping channel.
#     play sound "audio/bgm_mystery.mp3"

#     # Begin Story
#     scene black with fade
    
#     "You wake up on a cold stone floor. The air is damp, heavy, and smells of old iron."
#     "In the distance, you hear the rhythmic sound of water dripping from the ceiling..."
    
#     p "Ugh... my head. Where am I? It's pitch black."
    
#     # Showcase sound effect (one-shot SFX)
#     # The 'sound' channel is the standard Ren'Py one-shot channel.
#     play sound "audio/sfx_pickup.mp3"
#     "You feel around the floor and find a heavy metal flashlight. You click it on."
    
#     "A beam of light cuts through the darkness, revealing a branching stone corridor."
    
#     label corridor:
#         scene black with dissolve
#         "The dripping noise grows slightly louder here. You stand at a fork in the cave."

#         menu:
#             "Which direction will you explore?"

#             "Explore the Left Tunnel (Flooded Cavern)":
#                 jump flooded_cavern

#             "Explore the Right Tunnel (Iron Gate)":
#                 jump iron_gate

#             "Examine your surroundings closely":
#                 jump search_area


# label flooded_cavern:
#     "You walk down the damp left tunnel. Water pools around your boots."
    
#     # We increase the volume of the ambient dripping sound as we get closer to water
#     queue ambience "audio/ambience_drip.mp3"
#     "The cavern opens up to a subterranean lake. The water looks black and perfectly still."
    
#     if not has_key:
#         "Something glints at the bottom of a shallow pool near the edge."
        
#         menu:
#             "Reach into the icy water":
#                 # Play a pickup sound effect
#                 play sound "audio/sfx_pickup.mp3"
#                 $ has_key = True
#                 "You plunge your hand into the freezing water and retrieve a heavy brass key."
#                 p "Brr! That was cold. But this key looks important."
#                 jump corridor
            
#             "Leave it alone":
#                 "You decide not to risk reaching into the mysterious pool."
#                 jump corridor
#     else:
#         "The lake remains quiet and dark. You've already retrieved the brass key from here."
#         p "Nothing else of interest in the water."
#         jump corridor


# label iron_gate:
#     "You approach the end of the right tunnel, where a rusted iron gate blocks the path."
    
#     if not has_key:
#         "You shake the gate, but it is locked tight."
#         p "It's locked. It looks like it needs a heavy brass key."
        
#         # We can fade out the music to highlight the player's isolation
#         stop music
#         "Without the key, there is nothing else you can do here."
        
#         # Fade music back in as we prepare to return
#         play music "audio/bgm_mystery.mp3"
#         jump corridor
#     else:
#         "You insert the brass key into the rusted gate lock."
        
#         # Play the gate creak sound effect
#         play sound "audio/sfx_door.mp3"
#         "With a heavy metallic groan, the gate swings open."
        
#         jump chamber_of_echoes


# label search_area:
#     "You sweep your flashlight over the stone walls and inspect the debris."
#     $ clues_found += 1
    
#     if clues_found == 1:
#         "You discover strange carvings on the wall: a drawing of a gate and a key submerged in water."
#         p "Ah, this must be a clue for how to proceed!"
#     elif clues_found == 2:
#         "You notice a faint breeze coming from the right. The air smells slightly cleaner there."
#     else:
#         "You find nothing else of value in the dust."
        
#     jump corridor


# label chamber_of_echoes:
#     # Transition to a new area: fade out the dripping noise and play a new scene
#     stop ambience
#     stop music
    
#     scene black with fade
#     "You step through the gate into a massive, cavernous cathedral of stone."
    
#     # Play victory/chime sound
#     play sound "audio/sfx_pickup.mp3"
    
#     # Introduce a new character with their own dialogue
#     g "Welcome, traveler. You have navigated the acoustic shadows of this place."
    
#     g "Many enter, but few listen closely enough to find the key."
    
#     p "Who are you? Can you show me the way out?"
    
#     g "The path to the surface is open behind me. Go, and remember to trust what you hear."
    
#     "A shaft of warm sunlight shines down from a opening in the distance."
    
#     "You walk toward the light, feeling the warm wind on your face."
    
#     # End scene: fade everything out
#     stop music
#     "You have escaped the cave."
    
#     "CONGRATULATIONS - You completed the demo adventure!"
    
#     return
