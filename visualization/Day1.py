#!/usr/bin/env python3
import time
import math

# =========================
# INPUT
# =========================

with open("../input1.txt") as f:
    rotations = [
        (line[0], int(line[1:]))
        for line in f.read().strip().split("\n")
        if line
    ]

# =========================
# TERMINAL HELPERS
# =========================

def clear():
    print("\033[H\033[J", end="")

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

GREEN = "\033[92m"
RESET = "\033[0m"

# =========================
# DIAL CONFIG
# =========================

RING_ROWS = 28
SLOT_WIDTH = 4         # <-- each number gets 4 chars -> guaranteed spacing
ROW_WIDTH = 90         # visual width (#slots * SLOT_WIDTH)
NUM_SLOTS = ROW_WIDTH // SLOT_WIDTH

ASPECT_X = 1.8

# =========================
# DRAW ROUND DIAL (SLOT-BASED, NO COLLISIONS)
# =========================

def draw_dial(pos, zero_count, highlight_zero):
    # prepare row slot arrays
    slot_rows = [[" " * SLOT_WIDTH for _ in range(NUM_SLOTS)] for _ in range(RING_ROWS)]

    # assign numbers to slots
    for n in range(100):
        angle = ((n - pos) / 100) * 2 * math.pi - math.pi / 2

        # 1) determine row via angle
        row = int(((math.sin(angle) + 1) / 2) * (RING_ROWS - 1))

        # 2) determine slot via angle
        slot_f = ((math.cos(angle) + 1) / 2) * (NUM_SLOTS - 1)
        slot = int(slot_f)

        label = f"{n:02}"

        # highlight zero if at top
        if n == 0 and highlight_zero:
            label = f"{GREEN}00{RESET}"

        # 3) resolve collisions by moving left/right
        s = slot
        for d in range(NUM_SLOTS):
            for sign in (-1, 1):
                test = slot + d * sign
                if 0 <= test < NUM_SLOTS and slot_rows[row][test].strip() == "":
                    s = test
                    break
            else:
                continue
            break

        # 4) place number into slot
        label = label.ljust(SLOT_WIDTH)
        slot_rows[row][s] = label

    # center counter row
    lines = ["".join(slots) for slots in slot_rows]
    mid = RING_ROWS // 2
    line = list(lines[mid])
    counter = f"hits: {zero_count}"
    start = (ROW_WIDTH - len(counter)) // 2
    line[start:start+len(counter)] = counter
    lines[mid] = "".join(line)

    return "\n".join(lines)

# =========================
# ANIMATION LOOP
# =========================

def animate(rotations, start=0, delay=0.03):
    pos = start
    hits = 0
    hide_cursor()

    try:
        for d, steps in rotations:
            step = -1 if d == "L" else 1

            for _ in range(steps):
                pos = (pos + step) % 100
                zero_at_top = (pos == 0)
                if zero_at_top:
                    hits += 1

                clear()
                print(draw_dial(pos, hits, zero_at_top))

                if zero_at_top:
                    time.sleep(0.3)
                time.sleep(delay)

    finally:
        show_cursor()


# =========================
# RUN
# =========================

animate(rotations, start=0)

