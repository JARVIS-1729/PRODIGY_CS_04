# PRODIGY_CS_04

Task 04: Simple Keylogger

A lightweight, background-running script that hooks into the operating system's keyboard events to capture and record physical keystrokes to a hidden text file.

Concept: OS-level event hooking, continuous background execution, and malware analysis concepts.

Features:

Silently records all alphanumeric keys.

Formats special keys (Space, Enter, Shift) cleanly for log readability.

Includes an emergency "Kill Switch" (ESC key) to safely terminate the listener.

Tech Stack: Python, pynput
