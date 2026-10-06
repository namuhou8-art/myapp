import json
import urllib.request
import re
from html import unescape
from datetime import datetime

OUTPUT = "jobs.json"

SOURCES = [
    {
        "title": "كاشير / مبيعات - الحسني هوم سنتر",
        "company": "الحسني هوم سنتر",
        "location": "النجف - بين حي الزهراء وحي الأمير",
        "salary": "500,000 - 1,000,000 دينار",
        "experience": "خبرة مطلوبة",
        "training": "غير مذكور",
        "date": "2026-10-05",
        "description": "وظائف كاشير ومبيعات في النجف",
        "source": "https://honjob.com/job/%D9%81%D8%B1%D8%B5-%D8%B9%D9%85%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%AD%D8%B3%D9%86%D9%8A-%D9%87%D9%88%D9%85-%D8%B3%D9%86%D8%AA%D8%B1-%D8%A8%D8%A7%D9%84%D9%86%D8%AC%D9%81/"
    },
    {
        "title": "كاشير وموظفو مطعم",
        "company": "جكن الشيخ - شركة الأفق الذهبي",
        "location": "النجف الأشرف",
        "salary": "يحدد في المقابلة + حوافز",
        "experience": "يمكن قبول المبتدئين",
        "training": "مناسب للمبتدئين",
        "date": "2026-09-10",
        "description": "كاشير وتجهيز وشواء وسنتر",
        "source": "https://honjob.com/job/%D9%81%D8%B1%D8%B5-%D8%B9%D9%85%D9%84-%D9%81%D9%8A-%D9%85%D8%B7%D8%B9%D9%85-%D8%AC%D9%83%D9%86-%D8%A7%D9%84%D8%B4%D9%8A%D8%AE-%D8%A8%D8%A7%D9%84%D9%86%D8%AC%D9%81-%D8%A7%D9%84%D8%A3%D8%B4%D8%B1/"
    }
]

def source_is_available(url):
    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        with urllib.request.urlopen(
            request,
            timeout=20
        ) as response:
            return response.status == 200

    except Exception as error:
        print("تعذر فحص المصدر:", error)
        return False


jobs = []

for job in SOURCES:

    print("فحص:", job["title"])

    if source_is_available(job["source"]):
        job["verified"] = True
    else:
        job["verified"] = False

    job["checked_at"] = datetime.utcnow().isoformat()

    jobs.append(job)


jobs.sort(
    key=lambda x: x.get("date", ""),
    reverse=True
)

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        jobs,
        file,
        ensure_ascii=False,
        indent=2
    )


print("تم إنشاء jobs.json")
print("عدد الوظائف:", len(jobs))
