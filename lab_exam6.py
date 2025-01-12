import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Define the line-drawing function
def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)  # Begin line drawing mode
    glColor3f(1.0, 0.0, 0.0)  # Set line color (red)
    glVertex2f(x1, y1)  # First point
    glVertex2f(x2, y2)  # Second point
    glEnd()  # End line drawing

def main():
    # Initialize PyGame
    pygame.init()
    
    # Set up the display
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Draw a Line Using PyOpenGL")
    
    # Set up the 2D coordinate system
    glOrtho(-1, 1, -1, 1, -1, 1)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw a line between two points
        draw_line(-0.5, -0.5, 0.5, 0.5)  # Line from (-0.5, -0.5) to (0.5, 0.5)
        
        # Swap the buffers to display the line
        pygame.display.flip()
        pygame.time.wait(10)

    # Quit PyGame
    pygame.quit()

if __name__ == "__main__":
    main()
