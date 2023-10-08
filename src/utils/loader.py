def loader_time(time, show_loading_screen, seconds):
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= seconds:
            show_loading_screen = False
            break
    return show_loading_screen
