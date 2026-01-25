import json
import os
from typing import Any, List, Dict
from models import Student

file_path = "data/students.json"


def _ensure_data_dir():
    """Make sure the data folder exists."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


def to_dict() -> List[Dict[str, Any]]:
    """
    Load and return students as a list of dicts.
    Returns [] if file doesn't exist or is empty.
    """
    _ensure_data_dir()

    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("students.json must contain a JSON array (list), e.g. []")

    # Optional: ensure each record is a dict
    for rec in data:
        if not isinstance(rec, dict):
            raise ValueError(f"Invalid record type in JSON: {type(rec)} -> {rec}")

    return data


def save_data(data: List[Dict[str, Any]]) -> None:
    """
    Persist the full students list back to JSON (overwrite file).
    """
    _ensure_data_dir()

    if data is None:
        data = []

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_student(student: Student) -> None:
    students =  to_dict()         #to read the previous data
    students.append(student.to_dict())
    save_data(students)
