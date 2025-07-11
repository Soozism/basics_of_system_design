# مثال واقعی: استفاده از متعادل‌ساز بار الاستیک AWS در آمازون

این سند به بررسی استفاده آمازون از **متعادل‌ساز بار الاستیک AWS (Elastic Load Balancer - ELB)** به‌عنوان یک ابزار کلیدی در طراحی سیستم‌های مقیاس‌پذیر، قابل‌اعتماد و با دسترس‌پذیری بالا می‌پردازد. هدف این است که با ارائه توضیحات در مورد نقش ELB، انواع آن، معماری‌های استفاده‌شده، مزایا، ادغام با سایر سرویس‌های AWS و بهترین روش‌ها، یک راهنمای جامع و آموزشی برای مهندسان سیستم طراحی فراهم شود. این محتوا به زبان فارسی و با فرمت مارک‌داون ارائه شده است تا برای مستندسازی آموزشی مناسب باشد.

---

## مقدمه: چرا آمازون از متعادل‌سازی بار استفاده می‌کند و نقش AWS ELB چیست؟

آمازون به‌عنوان یکی از بزرگ‌ترین پلتفرم‌های تجارت الکترونیک و ارائه‌دهنده خدمات ابری در جهان، روزانه با حجم عظیمی از ترافیک کاربران (مانند میلیون‌ها درخواست در ثانیه) مواجه است. برای مدیریت این ترافیک، **متعادل‌سازی بار** حیاتی است، زیرا:
- **مقیاس‌پذیری:** امکان توزیع ترافیک بین سرورهای متعدد برای پاسخگویی به افزایش تقاضا.
- **دسترس‌پذیری بالا:** تضمین دسترسی مداوم به خدمات حتی در صورت خرابی سرورها.
- **تحمل‌پذیری خطا:** هدایت ترافیک به سرورهای سالم برای جلوگیری از قطعی سرویس.
- **بهبود تجربه کاربری:** کاهش تأخیر و ارائه پاسخ‌های سریع به کاربران.

**AWS Elastic Load Balancer (ELB)** یک سرویس مدیریت‌شده است که ترافیک ورودی را به‌طور خودکار بین چندین هدف (مانند نمونه‌های EC2، کانتینرها یا آدرس‌های IP) در یک یا چند منطقه دسترسی (Availability Zone) توزیع می‌کند. آمازون از ELB برای مدیریت ترافیک وب‌سایت خود، خدمات ابری AWS و برنامه‌های داخلی استفاده می‌کند تا عملکرد، مقیاس‌پذیری و قابلیت اطمینان را تضمین کند.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

---

## مروری بر انواع AWS ELB

AWS ELB در سه نوع اصلی ارائه می‌شود که هر کدام برای سناریوهای خاص طراحی شده‌اند:

1. **Classic Load Balancer (CLB):**
   - **توضیح:** نسخه قدیمی‌تر ELB که در لایه‌های ۴ (انتقال) و ۷ (برنامه) عمل می‌کند.
   - **ویژگی‌ها:** مناسب برای برنامه‌های ساده، پشتیبانی از پروتکل‌های HTTP، HTTPS، TCP و SSL.
   - **موارد استفاده:** برنامه‌های سنتی که نیاز به تنظیمات پیچیده ندارند.
   - **محدودیت‌ها:** امکانات محدودتر نسبت به ALB و NLB، مناسب برای سیستم‌های قدیمی.

2. **Application Load Balancer (ALB):**
   - **توضیح:** در لایه ۷ (برنامه) عمل می‌کند و برای برنامه‌های وب مدرن با پروتکل‌های HTTP/HTTPS مناسب است.
   - **ویژگی‌ها:** پشتیبانی از مسیریابی مبتنی بر محتوا (مانند URL یا هدرها)، WebSocket، و ادغام با AWS WAF.
   - **موارد استفاده:** معماری‌های میکروسرویس، برنامه‌های وب پیشرفته و کانتینرها.

3. **Network Load Balancer (NLB):**
   - **توضیح:** در لایه ۴ (انتقال) عمل می‌کند و برای ترافیک TCP/UDP با تأخیر کم و حجم بالا مناسب است.
   - **ویژگی‌ها:** پشتیبانی از میلیون‌ها درخواست در ثانیه، حفظ آدرس IP منبع و آدرس‌های IP ثابت.
   - **موارد استفاده:** برنامه‌های بلادرنگ مانند بازی‌های آنلاین یا استریمینگ.

**Gateway Load Balancer (GLB):** نوع جدیدتری است که برای مدیریت دستگاه‌های مجازی (مانند فایروال‌ها) استفاده می‌شود، اما در این سند به دلیل تمرکز آمازون بر ALB و NLB کمتر بررسی می‌شود.[](https://www.prosperops.com/blog/aws-load-balancer/)

---

## چگونه آمازون از ELB برای مقیاس‌پذیری، تحمل‌پذیری خطا و دسترس‌پذیری بالا استفاده می‌کند؟

آمازون از ELB برای مدیریت ترافیک عظیم پلتفرم تجارت الکترونیک، خدمات AWS و برنامه‌های داخلی خود استفاده می‌کند. در ادامه، چگونگی استفاده آمازون از ELB توضیح داده می‌شود:

- **مقیاس‌پذیری:**
  - ELB به‌طور خودکار با افزایش یا کاهش ترافیک مقیاس‌پذیری می‌کند. برای مثال، در رویدادهای فروش بزرگ مانند **Black Friday**، آمازون از ALB برای توزیع ترافیک بین صدها نمونه EC2 در چندین منطقه دسترسی استفاده می‌کند.
  - با ادغام ELB با **Auto Scaling**، آمازون تعداد نمونه‌های EC2 را به‌صورت پویا بر اساس تقاضا تنظیم می‌کند.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

- **تحمل‌پذیری خطا:**
  - ELB از بررسی‌های سلامت (Health Checks) برای شناسایی نمونه‌های معیوب استفاده می‌کند و ترافیک را تنها به نمونه‌های سالم هدایت می‌کند.
  - در صورت خرابی یک منطقه دسترسی (AZ)، ELB ترافیک را به نمونه‌های سالم در سایر AZها هدایت می‌کند، که باعث کاهش قطعی سرویس می‌شود.[](https://www.prosperops.com/blog/aws-load-balancer/)

- **دسترس‌پذیری بالا:**
  - آمازون ELB را در چندین منطقه دسترسی (Multi-AZ) مستقر می‌کند تا از دسترس‌پذیری بالا اطمینان حاصل کند. این کار خطر نقاط شکست تک (Single Points of Failure) را کاهش می‌دهد.
  - برای مثال، در وب‌سایت آمازون، ALB ترافیک را بین سرورهای وب در AZهای مختلف توزیع می‌کند تا قطعی در یک AZ تأثیری بر تجربه کاربران نداشته باشد.[](https://www.stormit.cloud/blog/aws-high-availability-architecture/)

**مثال واقعی:** در پلتفرم تجارت الکترونیک آمازون، ALB برای مسیریابی درخواست‌های کاربران به سرویس‌های مختلف (مانند کاتالوگ محصولات، سبد خرید یا پردازش پرداخت) استفاده می‌شود. این کار با استفاده از قوانین مسیریابی مبتنی بر URL (مانند `/cart` یا `/payment`) انجام می‌شود.

---

## معماری و سناریوهای استقرار در آمازون با استفاده از ELB

آمازون از معماری‌های پیچیده و چندلایه برای استقرار ELB استفاده می‌کند. در ادامه، یک سناریوی نمونه از معماری آمازون ارائه می‌شود:

### معماری نمونه:
- **لایه وب:** نمونه‌های EC2 که برنامه‌های وب را میزبانی می‌کنند، پشت یک ALB قرار دارند. ALB درخواست‌های HTTP/HTTPS را بر اساس قوانین مسیریابی (مانند مسیر URL) توزیع می‌کند.
- **لایه برنامه:** سرویس‌های میکروسرویس (مانند سرویس پرداخت یا کاتالوگ) روی کانتینرهای ECS یا نمونه‌های EC2 اجرا می‌شوند و از ALB یا NLB برای توزیع ترافیک استفاده می‌کنند.
- **لایه پایگاه داده:** پایگاه داده‌هایی مانند Amazon RDS یا Aurora در حالت Multi-AZ برای دسترس‌پذیری بالا پیکربندی شده‌اند.
- **DNS:** Amazon Route 53 برای هدایت ترافیک کاربران به ALB یا NLB استفاده می‌شود و از سیاست‌های مسیریابی مبتنی بر تأخیر (Latency-Based Routing) بهره می‌برد.

### سناریوی استقرار:
- **سناریو:** توزیع ترافیک وب‌سایت آمازون در رویداد فروش Black Friday.
  - **مرحله ۱:** کاربران از طریق Route 53 به آدرس وب‌سایت (مانند `www.amazon.com`) هدایت می‌شوند.
  - **مرحله ۲:** Route 53 ترافیک را به یک ALB در منطقه‌ای نزدیک (مانند us-east-1) هدایت می‌کند.
  - **مرحله ۳:** ALB درخواست‌ها را بر اساس مسیر URL (مانند `/products` یا `/checkout`) به گروه‌های هدف (Target Groups) شامل نمونه‌های EC2 یا کانتینرهای ECS توزیع می‌کند.
  - **مرحله ۴:** Auto Scaling تعداد نمونه‌های EC2 را بر اساس معیارهای CloudWatch (مانند استفاده از CPU یا تعداد درخواست‌ها) تنظیم می‌کند.
  - **مرحله ۵:** در صورت خرابی یک AZ، ELB ترافیک را به نمونه‌های سالم در AZهای دیگر هدایت می‌کند.

**نمودار معماری:**
```
[کاربران] --> [Route 53] --> [ALB/NLB] --> [EC2 Instances / ECS Containers in Multiple AZs]
                                         --> [RDS/Aurora Multi-AZ]
```

این معماری مقیاس‌پذیری، تحمل‌پذیری خطا و دسترس‌پذیری بالا را تضمین می‌کند.[](https://jayendrapatil.com/aws-high-availability-fault-tolerance-architecture-certification/)[](https://www.stormit.cloud/blog/aws-high-availability-architecture/)

---

## مزایای کلیدی و درس‌های آموخته‌شده از استفاده ELB در مقیاس بزرگ

### مزایا:
1. **مقیاس‌پذیری خودکار:** ELB به‌طور خودکار با افزایش ترافیک مقیاس‌پذیر می‌شود، که برای رویدادهای پرترافیک مانند فروش‌های فصلی حیاتی است.
2. **تحمل‌پذیری خطا:** بررسی‌های سلامت و توزیع ترافیک بین AZها خطر قطعی را کاهش می‌دهد.
3. **انعطاف‌پذیری:** ALB از مسیریابی مبتنی بر محتوا پشتیبانی می‌کند، که برای معماری‌های میکروسرویس آمازون ایده‌آل است.
4. **امنیت پیشرفته:** ادغام با AWS WAF و AWS Shield برای محافظت در برابر حملات DDoS و بهره‌جویی‌های وب.[](https://www.prosperops.com/blog/aws-load-balancer/)
5. **هزینه بهینه:** مدل پرداخت به ازای استفاده (Pay-as-you-go) هزینه‌ها را برای آمازون بهینه می‌کند.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

### درس‌های آموخته‌شده:
- **بررسی‌های سلامت دقیق:** تنظیم نادرست بررسی‌های سلامت می‌تواند باعث هدایت ترافیک به نمونه‌های ناسالم شود.
- **مانیتورینگ جامع:** استفاده از CloudWatch برای رصد معیارهای کلیدی (مانند تأخیر و نرخ خطا) برای بهینه‌سازی عملکرد ضروری است.
- **مقیاس‌پذیری پیش‌بینی‌شده:** پیش‌بینی افزایش ترافیک (مانند Black Friday) و تنظیم سیاست‌های Auto Scaling از قبل، از گلوگاه‌ها جلوگیری می‌کند.
- **مدیریت پیچیدگی:** در معماری‌های میکروسرویس، استفاده از چندین ALB برای سرویس‌های مختلف می‌تواند مدیریت را پیچیده کند، بنابراین استفاده از ابزارهای IaC (مانند CloudFormation) توصیه می‌شود.

---

## ادغام ELB با سایر سرویس‌های AWS

ELB با سرویس‌های دیگر AWS ادغام می‌شود تا عملکرد و قابلیت اطمینان سیستم را بهبود بخشد:

1. **Amazon EC2 Auto Scaling:**
   - ELB با Auto Scaling ادغام می‌شود تا نمونه‌های EC2 به‌طور خودکار بر اساس تقاضا اضافه یا حذف شوند.
   - نمونه‌های جدید به‌طور خودکار در گروه‌های هدف ELB ثبت می‌شوند و نمونه‌های پایان‌یافته حذف می‌شوند.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

2. **Amazon Route 53:**
   - Route 53 برای هدایت ترافیک به ELB استفاده می‌شود و از سیاست‌های مسیریابی مانند Latency-Based یا Weighted Routing پشتیبانی می‌کند.
   - برای مثال، آمازون از Route 53 برای هدایت کاربران به ALB در نزدیک‌ترین منطقه جغرافیایی استفاده می‌کند.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

3. **Amazon CloudWatch:**
   - برای مانیتورینگ معیارهای ELB (مانند تعداد درخواست‌ها، تأخیر و نرخ خطا) استفاده می‌شود.
   - هشدارهای CloudWatch می‌توانند سیاست‌های Auto Scaling را فعال کنند.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

4. **AWS WAF:**
   - برای محافظت از ALB در برابر حملات مانند SQL Injection یا XSS استفاده می‌شود.
   - آمازون از WAF برای فیلتر کردن ترافیک مخرب به وب‌سایت خود استفاده می‌کند.[](https://www.prosperops.com/blog/aws-load-balancer/)

5. **Amazon ECS و EKS:**
   - ELB برای توزیع ترافیک بین کانتینرهای ECS یا EKS استفاده می‌شود.
   - آمازون از ALB برای مسیریابی ترافیک به سرویس‌های میکروسرویس در ECS استفاده می‌کند.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

6. **AWS Certificate Manager (ACM):**
   - برای مدیریت گواهینامه‌های SSL/TLS در ALB استفاده می‌شود تا ارتباطات امن HTTPS فراهم شود.[](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

---

## بهترین روش‌ها برای استفاده از ELB در معماری‌های ابری

1. **استفاده از Multi-AZ:**
   - ELB را در چندین منطقه دسترسی مستقر کنید تا دسترس‌پذیری بالا تضمین شود.[](https://www.stormit.cloud/blog/aws-high-availability-architecture/)

2. **تنظیم بررسی‌های سلامت دقیق:**
   - بررسی‌های سلامت را برای شناسایی سریع نمونه‌های ناسالم تنظیم کنید (مانند بررسی وضعیت HTTP 200 در بازه‌های 10 ثانیه‌ای).

3. **استفاده از مسیریابی پیشرفته:**
   - در ALB، از قوانین مسیریابی مبتنی بر URL یا هدر برای هدایت ترافیک به سرویس‌های خاص استفاده کنید.

4. **ادغام با Auto Scaling:**
   - سیاست‌های مقیاس‌پذیری را بر اساس معیارهای CloudWatch (مانند استفاده از CPU یا تعداد درخواست‌ها) تنظیم کنید.[](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html)

5. **امنیت:**
   - از AWS WAF برای محافظت در برابر حملات و AWS Shield برای دفاع در برابر DDoS استفاده کنید.
   - از گواهینامه‌های SSL/TLS از طریق ACM برای رمزنگاری ترافیک استفاده کنید.[](https://www.prosperops.com/blog/aws-load-balancer/)

6. **مانیتورینگ و لاگ‌گیری:**
   - از CloudWatch برای رصد معیارهای ELB و فعال کردن لاگ‌های دسترسی (Access Logs) برای تحلیل ترافیک استفاده کنید.[](https://aws.amazon.com/elasticloadbalancing/features/)

7. **استفاده از ابزارهای IaC:**
   - از AWS CloudFormation برای خودکارسازی استقرار ELB و مدیریت تنظیمات استفاده کنید.[](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html)

8. **بهینه‌سازی هزینه:**
   - معیارهای استفاده ELB را رصد کنید و از مدل پرداخت به ازای استفاده برای کاهش هزینه‌ها بهره ببرید.

---

## خلاصه و نکات عملی برای مهندسان

### خلاصه
- **چرا ELB؟** آمازون از ELB برای مدیریت ترافیک عظیم، تضمین مقیاس‌پذیری، تحمل‌پذیری خطا و دسترس‌پذیری بالا در پلتفرم تجارت الکترونیک و خدمات AWS استفاده می‌کند.
- **انواع ELB:** Classic Load Balancer (برای برنامه‌های قدیمی)، Application Load Balancer (برای برنامه‌های وب مدرن) و Network Load Balancer (برای ترافیک با تأخیر کم).
- **مزایا:** مقیاس‌پذیری خودکار، تحمل‌پذیری خطا، امنیت پیشرفته و ادغام با سرویس‌های AWS.
- **معماری:** آمازون از ELB در معماری‌های چندلایه با Multi-AZ، Route 53 و Auto Scaling استفاده می‌کند.
- **درس‌ها:** تنظیم دقیق بررسی‌های سلامت، مانیتورینگ جامع و پیش‌بینی افزایش ترافیک برای موفقیت حیاتی است.

### نکات عملی
1. **انتخاب نوع مناسب ELB:**
   - برای برنامه‌های وب مدرن و میکروسرویس‌ها از ALB استفاده کنید.
   - برای ترافیک TCP/UDP با حجم بالا از NLB استفاده کنید.
2. **پیکربندی Multi-AZ:** همیشه ELB را در چندین AZ مستقر کنید تا از دسترس‌پذیری بالا اطمینان حاصل شود.
3. **مانیتورینگ با CloudWatch:** معیارهای کلیدی مانند تأخیر، نرخ خطا و تعداد درخواست‌ها را رصد کنید.
4. **ادغام با Auto Scaling:** برای مدیریت پویا منابع و کاهش هزینه‌ها، ELB را با Auto Scaling ترکیب کنید.
5. **امنیت:** از WAF، Shield و ACM برای حفاظت از ترافیک و داده‌ها استفاده کنید.
6. **آزمایش و بهینه‌سازی:** معماری را در محیط‌های آزمایشی تست کنید و سیاست‌های مقیاس‌پذیری را بر اساس الگوهای ترافیک تنظیم کنید.

---

## منابع پیشنهادی برای مطالعه بیشتر
1. *Designing Data-Intensive Applications* نوشته مارتین کلپمن: کتابی جامع برای یادگیری طراحی سیستم‌های مقیاس‌پذیر.
2. *AWS Well-Architected Framework*: راهنمای رسمی AWS برای طراحی معماری‌های ابری.
3. وبلاگ‌های مهندسی:
   - *AWS Architecture Blog*: مقالات در مورد استفاده از ELB در مقیاس بزرگ.[](https://aws.amazon.com/blogs/architecture/category/networking-content-delivery/elastic-load-balancing/)
   - *AWS re:Invent Sessions*: ویدئوهای NET318 در مورد ELB.[](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/)
4. مستندات رسمی:
   - [AWS ELB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/)[](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
   - [Amazon Route 53 Documentation](https://docs.aws.amazon.com/route53/)[](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
   - [AWS Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/)[](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html)
5. دوره‌های آنلاین:
   - *Grokking the System Design Interview* در DesignGuru.io
   - *AWS Certified Solutions Architect* در Udemy یا AWS Skill Builder

---

این سند استفاده آمازون از AWS ELB را به‌صورت جامع توضیح داده و برای مهندسان علاقه‌مند به طراحی سیستم‌های مقیاس‌پذیر مناسب است. در صورت نیاز به جزئیات بیشتر یا مثال‌های دیگر، لطفاً اطلاع دهید!