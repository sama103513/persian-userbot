import os
import jdatetime
from datetime import datetime
import pytz
from pyrogram import Client, filters

# ---------------------------------------------------------
# دریافت اطلاعات حساس از Environment Variables (ایمن)
# ---------------------------------------------------------
# در Railway این دو را به صورت متغیر وارد می‌کنیم
API_ID = int(os.environ.get("31586956"))
API_HASH = os.environ.get("f36c0753be9379b0f40d9a6c9077e10e")

# ---------------------------------------------------------
# ایجاد کلاینت
# ---------------------------------------------------------
app = Client(
    name="my_account",  # این نام باید دقیقاً با نام فایل session یکی باشد
    api_id=API_ID,
    api_hash=API_HASH
)

# ---------------------------------------------------------
# تابع دریافت تاریخ
# ---------------------------------------------------------
def get_persian_date():
    tehran_tz = pytz.timezone("Asia/Tehran")
    now = datetime.now(tehran_tz)
    j_date = jdatetime.date.fromgregorian(date=now, locale='fa_IR')
    day_name = j_date.strftime("%A")
    formatted_date = f"{day_name} {j_date.year}/{j_date.month:02d}/{j_date.day:02d}"
    return formatted_date

# ---------------------------------------------------------
# هندلر اصلی
# ---------------------------------------------------------
@app.on_message(filters.outgoing & filters.text)
async def add_footer(client, message):
    try:
        text = message.text
        date_str = get_persian_date()
        new_text = f"{text}\n\n📅 {date_str}"
        await message.edit(new_text)
    except Exception as e:
        print(f"Error editing message: {e}")

print("یوزر بات با موفقیت اجرا شد...")
app.run()