
```markdown
# Reddit User Persona Generator

This project generates a detailed **user persona** from a given Reddit profile by analyzing their recent posts and comments. It uses the Reddit API (`praw`) to fetch user data and Google's Gemini 2.5 Flash model to analyze the data and generate a structured persona.

---

## 🧠 What It Does

For any given Reddit profile URL like:
```

[https://www.reddit.com/user/kojied/](https://www.reddit.com/user/kojied/)

````

It will:
1. Fetch the user’s **latest 50 comments** and **20 posts**.
2. Build a prompt using their text content.
3. Send it to **Gemini 2.5 Flash** to analyze and generate a persona.
4. Save the persona (with citations) to a `.txt` file in the `output/` folder.

---

## 🛠 Technologies Used

- Python 3.10+
- [PRAW](https://praw.readthedocs.io/en/stable/) (Reddit API wrapper)
- [Google Generative AI](https://ai.google.dev/)
- dotenv for secret management
- Gemini 2.5 Flash model

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/reddit-persona-generator.git
cd reddit-persona-generator
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup `.env` File

Create a `.env` file in the root directory and add your credentials:

```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_custom_user_agent
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 🚀 Usage

To generate a persona:

```bash
python persona_generator.py
```

Then enter the Reddit username (without `u/` or the full URL).

Example input:

```
kojied
```

A file will be saved as:

```
output/kojied.txt
```

---

## 📁 Output

Two sample outputs are already included:

```
output/kojied.txt
output/Hungry-Move-6603.txt
```

Each `.txt` file contains:

* Inferred interests, tone, style, occupation
* Direct quotes and citations (with Reddit URLs)

---

## 🧪 Example

Example prompt used internally by the model:

> "Reddit User: u/kojied...
> Based on these posts and comments, generate a persona...
> Cite all claims with Reddit URLs."

---

## 📜 License

This project was created solely as part of an internship assignment for BeyondChats.

All code and outputs are original work and intended only for evaluation.
Please do not reuse, copy, or redistribute without permission.

---
