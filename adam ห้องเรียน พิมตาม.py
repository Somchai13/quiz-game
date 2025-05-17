import tkinter as tk
import random

# คำถามและคำตอบที่เกี่ยวข้องกับการเขียนโค้ด
questions = {
    "print(คำสั่งปริ้นออกมา)": "print",
    "loop(คำสั่งวนลูบเพื่อแสดง)": "loop",
    "import(คำสั่งนำอินเดอร์เครเตอร์เข้ามา)": "import",
    "def(สร้างฟังก์ชัน)": "def",
    
    # เพิ่มคำถามเพิ่มเติมตามต้องการ
}

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("เกมตอบคำถาม")
        self.root.geometry("900x700")  # ขนาดหน้าต่างที่ใหญ่ขึ้นเพื่อความสะดวก
        self.root.configure(bg="white")  # สีพื้นหลังเป็นสีขาว

        self.score = 0
        self.current_question = ""
        self.correct_answer = ""
        self.time_left = 10  # เวลาตอบคำถาม 10 วินาที

        # สร้างกรอบหลักสำหรับเนื้อหา
        self.main_frame = tk.Frame(root, bg="white")
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # ป้ายคำถาม
        self.question_label = tk.Label(self.main_frame, text="", font=("Helvetica", 25), bg="white", fg="red", padx=10, pady=10)
        self.question_label.pack(pady=20, fill=tk.X)

        # ช่องกรอกคำตอบ
        self.answer_frame = tk.Frame(self.main_frame, bg="white")
        self.answer_frame.pack(pady=10, fill=tk.X, expand=True)

        # ขนาดช่องกรอกคำตอบ
        self.answer_entry = tk.Entry(self.answer_frame, font=("Helvetica", 20), bg="white", fg="red", borderwidth=1, relief="solid", width=25)
        self.answer_entry.pack(padx=10, pady=5, fill=tk.X, expand=False)

        # ป้ายผลลัพธ์
        self.result_label = tk.Label(self.main_frame, text="", font=("Helvetica", 20), bg="white", fg="red", padx=10, pady=10)
        self.result_label.pack(pady=10, fill=tk.X)

        # ป้ายคะแนน
        self.score_label = tk.Label(self.main_frame, text=f"คะแนน: {self.score}", font=("Helvetica", 20), bg="white", fg="red", padx=10, pady=10)
        self.score_label.pack(pady=10, fill=tk.X)

        # ป้ายตัวจับเวลา
        self.timer_label = tk.Label(self.main_frame, text=f"เวลาที่เหลือ: {self.time_left}", font=("Helvetica", 20), bg="white", fg="red", padx=10, pady=10)
        self.timer_label.pack(pady=10, fill=tk.X)

        self.timer_id = None  # ตัวแปรสำหรับเก็บ ID ของตัวจับเวลา
        self.next_question()

        # ผูกเหตุการณ์การกด Enter
        self.answer_entry.bind("<Return>", self.check_answer)

    def next_question(self):
        # เลือกคำถามแบบสุ่ม
        question = random.choice(list(questions.keys()))
        self.current_question = question
        self.correct_answer = questions[question]

        # แสดงคำถามที่เลือก
        self.question_label.config(text=question)
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")

        # รีเซ็ตเวลา
        self.time_left = 10
        self.timer_label.config(text=f"เวลาที่เหลือ: {self.time_left}")

        # ยกเลิกตัวจับเวลาที่มีอยู่ก่อนหน้า
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        
        # เริ่มตัวจับเวลาใหม่
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"เวลาที่เหลือ: {self.time_left}")
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.result_label.config(text=f"หมดเวลา! คำตอบที่ถูกต้องคือ '{self.correct_answer}'", fg="red")
            self.flash_incorrect_answer()  # เรียกใช้งานเอฟเฟกต์พุไฟสำหรับการตอบผิด
            self.score = 0  # รีเซ็ตคะแนนเมื่อตอบผิด
            self.score_label.config(text=f"คะแนน: {self.score}")
            self.root.after(2000, self.next_question)  # แสดงคำถามใหม่หลังจาก 2 วินาที

    def flash_correct_answer(self):
        # เปลี่ยนสีพื้นหลังของป้ายผลลัพธ์เป็นสีแดงแล้วกลับไปเป็นสีขาว
        self.result_label.config(bg="red")
        self.root.after(200, lambda: self.result_label.config(bg="white"))

    def flash_incorrect_answer(self):
        # เปลี่ยนสีพื้นหลังของป้ายผลลัพธ์เป็นสีแดงแล้วกลับไปเป็นสีขาว
        self.result_label.config(bg="red")
        self.root.after(200, lambda: self.result_label.config(bg="white"))

    def check_answer(self, event):
        if self.time_left > 0:
            user_answer = self.answer_entry.get().strip()
            if user_answer.lower() == self.correct_answer.lower():
                self.result_label.config(text="คำตอบถูกต้อง!", fg="green")
                self.score += 1
                self.flash_correct_answer()  # เรียกใช้งานเอฟเฟกต์พุไฟสำหรับคำตอบถูกต้อง
            else:
                self.result_label.config(text=f"คำตอบผิด! คำตอบที่ถูกต้องคือ '{self.correct_answer}'", fg="red")
                self.flash_incorrect_answer()  # เรียกใช้งานเอฟเฟกต์พุไฟสำหรับการตอบผิด
                self.score = 0  # รีเซ็ตคะแนนเมื่อตอบผิด

            self.score_label.config(text=f"คะแนน: {self.score}")

            # ยกเลิกตัวจับเวลาที่มีอยู่ก่อนหน้าและแสดงคำถามใหม่หลังจาก 2 วินาที
            if self.timer_id is not None:
                self.root.after_cancel(self.timer_id)
            self.root.after(2000, self.next_question)

# สร้างหน้าต่าง GUI ด้วย tkinter
root = tk.Tk()
game = QuizGame(root)
root.mainloop()
