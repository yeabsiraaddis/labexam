import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_triangle():
    # Set the color to purple (R, G, B)
    glColor3f(0.5, 0.0, 0.5)
    
    # Begin drawing a triangle
    glBegin(GL_TRIANGLES)
    
    # Define the 3 vertices of the triangle
    glVertex2f(-0.5, -0.5)  # Bottom-left
    glVertex2f(0.5, -0.5)   # Bottom-right
    glVertex2f(0.0, 0.5)    # Top-center
    
    glEnd()

def main():
    # Initialize PyGame
    pygame.init()
    
    # Set up display mode
    display = (800, 600)  # Window size
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Purple Triangle with PyOpenGL")
    
    # Set up the 2D orthogonal projection
    glOrtho(-1, 1, -1, 1, -1, 1)  # Coordinate system bounds

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen with black
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the triangle
        draw_triangle()
        
        # Swap the buffers (double buffering)
        pygame.display.flip()
        pygame.time.wait(10)

    # Quit PyGame
    pygame.quit()

if __name__ == "__main__":
    main()
