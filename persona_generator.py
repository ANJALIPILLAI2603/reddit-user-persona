import praw
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Reddit API setup
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

# Gemini API setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def fetch_reddit_data(username):
    user = reddit.redditor(username)
    comments = []
    posts = []

    for comment in user.comments.new(limit=50):
        comments.append({
            "text": comment.body,
            "permalink": f"https://www.reddit.com{comment.permalink}"
        })

    for submission in user.submissions.new(limit=20):
        posts.append({
            "title": submission.title,
            "text": submission.selftext,
            "url": f"https://www.reddit.com{submission.permalink}"
        })

    return comments, posts

def build_prompt(username, comments, posts):
    text = f"Reddit User: u/{username}\n\n"
    text += "Recent Comments:\n"
    for c in comments:
        text += f"- {c['text'][:300]} (source: {c['permalink']})\n"

    text += "\nRecent Posts:\n"
    for p in posts:
        text += f"- {p['title']} — {p['text'][:300]} (source: {p['url']})\n"

    text += "\n\nInstructions:\n"
    text += "Write a detailed Reddit user persona. For every insight or claim you make (like interests, tone, occupation, beliefs), directly quote or paraphrase the Reddit user's own words from the comments/posts above. After each quote or paraphrase, cite the source URL in parentheses. Do NOT invent any facts. Only use what is explicitly available in the comments/posts above."
    text += "- Name (if mentioned)\n- Interests\n- Writing style\n- Tone\n"
    text += "- Occupation (if inferred)\n- Strong beliefs/opinions\n"
    text += "- Reddit usage pattern\n\nAlso, **cite** specific comment/post content."
    text += "\n\nAppendix: Full comments and posts are listed above to help you build citations accurately."


    return text

def generate_persona(prompt):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

def save_to_file(username, persona_text):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{username}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"[✅] Persona saved to: {path}")

if __name__ == "__main__":
    username = input("Enter Reddit username (without u/): ").strip()
    comments, posts = fetch_reddit_data(username)
    prompt = build_prompt(username, comments, posts)
    persona = generate_persona(prompt)
    save_to_file(username, persona)
