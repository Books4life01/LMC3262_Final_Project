## Options File - Game Settings and Configurations

## The name of the game, used in window title.
define config.name = _("Acoustic Echoes")
define gui.show_name = True

## The version of the game.
define config.version = "1.0.0"

## Build directory name.
define build.name = "AcousticEchoes"

## Audio configurations.
# Standard Ren'Py channels: music (looping), sound (one-shot), voice (one-shot, voice override)
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Register custom audio channels.
init python:
    # We register a custom 'ambience' channel that loops by default and uses the 'sfx' mixer.
    # This allows playing environmental background loops separate from the main background music.
    renpy.music.register_channel("ambience", mixer="sfx", loop=True)

## Transitions.
# Used when entering or exiting game menus.
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = fade
define config.end_game_transition = fade

## Save Game Settings.
# The unique directory name where save files will be stored.
define config.save_directory = "AcousticEchoes-Template-Save"

## Window Icon (Optional - will fall back to default if not defined).
# define config.window_icon = "gui/window_icon.png"
