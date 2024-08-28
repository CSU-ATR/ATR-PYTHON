from PySide6.QtWidgets import QApplication, QWidget

def main():
    # Create the application instance
    app = QApplication([])

    # Create the main window
    window = QWidget()
    window.setWindowTitle("ATR")

    # Get computer screen's geometry
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()

    # Get computer screen's width and height
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    # Define the window's width and height
    window_width = 600
    window_height = 600

    # Calculate the center position
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window's geometry (position and size)
    window.setGeometry(x, y, window_width, window_height)

    # Show the window
    window.show()

    # Run the application event loop
    app.exec()

if __name__ == "__main__":
    main()
