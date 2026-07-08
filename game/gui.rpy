## init offset statement ensures this runs before screens or script files
init offset = -2

## Calling gui.init resets style variables and sets base dimensions.
init python:
    gui.init(1280, 720)

## Design System Tokens (Aesthetic Modern Dark Theme with Neon Accents)
# Harmonious Dark Theme Colors
define gui.accent_color = "#00e5ff"       # Neon cyan for highlights
define gui.idle_color = "#99aabb"         # Slate gray for normal text/buttons
define gui.idle_small_color = "#778899"   # Muted small text
define gui.hover_color = "#ffffff"        # Bright white for interactive hover
define gui.selected_color = "#00e5ff"     # Neon cyan for selected tabs
define gui.insensitive_color = "#445566"  # Dark slate for disabled items
define gui.text_color = "#f0f4f8"         # Crisp light blue-gray for text
define gui.interface_text_color = "#e2e8f0"# Clean UI text color
define gui.background_color = "#0a0f1d"    # Deep space black/dark blue background
define gui.panel_color = "#111827"        # Dark grey card background

# Font configuration
# Ren'Py bundles "DejaVuSans.ttf" as default, which is clean, readable, and always present.
define gui.text_font = "DejaVuSans.ttf"
define gui.name_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

# Sizes
define gui.text_size = 24
define gui.name_text_size = 30
define gui.interface_text_size = 20
define gui.title_text_size = 40

# Dialogue Box Positioning
define gui.textbox_height = 180
define gui.textbox_yalign = 1.0

# Dialogue Text positioning within the textbox
define gui.dialogue_xpos = 260
define gui.dialogue_ypos = 50
define gui.dialogue_width = 760
define gui.dialogue_text_xalign = 0.0

# Character Name positioning
define gui.name_xpos = 260
define gui.name_ypos = 15
define gui.name_xalign = 0.0

# Choice menu options positioning
define gui.choice_spacing = 15

# Main Menu Button layout spacing
define gui.navigation_spacing = 15
