# Mouse and Keyboard Tracker

## Overview
The **Mouse and Keyboard Tracker** is a Python project designed to monitor and track user interactions with their computer. It records the total distance traveled by the mouse cursor on the screen, the number of mouse button presses, and the number of keyboard keys pressed.

### Features
- Tracks the total distance traveled by the mouse cursor in centimeters.
- Monitors mouse button press events.
- Tracks the total number of keyboard keys pressed.


---

## Installation

### Prerequisites
- Python 3.10+
- Required Python packages:
  - `pynput`
  - `math`
  - `time`


### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/mouse-keyboard-tracker.git
   cd mouse-keyboard-tracker
2. Install required packages:
   ```bash
   pip install pynput
   python tracker.py
## Methodology
## Calculation of Mouse Cursor Distance
Monitor Specifications
Screen Resolution:
Example: 1920 x 1080 pixels
Physical Dimensions:
Example: Width = 59.67 cm, Height = 33.57 cm

Conversion Factors

Pixels per cm (horizontal):
   ```python
   px_per_cm_x = Screen Width in Pixels / Screen Width in cm
   ```
Pixels per cm (vertical):
   ```python
   px_per_cm_y = Screen Height in Pixels / Screen Height in cm
   ```

Distance Formula
For each mouse movement event, the distance in pixels is calculated using the Pythagorean theorem:
   ```python
   Distance in Pixels = sqrt((Δx)^2 + (Δy)^2)
   ```
The pixel distance is then converted to centimeters:
   ```python
    Distance in cm (x) = Δx / px_per_cm_x
    Distance in cm (y) = Δy / px_per_cm_y
   ```

Finally, the total Euclidean distance in centimeters:
   ```python
    Total Distance in cm = sqrt((Distance in cm (x))^2 + (Distance in cm (y))^2)
   ```

## Usage
Start the tracker:
   ```python
   python mouse_tracker.py
   ```
Interact with the mouse and keyboard.

Exit the tracker using Ctrl+C.
 - View the final results:
 - Total distance traveled by the mouse cursor in meters.
 - Total mouse button presses.
 - Total keyboard keys pressed.

Example Output

<pre>
Tracking mouse. Press Ctrl+C to stop (if supported).

Final total distance: 170.14 cm
Total times mouse buttons pressed: 9
Total times keyboard buttons pressed: 23
Press Enter to close.
</pre>


