# DAY 12: Catch-up Logic & Performance Tracking
# Combining skipped days into one logic check

exam_updates = {
    "Feb 6": {"Status": "Studying", "Focus": "Theory"},
    "Feb 7": {"Status": "Revision", "Focus": "Lab Programs"},
    "Feb 8": {"Status": "Exam Day", "Focus": "External Paper"}
}
print("--- RECOVERY LOG ---")
for date, details in exam_updates.items():
    status = details["Status"]
    focus = details["Focus"]
    print(f"Date: {date} | Activity: {status} | Focus Area: {focus}")
days_logged = len(exam_updates)
print(f"\nStreak status: Logged {days_logged} days of activity today.")