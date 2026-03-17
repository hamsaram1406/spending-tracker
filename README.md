# $$$ Spending Tracker $$$

A simple, clean web app to track your monthly spending by category. Built with Flask and SQLite.

## Features

-  Add spending entries with amount, category, date, and notes
-  View all entries organized by date
-  Organized grocery categories (Costco, Walmart, Target, Trader Joe's, Indian Store)
-  Delete individual entries or clear all data
-  Prevents future date entries
-  Timezone-aware (PDT support)
-  Persistent storage with SQLite database
-  Live online at https://spending-tracker-yiao.onrender.com

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** SQLite
- **Hosting:** Render (free tier)

## Installation & Setup

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/hamsaram1406/spending-tracker.git
cd spending-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open your browser and go to:
```
http://localhost:5000
```

## Project Structure

```
spending-tracker/
├── app.py                 # Flask backend with SQLite
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML/CSS/JavaScript
└── spending.db           # SQLite database (auto-created)
```

## Categories

The app comes with the following spending categories:

**Groceries:**
- Costco
- Indian Store
- Walmart
- Trader Joe's
- Target

**Other:**
- Food
- Transport
- Entertainment
- Utilities
- Shopping
- Health
- Other

## How to Use

1. **Add Entry:** Fill in the form with amount, category, date, and optional notes. Click "Add entry"
2. **View Entries:** All entries appear in "Recent entries" section, sorted by date
3. **Delete Entry:** Click the "Delete" button on any entry to remove it
4. **Clear All:** Click "Clear all data" to delete everything (use with caution!)

## Deployment

The app is deployed on Render's free tier. To redeploy after making changes:

1. Make changes locally and test with `python app.py`
2. Push to GitHub:
```bash
git add .
git commit -m "Your message"
git push
```
3. Go to [Render Dashboard](https://dashboard.render.com)
4. Click "Manual Deploy" on the spending-tracker service
5. Changes go live in 1-2 minutes

## Future Features

- Monthly spending summary
- Spending by category visualization (pie/bar charts)
- Budget alerts
- Search/filter entries
- Dark mode
- Export to CSV

## Notes

- Uses PDT timezone (can be adjusted in code)
- Prevents adding entries for future dates
- Data persists across sessions in SQLite database
- Free deployment means app may sleep after 15 min of inactivity (wakes up on next visit)

## Author

Created as a personal spending tracker project.

## License

MIT License - feel free to use and modify!
