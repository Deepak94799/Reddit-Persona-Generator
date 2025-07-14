# 🧠 Reddit Persona Generator

Generate insightful persona summaries from Reddit users’ recent activity using NLP and deliver them in professional PDF reports — all via a simple GUI.

---

## 📌 Overview

**Reddit Persona Generator** is a Python-based tool that scrapes a user's recent Reddit posts and comments, summarizes them using a Transformer model, and compiles the findings into a well-formatted PDF report. It features a user-friendly GUI built with Tkinter and supports batch processing for multiple profiles.

---

## ✨ Features

- 🔍 **Reddit Scraper**: Fetches the latest 50 posts and 50 comments from each Reddit profile.
- 🧠 **Text Summarization**: Uses the `sshleifer/distilbart-cnn-12-6` model from Hugging Face to summarize user activity in chunks.
- 🖼️ **GUI Interface**: Clean Tkinter GUI for easy input and status monitoring.
- 📄 **PDF Report Generation**: Generates detailed reports including summaries and direct links to original content.
- 🧹 **Data Cleaning**: Automatically removes emojis and normalizes Unicode characters for PDF compatibility.
- 📦 **Batch Mode**: Paste multiple Reddit profile URLs to generate multiple reports in one go.

---

## ⚙️ How It Works

1. **Input**: Enter one or more Reddit profile URLs into the GUI text box (one per line).
2. **Scraping**: The app uses PRAW to retrieve each user's latest 50 posts and 50 comments.
3. **Chunking & Summarization**: Content is chunked and passed through the summarization model.
4. **PDF Output**: Each user's summarized persona is saved as `{username}_persona.pdf`.
5. **Status Feedback**: Real-time processing updates are shown in the GUI.

---

## 📁 Requirements

- Python 3
- [PRAW](https://praw.readthedocs.io/)
- Tkinter
- `python-dotenv`
- `transformers` (Hugging Face)
- `fpdf2`
- `torch` or `tensorflow` (backend for Transformers)

Install dependencies via:

```bash
pip install praw python-dotenv transformers fpdf2 torch
