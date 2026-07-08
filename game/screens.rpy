## Screens File - Defines User Interface layouts and styles

init offset = -1

################################################################################
## Styles definitions for clean UI layouts
################################################################################
style gui_text:
    font gui.interface_text_font
    color gui.text_color
    size gui.interface_text_size

style gui_button:
    padding (10, 10, 10, 10)
    background Solid("#1e293b")
    hover_background Solid("#334155")

style gui_button_text:
    font gui.interface_text_font
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    size gui.interface_text_size
    xalign 0.5

style slider:
    ysize 12
    xsize 250
    left_bar Solid(gui.accent_color)
    right_bar Solid("#1e293b")
    thumb Solid("#ffffff")
    thumb_shadow None
    thumb_offset 6

################################################################################
## Say screen (Dialogue UI)
################################################################################
screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Solid("#0f172aee") # Semi-transparent dark slate dialogue window
        padding (30, 20, 30, 20)
        xalign 0.5
        yalign 0.95
        xsize 1000
        ysize 160

        vbox:
            spacing 10
            if who is not None:
                text who:
                    id "who"
                    font gui.name_font
                    color gui.accent_color
                    size gui.name_text_size
                    bold True

            text what:
                id "what"
                font gui.text_font
                color gui.text_color
                size gui.text_size

    # Add quick menu access overlay
    use quick_menu


################################################################################
## Choice screen (Menus / Decisions)
################################################################################
screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15
        xsize 600

        for i in items:
            button:
                action i.action
                background Solid("#0f172aee")
                hover_background Solid("#0284c7")
                padding (15, 12)
                xfill True
                text i.caption:
                    color gui.text_color
                    hover_color "#ffffff"
                    size gui.text_size
                    xalign 0.5


################################################################################
## Quick Menu screen (Dialogue overlay helpers)
################################################################################
screen quick_menu():
    hbox:
        xalign 0.5
        yalign 0.99
        spacing 20
        
        textbutton _("Back") action Rollback() text_size 14
        textbutton _("History") action ShowMenu("history") text_size 14
        textbutton _("Skip") action Skip() alternate Skip(fast=True) text_size 14
        textbutton _("Auto") action Preference("auto-forward", "toggle") text_size 14
        textbutton _("Save") action ShowMenu("save") text_size 14
        textbutton _("Q.Save") action QuickSave() text_size 14
        textbutton _("Load") action ShowMenu("load") text_size 14
        textbutton _("Prefs") action ShowMenu("preferences") text_size 14


################################################################################
## Main Menu screen
################################################################################
screen main_menu():
    tag menu

    # Dark background fill
    add Solid(gui.background_color)

    # Core menu contents wrapper
    frame:
        background Solid("#0f172acc")
        padding (40, 40)
        xsize 400
        yfill True
        xalign 0.08
        
        vbox:
            yalign 0.5
            spacing 30
            
            # Title Group
            vbox:
                spacing 5
                text "[config.name]":
                    size gui.title_text_size
                    color gui.accent_color
                    bold True
                text "An Audio & Text Adventure Template":
                    size 14
                    color gui.idle_small_color

            # Navigation buttons
            vbox:
                spacing 12
                xfill True
                style_prefix "navigation"
                
                textbutton _("Start Game") action Start() style "gui_button"
                textbutton _("Load Game") action ShowMenu("load") style "gui_button"
                textbutton _("Preferences") action ShowMenu("preferences") style "gui_button"
                textbutton _("About") action ShowMenu("about") style "gui_button"
                textbutton _("Quit") action Quit(confirm=True) style "gui_button"


################################################################################
## Game Menu navigation (Backdrop wrapper for menus)
################################################################################
screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu
    
    add Solid(gui.background_color)

    # Header Top Bar
    frame:
        background Solid("#1e293b")
        xfill True
        ysize 60
        yalign 0.0
        padding (20, 10)
        
        hbox:
            align (0.0, 0.5)
            spacing 20
            textbutton _("<- Back to Game") action Return() text_color gui.accent_color
            text "|":
                color gui.idle_small_color
            text title:
                size 24
                color "#ffffff"
                bold True

    # Main contents box
    frame:
        background Solid("#0f172acc")
        xsize 1100
        ysize 580
        align (0.5, 0.6)
        padding (30, 30)
        
        transclude


################################################################################
## Preferences/Settings screen (Audio adjustments are defined here!)
################################################################################
screen preferences():
    tag menu
    use game_menu(_("Preferences")):
        
        hbox:
            spacing 80
            xalign 0.5
            yalign 0.5
            
            # Left Column: Speeds & Toggles
            vbox:
                spacing 35
                
                vbox:
                    spacing 10
                    text _("Text Speed") style "gui_text" color gui.accent_color
                    bar value Preference("text speed") style "slider"

                vbox:
                    spacing 10
                    text _("Auto-Forward Time") style "gui_text" color gui.accent_color
                    bar value Preference("auto-forward time") style "slider"
                
                vbox:
                    spacing 10
                    text _("Skip Mode") style "gui_text" color gui.accent_color
                    hbox:
                        spacing 15
                        textbutton _("Unseen Text") action Preference("skip", "toggle") style "gui_button"
                        textbutton _("After Choices") action Preference("after choices", "toggle") style "gui_button"

            # Right Column: Audio Mixers (Shows off the volume bars)
            vbox:
                spacing 35
                
                vbox:
                    spacing 10
                    text _("Music Volume") style "gui_text" color gui.accent_color
                    bar value Preference("music volume") style "slider"

                vbox:
                    spacing 10
                    text _("SFX / Ambient Volume") style "gui_text" color gui.accent_color
                    bar value Preference("sound volume") style "slider"

                vbox:
                    spacing 10
                    text _("Voice Volume") style "gui_text" color gui.accent_color
                    bar value Preference("voice volume") style "slider"

                textbutton _("Mute All Audio") action Preference("all mute", "toggle") style "gui_button"


################################################################################
## About Screen
################################################################################
screen about():
    tag menu
    use game_menu(_("About")):
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            
            text "[config.name]":
                size 36
                color gui.accent_color
                bold True
                xalign 0.5

            text "Version [config.version]":
                size 18
                color gui.idle_small_color
                xalign 0.5

            text "Created manually as a template showcasing narrative branching and multi-channel audio controls (Music, SFX, and custom loops on the Ambient mixer channel).":
                size 18
                color gui.text_color
                justify True
                xsize 700
                xalign 0.5


################################################################################
## Save / Load slots
################################################################################
screen save():
    tag menu
    use game_menu(_("Save Game")):
        use file_slots(_("Save"))

screen load():
    tag menu
    use game_menu(_("Load Game")):
        use file_slots(_("Load"))

screen file_slots(title):
    grid 3 2:
        xalign 0.5
        yalign 0.5
        spacing 25
        
        for i in range(1, 7):
            button:
                action FileAction(i)
                xsize 300
                ysize 180
                background Solid("#1e293b")
                hover_background Solid("#0284c7")
                padding (15, 15)
                
                vbox:
                    spacing 10
                    xfill True
                    text "Slot [i]":
                        bold True
                        size 18
                        color gui.accent_color
                    
                    # File description details
                    text FileTime(i, empty=_("Empty Slot")):
                        size 14
                        color gui.idle_small_color
                    text FileSaveName(i):
                        size 14
                        color gui.text_color


################################################################################
## Confirm Action Prompt (e.g. Quitting, Overwriting)
################################################################################
screen confirm(message, yes_action, no_action):
    modal True
    tag menu
    
    add Solid("#020617bb") # Dark dims behind confirmation window

    frame:
        background Solid("#0f172a")
        padding (30, 30)
        xsize 500
        ysize 250
        align (0.5, 0.5)

        vbox:
            align (0.5, 0.5)
            spacing 35
            
            text message:
                size 20
                color "#ffffff"
                xalign 0.5
                justify True
                xsize 400

            hbox:
                spacing 40
                xalign 0.5
                textbutton _("Yes") action yes_action style "gui_button" xsize 120
                textbutton _("No") action no_action style "gui_button" xsize 120


################################################################################
## History log overlay
################################################################################
screen history():
    tag menu
    use game_menu(_("Dialogue History")):
        viewport:
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 15
                xsize 900
                for h in _history_list:
                    hbox:
                        spacing 20
                        if h.who:
                            text h.who:
                                size 18
                                color gui.accent_color
                                bold True
                                xsize 150
                        text h.what:
                            size 18
                            color gui.text_color
                            xsize 700


################################################################################
## Empty keymap and confirmation screens (required for fallback defaults)
################################################################################
screen nvl(dialogue, items=None):
    pass
