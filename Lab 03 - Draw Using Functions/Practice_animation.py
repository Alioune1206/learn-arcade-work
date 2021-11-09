# Open up a window.
# From the "arcade" library, use a function called "open_window_2"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
import arcade



def space_needle(x,y):
    arcade.draw_ellipse_filled(x, y, 50, 300, arcade.csscolor.CADET_BLUE)
    arcade.draw_rectangle_filled(x, y - 325, 100, 600, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_ellipse_filled(x, y - 25, 400, 150, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_ellipse_filled(x, y - 25, 600, 25, arcade.csscolor.CADET_BLUE)
    arcade.draw_ellipse_filled(x - 60, y - 370, 79, 550, arcade.csscolor.SKY_BLUE)
    arcade.draw_ellipse_filled(x + 50, y - 370, 79, 550, arcade.csscolor.SKY_BLUE)

def bird(x,y):
    arcade.draw_ellipse_filled(x, y, 160, 40, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_circle_filled(x - 50, y + 10, 10, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(x, 650, y - 650, 100, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_ellipse_filled(x - 80, y, 25, 25, arcade.csscolor.YELLOW)

def sun(x,y):
    arcade.draw_circle_filled(x, y, 100, arcade.color.YELLOW)

def on_draw(delta_time):
    """draw everything"""
    arcade.start_render()
    space_needle(400, 600)
    space_needle(200, 100)
    bird(bird_x, 500)
    bird(bird_x + 50, 700)
    bird_x += 1
bird_x = 450

def main():
    arcade.open_window(750, 750, "Space Needle")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)
    arcade.schedule(on_draw, 1/60)

    arcade.run()

main()