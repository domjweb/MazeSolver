from window import Window
from shapes import Point, Line

def main():
    # Initialize a window
    win = Window(800, 600)
    
    # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(400, 200)
    
    # Create lines from points
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    
    # Draw lines on the window
    win.draw_line(line1, 'red')
    win.draw_line(line2, 'blue')
    
    # Wait for the window to close
    win.wait_for_close()

if __name__ == '__main__':
    main()