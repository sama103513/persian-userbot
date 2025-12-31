import jdatetime
from datetime import datetime
import pytz
from pyrogram import Client, filters

# ---------------------------------------------------------
# تنظیمات اکانت یوزر بات
# ---------------------------------------------------------
API_ID = 12345678  # API ID اختصاصی خود را اینجا بگذارید
API_HASH = "your_api_hash_here"  # API Hash اختصاصی خود را اینجا بگذارید

# نام فایل نشست (Session) - بعد از لاگین فایل my_account.session ساخته می‌شود
SESSION_NAME = "my_account"

# ---------------------------------------------------------
# ایجاد کلاینت یوزر بات
# ---------------------------------------------------------
app = Client(
    name=SESSION_NAME,
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
# هندلر ۱: وقتی شما به دیگران پیام می‌دهید (Outgoing)
# ---------------------------------------------------------
@app.on_message(filters.outgoing)
async def add_footer_to_my_messages(client, message):
    # اگر متن پیام خالی نباشد
    if message.text:
        original_text = message.text
        date_str = get_persian_date()
        new_text = f"{original_text}\n\n📅 {date_str}"
        
        # ویرایش پیام خودتان و اضافه کردن تاریخ
        await message.edit(new_text)

# ---------------------------------------------------------
# هندلر ۲: وقتی دیگران به شما پیام می‌دهند (Incoming)
# ---------------------------------------------------------
@app.on_message(filters.incoming)
async def reply_to_others(client, message):
    # فقط اگر کاربر دکمه استارت را زده باشد یا هر شرطی که بخواهید
    # برای حالت ساده، به پیام‌های خصوصی پاسخ می‌دهیم
    if message.chat.type == "private" and message.text:
        # می‌توانید پیام کاربر را پاک کنید یا جواب دهید
        # اینجا فقط جواب ساده می‌دهیم که تاریخش دارد
        date_str = get_persian_date()
        reply_text = f"پیام شما دریافت شد.\n\n📅 {date_str}"
        await message.reply(reply_text)

# ---------------------------------------------------------
# اجرای یوزر بات
# ---------------------------------------------------------
print("در حال اجرای یوزر بات...")
print("لطفاً شماره تلفن خود را وارد کنید:")
app.run()