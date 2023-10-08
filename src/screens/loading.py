def loading(pygame, screen):
    game_font = pygame.font.Font('font/Pixeltype.ttf', 60)

    # pause screen
    game_name = game_font.render('GAME BY', False, '#eeeeee')
    game_name_rect = game_name.get_rect(center=(400, 200))
    game_message = game_font.render('ARIOUM', False, '#eeeeee')
    game_message_rect = game_message.get_rect(center=(400, 250))

    #
    screen.fill("#000000")
    screen.blit(game_name, game_name_rect)
    screen.blit(game_message, game_message_rect)
