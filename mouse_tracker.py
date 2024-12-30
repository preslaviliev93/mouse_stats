from pynput import mouse
from math import hypot
import time


class Tracker:
    def __init__(self):
        self.pixel_to_cm = 0.0264583
        self.total_distance_cm = 0.0
        self.last_position = None

    def on_move(self, x, y):
        if self.last_position is not None:
            dx = x - self.last_position[0]
            dy = y - self.last_position[1]
            distance_px = hypot(dx, dy)
            self.total_distance_cm += distance_px * self.pixel_to_cm
        self.last_position = (x, y)

    def main(self):
        listener = mouse.Listener(on_move=self.on_move)
        listener.start()

        print("Tracking mouse. Press Ctrl+C to stop (if supported).")

        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nCaught KeyboardInterrupt. Exiting.")
        finally:
            listener.stop()

        print(f"Final total distance: {self.total_distance_cm:.2f} cm")


if __name__ == "__main__":
    tracker = Tracker()
    tracker.main()
