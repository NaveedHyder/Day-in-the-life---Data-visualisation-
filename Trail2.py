import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Define the screen size and set up the Pygame display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the colors and positions of the activities
activity_colors = {
    "Sleeping": pygame.Color("#1e81b0"),
    "Class": pygame.Color("#ad2f87"),
    "Canteen": pygame.Color("#e28743"),
    "Hostel": pygame.Color("#eab676"),
    "Potheri": pygame.Color("#76b5c5"),
    "Lab": pygame.Color("#873e23"),
    "TP ganesan auditorium": pygame.Color("#6fd6c2"),
    "Java": pygame.Color("#6f91d6")
}
activity_positions = []
num_activities = 8
for i in range(num_activities):
    angle = i * (2 * math.pi / num_activities)
    x = int(screen_width / 2 + 200 * math.cos(angle))
    y = int(screen_height / 2 + 200 * math.sin(angle))
    activity_positions.append((x, y))

# Define the positions of the dots
num_dots = 30
dot_positions = []
for i in range(num_dots):
    angle = random.uniform(0, 2 * math.pi)
    x = int(screen_width / 2 + 150 * math.cos(angle))
    y = int(screen_height / 2 + 150 * math.sin(angle))
    dot_positions.append((x, y))

# Define the speed of the dots' movement
speed = 2

# Define the initial activities of the dots
activities = ["Sleeping", "Class", "Canteen", "Hostel","Potheri","TP ganesan auditorium","Lab", "Java"]
activity_indices = [random.randint(0, num_activities-1) for _ in range(num_dots)]

# Start the Pygame game loop
running = True
while running:
    # Check for Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Move the dots towards the center of their current activity
    for i, dot in enumerate(dot_positions):
        current_activity = activity_positions[activity_indices[i]]
        dx = current_activity[0] - dot[0]
        dy = current_activity[1] - dot[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > speed:
            dot = (dot[0] + int(dx * speed / distance), dot[1] + int(dy * speed / distance))
            dot_positions[i] = dot
        else:
            # Randomly change the activity of the dot once it reaches the center of the current activity
            activity_indices[i] = random.randint(0, num_activities-1)
        
    # Draw the circles representing the activities
    font = pygame.font.Font(None, 20)
    for i, activity_position in enumerate(activity_positions):
        activity_color = activity_colors[activities[i]]
        pygame.draw.circle(screen, activity_color, activity_position, 30)
        text = font.render(activities[i], True, (255, 255, 255))
        text_rect = text.get_rect(center=activity_position)
        screen.blit(text, text_rect)
    
    # Draw the dots
    for dot in dot_positions:
        pygame.draw.circle(screen, (255, 255, 255), dot, 3)
    
    # Update the Pygame display
    pygame.display.update()

# Quit Pygame when the game loop is exited
pygame.quit()
