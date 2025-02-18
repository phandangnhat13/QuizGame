# Quiz Game

This is a simple command-line quiz game that challenges users to answer questions about countries and their capitals. The game pulls data from a Google Sheets document, tracks user performance, and stores results in a log.

## Features
- Randomly selects questions from the sheet.
- Tracks correct answers and updates statistics in real-time.
- Logs test attempts and scores.

## Setup
1. Clone this repository.
2. Install required dependencies:
   ```bash
   pip install gspread termcolor
3. Set up the Google Sheets API and download your secret_key.json.

## Run the Game
Execute the script:
  ```bash
   python Quiz_Game.py
