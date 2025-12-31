import os
from pyrogram import Client, filters
import jdatetime
from datetime import datetime

# دریافت اطلاعات از متغیرهای محیطی
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

app = Client(
    name="my_account",
    api_id=API_ID,
    api_hash=API_HASH
)

# تابع تاریخ
def get_persian_date():
    now = datetime.now()
    j_date = jdatetime.date.fromgregorian(date=now, locale='fa_IR')
    day_name = j_date.strftime("%A")
    formatted_date = f"{day_name} {j_date.year}/{j_date.month:02d}/{j_date.day:02d}"
    return formatted_date

# هندلر اصلی
@app.on_message(filters.outgoing & filters.text)
async def add_footer(client, message):
    try:
        text = message.text
        date_str = get_persian_date()
        new_text = f"{text}\n\n📅 {date_str}"
        await message.edit(new_text)
    except Exception as e:
        print(f"Error: {e}")

print("ربات در حال شروع...")
app.run()
