# مدیریت نیازمندی‌های غیرکارکردی (NFRs) در طراحی سیستم

## مقدمه
نیازمندی‌های غیرکارکردی (Non-Functional Requirements - NFRs) جنبه‌هایی از یک سیستم هستند که عملکرد کلی، کیفیت و تجربه کاربری آن را تعریف می‌کنند، اما مستقیماً به قابلیت‌های خاص (مانند ویژگی‌های یک اپلیکیشن) مربوط نمی‌شوند. این نیازمندی‌ها تأثیر عمیقی بر معماری سیستم دارند و در طراحی سیستم‌های مقیاس‌پذیر، قابل‌اعتماد و امن نقش کلیدی ایفا می‌کنند. این سند به بررسی تعریف NFRها، اهمیت آن‌ها، روش‌های شناسایی و اولویت‌بندی، استراتژی‌های طراحی، مستندسازی، چالش‌ها و مثال‌های کاربردی برای مهندسان نرم‌افزار فارسی‌زبان که برای مصاحبه‌های طراحی سیستم آماده می‌شوند، می‌پردازد.

---

## تعریف و نمونه‌های نیازمندی‌های غیرکارکردی

نیازمندی‌های غیرکارکردی مشخص می‌کنند که یک سیستم باید **چگونه** عمل کند، در حالی که نیازمندی‌های کارکردی (Functional Requirements) مشخص می‌کنند که سیستم **چه کاری** انجام می‌دهد. NFRها معیارهای کیفیتی هستند که عملکرد، پایداری و تجربه کاربری سیستم را تضمین می‌کنند.

### نمونه‌های رایج NFRها
1. **مقیاس‌پذیری (Scalability):**
   - توانایی سیستم برای مدیریت افزایش بار (مانند تعداد کاربران یا درخواست‌ها) بدون افت عملکرد.
   - مثال: یک اپلیکیشن تجارت الکترونیک باید بتواند 10,000 کاربر همزمان را در زمان فروش ویژه مدیریت کند.
2. **قابلیت اطمینان (Reliability):**
   - توانایی سیستم برای ارائه خدمات بدون قطعی یا خطا.
   - مثال: تضمین آپ‌تایم 99.99% برای یک سرویس بانکی آنلاین.
3. **عملکرد (Performance):**
   - سرعت و کارایی سیستم در پاسخ به درخواست‌ها.
   - مثال: زمان پاسخ‌گویی API باید کمتر از 200 میلی‌ثانیه باشد.
4. **امنیت (Security):**
   - حفاظت از داده‌ها و سیستم در برابر دسترسی غیرمجاز یا حملات.
   - مثال: رمزنگاری داده‌های حساس کاربران با استفاده از AES-256.
5. **قابلیت نگهداری (Maintainability):**
   - سهولت در به‌روزرسانی، عیب‌یابی و توسعه سیستم.
   - مثال: طراحی ماژولار برای کاهش زمان موردنیاز برای افزودن ویژگی‌های جدید.

---

## اهمیت NFRها در طراحی سیستم
NFRها تأثیر مستقیمی بر معماری سیستم دارند و می‌توانند موفقیت یا شکست یک پروژه را تعیین کنند. دلایل اهمیت NFRها:
- **تجربه کاربری:** عملکرد ضعیف یا قطعی‌های مکرر می‌توانند اعتماد کاربران را کاهش دهند.
- **هزینه‌ها:** عدم توجه به مقیاس‌پذیری ممکن است منجر به بازطراحی پرهزینه سیستم شود.
- **تطابق قانونی:** امنیت و حریم خصوصی برای رعایت استانداردهایی مانند GDPR ضروری هستند.
- **تصمیم‌گیری معماری:** انتخاب معماری (مانند میکروسرویس‌ها در مقابل مونولیت) اغلب تحت تأثیر NFRها قرار می‌گیرد.
  - مثال: برای مقیاس‌پذیری بالا، ممکن است معماری میکروسرویس انتخاب شود، در حالی که برای سادگی و قابلیت نگهداری، معماری مونولیت مناسب‌تر باشد.

---

## روش‌های شناسایی و اولویت‌بندی NFRها

### شناسایی NFRها
1. **گفت‌وگو با ذی‌نفعان:**
   - با مشتریان، کاربران نهایی و تیم‌های تجاری صحبت کنید تا نیازهای کیفیتی (مانند آپ‌تایم یا سرعت) مشخص شوند.
   - مثال: کاربران یک اپلیکیشن پخش ویدئو انتظار تأخیر کمتر از 2 ثانیه برای بارگذاری ویدئو دارند.
2. **تحلیل رقبا:**
   - بررسی سیستم‌های مشابه برای شناسایی استانداردهای صنعتی (مانند آپ‌تایم 99.9% در صنعت تجارت الکترونیک).
3. **استانداردها و قوانین:**
   - شناسایی الزامات قانونی مانند PCI-DSS برای سیستم‌های پرداخت یا GDPR برای حفاظت از داده‌ها.
4. **سناریوهای کاربری:**
   - تحلیل سناریوهای واقعی (مانند افزایش بار در فروش ویژه) برای شناسایی نیازهای مقیاس‌پذیری و عملکرد.

### اولویت‌بندی NFRها
- **چارچوب MoSCoW:**
  - **Must have:** ضروری (مانند امنیت برای یک اپلیکیشن بانکی).
  - **Should have:** مهم اما غیرضروری (مانند عملکرد بالا برای یک داشبورد تحلیلی).
  - **Could have:** مطلوب اما کم‌اولویت (مانند پشتیبانی از چندین زبان).
  - **Won’t have:** در حال حاضر غیرضروری.
- **تحلیل ریسک:** اولویت‌بندی NFRهایی که عدم رعایت آن‌ها بیشترین تأثیر منفی را دارد (مانند امنیت در برابر مقیاس‌پذیری).
- **ماتریس وزن‌دهی:** اختصاص امتیاز به NFRها بر اساس تأثیر بر کاربر، هزینه پیاده‌سازی و الزامات قانونی.

---

## استراتژی‌های طراحی برای پاسخ به NFRها

1. **مقیاس‌پذیری:**
   - **مقیاس‌پذیری عمودی (Vertical Scaling):** افزایش منابع سرور (مانند CPU یا RAM).
   - **مقیاس‌پذیری افقی (Horizontal Scaling):** افزودن سرورهای بیشتر با استفاده از Load Balancer.
   - **مثال:** استفاده از Kubernetes برای مقیاس‌بندی خودکار میکروسرویس‌ها.
2. **قابلیت اطمینان:**
   - استفاده از افزونگی (Redundancy) مانند سرورهای پشتیبان یا پایگاه داده‌های Replica.
   - پیاده‌سازی مکانیزم‌های Failover برای جابجایی خودکار به سرورهای سالم.
   - **مثال:** استفاده از AWS RDS با Multi-AZ برای پایگاه داده‌های مقاوم در برابر خرابی.
3. **عملکرد:**
   - استفاده از کش (مانند Redis یا Memcached) برای کاهش تأخیر.
   - بهینه‌سازی کوئری‌های پایگاه داده و استفاده از ایندکس‌ها.
   - **مثال:** استفاده از CDN برای ارائه سریع‌تر محتوا به کاربران جهانی.
4. **امنیت:**
   - رمزنگاری داده‌ها در حالت سکون (با AES) و در حال انتقال (با TLS).
   - پیاده‌سازی احراز هویت چندمرحله‌ای (MFA) و کنترل دسترسی مبتنی بر نقش (RBAC).
   - **مثال:** استفاده از AWS KMS برای مدیریت کلیدهای رمزنگاری.
5. **قابلیت نگهداری:**
   - طراحی ماژولار با استفاده از اصول SOLID.
   - مستندسازی کد و معماری برای سهولت عیب‌یابی.
   - **مثال:** استفاده از CI/CD برای استقرار سریع و خودکار تغییرات.

---

## مستندسازی و ارتباط NFRها در مصاحبه‌های طراحی سیستم

### نحوه مستندسازی
- **استفاده از قالب استاندارد:**
  - هر NFR را با تعریف، معیار موفقیت و راه‌حل پیشنهادی مستند کنید.
  - مثال: **مقیاس‌پذیری:** سیستم باید 100,000 درخواست در ثانیه را مدیریت کند؛ راه‌حل: استفاده از Load Balancer و معماری میکروسرویس.
- **دیاگرام‌های معماری:**
  - از دیاگرام‌ها (مانند C4 یا UML) برای نمایش تأثیر NFRها بر معماری استفاده کنید.
  - مثال: نمایش یک Load Balancer و سرورهای مقیاس‌پذیر در یک دیاگرام.
- **معیارهای قابل اندازه‌گیری:**
  - NFRها را با معیارهای مشخص (مانند آپ‌تایم 99.9% یا زمان پاسخ‌گویی کمتر از 200ms) تعریف کنید.

### نحوه ارتباط در مصاحبه
1. **شروع با نیازمندی‌ها:**
   - ابتدا NFRهای کلیدی را با مصاحبه‌کننده تأیید کنید (مانند مقیاس‌پذیری یا امنیت).
2. **توضیح تأثیر بر طراحی:**
   - برای هر NFR، توضیح دهید که چگونه معماری را تحت تأثیر قرار می‌دهد.
   - مثال: برای مقیاس‌پذیری، از معماری میکروسرویس و کش استفاده می‌کنم.
3. **تعادل بین NFRها:**
   - نشان دهید که چگونه تعادل بین NFRها (مانند عملکرد در مقابل هزینه) را مدیریت می‌کنید.
4. **ارائه مثال‌های واقعی:**
   - از سناریوهای واقعی (مانند سیستم‌های تجارت الکترونیک) برای توضیح راه‌حل‌ها استفاده کنید.

---

## چالش‌های رایج و بهترین روش‌ها

### چالش‌ها
1. **ابهام در تعریف NFRها:**
   - ذی‌نفعان ممکن است معیارهای واضحی ارائه ندهند (مانند "سیستم باید سریع باشد").
   - **راه‌حل:** با پرس‌وجو و تعریف معیارهای قابل اندازه‌گیری (مانند زمان پاسخ کمتر از 200ms) ابهام را برطرف کنید.
2. **تعارض بین NFRها:**
   - مثال: افزایش امنیت ممکن است عملکرد را کاهش دهد.
   - **راه‌حل:** استفاده از چارچوب اولویت‌بندی مانند MoSCoW و بحث با ذی‌نفعان.
3. **هزینه‌های پیاده‌سازی:**
   - برخی NFRها (مانند مقیاس‌پذیری افقی) هزینه‌بر هستند.
   - **راه‌حل:** تحلیل هزینه-فایده و انتخاب راه‌حل‌های مقرون‌به‌صرفه (مانند استفاده از سرویس‌های ابری).
4. **عدم مستندسازی مناسب:**
   - NFRها ممکن است در طول توسعه نادیده گرفته شوند.
   - **راه‌حل:** مستندسازی دقیق و بررسی دوره‌ای NFRها در طول چرخه توسعه.

### بهترین روش‌ها
1. **تعریف زودهنگام NFRها:**
   - در مراحل اولیه پروژه، NFRها را با ذی‌نفعان نهایی کنید.
2. **اندازه‌گیری و اعتبارسنجی:**
   - از ابزارهای مانیتورینگ (مانند Prometheus) برای اعتبارسنجی NFRها در محیط تولید استفاده کنید.
3. **تست NFRها:**
   - تست‌های بار (Load Testing) و تست‌های امنیتی برای اطمینان از رعایت NFRها انجام دهید.
4. **طراحی انعطاف‌پذیر:**
   - معماری را به‌گونه‌ای طراحی کنید که امکان بهبود NFRها (مانند مقیاس‌پذیری) در آینده وجود داشته باشد.
5. **همکاری تیمی:**
   - تیم‌های توسعه، عملیات و امنیت را در تعریف و پیاده‌سازی NFRها دخیل کنید.

---

## مثال‌های کاربردی تأثیر NFRها بر طراحی سیستم

1. **سناریو: اپلیکیشن تجارت الکترونیک**
   - **نیازمندی غیرکارکردی:** مقیاس‌پذیری برای مدیریت 50,000 کاربر همزمان در فروش ویژه.
   - **راه‌حل طراحی:**
     - استفاده از Load Balancer برای توزیع ترافیک.
     - کش با Redis برای کاهش بار پایگاه داده.
     - مقیاس‌بندی افقی با Kubernetes.
   - **تأثیر:** کاهش زمان پاسخ و افزایش آپ‌تایم در زمان اوج ترافیک.

2. **سناریو: اپلیکیشن بانکی**
   - **نیازمندی غیرکارکردی:** امنیت برای حفاظت از داده‌های مالی.
   - **راه‌حل طراحی:**
     - رمزنگاری داده‌ها با AES-256 و TLS 1.3.
     - احراز هویت چندمرحله‌ای (MFA).
     - استفاده از AWS KMS برای مدیریت کلیدها.
   - **تأثیر:** رعایت استانداردهای PCI-DSS و افزایش اعتماد کاربران.

3. **سناریو: سیستم پخش ویدئو**
   - **نیازمندی غیرکارکردی:** عملکرد برای بارگذاری ویدئو در کمتر از 2 ثانیه.
   - **راه‌حل طراحی:**
     - استفاده از CDN برای ارائه محتوا از سرورهای نزدیک به کاربر.
     - بهینه‌سازی کدک‌های ویدئو برای کاهش تأخیر.
   - **تأثیر:** بهبود تجربه کاربری و کاهش نرخ ترک کاربران.

---

## خلاصه
نیازمندی‌های غیرکارکردی (NFRها) ستون فقرات طراحی سیستم‌های مقیاس‌پذیر، قابل‌اعتماد و امن هستند. این نیازمندی‌ها بر تصمیمات معماری تأثیر می‌گذارند و باید در کنار نیازمندی‌های کارکردی شناسایی و اولویت‌بندی شوند. با استفاده از استراتژی‌های مناسب (مانند مقیاس‌پذیری افقی، رمزنگاری و طراحی ماژولار)، مستندسازی دقیق و مدیریت چالش‌ها، مهندسان می‌توانند سیستم‌هایی طراحی کنند که هم عملکرد بالا داشته باشند و هم نیازهای کیفیتی را برآورده کنند. در مصاحبه‌های طراحی سیستم، توانایی توضیح NFRها، ارائه راه‌حل‌های عملی و نشان دادن تعادل بین آن‌ها می‌تواند تمایز شما را نشان دهد.