import pyautogui
import threading
import time
import tkinter as tk
import keyboard


key = 'bot.png'
running = False
count = 0

# Link Test Bot
# https://humanbenchmark.com/tests/aim

# ฟังก์ชันหลักของบอท
def run_bot():
    global running, count
    while running:
        try:
            find = pyautogui.locateCenterOnScreen(key, confidence=0.5)
            if find:
                x, y = find
                pyautogui.click(x, y)
                print("Position:", x, y)
            # else:
            #     count += 1
            #     print("ไม่พบภาพ [", count, "]")
        except Exception as e:
            if str(e).strip() == "":  # ตรวจสอบว่า e เป็นข้อความที่ว่างหรือไม่
                count += 1
                print("ไม่พบภาพ [", count, "]")
                time.sleep(0.5)
            else:
                print("เกิดข้อผิดพลาด:", e)
        time.sleep(0.1)

# เริ่มบอท
def start():
    global running
    if not running:
        running = True
        threading.Thread(target=run_bot, daemon=True).start()
        status_label.config(text="🟢 กำลังทำงาน...")

# หยุดบอท
def stop():
    global running
    running = False
    status_label.config(text="⛔ หยุดแล้ว")

# ออกจากโปรแกรม
def on_close():
    global running
    running = False
    keyboard.unhook_all_hotkeys()  # ลบ hotkey ก่อนปิด
    root.destroy()

# ---------- สร้าง UI ----------
root = tk.Tk()
root.title("Auto Click")
root.geometry("300x150")

start_button = tk.Button(root, text="Start", command=start, bg="green", fg="white", width=10)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop, bg="red", fg="white", width=10)
stop_button.pack(pady=5)

status_label = tk.Label(root, text="⛔ ยังไม่เริ่มทำงาน")
status_label.pack(pady=10)

# ---------- ตั้ง hotkey ระดับ global ----------
keyboard.add_hotkey('s', start)
keyboard.add_hotkey('p', stop)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
