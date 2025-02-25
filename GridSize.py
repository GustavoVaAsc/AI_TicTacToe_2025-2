import pygame
import sys
from Settings import *  # If you need to import any other module

def gridSize(difficulty):
    # Initialize pygame
    pygame.init()  # This is important for the font system and other modules to work

    # The rest of your code goes here
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TicTacToe ChatGPI")
    
    # Load background "bg"
    bg = pygame.image.load("bg.png")
    bg = pygame.transform.scale(bg, (width, height))

    # Button configuration
    button_width, button_height = 300, 60
    button_x = (width - button_width) // 2
    button_y_start = 200
    button_spacing = 20

    buttons = [
        {"text": "4X4", "action": lambda: Settings(difficulty, 4)},  
        {"text": "5X5", "action": lambda: Settings(difficulty, 5)}, 
    ]

    # Font and text
    font = pygame.font.SysFont('Comic Sans MS', 30)    
    text = font.render('TicTacToeGPI', True, (255, 255, 255))

    # Function to draw buttons with text
    def draw_button(text, x, y, is_hovered):
        button_color = (159, 103, 255) if is_hovered else (189, 150, 255)
        pygame.draw.rect(screen, button_color, (x, y, button_width, button_height), border_radius=10)
        
        # Draw the text centered on the button
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x + button_width // 2, y + button_height // 2))
        screen.blit(text_surface, text_rect)

    # Main loop
    running = True
    while running:
        screen.blit(bg, (0, 0))
        
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, button in enumerate(buttons):
                    button_y = button_y_start + i * (button_height + button_spacing)
                    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                    if button_rect.collidepoint(mouse_pos):
                        pygame.quit() 
                        button["action"]()  
        # Draw the buttons with text
        for i, button in enumerate(buttons):
            button_y = button_y_start + i * (button_height + button_spacing)
            is_hovered = pygame.Rect(button_x, button_y, button_width, button_height).collidepoint(mouse_pos)
            draw_button(button["text"], button_x, button_y, is_hovered)
        
        # Draw the text at the top
        screen.blit(text, (239, 100))
        pygame.display.flip()
    
    # Clean up and close
    pygame.quit()
    sys.exit()
