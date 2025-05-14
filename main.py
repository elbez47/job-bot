from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7429376542:AAEWlmZjbu7eI8ULf6Bw0SG916evwdwLNJ8"

# قائمة الولايات الجزائرية (47 ولاية)
locations = [
    "أدرار", "الشلف", "الأغواط", "باتنة", "بجاية", "بليدة", "بومرداس",
    "تبسة", "تلمسان", "تيبازة", "قسنطينة", "الجزائر", "المدية", "مستغانم",
    "مسيلة", "معسكر", "ورقلة", "وهران", "البيض", "الطارف", "تندوف", "تيسمسيلت",
    "الجلفة", "سطيف", "سيدي بلعباس", "سوق أهراس", "عنابة", "قالمة", "قسنطينة",
    "ميلة", "عين الدفلى", "المسيلة", "النعامة", "خنشلة", "تيارت", "الواد", 
    "غرداية",
]

# القطاعات المختلفة
sectors = [
    "الصناعة", "الفلاحة", "الإدارة", "التسويق", "البرمجيات و إعلام الآلات",
    "التصميم", "التجارة", "التعليم", "النقل"
]

# دالة الرد على أمر /start مع عرض الأزرار
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("اختيار المكان", callback_data='choose_location')],
        [InlineKeyboardButton("اختيار قطاع الوظيفة", callback_data='choose_sector')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "مرحبا... رب أتيـدج الرزق الحلال 🤲\nاختَر ما ترغب به:",
        reply_markup=reply_markup
    )

# معالجة الأزرار التي يضغط عليها المستخدم
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # اختيار المكان
    if query.data == 'choose_location':
        keyboard = [[InlineKeyboardButton(location, callback_data=f'location_{location}')] for location in locations]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="الوظائف حسب الولاية:",
            reply_markup=reply_markup
        )

    # اختيار قطاع الوظيفة
    elif query.data == 'choose_sector':
        keyboard = [[InlineKeyboardButton(sector, callback_data=f'sector_{sector}')] for sector in sectors]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="الوظائف حسب القطاع:",
            reply_markup=reply_markup
        )

    # نتائج اختيار المكان
    elif query.data.startswith('location_'):
        location = query.data.split('_')[1].capitalize()
        await query.edit_message_text(text=f"لقد اخترت ولاية {location}. الآن اختر قطاع الوظيفة.")

    # نتائج اختيار القطاع
    elif query.data.startswith('sector_'):
        sector = query.data.split('_')[1].capitalize()
        await query.edit_message_text(text=f"لقد اخترت قطاع {sector}. يمكنك الآن التقديم للوظائف في هذا المجال.")

# تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("✅ البوت يعمل الآن، انتقل لتليغرام وجرب /start")
    app.run_polling()

    app.add_handler(CallbackQueryHandler(button))
    print("✅ البوت يعمل الآن، انتقل لتليغرام وجرب /start")
    app.run_polling()
