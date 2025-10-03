from canvas import Canvas
from shapes import Square, Rectangle

#Colors dict
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}

#Get canvas size
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))


canvas_color = colors.get(
    input("Enter canvas color (white, black) default black: ")
    ,"black"
)

canvas = Canvas(canvas_width, canvas_height, canvas_color, canvas_path="assets/canvas.png")

while True:
    shape_type = input("What do you like to draw? (square, rectangle) enter quit to quit: ")
    if shape_type == "square":
        red = int(input(f"How much red should the {shape_type} have (0 - 255): "))
        green = int(input(f"How much green should the {shape_type} have (0 - 255): "))
        blue = int(input(f"How much blue should the {shape_type} have (0 - 255): "))
        color = (red, green, blue)
        x_position = int(input("Enter x position: "))
        y_position = int(input("Enter y position: "))
        side = int(input("Enter side size: "))
        square = Square(x_position, y_position, side, color)
        square.draw(canvas)
    elif shape_type == "rectangle":
        red = int(input(f"How much red should the {shape_type} have (0 - 255): "))
        green = int(input("How much green should the {shape_type} have (0 - 255): "))
        blue = int(input(f"How much blue should the {shape_type} have (0 - 255): "))
        color = (red, green, blue)
        x_position = int(input("Enter x position: "))
        y_position = int(input("Enter y position: "))
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        rectangle = Rectangle(x_position, y_position, width, height, color)
        rectangle.draw(canvas)
    elif shape_type == "quit":
        canvas.save()
        print("Thank you for playing!")
        break
    else:
        print("Invalid figure name")
        break


