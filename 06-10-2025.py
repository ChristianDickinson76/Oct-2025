import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("Pygame + PyOpenGL Template")

# Set up OpenGL
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Set up lighting
light_position = [2.0, 2.0, 2.0, 1.0]  # Point light
light_diffuse = [1.0, 1.0, 1.0, 1.0]   # White light
light_ambient = [0.2, 0.2, 0.2, 1.0]   # Dim ambient light

glLightfv(GL_LIGHT0, GL_POSITION, light_position)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)

# Colors
WHITE = (1.0, 1.0, 1.0)
RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)
YELLOW = (1.0, 1.0, 0.0)

def calculate_normal(v1, v2, v3):
    """Calculate normal vector for a triangle"""
    # Vector from v1 to v2
    edge1 = [v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]]
    # Vector from v1 to v3
    edge2 = [v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]]
    
    # Cross product
    normal = [
        edge1[1] * edge2[2] - edge1[2] * edge2[1],
        edge1[2] * edge2[0] - edge1[0] * edge2[2],
        edge1[0] * edge2[1] - edge1[1] * edge2[0]
    ]
    
    # Normalize
    length = (normal[0]**2 + normal[1]**2 + normal[2]**2) ** 0.5
    if length > 0:
        normal = [normal[0]/length, normal[1]/length, normal[2]/length]
    
    return normal

def draw_cube():
    """Draw a simple pyramid (4 triangular faces + 1 square base)"""
    
    # Define vertices
    apex = [0, 0, 2]
    base_vertices = [
        [-1, -1, 0],  # bottom-left
        [1, -1, 0],   # bottom-right
        [1, 1, 0],    # top-right
        [-1, 1, 0]    # top-left
    ]
    
    glBegin(GL_TRIANGLES)
    
    # Front face
    glColor3f(*YELLOW)
    normal = calculate_normal(apex, base_vertices[0], base_vertices[1])
    glNormal3f(*normal)
    glVertex3f(*apex)
    glVertex3f(*base_vertices[0])
    glVertex3f(*base_vertices[1])
    
    # Right face
    glColor3f(*YELLOW)
    normal = calculate_normal(apex, base_vertices[1], base_vertices[2])
    glNormal3f(*normal)
    glVertex3f(*apex)
    glVertex3f(*base_vertices[1])
    glVertex3f(*base_vertices[2])

    # Back face
    glColor3f(*YELLOW)
    normal = calculate_normal(apex, base_vertices[2], base_vertices[3])
    glNormal3f(*normal)
    glVertex3f(*apex)
    glVertex3f(*base_vertices[2])
    glVertex3f(*base_vertices[3])

    # Left face
    glColor3f(*YELLOW)
    normal = calculate_normal(apex, base_vertices[3], base_vertices[0])
    glNormal3f(*normal)
    glVertex3f(*apex)
    glVertex3f(*base_vertices[3])
    glVertex3f(*base_vertices[0])
    
    glEnd()
    
    # Draw base with normal pointing down
    glBegin(GL_QUADS)
    glColor3f(*YELLOW)
    glNormal3f(0, 0, -1)  # Normal pointing down
    glVertex3f(*base_vertices[0])
    glVertex3f(*base_vertices[1])
    glVertex3f(*base_vertices[2])
    glVertex3f(*base_vertices[3])
    glEnd()

def main():
    clock = pygame.time.Clock()
    rotation = 0
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        # Clear screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Rotate the pyramid
        glPushMatrix()
        glRotatef(rotation, 1, 1, 1)
        draw_cube()
        glPopMatrix()
        
        # Update rotation
        rotation += 1
        if rotation >= 360:
            rotation = 0
        
        # Update display
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

if __name__ == "__main__":
    main()