# Workday Timer

A real-time productivity timer designed to help you manage your workday with structured activities and time blocks. The program runs continuously, automatically starting your workday at 8:00 AM on weekdays.

## What It Is

Workday Timer is a terminal-based time management tool that guides you through an 8-hour workday with predefined activities. Each activity runs for its actual duration in real-time, helping you stay focused and on schedule throughout your day.

The timer displays:
- **Live Clock Header**: Continuously updated date, time, and personalized greeting
- Current activity progress with visual progress bars
- Overall day completion percentage
- Time remaining for each task
- Start and completion times for each activity
- A summary report at the end of your workday that persists until the next morning

## Features

- ⏰ **Continuous Clock Display**: Live updating date, time (hh:mm:ss AM/PM), and time-based greetings
  - "Good Morning" (6:00 AM - 12:00 PM)
  - "Good Afternoon" (12:00 PM - 5:00 PM)
  - "Good Evening" (5:00 PM - 8:00 PM)
  - "Good Night" (all other times)
- 📅 **Automatic Scheduling**: Timer automatically starts at 8:00 AM on weekdays (Monday-Friday)
- 📊 **Real-time Progress Tracking**: Live progress bars showing both current task and overall day completion
- ⏱️ **Accurate Timing**: Each activity runs for its actual duration (e.g., 0.5 hours = 30 real minutes)
- 🎨 **Beautiful Terminal UI**: Rich, colorful interface with emojis and formatted text
- 📋 **Persistent Stats**: End-of-day summary remains displayed until 7:55 AM the next day
- 🏖️ **Weekend Mode**: On Saturdays and Sundays, prompts whether to run the timer
- ☕ **Structured Schedule**: Pre-defined activities including meetings, deep work, breaks, and administrative tasks

## Default Schedule

| Activity | Duration |
|----------|----------|
| ☕ Morning coffee & emails | 30 minutes |
| 💼 Team standup meeting | 30 minutes |
| ⌨️ Deep work session | 2 hours |
| 🍽️ Lunch break | 1 hour |
| 📞 Client call | 1 hour |
| ⌨️ Coding/Project work | 2 hours |
| 📊 Status report | 30 minutes |
| 📧 End-of-day emails | 30 minutes |

**Total Duration**: 8 hours

## Frameworks & Dependencies

This project uses the following Python framework:

- **[Rich](https://rich.readthedocs.io/)** (v10.0+): A Python library for rich text and beautiful formatting in the terminal
  - Provides progress bars, panels, tables, and colored output
  - Creates an interactive and visually appealing user experience

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download** the project files

2. **Install the required dependency**:
   ```bash
   pip install rich
   ```

   Or if you're using Python 3:
   ```bash
   pip3 install rich
   ```

## How to Run

1. **Open your terminal** and navigate to the project directory:
   ```bash
   cd path/to/workday-timer
   ```

2. **Run the script** (it will run continuously):
   ```bash
   python workday_sim.py
   ```

   Or if you're using Python 3:
   ```bash
   python3 workday_sim.py
   ```

3. **The program runs continuously** with the following behavior:
   - **Weekdays (Mon-Fri)**: Automatically starts the workday timer at 8:00 AM
   - **Weekends (Sat-Sun)**: Prompts "Shall I run the workday timer? (Y or N)"
   - **After completion**: Displays workday stats until 7:55 AM the next day
   - **7:55 AM**: Resets and prepares for the new workday

4. **To stop the program**, press `Ctrl+C` at any time

## Customization

You can customize the activities and durations by editing the `activities` list in the script:

```python
activities = [
    ("☕ Morning coffee & emails", 0.5),  # Duration in hours
    ("💼 Team standup meeting", 0.5),
    # Add or modify activities here
]
```

## Example Output

```
Friday, 3 April 2025
08:00:15 AM - Good Morning

🏢 Workday Timer Starting
Start time: 08:00 AM
Total duration: 8 hours

Starting: ☕ Morning coffee & emails
Duration: 0.5 hours | Expected completion: 08:30 AM

⠋ ☕ Morning coffee & emails ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45% 0:08:15
⠋ 📅 Total Day Progress ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3% 7:42:30
```

**Weekend Prompt:**
```
Saturday, 5 April 2025
09:30:42 AM - Good Morning

Weekend Day - Saturday

Shall I run the workday timer? (Y or N):
```

## Use Cases

- **Automated Time Management**: Set it and forget it - runs automatically on weekdays
- **Focus Sessions**: Dedicated time blocks for deep work with progress tracking
- **Break Reminders**: Ensure you take regular breaks throughout the day
- **Productivity Tracking**: Visual representation of your workday progress with persistent stats
- **Remote Work**: Structure your day when working from home
- **Consistent Schedule**: Maintains work-life balance by adhering to set work hours
- **Flexible Weekends**: Optional timer on weekends for those occasional work days

## License

Free to use and modify for personal or commercial purposes.

## Support

For issues or questions, please review the code comments or modify the script to suit your specific needs.

### I love you all!! Happy coding!!