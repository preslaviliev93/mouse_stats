from pynput import mouse
from math import hypot


class Tracker:

    def __init__(self):
        self.mouse = mouse.Controller()
        self.click_counter = 0
        self.distance_pixels = 0.0
        self.last_pointer_position = None
        self.pixels_per_meter = 3780

    def read_pointer_current_position(self):
        """
        This method will read the current position of the mouse pointer
        :return: tuple of coordinates, i.e. (1915,1028)
        """
        return self.mouse.position

    def on_move(self, x, y):
        if self.last_pointer_position is not None:
            dx = x - self.last_pointer_position[0]
            dy = y - self.last_pointer_position[1]
            self.distance_pixels += hypot(dx, dy)
        self.last_pointer_position = (x, y)

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_counter += 1

    def main(self):
        with mouse.Listener(on_move=self.on_move, on_click=self.on_click) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                pass
        distance_meters = self.distance_pixels / self.pixels_per_meter
        print(f"Total clicks: {self.click_counter}")
        print(f'Total distance {distance_meters} m.')


tracker = Tracker()
distance = tracker.main()
print(f"Total distance: {distance} m.")
