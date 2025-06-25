# automated-data-entry-task


Description:
This project automates the process of fetching and saving post data from an online API into text files using Notepad, leveraging BotCity Maestro for task orchestration and PyAutoGUI for desktop interaction.

 Key Features:
Integrates with JSONPlaceholder (mock API) to fetch post data by ID.

Opens Notepad, types in the post title and body, and saves it to a .txt file.

Automates saving using pyautogui keystrokes and mouse simulation.

Reports task status to BotCity Maestro, including total, successful, and failed entries.

Includes exception handling for API errors, file save errors, and desktop automation interruptions.


Technologies Used:

Python 3.x

BotCity Maestro SDK

PyAutoGUI

Requests
