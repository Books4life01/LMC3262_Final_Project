define king = Character("King")
define atlas = Character("Atlas")
define sibyl = Character("Sibyl")
define warrior = Character("Warrior")
define siegfried = Character("Siegfried")

# Defaults
default completed_atlas = False
default completed_sibyl = False
default completed_warrior = False
default has_lion = False

# Images
image atlas_img = 'images/atlas.jpeg'
image sibyl_img = 'images/sibyl.jpeg'
image siegfried_img = 'images/sibyl.jpeg'
image warrior_img = 'images/warrior.jpeg'
image bismarck_img = 'images/bismarck.jpeg'

label bismarck_intro:
    play sound "audio/approachbismark.mp3"
    "As you exit the forest, you are greeted by an ancient king guarded by four extremely powerful human-like beings."
    "Go to the front of the statue and face Bismarck."
    jump bismarck_king

label bismarck_king:
    scene expression "#332211" # Adjust or add your background image here
    show bismarck_img at truecenter:
        zoom 0.25
    play sound "audio/kingwelcome.mp3"
    king "Greetings, traveler. I have been observing your journey through this forest from atop this tower. You truly might be the one to free these lands from accursed Victory. But I have one more task for you to prove your worth."
    play sound "audio/kingtrials.mp3"
    king "I am surrounded by four guardians. The three in front of me will each present you with a test. The smith behind me is the keeper of the Champions Blade, but you may only speak to him once you have proven yourself worthy by completing all three trials."

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


# -------------------------------------------------------------------------
# TRIAL 1: ATLAS
# -------------------------------------------------------------------------

label atlas_trial:
    show atlas_img at truecenter:
        zoom 0.25
    play sound "audio/atlasintro.mp3"
    atlas "I have held the world on my back since the dawn of time."
    play sound "audio/atlasburdens.mp3"
    atlas "Hold the world for 15 seconds, and prove you possess the strength to bear impossible burdens."
    sys "Stand in Atlas's position for 15 seconds. Your Guardian Angel will time you."

    menu:
        "Guardian Angel: Did the player hold the pose for 15 seconds?":
            play sound "audio/atlaswin.mp3"
            atlas "You have proven your strength. You may move on to the next trial."
            $ completed_atlas = True
            jump bismarck_king
            
        "Guardian Angel: The player failed or gave up.":
            play sound "audio/narratoratlaslose.mp3"
            "Your arms begin to shake as the weight becomes unbearable."
            play sound "audio/atlaslose.mp3"
            atlas "The world is heavier than you imagined. Gather your strength, and try again."
            jump atlas_trial


# -------------------------------------------------------------------------
# TRIAL 2: SIBYL
# -------------------------------------------------------------------------

label sibyl_trial:
    show sibyl_img at truecenter:
        zoom 0.25
    play sound "audio/siyblquestion.mp3"
    sibyl "I test your intelligence. Since what year have we been standing here?"
    play sound "audio/narratordictionary.mp3"
    "Your dictionary begins to glow. The inscriptions on the monument unscramble. Study the text on the front and back of the monument and give the Guardian Angel your answer."

    # Correct answer is 1901
    menu:
        "Guardian Angel: Did the player give the correct answer?":
            menu:
                "Yes":
                    play sound "audio/siyblcorrect.mp3"
                    sibyl "Correct! You may move on to the next trial."
                    $ completed_sibyl = True
                    jump bismarck_king
                    
                "No":
                    play sound "audio/siyblincorrect.mp3"
                    sibyl "Incorrect! Try again."
                    jump sibyl_trial


# -------------------------------------------------------------------------
# TRIAL 3: WARRIOR
# -------------------------------------------------------------------------

label warrior_trial:
    show warrior_img at truecenter:
        zoom 0.25
    play sound "audio/warriorchallenge.mp3"
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
    play sound "audio/lionroar.mp3"
    "The lion roars, scaring away the panther."
    $ completed_warrior = True
    jump bismarck_king

label fight_yourself:
    play sound "audio/narratorfists.mp3"
    "You clench your fists."
    menu:
        "Tackle the beast head-on":
            jump tackle
        "Make a slingshot":
            jump slingshot

label tackle:
    play sound "audio/panthercharge.mp3"
    "You charge at the panther, but it knocks you back. It's too strong to fight with your bare hands."
    jump slingshot

label slingshot:
    play sound "audio/narratorslingshot.mp3"
    "You decide to build a slingshot, but you need a stick and a pebble. Search the nearby woods."
    play sound "audio/narratorreturn.mp3"
    "Once you've collected the materials, return."
    jump fight_w_slingshot

label fight_w_slingshot:
    play sound "audio/pantherclimax.mp3"
    "The panther attacks again. Luckily, you now have a slingshot. Hold the pebble in front of the stick to fire it."
    "You aim true and strike the panther, forcing it to flee!"
    $ completed_warrior = True
    jump bismarck_king


# -------------------------------------------------------------------------
# CONCLUSION: SIEGFRIED & THE SWORD
# -------------------------------------------------------------------------

label sword:
    show siegfried_img at truecenter:
        zoom 0.25
    play sound "audio/narratorsword.mp3"
    "Having completed all the trials, you approach the legendary sword."
    play sound "audio/ornnworthy.mp3"
    siegfried "You have proven yourself worthy. But one final test remains."
    play sound "audio/ornnchallenge.mp3"
    siegfried "Roll a physical d20. If you get 17 or higher, you shall receive not only the Champions Blade, but also the infamous Unseen Cloak which graces my shoulders."
    
    menu:
        "Roll is 17 or higher":
            play sound "audio/swordaura.mp3"
            "As you grasp the sword's hilt, you feel its powerful aura."
            play sound "audio/cape.mp3"
            "Siegfried also drapes the enchanted cloak across your shoulders."
            $ cloak_obtained = True

            
        "Roll is under 17":
            play sound "audio/swordaura.mp3"
            "As you grasp the sword's hilt, you feel its powerful aura."
    play sound "audio/narratortunnels.mp3"
    "Brave soldier, before you leave take heed. You must approach the tyrant unseen before you launch your attack. There is a series of underground tunnels that should lead you to its perch."
    play sound "audio/narratorluck.mp3"
    "Your gaurdian angel should know the way and guide you. Best of luck!"
    return