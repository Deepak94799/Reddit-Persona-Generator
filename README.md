🧠 Reddit Persona Generator
Generate insightful persona summaries from Reddit users’ recent activity using NLP and deliver them in professional PDF reports — all via a simple GUI.

📌 Overview
Reddit Persona Generator is a Python-based tool that scrapes a user's recent Reddit posts and comments, summarizes them using a Transformer model, and compiles the findings into a well-formatted PDF report. It features a user-friendly GUI built with Tkinter and supports batch processing for multiple profiles.

✨ Features
🔍 Reddit Scraper: Fetches the latest 50 posts and 50 comments from each Reddit profile.

🧠 Text Summarization: Uses the sshleifer/distilbart-cnn-12-6 model from Hugging Face to summarize user activity in chunks.

🖼️ GUI Interface: Clean Tkinter GUI for easy input and status monitoring.

📄 PDF Report Generation: Generates detailed reports including summaries and direct links to original content.

🧹 Data Cleaning: Automatically removes emojis and normalizes Unicode characters for PDF compatibility.

📦 Batch Mode: Paste multiple Reddit profile URLs to generate multiple reports in one go.

⚙️ How It Works
Input: Enter one or more Reddit profile URLs into the GUI text box (one per line).

Scraping: The app uses PRAW to retrieve each user's latest 50 posts and 50 comments.

Chunking & Summarization: Content is chunked and passed through the summarization model.

PDF Output: Each user's summarized persona is saved as {username}_persona.pdf.

Status Feedback: Real-time processing updates are shown in the GUI.

📁 Requirements
Python 3

PRAW

Tkinter

python-dotenv

transformers (Hugging Face)

fpdf2

torch or tensorflow (backend for Transformers)

Install dependencies via:

bash
Copy
Edit
pip install praw python-dotenv transformers fpdf2 torch
🚀 Setup Instructions
1. Clone or Download
bash
Copy
Edit
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
2. Create a Reddit App
Visit: Reddit App Preferences

Click "are you a developer? create an app..."

Fill the form:

Name: e.g., PersonaGenerator

Type: script

Redirect URI: http://localhost:8080

Click "Create app"

Copy your client_id and client_secret.

3. Configure .env
In the root directory, create a .env file with:

ini
Copy
Edit
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=PersonaGenerator/0.1 by YourUsername
🧑‍💻 How to Run
Launch the application:

bash
Copy
Edit
python reddit_persona_ui.py
Then:

Paste full Reddit profile URLs (one per line).

Click "Generate Persona PDFs".

PDFs will be saved in the current directory.

📌 Example
arduino
Copy
Edit
https://www.reddit.com/user/exampleuser1
https://www.reddit.com/user/exampleuser2
Output:

exampleuser1_persona.pdf

exampleuser2_persona.pdf
