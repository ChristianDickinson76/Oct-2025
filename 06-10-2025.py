try:
    import pygame
    import math
    from pygame.locals import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    print("All imports successful!")
except ImportError as e:
    print(f"Import error: {e}")

# Base vertex list (without animation)
base_humanoid_vertices = [
    # Torso
    (-0.5, -0.75, -0.25), (0.5, -0.75, -0.25),
    (0.5, 0.75, -0.25), (-0.5, 0.75, -0.25),
    (-0.5, -0.75, 0.25), (0.5, -0.75, 0.25),
    (0.5, 0.75, 0.25), (-0.5, 0.75, 0.25),

    # Left Arm
    (-0.8, 0.6, -0.15), (-0.5, 0.6, -0.15),
    (-0.5, -0.6, -0.15), (-0.8, -0.6, -0.15),
    (-0.8, 0.6, 0.15), (-0.5, 0.6, 0.15),
    (-0.5, -0.6, 0.15), (-0.8, -0.6, 0.15),

    # Right Arm
    (0.5, 0.6, -0.15), (0.8, 0.6, -0.15),
    (0.8, -0.6, -0.15), (0.5, -0.6, -0.15),
    (0.5, 0.6, 0.15), (0.8, 0.6, 0.15),
    (0.8, -0.6, 0.15), (0.5, -0.6, 0.15),

    # Left Leg
    (-0.3, -0.75, -0.15), (-0.0, -0.75, -0.15),
    (-0.0, -1.95, -0.15), (-0.3, -1.95, -0.15),
    (-0.3, -0.75, 0.15), (-0.0, -0.75, 0.15),
    (-0.0, -1.95, 0.15), (-0.3, -1.95, 0.15),

    # Right Leg
    (0.0, -0.75, -0.15), (0.3, -0.75, -0.15),
    (0.3, -1.95, -0.15), (0.0, -1.95, -0.15),
    (0.0, -0.75, 0.15), (0.3, -0.75, 0.15),
    (0.3, -1.95, 0.15), (0.0, -1.95, 0.15),

    # Head
    (-0.3, 0.9, -0.3), (0.3, 0.9, -0.3),
    (0.3, 1.5, -0.3), (-0.3, 1.5, -0.3),
    (-0.3, 0.9, 0.3), (0.3, 0.9, 0.3),
    (0.3, 1.5, 0.3), (-0.3, 1.5, 0.3)
]

# Face normals for each face direction
face_normals = [
    (0, 0, -1),   # back
    (0, 0, 1),    # front
    (0, -1, 0),   # bottom
    (0, 1, 0),    # top
    (1, 0, 0),    # right
    (-1, 0, 0)    # left
]

# Body part indices (start index for each body part)
TORSO = 0
LEFT_ARM = 8
RIGHT_ARM = 16
LEFT_LEG = 24
RIGHT_LEG = 32
HEAD = 40

# Box data - position and size
boxes = [
    {'x': 3, 'y': -2, 'z': 2, 'width': 2, 'height': 1.5, 'depth': 2},
    {'x': -4, 'y': -2, 'z': -3, 'width': 1.5, 'height': 2, 'depth': 1.5},
    {'x': 6, 'y': -2, 'z': -1, 'width': 2, 'height': 3, 'depth': 2},
    {'x': -2, 'y': -2, 'z': 5, 'width': 1, 'height': 1, 'depth': 1},
    {'x': 0, 'y': -2, 'z': -6, 'width': 3, 'height': 0.5, 'depth': 1},
    {'x': 8, 'y': -2, 'z': 4, 'width': 1, 'height': 4, 'depth': 1}
]

def get_faces(start_index):
    return [
        [start_index, start_index+1, start_index+2, start_index+3],  # back
        [start_index+4, start_index+5, start_index+6, start_index+7],  # front
        [start_index, start_index+1, start_index+5, start_index+4],  # bottom
        [start_index+2, start_index+3, start_index+7, start_index+6],  # top
        [start_index+1, start_index+2, start_index+6, start_index+5],  # right
        [start_index+0, start_index+3, start_index+7, start_index+4]   # left
    ]

def draw_ground():
    """Draw a large ground plane"""
    glBegin(GL_QUADS)
    
    # Set normal pointing up
    glNormal3f(0, 1, 0)
    
    # Set ground color (green grass)
    glColor3f(0.2, 0.8, 0.2)
    
    # Large ground plane
    size = 20
    glVertex3f(-size, -2, -size)
    glVertex3f(size, -2, -size)
    glVertex3f(size, -2, size)
    glVertex3f(-size, -2, size)
    
    glEnd()

def draw_box(box):
    """Draw a single box"""
    x, y, z = box['x'], box['y'], box['z']
    w, h, d = box['width'], box['height'], box['depth']
    
    # Define box vertices
    vertices = [
        [x-w/2, y, z-d/2], [x+w/2, y, z-d/2], [x+w/2, y+h, z-d/2], [x-w/2, y+h, z-d/2],  # back
        [x-w/2, y, z+d/2], [x+w/2, y, z+d/2], [x+w/2, y+h, z+d/2], [x-w/2, y+h, z+d/2],  # front
    ]
    
    faces = get_faces(0)
    
    glBegin(GL_QUADS)
    face_index = 0
    for face in faces:
        normal = face_normals[face_index % 6]
        glNormal3f(*normal)
        glColor3f(0.6, 0.4, 0.2)  # Brown color for boxes
        
        for vertex_idx in face:
            glVertex3fv(vertices[vertex_idx])
        
        face_index += 1
    glEnd()

def check_box_collision(player_x, player_y, player_z):
    """Check if player is standing on any box"""
    tolerance = 0.3  # How close player needs to be to box surface
    
    for box in boxes:
        bx, by, bz = box['x'], box['y'], box['z']
        bw, bh, bd = box['width'], box['height'], box['depth']
        
        # Check if player is horizontally within box bounds
        if (bx - bw/2 - tolerance <= player_x <= bx + bw/2 + tolerance and 
            bz - bd/2 - tolerance <= player_z <= bz + bd/2 + tolerance):
            
            # Check if player is at the right height to be standing on box
            box_top = by + bh
            if abs(player_y - box_top) <= tolerance:
                return box_top  # Return the height the player should be at
    
    return None  # Not on any box

def animate_walking(time, is_moving):
    """Apply walking animation to vertices"""
    animated_vertices = base_humanoid_vertices.copy()
    
    if is_moving:
        # Walking cycle parameters
        cycle_speed = 0.3
        leg_swing = math.sin(time * cycle_speed) * 0.3
        arm_swing = math.sin(time * cycle_speed) * 0.2
        body_bob = math.sin(time * cycle_speed * 2) * 0.05
        
        # Animate left leg (forward/back swing)
        for i in range(LEFT_LEG, LEFT_LEG + 8):
            x, y, z = animated_vertices[i]
            animated_vertices[i] = (x, y + body_bob, z + leg_swing)
        
        # Animate right leg (opposite swing)
        for i in range(RIGHT_LEG, RIGHT_LEG + 8):
            x, y, z = animated_vertices[i]
            animated_vertices[i] = (x, y + body_bob, z - leg_swing)
        
        # Animate left arm (opposite to left leg)
        for i in range(LEFT_ARM, LEFT_ARM + 8):
            x, y, z = animated_vertices[i]
            animated_vertices[i] = (x, y + body_bob, z - arm_swing)
        
        # Animate right arm (opposite to right leg)
        for i in range(RIGHT_ARM, RIGHT_ARM + 8):
            x, y, z = animated_vertices[i]
            animated_vertices[i] = (x, y + body_bob, z + arm_swing)
        
        # Animate torso (slight bob)
        for i in range(TORSO, TORSO + 8):
            x, y, z = animated_vertices[i]
            animated_vertices[i] = (x, y + body_bob, z)
        
        # Animate head (slight bob)
        for i in range(HEAD, HEAD + 8):
            x, y, z = animated_vertices[i]
            animated_vertices[i] = (x, y + body_bob, z)
    
    return animated_vertices

def draw_humanoid(animated_vertices):
    # Build faces for current frame
    humanoid_faces = []
    for i in range(0, len(animated_vertices), 8):
        humanoid_faces.extend(get_faces(i))
    
    glBegin(GL_QUADS)
    face_index = 0
    for face in humanoid_faces:
        # Set normal for this face
        normal = face_normals[face_index % 6]
        glNormal3f(*normal)
        
        for vertex in face:
            glColor3f(0.8, 0.6, 0.4)  # Skin-like color
            glVertex3fv(animated_vertices[vertex])
        
        face_index += 1
    glEnd()

# Setup Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Setup lighting
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

# Light properties
light_position = [2.0, 2.0, 5.0, 1.0]  # Point light
light_diffuse = [1.0, 1.0, 1.0, 1.0]   # White light
light_ambient = [0.3, 0.3, 0.3, 1.0]   # Ambient light

glLightfv(GL_LIGHT0, GL_POSITION, light_position)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)

# Movement variables
player_x = 0.0
player_y = 0.0
player_z = 0.0
player_isJumping = False
player_force = [0,0,0]
move_speed = 0.1
time = 0

# Setup perspective
gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, -2.5, -2)
glEnable(GL_DEPTH_TEST)

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get key states
    keys = pygame.key.get_pressed()
    is_moving = False
    
    # Handle WASD movement
    if keys[K_w]:  # Forward
        player_force[0] = -1
        is_moving = True
    if keys[K_s]:  # Backward
        player_force[0] = 1
        is_moving = True
    if keys[K_a]:  # Left
        player_force[2] = -1
        is_moving = True
    if keys[K_d]:  # Right
        player_force[2] = 1
        is_moving = True
    if keys[K_SPACE] and not player_isJumping:  # Jump
        player_force[1] = 1
        player_isJumping = True

    player_x += player_force[2] * move_speed
    player_y += player_force[1]
    player_z += player_force[0] * move_speed

    # Check if player is standing on a box
    box_height = check_box_collision(player_x, player_y, player_z)
    
    if box_height is not None:
        # Player is on a box
        player_y = box_height
        player_isJumping = False
        player_force[1] = 0
    else:
        # Player is in the air or on ground
        if player_isJumping and player_y > 0:
            player_force[1] -= 0.1  # Apply gravity
        elif player_y <= 0:
            player_y = 0  # Hit ground
            player_force[1] = 0
            player_isJumping = False

    # Damping for horizontal movement
    if player_force[0] > 0:
        player_force[0] = max(0, player_force[0] - 1)
    elif player_force[0] < 0:
        player_force[0] = min(0, player_force[0] + 1)
    
    if player_force[2] > 0:
        player_force[2] = max(0, player_force[2] - 1)
    elif player_force[2] < 0:
        player_force[2] = min(0, player_force[2] + 1)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Draw the ground plane
    draw_ground()
    
    # Draw all boxes
    for box in boxes:
        draw_box(box)
    
    # Get animated vertices for current frame
    animated_vertices = animate_walking(time, is_moving)
    
    # Draw the animated humanoid at player position
    glPushMatrix()
    glTranslatef(player_x, player_y + 2, player_z - 2)
    draw_humanoid(animated_vertices)
    glPopMatrix()
    
    pygame.display.flip()
    pygame.time.wait(16)  # ~60 FPS
    
    # Only increment time if moving (for animation)
    if is_moving and not player_isJumping:
        time += 1