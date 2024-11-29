import tkinter as tk
import time

# إعداد نافذة الساعة
root = tk.Tk()
root.title("Digital Clock")

# إزالة الحواف وتعيين الشفافية الكاملة
root.overrideredirect(True)
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")

# جعل النافذة دائمًا في الأعلى
root.wm_attributes("-topmost", 1)

# تثبيت حجم النافذة
root.geometry("350x180")

# إعداد العنصر لعرض الوقت بخلفية شفافة
label_time = tk.Label(root, font=("Digital-7", 30), fg="cyan", bg="black")
label_time.place(relx=0.5, rely=0.4, anchor="center")

# إعداد العنصر لعرض التاريخ أسفل الوقت
label_date = tk.Label(root, font=("Digital-7", 30), fg="white", bg="black", anchor="center", justify="left")
label_date.place(relx=0.5, rely=0.75, anchor="center")

# قائمة درجات اللون البنفسجي للتدرج
purple_shades = [
    "#4B0082", "#6A0DAD", "#800080", "#9400D3", "#9932CC", 
    "#8A2BE2", "#BA55D3", "#D8BFD8", "#E6E6FA"
]

# دالة لتوليد تدرج لوني مستمر بين الألوان
def generate_smooth_gradient(colors, steps_per_color=50):
    gradient = []
    num_colors = len(colors)
    for i in range(num_colors):
        color1 = colors[i]
        color2 = colors[(i + 1) % num_colors]  # يجعله دائريًا

        r1, g1, b1 = [int(color1[j:j+2], 16) for j in (1, 3, 5)]
        r2, g2, b2 = [int(color2[j:j+2], 16) for j in (1, 3, 5)]

        for step in range(steps_per_color):
            r = int(r1 + (r2 - r1) * (step / steps_per_color))
            g = int(g1 + (g2 - g1) * (step / steps_per_color))
            b = int(b1 + (b2 - b1) * (step / steps_per_color))
            gradient.append(f"#{r:02x}{g:02x}{b:02x}")
    
    return gradient

# إنشاء التدرج اللوني السلس
gradient_colors = generate_smooth_gradient(purple_shades, steps_per_color=100)

# متغير للتحكم في التغيير التدريجي
color_index = 0
clock_running = False

# دالة لتحديث الوقت والتدرج اللوني
def update_time():
    global color_index
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%Y-%m-%d")
    label_time.config(text=current_time, fg=gradient_colors[color_index])
    label_date.config(text=current_date, fg=gradient_colors[color_index])
    color_index = (color_index + 1) % len(gradient_colors)  # يدور مرة أخرى من البداية
    if clock_running:
        root.after(100, update_time)  # تابع التحديث كل 100 مللي ثانية

# دالة للتحكم بتشغيل/إيقاف الساعة أو إغلاقها
def toggle_clock(event=None):
    global clock_running
    if clock_running:
        root.quit()  # إغلاق النافذة بالكامل
    else:
        clock_running = True
        update_time()  # بدء التحديث عند تشغيل الساعة

# ربط زر Tab لتشغيل وإيقاف الساعة
root.bind("<F5>", toggle_clock)
# تشغيل البرنامج
root.mainloop()
