# Workday Timer

A real-time productivity timer designed to help you manage your workday with structured activities and time blocks.

## What It Is

Workday Timer is a terminal-based time management tool that guides you through an 8-hour workday with predefined activities. Each activity runs for its actual duration in real-time, helping you stay focused and on schedule throughout your day.

The timer displays:
- Current activity progress with visual progress bars
- Overall day completion percentage
- Time remaining for each task
- Start and completion times for each activity
- A summary report at the end of your workday

## Features

- ☕ **Structured Schedule**: Pre-defined activities including meetings, deep work, breaks, and administrative tasks
- 📊 **Real-time Progress Tracking**: Live progress bars showing both current task and overall day completion
- ⏱️ **Accurate Timing**: Each activity runs for its actual duration (e.g., 0.5 hours = 30 real minutes)
- 🎨 **Beautiful Terminal UI**: Rich, colorful interface with emojis and formatted text
- 📋 **End-of-Day Summary**: Comprehensive report showing start/end times and total activities completed

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

2. **Run the script**:
   ```bash
   python workday_sim.py
   ```

   Or if you're using Python 3:
   ```bash
   python3 workday_sim.py
   ```

3. **The timer will start immediately** and guide you through your 8-hour workday

4. **To stop the timer early**, press `Ctrl+C` at any time

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
🏢 Workday Timer Starting
Start time: 09:00 AM
Total duration: 8 hours

Starting: ☕ Morning coffee & emails
Duration: 0.5 hours | Expected completion: 09:30 AM

⠋ ☕ Morning coffee & emails ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45% 0:08:15
⠋ 📅 Total Day Progress ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3% 7:42:30
```

## Use Cases

- **Time Management**: Stay accountable to your daily schedule
- **Focus Sessions**: Dedicated time blocks for deep work
- **Break Reminders**: Ensure you take regular breaks throughout the day
- **Productivity Tracking**: Visual representation of your workday progress
- **Remote Work**: Structure your day when working from home

## License

Free to use and modify for personal or commercial purposes.

## Support

For issues or questions, please review the code comments or modify the script to suit your specific needs.

### I love you all!! Happy coding!!