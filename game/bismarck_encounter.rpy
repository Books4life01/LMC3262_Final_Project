define king = Character("King")
define atlas = Character("Atlas")
define sibyl = Character("Sibyl")
define warrior = Character("Warrior")
define siegfried = Character("Siegfried")

# defaults
default completed_atlas = False
default completed_sibyl = False
default completed_warrior = False
default has_lion = False

label bismarck_intro:
    "As you exit the forest, you are greeted by an ancient king guarded by four extremely powerful human-like beings."
    "Go to the front of the statue and face Bismarck."
    jump bismarck_king

label bismarck_king:
    king "Greetings, traveler. I have been observing your journey through this forest from atop this tower. You have done well so far. But I have one more task for you to prove your worth."
    king "I am surrounded by four guardians. The three in front of me will each present you with a test. The smith behind me has forged a magical sword that will be the key back to your world. But only speak to him once you have proven yourself worthy by completing all three trials."

    menu:
        "Speak to Atlas" if not completed_atlas:
            jump atlas_trial
        "Speak to the Sibyl" if not completed_sibyl:
            jump sibyl_trial
        "Speak to the Warrior" if not completed_warrior:
            jump warrior_trial
        "Collect the sword" if completed_atlas and completed_sibyl and completed_warrior:
            jump sword
        "Leave":
            return

label atlas_trial:
    atlas "I have held the world on my back since the dawn of time."
    atlas "Hold the world for 15 seconds, and prove you possess the strength to bear impossible burdens."
    "Stand in Atlas's position for 15 seconds. Your Guardian Angel will time you."

    menu:
        "Guardian Angel: Did the player hold the pose for 15 seconds?":
            atlas "You have proven your strength. You may move on to the next trial."
            $ completed_atlas = True
            
        "Guardian Angel: The player failed or gave up.":
            "Your arms begin to shake as the weight becomes unbearable."
            atlas "The world is heavier than you imagined. Gather your strength, and try again."
            jump atlas_trial

    jump bismarck_king

label sibyl_trial:
    sibyl "I test your intelligence. Since what year have we been standing here?"
    "Your dictionary begins to glow. The inscriptions on the monument unscramble. Study the text on the front and back of the monument and give the Guardian Angel your answer."

    # correct answer is 1901
    menu:
        "Guardian Angel: Did the player give the correct answer?"
        "Yes":
            sibyl "Correct. You may move on to the next trial."
            $ completed_sibyl = True
            
        "No":
            sibyl "Incorrect! Try again."
            jump sibyl_trial

    $ completed_sibyl=True
    jump bismarck_king

label warrior_trial:
    warrior "You must confront this beast to pass."
    if has_lion:
        menu:
            "Summon your lion":
                jump summon_lion
            "Fight the panther yourself":
                jump fight_yourself
    else:
        jump fight_yourself

label summon_lion:
    "The lion roars, scaring away the panther."
    $ completed_warrior=True
    jump bismarck_king

label fight_yourself:
    "You clench your fists."
    menu:
        "Tackle the beast head-on":
            jump tackle
        "Make a slingshot":
            jump slingshot

label tackle:
    "You charge at the panther, but it knocks you back. It's too strong to fight with your bare hands."
    jump slingshot

label slingshot:
    "You decide to build a slingshot, but you need a stick and a pebble. Search the nearby woods."
    "Once you've collected the materials, return."
    jump fight_w_slingshot

label fight_w_slingshot:
    "The panther attacks again. Luckily, you now have a slingshot. Hold the pebble in front of the stick to fire it."
    $ completed_warrior=True
    jump bismarck_king

label sword:
    "Having completed all the trials, you approach the legendary sword."
    siegfried "You have proven yourself worthy. But one final test remains."
    siegfried "Roll a physical d20. If you get 17 or higher, you shall receive not only my sword, but also my enchanted cloak."
    menu:
        "Roll is 17 or higher":
            "As you grasp the sword's hilt, you feel its powerful aura."
            "Siegfried also drapes the enchanted cloak across your shoulders."
        "Roll is under 17":
            "As you grasp the sword's hilt, you feel its powerful aura."
    return
