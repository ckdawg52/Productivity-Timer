# Productivity Timer CLI 🚀

A visually engaging Command Line Interface (CLI) productivity timer designed to help you stay focused using interval-based reminders. Built with Python, it features dynamic ASCII art animations and progress bars to make focus sessions less boring. I also made a browser version but it isn't as cool as the CLI version.

## ✨ Features

*   **Interactive Prompts:** If you don't provide arguments, the timer will guide you through the setup with animated prompts.
*   **Dynamic Visuals:** Uses `terminaltexteffects` for "Wave," "Smoke," and "Slide" text animations.
*   **Progress Tracking:** Real-time feedback using `alive-progress` bars.
*   **Audible Alerts:** Plays a terminal bell sound (`\a`) at the end of each interval to nudge you back to focus.
*   **Flexible Setup:** Launch with quick command-line arguments or follow the interactive flow.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ckdawg52/Productivity-Timer.git

   cd Productivity-Timer
    ```

2. **Install the required dependencies:**
    This project relies on alive-progress for the bars and terminaltexteffects for the animations.

    ```bash
    pip install alive-progress terminaltexteffects
    ```

#### OR

Use this [link](https://ckdawg52.github.io/Productivity-Timer/) to access the browser version (witch isn't as cool).

## 🚀 Usage
You can run the timer in two ways:

1. **Interactive Mode**
Simply run the script, and it will ask you for the duration and intervals.

    ```bash
    python3 src/main.py
    ```

2. **Quick Start (Arguments)**
Pass the total duration and the interval length (in minutes) directly as flags.

    ```bash
    # Example: 60-minute session with reminders every 15 minutes
    python3 src/main.py --duration 60 --interval 15
    ```

**Flags:**
*   `-d` or `--duration`: Total session time in minutes.
*   `-i` or `--interval`: How often the focus reminder should go off (in minutes).

## 📦 Dependencies

*   [alive-progress](https://github.com/rsalmei/alive-progress): For the sleek, animated progress bars.
*   [terminaltexteffects](https://github.com/Chris-B-B/terminaltexteffects): For the professional terminal animations and transitions.

## 📝 How it Works

1.  **Welcome:** Displays a "Welcome Focus Timer" banner with a wave effect.
2.  **Countdown:** A dramatic 3-2-1 countdown sequence starts your session.
3.  **Active Timer:** A progress bar shows exactly how much time is left in your current interval.
4.  **Interval Alert:** At the end of each interval, the terminal rings and a "FOCUS" banner smokes onto the screen before the next timer starts.
5.  **Completion:** Once the total duration is reached, a "FINISHED" banner is displayed.