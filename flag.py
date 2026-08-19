import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Waving Tiranga 🇮🇳")
clock = pygame.time.Clock()

# Colors
SAFFRON = (255, 153, 51)
WHITE = (255, 255, 255)
GREEN = (19, 136, 8)
BLUE = (0, 0, 128)
BROWN = (101, 67, 33)
SKY = (135, 206, 235)

# Flag setup
flag_w, flag_h = 600, 360
flag_x, flag_y = 200, 150
pole_x = flag_x - 15
pole_h = 450

def draw_chakra(cx, cy, r, angle):
    pygame.draw.circle(screen, BLUE, (cx, cy), r, 2)
    pygame.draw.circle(screen, BLUE, (cx, cy), 5)
    for i in range(24):
        a = math.radians(i * 15 + angle)
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        pygame.draw.line(screen, BLUE, (cx, cy), (x, y), 2)

def draw_real_flag(t):
    segments = 60 # jitne zyada segments utna smooth wave
    seg_w = flag_w / segments
    stripe_h = flag_h / 3

    for i in range(segments):
        x = flag_x + i * seg_w
        wave1 = math.sin(i * 0.3 + t * 0.1) * 12
        wave2 = math.sin(i * 0.3 + t * 0.1 + 0.5) * 12

        points = []
        for j in range(4): # 4 points per segment for smooth curve
            y_offset = j * stripe_h
            wy = wave1 if j < 2 else wave2
            points.append((x, flag_y + y_offset + wy))
            points.append((x + seg_w, flag_y + y_offset + wy))

        # Draw 3 stripes in this segment
        for s in range(3):
            color = [SAFFRON, WHITE, GREEN][s]
            y_base = flag_y + s * stripe_h
            poly = [
                (x, y_base + wave1),
                (x + seg_w, y_base + wave2),
                (x + seg_w, y_base + stripe_h + wave2),
                (x, y_base + stripe_h + wave1)
            ]
            pygame.draw.polygon(screen, color, poly)

            # shadow effect for depth
            shadow = [(p[0]+2, p[1]+2) for p in poly]
            pygame.draw.polygon(screen, (0,0,0,30), shadow)

    # Ashok Chakra with rotation
    chakra_x = flag_x + flag_w/2 + math.sin(t*0.1)*10
    chakra_y = flag_y + stripe_h + stripe_h/2
    draw_chakra(int(chakra_x), int(chakra_y), 35, t*2)

def draw_pole():
    pygame.draw.rect(screen, BROWN, (pole_x, flag_y, 15, pole_h))
    pygame.draw.circle(screen, (80,50,20), (pole_x+7, flag_y+pole_h), 10) # base

def draw_clouds(t):
    for i in range(3):
        x = 100 + i*200 + math.sin(t*0.05 + i)*20
        y = 80 + i*10
        pygame.draw.circle(screen, WHITE, (int(x), y), 30)
        pygame.draw.circle(screen, WHITE, (int(x)+40, y), 25)
        pygame.draw.circle(screen, WHITE, (int(x)+20, y-15), 20)

# Main loop
time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    draw_clouds(time)
    draw_pole()
    draw_real_flag(time)

    # Ground
    pygame.draw.rect(screen, (34, 139, 34), (0, flag_y+pole_h-20, WIDTH, 100))

    pygame.display.flip()
    clock.tick(50 )
    time += 1

pygame.quit()
pygame.draw.rect(screen, (34, 139, 34), (0, flag_y+pole_h-20, WIDTH, 100))
d
your code

both are my code

