# Program Code: LIST-HOT-02
# Title: Design Your Todo App — Build a Real App from Scratch!
# Cognitive Skill: Higher Order Thinking (Design from scratch)
# Topic: Lists in Python
#
# ════════════════════════════════════════════════════════
#  DESIGN THINKING SECTION — How Do We Build This App?
# ════════════════════════════════════════════════════════
#
#  Before writing a single line of code, a good programmer DESIGNS.
#  They ask: WHAT does the app do? HOW will it be structured?
#  This section walks you through the design decisions we made.
#
#  ── STEP 1: WHAT does this app need to do? ──────────────
#
#    A Todo app helps you keep track of tasks — things you need to do.
#    It should let the user:
#      a) ADD a new task             (append to list)
#      b) VIEW all tasks             (loop through list + enumerate)
#      c) MARK a task as done        (update item in list)
#      d) REMOVE a task              (pop from list)
#      e) EXIT                       (break the menu loop)
#
#  ── STEP 2: WHAT data structure will we use? ────────────
#
#    We need to store a COLLECTION of tasks that can GROW and SHRINK.
#    → A Python LIST is perfect!
#
#    tasks = []     ← starts empty, fills up as the user adds tasks
#
#    Each task is stored as a plain string.
#    When marked done, we ADD "✅ " to the beginning of the string.
#    Example:
#      "Buy milk"      → pending (no prefix)
#      "✅ Buy milk"   → done    (has "✅ " prefix)
#
#  ── STEP 3: HOW will the menu work? ─────────────────────
#
#    A menu-driven app uses a loop that keeps running until the user
#    chooses to exit. The pattern:
#
#      while True:
#          show_menu()
#          choice = input(...)
#          if choice == "1":   add_task()
#          elif choice == "2": view_tasks()
#          ...
#          elif choice == "5": break    ← this exits the loop
#
#    while True means "run forever" — we only stop when we say break.
#
#  ── STEP 4: HOW will we display tasks? ──────────────────
#
#    We use enumerate() to show tasks with numbers:
#
#      for i, task in enumerate(tasks, start=1):
#          print(f"  {i}. {task}")
#
#    enumerate(tasks, start=1) gives us (1, task1), (2, task2) ...
#    So i = the task number (starting from 1), task = the task text.
#
#  ── STEP 5: HOW do we handle invalid input? ─────────────
#
#    When the user types a task number, we check:
#      - Is it actually a number? (use .isdigit())
#      - Is it within the valid range? (1 to len(tasks))
#    If not → show an error, don't crash!
#
# ════════════════════════════════════════════════════════
#
# Problem Statement:
#   Build a working, interactive Todo List App using a Python list.
#   Apply design thinking: plan before coding, organise with functions,
#   and handle errors gracefully.
#
# Reflection:
#   1. Why is a list the right data structure for a todo app?
#      Could you build this with just variables (no list)? Why not?
#   2. We mark done tasks by adding "✅ " to the string. Can you think
#      of a better way to store "done or not done" information?
#   3. What happens if the user types a letter when a number is expected?
#      How does input validation protect the app from crashing?
#   4. What new FEATURE would you add to this app to make it even better?
#      Describe it in words — then think about what list operation it would use.

import time

# ─────────────────────────────────────────────
#  DATA — The list that powers the whole app
# ─────────────────────────────────────────────

tasks = []      # This one list holds ALL the tasks in the app.
                # It starts empty and grows as the user adds tasks.

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line(char="─", length=55):
    print(char * length)

def slow_print(text, delay=0.025):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def pause_brief():
    time.sleep(0.5)

def get_valid_task_number(action_label):
    """
    Ask the user for a task number.
    Validates:
      - Input is actually a number
      - Number is within the valid range (1 to len(tasks))
    Returns the 0-based index (index = number - 1), or -1 if invalid.
    """
    raw = input(f"  Enter task number to {action_label}: ").strip()

    # Check it's a digit string (no letters, no symbols)
    if not raw.isdigit():
        print("  ❌ Please enter a valid number, not text!")
        return -1

    num = int(raw)

    # Check it's within the range of actual tasks
    if num < 1 or num > len(tasks):
        print(f"  ❌ Invalid number! We only have {len(tasks)} task(s).")
        print(f"     Please enter a number between 1 and {len(tasks)}.")
        return -1

    return num - 1   # Convert to 0-based index for the list

# ─────────────────────────────────────────────
#  APP FUNCTIONS — one function per menu option
# ─────────────────────────────────────────────

def show_header():
    print("=" * 55)
    slow_print("  LIST-HOT-02 | Design Your Todo App")
    slow_print("  Built with Python Lists — Step by Step!")
    print("=" * 55)
    print()
    slow_print("  Welcome to Aarav's Todo App! 📋")
    slow_print("  Powered entirely by one Python list.")
    print()

def show_menu():
    """Display the main menu options."""
    print()
    print_line()
    print("  MAIN MENU")
    print_line()
    print("  1. ➕  Add a task")
    print("  2. 📋  View all tasks")
    print("  3. ✅  Mark task as done")
    print("  4. 🗑️   Remove a task")
    print("  5. 🚪  Exit")
    print_line()

def add_task():
    """
    Design Decision: We use tasks.append() to add new tasks.
    append() adds to the END of the list — so the newest task
    is always at the bottom, which is natural for a todo list.
    """
    print()
    print_line()
    print("  ADD A TASK")
    print_line()
    task_text = input("  Type your new task: ").strip()

    if task_text == "":
        print("  ❌ Task cannot be empty! Please type something.")
        return

    tasks.append(task_text)          # ← THE KEY OPERATION: append to list
    print()
    print(f"  ✅ Task added: \"{task_text}\"")
    print(f"  💡 You now have {len(tasks)} task(s) in your list.")
    pause_brief()

def view_tasks():
    """
    Design Decision: We use enumerate(tasks, start=1) to show
    each task with a user-friendly number starting from 1.
    Tasks with "✅ " prefix are shown as DONE.
    Tasks without are PENDING.
    """
    print()
    print_line()
    print("  YOUR TASKS")
    print_line()

    if len(tasks) == 0:
        print("  📋 Your list is empty! Add some tasks first.")
        return

    done_count = 0
    pending_count = 0

    for i, task in enumerate(tasks, start=1):
        # Check if the task has been marked done (has "✅ " at the start)
        if task.startswith("✅ "):
            print(f"  {i}. {task}")
            done_count += 1
        else:
            print(f"  {i}. ⬜ {task}")
            pending_count += 1

    print_line()
    print(f"  Total: {len(tasks)} task(s)  |  ✅ Done: {done_count}  |  ⬜ Pending: {pending_count}")

def mark_done():
    """
    Design Decision: We mark a task as done by modifying the
    string at that index — we prepend "✅ " to it.
    This is a LIST UPDATE operation: tasks[index] = new_value
    We first call view_tasks() so the user can see the numbers.
    """
    print()
    print_line()
    print("  MARK TASK AS DONE")
    print_line()

    if len(tasks) == 0:
        print("  ❌ No tasks to mark! Add some tasks first.")
        return

    view_tasks()
    print()

    index = get_valid_task_number("mark as done")
    if index == -1:
        return    # Invalid input — get_valid_task_number already printed the error

    if tasks[index].startswith("✅ "):
        print(f"  💡 This task is already done: \"{tasks[index]}\"")
        return

    original_task = tasks[index]
    tasks[index] = "✅ " + original_task    # ← THE KEY OPERATION: update list item
    print()
    print(f"  ✅ Marked as done: \"{original_task}\"")
    print(f"     It now shows as: \"{tasks[index]}\"")
    pause_brief()

def remove_task():
    """
    Design Decision: We use tasks.pop(index) to remove a task.
    pop(index) removes the item at a specific position and
    returns it — so we can print what was removed.
    We first call view_tasks() so the user can see the numbers.
    """
    print()
    print_line()
    print("  REMOVE A TASK")
    print_line()

    if len(tasks) == 0:
        print("  ❌ No tasks to remove! Your list is already empty.")
        return

    view_tasks()
    print()

    index = get_valid_task_number("remove")
    if index == -1:
        return    # Invalid input — already printed the error

    removed = tasks.pop(index)        # ← THE KEY OPERATION: pop from list
    print()
    print(f"  🗑️  Removed: \"{removed}\"")
    print(f"  💡 You now have {len(tasks)} task(s) remaining.")
    pause_brief()

def show_farewell():
    """Show a goodbye message with a summary of remaining tasks."""
    print()
    print("=" * 55)
    slow_print("  Goodbye! Here is your final task summary:")
    print("=" * 55)

    if len(tasks) == 0:
        print("  ✅ All done! Your list is completely empty.")
    else:
        done   = sum(1 for t in tasks if t.startswith("✅ "))
        pending = len(tasks) - done
        print(f"  Total tasks: {len(tasks)}")
        print(f"  ✅ Completed: {done}")
        print(f"  ⬜ Still pending: {pending}")
        if pending > 0:
            print()
            print("  Pending tasks:")
            for task in tasks:
                if not task.startswith("✅ "):
                    print(f"    • {task}")
    print()
    slow_print("  Keep building cool apps with lists! 🏆")
    print("=" * 55)

# ─────────────────────────────────────────────
#  DESIGN RECAP — Printed at startup
# ─────────────────────────────────────────────

def show_design_recap():
    """Briefly explain the design before the app starts."""
    print_line("─")
    slow_print("  HOW THIS APP IS BUILT (Design Recap):")
    print_line("─")
    print("  Data:      One list called  tasks = []")
    print("  Add task:  tasks.append(text)         → adds to end")
    print("  View:      enumerate(tasks, start=1)  → numbered list")
    print("  Mark done: tasks[index] = '✅ ' + task → update item")
    print("  Remove:    tasks.pop(index)            → delete by index")
    print("  Menu:      while True + if-elif + break")
    print_line("─")
    print()

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print("=" * 55)
    slow_print("  REFLECTION — Think About It")
    print("=" * 55)
    print()
    slow_print("  1. Why is a LIST the right data structure for a todo app?")
    slow_print("     Could you build this using only variables? Why not?")
    print()
    slow_print("  2. We mark done tasks by adding '✅ ' to the string.")
    slow_print("     Can you think of a BETTER way to track done/not-done?")
    slow_print("     (Think about what you have learned — any ideas?)")
    print()
    slow_print("  3. What happens if the user types a letter instead of a")
    slow_print("     number when choosing a task? Try it! Does the app crash?")
    slow_print("     Which part of the code protects it?")
    print()
    slow_print("  4. What ONE new feature would you add to make this app")
    slow_print("     even better? Describe it — then think about which")
    slow_print("     list operation you would use to build it.")
    print()
    print("=" * 55)

# ─────────────────────────────────────────────
#  MAIN — The app loop
# ─────────────────────────────────────────────

def main():
    show_header()
    show_design_recap()
    input("  Press ENTER to launch the app...\n")

    # ── THE CORE LOOP ──────────────────────────────────────
    # while True runs forever. We only stop when user types 5.
    # Each menu option calls one dedicated function.
    # ───────────────────────────────────────────────────────
    while True:
        show_menu()
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            show_farewell()
            show_reflection()
            break          # ← Exits the while True loop — app ends here
        else:
            print()
            print("  ❌ Invalid choice! Please enter a number from 1 to 5.")

main()
