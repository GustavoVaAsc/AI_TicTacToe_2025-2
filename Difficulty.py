import pygame
import sys
from GridSize import *



def menu_difficulty():
    pygame.init()
    
    # Screen configuration
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TicTacToe ChatGPI")
    
    # Load background "bg"
    bg = pygame.image.load("bg.png")
    bg= pygame.transform.scale(bg, (width, height))

    # Button properties
    button_width, button_height = 300, 60
    button_x = (width - button_width) // 2
    button_y_start = 200
    button_spacing = 20

    # Load button images (difficutly faces)
    easyFace = pygame.image.load("easyFace.png")
    mediumFace = pygame.image.load("mediumFace.png")
    insaneFace = pygame.image.load("insaneFace.png")

    # Resize the images 
    easyFace = pygame.transform.scale(easyFace, (40, 40))
    mediumFace = pygame.transform.scale(mediumFace, (40, 40))
    insaneFace = pygame.transform.scale(insaneFace, (40, 40))

    # Button list with lambda functions to make the actions
    buttons = [
        {"image": easyFace, "action": lambda: gridSize(1)},
        {"image": mediumFace, "action": lambda: gridSize(2)},
        {"image": insaneFace, "action": lambda: gridSize(3)},
    ]

    #Font and text
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('TicTacToeGPI', True, (255, 255, 255))

    # Draw buttons in the window
    def draw_button(image, x, y, is_hovered):

        button_color = (159, 103, 255) if is_hovered else (189, 150, 255)
        pygame.draw.rect(screen, button_color, (x, y, button_width, button_height), border_radius=10)
        
        # Calculate position to center the image on the button
        img_x = x + (button_width - image.get_width()) // 2
        img_y = y + (button_height - image.get_height()) // 2
        screen.blit(image, (img_x, img_y))

    # Main loop
    running = True
    while running:
        screen.blit(bg, (0, 0))
        
        # Initialize the mouse position
        mouse_pos = pygame.mouse.get_pos() 

        # Get the events of our pygame window
        for event in pygame.event.get():
            # Check for quit
            if event.type == pygame.QUIT:
                running = False
            
            # Check if we're pressing the buttons
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, button in enumerate(buttons):
                    button_y = button_y_start + i * (button_height + button_spacing)
                    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                    if button_rect.collidepoint(mouse_pos):
                        pygame.quit() 
                        button["action"]()
                        

        # Draw buttons
        for i, button in enumerate(buttons):
            button_y = button_y_start + i * (button_height + button_spacing)
            is_hovered = pygame.Rect(button_x, button_y, button_width, button_height).collidepoint(mouse_pos)
            draw_button(button["image"], button_x, button_y, is_hovered)
        
        # Text position on the screen
        screen.blit(text, (239, 100))
        pygame.display.flip()
    
    # Clean up and close
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu_difficulty()


