# Open up a window.
# From the "arcade" library, use a function called "open_window_2"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
import arcade

arcade.open_window(750, 750, "Space Needle")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw an Ellipse
arcade.draw_ellipse_filled(300, 575, 50, 300, arcade.csscolor.CADET_BLUE)

# Tree trunk
arcade.draw_rectangle_filled(300, 250, 100, 600, arcade.csscolor.WHITE_SMOKE)

# Tree Top
arcade.draw_ellipse_filled(300, 550, 400, 150, arcade.csscolor.WHITE_SMOKE)
arcade.draw_ellipse_filled(300, 550, 600, 25, arcade.csscolor.CADET_BLUE)
arcade.draw_ellipse_filled(240, 205, 79, 550, arcade.csscolor.SKY_BLUE)
arcade.draw_ellipse_filled(350, 205, 79, 550, arcade.csscolor.SKY_BLUE)

# Draw a sun
arcade.draw_circle_filled(700, 700, 100, arcade.color.YELLOW)

arcade.finish_render()

arcade.run()