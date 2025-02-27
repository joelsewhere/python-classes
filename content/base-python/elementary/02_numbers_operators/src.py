from ipycanvas import Canvas, hold_canvas
from time import sleep

def canvas(fill_style='orange'):
    global c 
    
    c = Canvas(width=1000, height=300)
    
    c.fill_style = fill_style
    
    c.fill_rect(0, 0, 1000, 600)

    return c


def write_message(message):
    
    message_ = str(message)
    # Number of steps in your animation
    steps_number = 200
    
    # Note how `hold_canvas` now wraps the entire for-loop
    with hold_canvas():
        for i in range(len(message_)):
            # Clear the old animation step
            fill_style = c.fill_style
            c.clear()
            c.fill_style = fill_style
            c.fill_rect(0, 0, 1000, 600)
    
            c.fill_style = 'white'
            c.font = "80px serif"
    
            c.fill_text(message_[:i + 1], 20, 180)

            c.fill_style = fill_style
    
            # Animation frequency ~50Hz = 1000./50. milliseconds
            c.sleep(50)