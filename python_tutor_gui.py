#!/usr/bin/env python3
"""
PCEP Python Exam Tutor - GUI Version
Interactive certification preparation with graphical interface
"""

import json
import os
import random
import sys
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk


class PythonTutorGUI:
    """GUI version of the PCEP Python Exam Tutor"""

    # Constants for duplicate literals
    OPTION_A_YES = "A) Yes"
    OPTION_B_NO = "B) No"
    OPTION_D_ERROR = "D) Error"

    def __init__(self, root):
        self.root = root
        self.root.title("PCEP Python Exam Tutor")
        self.root.geometry("1000x700")

        self.progress_file = "pcep_tutor_progress.json"
        self.current_lesson = 0
        self.completed_lessons = set()
        self.quiz_scores = {}
        self.load_progress()

        # Import lessons from the terminal version
        from python_tutor import PythonTutor

        temp_tutor = PythonTutor()
        self.lessons = temp_tutor.lessons
        self.practice_questions = temp_tutor.practice_questions

        self.setup_ui()
        self.show_main_menu()

    def setup_ui(self):
        """Set up the main UI components"""
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Reset Progress", command=self.reset_progress)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        exam_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Exam", menu=exam_menu)
        exam_menu.add_command(label="Practice Exam", command=self.take_practice_exam)
        exam_menu.add_command(label="Study Tips", command=self.show_study_tips)

        # Main container
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def show_main_menu(self):
        """Display the main lesson menu"""
        self.clear_main_frame()

        # Title
        title_frame = tk.Frame(self.main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 10))

        title_label = tk.Label(
            title_frame,
            text="🎓 PCEP Python Certification Exam Tutor",
            font=("Arial", 16, "bold"),
            fg="#2c3e50",
        )
        title_label.pack()

        subtitle_label = tk.Label(
            title_frame, text="Python Certified Entry-Level Programmer Preparation", font=("Arial", 10)
        )
        subtitle_label.pack()

        # Progress stats
        stats_frame = tk.Frame(self.main_frame)
        stats_frame.pack(fill=tk.X, pady=(0, 10))

        total_lessons = len(self.lessons)
        completed = len(self.completed_lessons)
        progress_pct = (completed / total_lessons * 100) if total_lessons > 0 else 0

        total_quiz_score = sum(self.quiz_scores.values())
        total_quizzes = len(self.quiz_scores)
        avg_score = (total_quiz_score / total_quizzes) if total_quizzes > 0 else 0

        progress_text = f"📊 Progress: {completed}/{total_lessons} lessons ({progress_pct:.0f}%)"
        if total_quizzes > 0:
            progress_text += f" | Quiz Average: {avg_score:.0f}%"

        stats_label = tk.Label(stats_frame, text=progress_text, font=("Arial", 10))
        stats_label.pack()

        # Lesson list with scrollbar
        list_frame = tk.Frame(self.main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lesson_listbox = tk.Listbox(
            list_frame, yscrollcommand=scrollbar.set, font=("Courier", 10), height=20
        )
        self.lesson_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lesson_listbox.yview)

        # Populate lessons
        current_section = ""
        for i, lesson in enumerate(self.lessons):
            section = lesson.get("section", "")
            if section != current_section:
                self.lesson_listbox.insert(tk.END, f"\n{section}:")
                current_section = section

            status = "✓" if i in self.completed_lessons else " "
            current = "→" if i == self.current_lesson else " "
            quiz_info = ""
            if str(i) in self.quiz_scores:
                quiz_info = f" [Quiz: {self.quiz_scores[str(i)]}%]"

            lesson_text = f"{current} [{status}] {i+1}. {lesson['title']}{quiz_info}"
            self.lesson_listbox.insert(tk.END, lesson_text)

        self.lesson_listbox.bind("<Double-Button-1>", self.on_lesson_select)

        # Buttons
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        tk.Button(button_frame, text="Open Lesson", command=self.open_selected_lesson, width=15).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(button_frame, text="Practice Exam", command=self.take_practice_exam, width=15).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(button_frame, text="Study Tips", command=self.show_study_tips, width=15).pack(side=tk.LEFT, padx=5)

    def on_lesson_select(self, event):
        """Handle double-click on lesson"""
        self.open_selected_lesson()

    def open_selected_lesson(self):
        """Open the selected lesson"""
        selection = self.lesson_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a lesson to open.")
            return

        # Find actual lesson number (skip section headers)
        selected_text = self.lesson_listbox.get(selection[0])
        if not selected_text.strip() or "Section" in selected_text:
            return

        # Extract lesson number
        import re

        match = re.search(r"(\d+)\.", selected_text)
        if match:
            lesson_num = int(match.group(1)) - 1
            if 0 <= lesson_num < len(self.lessons):
                self.current_lesson = lesson_num
                self.display_lesson(lesson_num)

    def display_lesson(self, lesson_num):
        """Display a specific lesson"""
        self.clear_main_frame()

        lesson = self.lessons[lesson_num]

        # Header
        header_frame = tk.Frame(self.main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))

        title_label = tk.Label(
            header_frame, text=f"Lesson {lesson_num + 1}: {lesson['title']}", font=("Arial", 14, "bold"), fg="#2c3e50"
        )
        title_label.pack()

        section_label = tk.Label(header_frame, text=lesson.get("section", ""), font=("Arial", 10), fg="#7f8c8d")
        section_label.pack()

        # Notebook for tabs
        notebook = ttk.Notebook(self.main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Content tab
        content_frame = tk.Frame(notebook)
        notebook.add(content_frame, text="📚 Content")

        content_text = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, font=("Courier", 10))
        content_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        content_text.insert(tk.END, lesson["content"])
        content_text.config(state=tk.DISABLED)

        # Example tab
        example_frame = tk.Frame(notebook)
        notebook.add(example_frame, text="💡 Example")

        example_text = scrolledtext.ScrolledText(example_frame, wrap=tk.WORD, font=("Courier", 10))
        example_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        example_text.insert(tk.END, lesson["example"])
        example_text.config(state=tk.DISABLED)

        tk.Button(example_frame, text="▶ Run Example", command=lambda: self.run_example(lesson_num)).pack(pady=5)

        # Exercise tab
        exercise_frame = tk.Frame(notebook)
        notebook.add(exercise_frame, text="✏️ Exercise")

        exercise_desc = tk.Label(
            exercise_frame, text=lesson["exercise"]["description"], wraplength=900, font=("Arial", 10)
        )
        exercise_desc.pack(pady=5)

        hint_label = tk.Label(
            exercise_frame, text=f"💭 Hint: {lesson['exercise']['hint']}", wraplength=900, font=("Arial", 9), fg="#7f8c8d"
        )
        hint_label.pack(pady=5)

        self.exercise_text = scrolledtext.ScrolledText(exercise_frame, wrap=tk.WORD, font=("Courier", 10), height=15)
        self.exercise_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        tk.Button(exercise_frame, text="✓ Check Exercise", command=lambda: self.check_exercise(lesson_num)).pack(pady=5)

        # Quiz tab
        if "quiz" in lesson:
            quiz_frame = tk.Frame(notebook)
            notebook.add(quiz_frame, text=f"📝 Quiz ({len(lesson['quiz'])} questions)")

            tk.Label(quiz_frame, text="Take the quiz to test your knowledge!", font=("Arial", 11)).pack(pady=20)
            tk.Button(quiz_frame, text="Start Quiz", command=lambda: self.take_quiz(lesson_num), width=20).pack()

        # Navigation buttons
        nav_frame = tk.Frame(self.main_frame)
        nav_frame.pack(fill=tk.X, pady=(10, 0))

        tk.Button(nav_frame, text="← Back to Menu", command=self.show_main_menu, width=15).pack(side=tk.LEFT, padx=5)

        if lesson_num > 0:
            tk.Button(
                nav_frame,
                text="← Previous Lesson",
                command=lambda: self.display_lesson(lesson_num - 1),
                width=15,
            ).pack(side=tk.LEFT, padx=5)

        if lesson_num < len(self.lessons) - 1:
            tk.Button(
                nav_frame, text="Next Lesson →", command=lambda: self.display_lesson(lesson_num + 1), width=15
            ).pack(side=tk.LEFT, padx=5)

    def run_example(self, lesson_num):
        """Run the example code for a lesson"""
        lesson = self.lessons[lesson_num]
        output_window = tk.Toplevel(self.root)
        output_window.title("Example Output")
        output_window.geometry("600x400")

        output_text = scrolledtext.ScrolledText(output_window, wrap=tk.WORD, font=("Courier", 10))
        output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Redirect stdout
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        try:
            with redirect_stdout(f):
                exec(lesson["example"])
            output_text.insert(tk.END, f.getvalue())
        except Exception as e:
            output_text.insert(tk.END, f"Error: {e}\n")

        output_text.config(state=tk.DISABLED)

    def check_exercise(self, lesson_num):
        """Check the user's exercise code"""
        lesson = self.lessons[lesson_num]
        user_code = self.exercise_text.get("1.0", tk.END).strip()

        if not user_code:
            messagebox.showwarning("Empty Exercise", "Please write some code first!")
            return

        exercise = lesson["exercise"]
        if exercise["check"](user_code):
            messagebox.showinfo(
                "✅ Correct!", "Great job! Your solution looks good!\n\nNow let's run it to see the output."
            )
            self.run_user_code(user_code)
        else:
            messagebox.showwarning(
                "⚠️ Not Quite", f"Your code doesn't match the exercise requirements.\n\nHint: {exercise['hint']}"
            )

    def run_user_code(self, code):
        """Run user's exercise code"""
        output_window = tk.Toplevel(self.root)
        output_window.title("Exercise Output")
        output_window.geometry("600x400")

        output_text = scrolledtext.ScrolledText(output_window, wrap=tk.WORD, font=("Courier", 10))
        output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        try:
            with redirect_stdout(f):
                exec(code)
            output_text.insert(tk.END, f.getvalue())
        except Exception as e:
            output_text.insert(tk.END, f"Runtime Error: {e}\n")

        output_text.config(state=tk.DISABLED)

    def take_quiz(self, lesson_num):
        """Take the quiz for a lesson"""
        lesson = self.lessons[lesson_num]
        quiz = lesson.get("quiz", [])

        if not quiz:
            messagebox.showinfo("No Quiz", "No quiz available for this lesson.")
            return

        quiz_window = tk.Toplevel(self.root)
        quiz_window.title(f"Quiz: {lesson['title']}")
        quiz_window.geometry("700x500")

        self.quiz_answers = []
        self.current_question = 0

        def show_question(q_num):
            for widget in quiz_window.winfo_children():
                widget.destroy()

            if q_num >= len(quiz):
                show_results()
                return

            q = quiz[q_num]

            # Question header
            tk.Label(
                quiz_window, text=f"Question {q_num + 1} of {len(quiz)}", font=("Arial", 10), fg="#7f8c8d"
            ).pack(pady=10)

            # Question
            tk.Label(quiz_window, text=q["question"], font=("Arial", 12), wraplength=650).pack(pady=20)

            # Options
            var = tk.StringVar()
            for option in q["options"]:
                tk.Radiobutton(quiz_window, text=option, variable=var, value=option[0], font=("Arial", 10)).pack(
                    anchor=tk.W, padx=50
                )

            def submit_answer():
                answer = var.get()
                if not answer:
                    messagebox.showwarning("No Answer", "Please select an answer!")
                    return

                is_correct = answer == q["answer"]
                self.quiz_answers.append(
                    {"question": q["question"], "answer": answer, "correct": q["answer"], "is_correct": is_correct}
                )

                # Show immediate feedback
                if is_correct:
                    messagebox.showinfo("✅ Correct!", f"Well done!\n\n{q['explanation']}")
                else:
                    messagebox.showinfo(
                        "❌ Incorrect", f"The correct answer is {q['answer']}\n\n{q['explanation']}"
                    )

                show_question(q_num + 1)

            tk.Button(quiz_window, text="Submit Answer", command=submit_answer, width=15).pack(pady=20)

        def show_results():
            for widget in quiz_window.winfo_children():
                widget.destroy()

            correct = sum(1 for a in self.quiz_answers if a["is_correct"])
            score = int((correct / len(quiz)) * 100)

            # Save score
            self.quiz_scores[str(lesson_num)] = score
            if score >= 80:
                self.completed_lessons.add(lesson_num)
            self.save_progress()

            tk.Label(quiz_window, text="📊 Quiz Results", font=("Arial", 16, "bold")).pack(pady=20)

            tk.Label(
                quiz_window, text=f"You got {correct} out of {len(quiz)} questions correct!", font=("Arial", 12)
            ).pack(pady=10)

            tk.Label(quiz_window, text=f"Score: {score}%", font=("Arial", 14, "bold"), fg="#2c3e50").pack(pady=10)

            if score >= 80:
                message = "🎉 Excellent work! You've mastered this topic!"
                color = "#27ae60"
            elif score >= 60:
                message = "👍 Good job! Review the lesson to improve further."
                color = "#f39c12"
            else:
                message = "📚 Keep studying! Review the lesson and try again."
                color = "#e74c3c"

            tk.Label(quiz_window, text=message, font=("Arial", 11), fg=color).pack(pady=10)

            tk.Button(quiz_window, text="Close", command=quiz_window.destroy, width=15).pack(pady=20)

        show_question(0)

    def take_practice_exam(self):
        """Take a 20-question practice exam"""
        if len(self.practice_questions) < 20:
            messagebox.showerror("Not Ready", "Not enough questions for practice exam.")
            return

        questions = random.sample(self.practice_questions, 20)

        exam_window = tk.Toplevel(self.root)
        exam_window.title("PCEP Practice Exam")
        exam_window.geometry("800x600")

        self.exam_answers = []
        self.current_exam_question = 0

        def show_question(q_num):
            for widget in exam_window.winfo_children():
                widget.destroy()

            if q_num >= 20:
                show_results()
                return

            q = questions[q_num]

            # Header
            header_frame = tk.Frame(exam_window)
            header_frame.pack(fill=tk.X, pady=10)

            tk.Label(header_frame, text="🎯 PCEP Practice Exam", font=("Arial", 14, "bold")).pack()
            tk.Label(header_frame, text=f"Question {q_num + 1} of 20", font=("Arial", 10), fg="#7f8c8d").pack()

            # Question
            tk.Label(exam_window, text=q["question"], font=("Arial", 12), wraplength=750).pack(pady=20)

            # Options
            var = tk.StringVar()
            for option in q["options"]:
                tk.Radiobutton(exam_window, text=option, variable=var, value=option[0], font=("Arial", 10)).pack(
                    anchor=tk.W, padx=50
                )

            def submit_answer():
                answer = var.get()
                if not answer:
                    messagebox.showwarning("No Answer", "Please select an answer!")
                    return

                is_correct = answer == q["answer"]
                self.exam_answers.append(
                    {
                        "question": q["question"],
                        "answer": answer,
                        "correct": q["answer"],
                        "is_correct": is_correct,
                        "topic": q["topic"],
                        "explanation": q["explanation"],
                    }
                )

                show_question(q_num + 1)

            tk.Button(exam_window, text="Next →", command=submit_answer, width=15).pack(pady=20)

        def show_results():
            for widget in exam_window.winfo_children():
                widget.destroy()

            correct = sum(1 for a in self.exam_answers if a["is_correct"])
            score = int((correct / 20) * 100)

            tk.Label(exam_window, text="📊 Practice Exam Results", font=("Arial", 16, "bold")).pack(pady=20)

            tk.Label(exam_window, text=f"Score: {score}%", font=("Arial", 14, "bold")).pack(pady=10)

            if score >= 70:
                message = "🎉 PASS! You're ready for the PCEP exam!"
                color = "#27ae60"
            else:
                message = "📚 Keep studying! Review weak areas and try again."
                color = "#e74c3c"

            tk.Label(exam_window, text=message, font=("Arial", 12), fg=color).pack(pady=10)
            tk.Label(exam_window, text=f"Passing score: 70%", font=("Arial", 10), fg="#7f8c8d").pack()

            # Review button
            def show_review():
                review_window = tk.Toplevel(exam_window)
                review_window.title("Exam Review")
                review_window.geometry("700x500")

                tk.Label(review_window, text="Review Incorrect Answers", font=("Arial", 12, "bold")).pack(pady=10)

                review_text = scrolledtext.ScrolledText(review_window, wrap=tk.WORD, font=("Courier", 9))
                review_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                for i, a in enumerate(self.exam_answers, 1):
                    if not a["is_correct"]:
                        review_text.insert(tk.END, f"\nQ{i}: {a['question']}\n")
                        review_text.insert(tk.END, f"Your answer: {a['answer']}\n")
                        review_text.insert(tk.END, f"Correct: {a['correct']}\n")
                        review_text.insert(tk.END, f"Topic: {a['topic']}\n")
                        review_text.insert(tk.END, f"Explanation: {a['explanation']}\n")
                        review_text.insert(tk.END, "-" * 70 + "\n")

                review_text.config(state=tk.DISABLED)

            tk.Button(exam_window, text="Review Mistakes", command=show_review, width=20).pack(pady=10)
            tk.Button(exam_window, text="Close", command=exam_window.destroy, width=20).pack(pady=5)

        show_question(0)

    def show_study_tips(self):
        """Display study tips window"""
        tips_window = tk.Toplevel(self.root)
        tips_window.title("PCEP Study Tips")
        tips_window.geometry("700x600")

        tk.Label(tips_window, text="📖 PCEP Exam Study Tips", font=("Arial", 14, "bold")).pack(pady=10)

        tips_text = scrolledtext.ScrolledText(tips_window, wrap=tk.WORD, font=("Courier", 9))
        tips_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tips_content = """
ABOUT THE PCEP EXAM:
- 30 multiple-choice questions
- 40 minutes
- Passing score: 70%
- Online proctored exam

EXAM SECTIONS:
1. Basic Concepts (18%)
   - Compilation vs interpretation
   - Python fundamentals

2. Data Types, Variables, I/O, Operators (29%)
   - Literals and variables
   - Operators and expressions
   - Strings and I/O

3. Boolean, Conditionals, Loops, Lists, Logic (25%)
   - Boolean values
   - Conditional execution
   - Loops (for, while)
   - Lists and operations
   - Logical and bitwise operators

4. Functions, Tuples, Dictionaries, Modules (28%)
   - Function definition and calling
   - Tuples
   - Dictionaries
   - Importing modules

STUDY STRATEGIES:
✓ Complete all lessons and quizzes (aim for 80%+ on quizzes)
✓ Take multiple practice exams
✓ Focus on weak areas
✓ Practice coding exercises regularly
✓ Understand operator precedence
✓ Know the difference between mutable and immutable types
✓ Be familiar with common built-in functions
✓ Understand indexing and slicing thoroughly

EXAM TIPS:
✓ Read questions carefully
✓ Eliminate obviously wrong answers first
✓ Watch out for tricky wording
✓ Pay attention to syntax details (case sensitivity, colons, etc.)
✓ Manage your time (45 seconds per question average)
✓ Review flagged questions if time permits

KEY THINGS TO MEMORIZE:
- Operator precedence: ** > unary > * / // % > + -
- Logical precedence: not > and > or
- String/list indexing and slicing
- Common built-in functions: len(), type(), range(), etc.
- Module import syntax variations
- Mutable vs immutable types
- Boolean truthy/falsy values
        """

        tips_text.insert(tk.END, tips_content)
        tips_text.config(state=tk.DISABLED)

        tk.Button(tips_window, text="Close", command=tips_window.destroy, width=15).pack(pady=10)

    def reset_progress(self):
        """Reset all progress"""
        if messagebox.askyesno("Reset Progress", "Are you sure you want to reset all progress?"):
            self.completed_lessons.clear()
            self.quiz_scores.clear()
            self.current_lesson = 0
            self.save_progress()
            messagebox.showinfo("Reset Complete", "All progress has been reset.")
            self.show_main_menu()

    def load_progress(self):
        """Load user's progress from file"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, "r") as f:
                    data = json.load(f)
                    self.current_lesson = data.get("current_lesson", 0)
                    self.completed_lessons = set(data.get("completed_lessons", []))
                    self.quiz_scores = data.get("quiz_scores", {})
            except Exception:
                pass

    def save_progress(self):
        """Save user's progress to file"""
        try:
            with open(self.progress_file, "w") as f:
                json.dump(
                    {
                        "current_lesson": self.current_lesson,
                        "completed_lessons": list(self.completed_lessons),
                        "quiz_scores": self.quiz_scores,
                    },
                    f,
                    indent=2,
                )
        except Exception:
            pass

    def clear_main_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()


def main():
    """Entry point for the GUI application"""
    root = tk.Tk()
    app = PythonTutorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
