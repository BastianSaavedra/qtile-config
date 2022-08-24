from libqtile import widget, bar
from libqtile.config import  Screen

color_bar = "#282a36"
size_bar = 28
system_font = "Hack NF"
widget_font_size = 15
active_color = "#F1FFFF"
inactive_color = "#4C566A"
icon_size = 25
fg_color = "#ffffff"
bg_color = "#282a36"
dark_color = "#212121"
light_color = "#982428"
urgent_color = "#ff5555"
text1_color = "#EF5350"
update_color = "#bc0000"
red_interface = "wlo1" 
# group_color_1 = "#ff7f00" # Naranja
# group_color_2 = "#d600f7" # Rosa oscuro
# group_color_3 = "#007bff" # Azul
# group_color_4 = "#c60000" # Rojo
group_update = "#37383B"
group_color_1 = "#334148"
group_color_2 = "#4C566A"
group_color_3 = "#556A74"
group_color_4 = "#982428"



# funcion
def separation():
    return widget.Sep(
        linewidth = 0,
        padding = 6,
        foreground = fg_color,
        background = bg_color,
    )

# left half circle (0) right half circle (1)
def half_circle(vColor, kind):
    if kind == 0:
        icon = "" # nf-ple-left_half_circle_thick
    else:
        icon = "" # nf-ple-right_half_circle_thick
    return widget.TextBox(
        text = icon,
        fontsize = size_bar ,
        foreground = vColor,
        background = bg_color,
        padding = -5
    )

# write text or icon
def icons(icon, group_color):
    return widget.TextBox(
        text = icon,
        foreground = fg_color,
        background = group_color,
        fontsize = icon_size,
    )


widget_defaults = dict(
    font=system_font,
    fontsize=widget_font_size,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = active_color,
                    inactive = inactive_color,
                    border_width = 1,
                    disable_drag = True,
                    fontsize = icon_size,
                    foreground = fg_color,
                    highlight_method = 'block',
                    margin_x = 0,
                    margin_y = 5,
                    other_current_screen_border = dark_color,
                    other_screen_border = dark_color,
                    padding_x = 0,
                    padding_y = 10,
                    this_current_screen_border = light_color,
                    this_screen_border = light_color,
                    urgent_alert_method = 'block',
                    urgent_border = urgent_color,
                ),
                separation(),
                widget.Prompt(),
                widget.WindowName(
                    foreground = text1_color,
                    background = bg_color,
                ),
                separation(),

                # Update group
                half_circle(group_update, 0),
                icons("", group_update), # nf-mdi-autorenew
                widget.CheckUpdates(
                    background = group_update,
                    colour_have_updates = update_color,
                    colour_no_updates = fg_color,
                    no_update_string = '0',
                    display_format = 'Updates: {updates}',
                    update_interval = 100,
                    distro = 'Arch_checkupdates'
                ),
                half_circle(group_update, 1),
                separation(),
                # End update group

                # Group 1
                half_circle(group_color_1, 0),
                widget.DF(
                    visible_on_warn = False,
                    partition = '/',
                    format = '{uf}{m}',
                    foreground = fg_color,
                    background = group_color_1,
                ),
                half_circle(group_color_1, 1),
                separation(),
                # End Group 1

                # Group 2
                half_circle(group_color_2, 0),
                # icons("", group_color_2), # nf-mdi-speedometer
                widget.Net(
                    foreground = fg_color,
                    background = group_color_2,
                    # format = red_interface + ' {down}   {up}', # nf-fa-arrow_circle_down nf-fa-arrow_circle_up
                    interface = red_interface,
                    use_bits = 'true'
                ),
                half_circle(group_color_2, 1),
                separation(),
                # End Group 2
                
                # Gruop 3
                half_circle(group_color_3, 0),
                widget.Clock(
                    background = group_color_3,
                    foreground = fg_color,
                    format="%Y/%m/%d %I:%M %p"
                ),
                half_circle(group_color_3, 1),
                separation(),
                # End Group 3
                # Group 4
                half_circle(group_color_4, 0),
                widget.CurrentLayoutIcon(
                    background = group_color_4,
                    scale = 0.7
                ),
                widget.CurrentLayout(
                    background = group_color_4,
                ),
                half_circle(group_color_4, 1),
                separation(),
                # End Group 4
                widget.Systray(
                    icon_size = icon_size,
                    background = bg_color,
                ),


            ],
            size_bar,
            background=color_bar
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]



