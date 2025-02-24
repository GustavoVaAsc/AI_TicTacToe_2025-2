import pygame
import sys
import subprocess


def menu_difficulty():
    pygame.init()
    
    # Window configuration
    width, height = 600, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TicTacToe ChatGPI")
    
    # Load background "bg."
    background_image = pygame.image.load("bg.png")
    background_image = pygame.transform.scale(background_image, (width, height))

    # Font settings
    font = pygame.font.SysFont(None, 36)

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


    buttons = [
        {"image": easyFace, "action": lambda: run("Main.py")},
        {"image": mediumFace, "action": lambda: print("No hay no existe :b")},
        {"image": insaneFace, "action": lambda: print("No hay no existe :b")},
    ]

   # Run the script with de mode selected
    def run(file):
        try:
            pygame.quit()  # Close the window
            subprocess.run(["python", file], check=True) 
            sys.exit() 
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script {file}: {e}")

    # Draw buttons in the window
    def draw_button(image, x, y, is_hovered):

        button_color = (159, 103, 255) if is_hovered else (189, 150, 255)
        pygame.draw.rect(window, button_color, (x, y, button_width, button_height), border_radius=10)
        
        # Calculate position to center the image on the button
        img_x = x + (button_width - image.get_width()) // 2
        img_y = y + (button_height - image.get_height()) // 2
        window.blit(image, (img_x, img_y))

    # Main loop
    running = True
    while running:
        window.blit(background_image, (0, 0))
        
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, button in enumerate(buttons):
                    button_y = button_y_start + i * (button_height + button_spacing)
                    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                    if button_rect.collidepoint(mouse_pos):
                        button["action"]()

        # Draw buttons
        for i, button in enumerate(buttons):
            button_y = button_y_start + i * (button_height + button_spacing)
            is_hovered = pygame.Rect(button_x, button_y, button_width, button_height).collidepoint(mouse_pos)
            draw_button(button["image"], button_x, button_y, is_hovered)
        
        pygame.display.flip()
    
    # Clean up and close
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    menu_difficulty()


