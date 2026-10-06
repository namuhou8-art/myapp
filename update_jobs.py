import json
from datetime import datetime

JOBS_FILE = "jobs.json"

def load_jobs():
    try:
        with open(JOBS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            return data

    except Exception:
        pass

    return []


def save_jobs(jobs):
    with open(JOBS_FILE, "w", encoding="utf-8") as f:
        json.dump(
            jobs,
            f,
            ensure_ascii=False,
            indent=2
        )


jobs = load_jobs()

print("عدد الوظائف الحالية:", len(jobs))
print("وقت التحديث:", datetime.now().isoformat())

save_jobs(jobs)

print("تم تحديث jobs.json بنجاح")
