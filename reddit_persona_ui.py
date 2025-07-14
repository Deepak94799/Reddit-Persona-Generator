import os
import praw
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
from transformers import pipeline
from fpdf import FPDF
import re
import unicodedata

# Load .env variables
load_dotenv()

# Reddit API Setup
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Load summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Remove emojis, smart quotes, and non-latin1 characters
def clean_text(text):
    # Normalize unicode characters (e.g. fancy quotes, em dashes)
    text = unicodedata.normalize("NFKD", text)
    # Replace smart quotes and special dashes with safe versions
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace('’', "'").replace('‘', "'")
    text = text.replace('–', '-').replace('—', '-')
    # Remove non-latin1 characters (e.g. emojis)
    return ''.join(c for c in text if ord(c) < 256)

# Scrape Reddit user data
def scrape_user_data(username, limit=50):
    try:
        user = reddit.redditor(username)
        posts, comments = [], []
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "type": "post",
                "text": f"{submission.title}\n{submission.selftext}",
                "subreddit": str(submission.subreddit),
                "url": f"https://www.reddit.com{submission.permalink}"
            })
        for comment in user.comments.new(limit=limit):
            comments.append({
                "type": "comment",
                "text": comment.body,
                "subreddit": str(comment.subreddit),
                "url": f"https://www.reddit.com{comment.permalink}"
            })
        return posts + comments
    except Exception as e:
        return []

# Chunk Reddit activity data
def chunk_data(data, chunk_size=5):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

# Build persona summary
def build_persona(data_chunks):
    full_persona = []
    for i, chunk in enumerate(data_chunks, 1):
        block = "\n\n".join([f"[{item['type'].upper()} in r/{item['subreddit']}]: {item['text']}" for item in chunk])
        try:
            summary = summarizer(block[:1024], max_length=180, min_length=80, do_sample=False)[0]['summary_text']
        except:
            summary = "Could not summarize this chunk."
        citations = "\n".join([f"- [{item['type'].capitalize()} in r/{item['subreddit']}]({item['url']})" for item in chunk])
        full_persona.append((i, summary, citations))
    return full_persona

# Save to PDF
def save_as_pdf(username, persona):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, clean_text(f"Reddit User Persona Report\nUsername: {username}\n\n"))
    for section in persona:
        i, summary, citations = section
        pdf.multi_cell(0, 10, clean_text(f"{i}. Insights from chunk {i}\n{summary}\n\nCitations:\n{citations}\n\n"))
    filename = f"{username}_persona.pdf"
    pdf.output(filename)
    return filename

# Handle one Reddit user
def process_user(username):
    data = scrape_user_data(username)
    if not data:
        return None
    persona = build_persona(chunk_data(data))
    return save_as_pdf(username, persona)

# Main GUI function
def run_generator():
    usernames_text = input_box.get("1.0", tk.END).strip()
    if not usernames_text:
        messagebox.showwarning("Input Missing", "Please enter at least one Reddit profile URL.")
        return

    urls = [u.strip() for u in usernames_text.splitlines() if u.strip()]
    for url in urls:
        if not url.startswith("https://www.reddit.com/user/"):
            messagebox.showerror("Invalid URL", f"Invalid Reddit profile URL: {url}")
            continue
        username = url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
        status_box.insert(tk.END, f"Processing {username}...\n")
        filename = process_user(username)
        if filename:
            status_box.insert(tk.END, f"Saved: {filename}\n")
        else:
            status_box.insert(tk.END, f"Failed to process {username}\n")
        status_box.insert(tk.END, "----------------------------\n")
        status_box.see(tk.END)
    messagebox.showinfo("Done", "All profiles processed.")

# Build the GUI
root = tk.Tk()
root.title("Reddit Persona Generator (UI PDF Multi)")
root.geometry("600x500")

tk.Label(root, text="Paste one or more Reddit profile URLs (one per line):").pack()
input_box = tk.Text(root, height=10, width=70)
input_box.pack(pady=10)

tk.Button(root, text="Generate Persona PDFs", command=run_generator).pack(pady=5)
status_box = tk.Text(root, height=15, width=70)
status_box.pack(pady=10)

root.mainloop()
