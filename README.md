# CodeAlpha_Voice_Assistant
This code is for a voice assistant application, named "APlus", that combines speech recognition and text-to-speech to help users with various tasks such as scheduling and performing Google searches. Here's a breakdown of how it works:

Key Components:
Speech Recognition:

The program uses the speech_recognition library to listen to user input via the microphone.
It listens to the user's speech and converts it into text using Google’s speech-to-text API.
Text-to-Speech (TTS):

The pyttsx3 library is used for text-to-speech functionality, allowing the assistant to speak responses back to the user.
The assistant speaks in a moderate rate (135 words per minute).
Task Scheduling:

The assistant can schedule tasks using the schedule library, allowing the user to set tasks that repeat at regular intervals (seconds, minutes, hours, or days).
The tasks include a description of what the user wants to do and how often the task should repeat.
The word2num library is used to convert text-based numbers (e.g., "five") into actual integers.
Google Search:

The assistant can perform a web search using the webbrowser module, launching the search in Google Chrome or the default web browser if Chrome is not installed.
Concurrency:

The code runs the task scheduling in a separate thread to ensure it doesn't block the rest of the program.
Workflow:
Initialization:

The assistant introduces itself and asks for the user's name. If the name is successfully recognized, it proceeds; otherwise, it asks again.
It explains its capabilities, including scheduling tasks and performing Google searches.
Main Interaction Loop:

After receiving the user’s command (e.g., "search on Google" or "schedule"), it executes the relevant functionality.

Google Search:

If the user asks to search on Google, the assistant prompts for a search query and opens the Google search results in the browser.
Scheduling Tasks:

If the user wants to schedule a task, the assistant asks for the task description, how often to repeat it, and the time period (e.g., seconds, minutes).
The assistant schedules the task and confirms its addition.
The user can also check their scheduled tasks and stop the scheduling process.
Task Execution & Updates:

The assistant keeps track of scheduled tasks and can tell the user all their scheduled tasks.
The tasks are executed periodically based on the user’s settings.
Exiting the Program:

The assistant listens for commands like "stop", "finally", "finish", or "end" to end the interaction.
The assistant thanks the user and says goodbye before exiting.
Key Features:
Voice-based Interaction: Allows users to interact with the assistant via voice commands.
Task Scheduling: Users can add, view, and manage scheduled tasks that repeat over different intervals (seconds, minutes, hours, or days).
Google Search: Users can search for information on Google via voice commands.
Multithreading: The scheduling functionality runs in a separate thread to avoid blocking the assistant’s primary tasks.
Potential Issues in the Code:
In the section for Google search (search_google), the query is not correctly passed to the search_google function. The line query = time.sleep(1) should instead capture the user's spoken input for the search query.
Some error handling for speech recognition could be enhanced, especially in cases where speech input is unclear or inaudible.
