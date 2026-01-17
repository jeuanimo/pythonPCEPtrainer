"""Unit tests for the PythonTutor class."""
import json
import os
import tempfile

from python_tutor import PythonTutor


def test_tutor_initialization():
    """Test that PythonTutor initializes correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        progress_file = os.path.join(tmpdir, "progress.json")
        tutor = PythonTutor()
        tutor.progress_file = progress_file  # Override for test
        assert tutor.current_lesson == 0
        assert len(tutor.completed_lessons) == 0
        assert len(tutor.quiz_scores) == 0
        assert len(tutor.lessons) > 0


def test_lesson_structure():
    """Test that all lessons have required fields."""
    tutor = PythonTutor()
    for i, lesson in enumerate(tutor.lessons):
        assert "title" in lesson, f"Lesson {i} missing 'title'"
        assert "section" in lesson, f"Lesson {i} missing 'section'"
        assert "content" in lesson, f"Lesson {i} missing 'content'"
        assert "example" in lesson, f"Lesson {i} missing 'example'"
        assert "exercise" in lesson, f"Lesson {i} missing 'exercise'"
        assert "quiz" in lesson, f"Lesson {i} missing 'quiz'"


def test_exercise_structure():
    """Test that all exercises have required fields."""
    tutor = PythonTutor()
    for i, lesson in enumerate(tutor.lessons):
        exercise = lesson["exercise"]
        assert "description" in exercise, f"Lesson {i} exercise missing 'description'"
        assert "hint" in exercise, f"Lesson {i} exercise missing 'hint'"
        assert "check" in exercise, f"Lesson {i} exercise missing 'check'"
        assert callable(exercise["check"]), f"Lesson {i} exercise 'check' is not callable"


def test_quiz_structure():
    """Test that all quizzes have required fields."""
    tutor = PythonTutor()
    for i, lesson in enumerate(tutor.lessons):
        if "quiz" in lesson:
            quiz = lesson["quiz"]
            assert isinstance(quiz, list), f"Lesson {i} quiz is not a list"
            for j, question in enumerate(quiz):
                assert "question" in question, f"Lesson {i}, Q{j} missing 'question'"
                assert "options" in question, f"Lesson {i}, Q{j} missing 'options'"
                assert "answer" in question, f"Lesson {i}, Q{j} missing 'answer'"
                assert "explanation" in question, f"Lesson {i}, Q{j} missing 'explanation'"
                assert len(question["options"]) == 4, f"Lesson {i}, Q{j} should have 4 options"
                assert question["answer"] in ["A", "B", "C", "D"], f"Lesson {i}, Q{j} answer not A/B/C/D"


def test_practice_questions_generated():
    """Test that practice question bank is populated."""
    tutor = PythonTutor()
    assert len(tutor.practice_questions) > 0, "Practice question bank is empty"


def test_save_and_load_progress():
    """Test saving and loading user progress."""
    with tempfile.TemporaryDirectory() as tmpdir:
        progress_file = os.path.join(tmpdir, "progress.json")
        tutor = PythonTutor()
        tutor.progress_file = progress_file

        # Set some progress
        tutor.completed_lessons.add(0)
        tutor.completed_lessons.add(2)
        tutor.quiz_scores["0"] = 85
        tutor.quiz_scores["2"] = 92

        # Save
        tutor.save_progress()
        assert os.path.exists(progress_file), "Progress file not created"

        # Load in new instance
        tutor2 = PythonTutor()
        tutor2.progress_file = progress_file
        tutor2.load_progress()

        assert 0 in tutor2.completed_lessons
        assert 2 in tutor2.completed_lessons
        assert tutor2.quiz_scores["0"] == 85
        assert tutor2.quiz_scores["2"] == 92
