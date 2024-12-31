from pynput import mouse, keyboard
from math import hypot
from time import sleep


class Tracker:
    def __init__(self):

        """     Monitor specifications    """
        self.screen_width_px = 1920
        self.screen_height_px = 1080
        self.screen_width_cm = 69.6736  # approx. width in cm
        self.screen_height_cm = 33.5664  # approx height in cm

        """    Calculating pixels per centimeter for both axes    """
        self.px_per_cm_x = self.screen_width_px / self.screen_width_cm
        self.px_per_cm_y = self.screen_height_px / self.screen_height_cm

        """    Helpers and counters   """
        self.total_distance_cm = 0
        self.last_pointer_position = None
        self.total_times_buttons_pressed = 0
        self.keyboard_key_pressed = None
        self.total_keys_pressed = 0

    """     Methods    """
    def on_move(self, x, y):
        if self.last_pointer_position is not None:
            dx = x - self.last_pointer_position[0]
            dy = y - self.last_pointer_position[1]

            """  Convert pixel movement to centimeters  """
            distance_cm_x = abs(dx) / self.px_per_cm_x
            distance_cm_y = abs(dy) / self.px_per_cm_y

            """  Calculating the Euclidean distance between the two points  """
            distance_cm = hypot(distance_cm_x, distance_cm_y)
            self.total_distance_cm += distance_cm

        """  If the position is None set the initial/starting pointer position for more accurate measurement  """
        self.last_pointer_position = (x, y)

    def on_click(self, x, y, button, pressed) -> None:
        if pressed:
            self.total_times_buttons_pressed += 1

    def on_press(self, key) -> None:
        if self.keyboard_key_pressed is None:
            self.keyboard_key_pressed = key

    def on_release(self, key) -> None:
        if self.keyboard_key_pressed is not None:
            self.keyboard_key_pressed = None
            self.total_keys_pressed += 1

    def main(self):
        mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
        )
        mouse_listener.start()

        keyboard_listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release,
        )
        keyboard_listener.start()

        print("Tracking mouse and keyboard. Press Ctrl+C to stop.")

        try:
            while True:
                sleep(0.001)
        except KeyboardInterrupt:
            print("\nCaught KeyboardInterrupt.")
        finally:
            try:
                mouse_listener.stop()
                keyboard_listener.stop()
            except KeyboardInterrupt:
                pass

        distance_in_meters = self.total_distance_cm / 100
        print(f"Final total distance: {self.total_distance_cm:.2f} cm")
        print(f"Total keys pressed: {self.total_keys_pressed}")
        print(f"Total times buttons pressed: {self.total_times_buttons_pressed}")

        input("Press Enter to close.")


if __name__ == "__main__":
    tracker = Tracker()
    tracker.main()


