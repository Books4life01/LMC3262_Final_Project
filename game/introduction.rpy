# --- Character Definitions ---
define nike = Character("Golden Angel Nike", color="#FFD700")
define sys = Character("System", color="#888888")

# --- Variables ---
default intro_option_one = False
default intro_option_two = False

label intro_forest_encounter:

    scene expression "#1a2419"
    scene tiergartenintro 
    play sound "audio/narratorintro1.mp3"
    "You wake up in the forest, dusting yourself off you realize you are no longer in Baldur's Gate"
    "You ask yourself, How did I get here? But No answer comes to light."

    menu intro_wakeup_menu:

        "Inspect yourself for injuries." if not intro_option_one:
            play sound "audio/introhealers.mp3"
            "You try to check yourself for injuries, but barbarians arent really the best healers..."
            $ intro_option_one = True
            jump intro_wakeup_menu

        "Check your surroundings." if not intro_option_two:
            sys "You look around the local area, desperately trying to find a portal or door out of here, but nothing shows."
            $ intro_option_two = True
            jump intro_wakeup_menu

        "How do I get home?":
            jump intro_statue_revelation


label intro_statue_revelation:
    play sound "audio/foreign.mp3"
    "Your vision blurs, as your mind gets controlled by a foreign entity..."
    play sound "audio/foreignvision.mp3"
    "The foreign entity, shows you a vision."
    scene black 
    show nikevision at truecenter:
        zoom 0.6



    nike "I AM NIKE, CONQUEROR OF HUMANITY AND GODDESS OF VICTORY"

    play sound "audio/fightvision.mp3"
    "You try to fight off her influence, but to no avail."
    jump fight_for_mind

label fight_for_mind:
    nike "IF YOU WISH TO GO HOME TO BALDUR'S GATE, YOU MUST GET THROUGH ME."

    sys "Cut her influence from your brain. DC: 10"
    menu:
        "Success >=10":
            play sound "audio/intromission.mp3"
            "You break her mental hold on you. As you pick yourself off the ground, you curse her name. Thankfully however, your mission becomes clear. Defeat Nike and return home to baldur's gate."
            jump transition_to_end
        "Failure <10":
            play sound "audio/introfail.mp3"
            "Your mind caves under the pressure, and you are unable to break free"
            jump fight_for_mind

label transition_to_end:
    hide nikevision
    scene tiergartenintro 
    play sound "audio/guardianmeeting.mp3"
    "A shadow approaches you from beyond the bushes and introduces himself to you as your guardian angel"
    sys "Your guardian angel will be your guide as you complete quests to defeat the angel nike, tell him when you are ready to proceed with the next challenge."
    menu:
        "I am ready":
            jump lion_bridge_encounter  # Transition to the next label