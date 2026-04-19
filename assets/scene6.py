import sys
import time
import random
import os

class C:
    OK = '\033[92m'
    WARN = '\033[93m'
    ERR = '\033[91m'
    INFO = '\033[94m'
    END = '\033[0m'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.03, realize_newlines=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(0, 0.01))
    if realize_newlines:
        print()

def fast_load(text, delay=0.1):
    print(text)
    time.sleep(delay)

# --- PRE-RECORDING BUFFER ---
time.sleep(0.5) 

# --- ANIMATION START ---
clear_terminal()
time.sleep(5) 

# --- TURN 1: THE INITIAL REQUEST (image_1c08a3.png) ---
sys.stdout.write(f"{C.OK}[RUN S:5 🔒]{C.END} {C.WARN}>{C.END} ")
sys.stdout.flush()
typewriter("in well h6 add 50 ul of copper, 50 ul of edta and 100 ul of bcs. do not home. remember to move the pump over the well", speed=0.04)

fast_load(f"[*] Goal received: 'in well h6 add 50 ul of copper, 50 ul of edta and 100 ul of bcs. do not home. remember to move the pump over the well'", 0.3)
typewriter("[*] Thinking...", speed=0.04)
time.sleep(2.0)
print()

print(f"{C.WARN}--- PLAN REVIEW (CTRL-C to abort) ---{C.END}")
steps_h6 = [
    "1. SIDEKICK: to_well {\"well\": \"h6\", \"pump\": \"p1\"}",
    "2. SIDEKICK: dispense {\"pump\": \"p1\", \"vol\": 50}",
    "3. SIDEKICK: to_well {\"well\": \"h6\", \"pump\": \"p2\"}",
    "4. SIDEKICK: dispense {\"pump\": \"p2\", \"vol\": 50}",
    "5. SIDEKICK: to_well {\"well\": \"h6\", \"pump\": \"p3\"}",
    "6. SIDEKICK: dispense {\"pump\": \"p3\", \"vol\": 100}"
]
for step in steps_h6:
    fast_load(f"{C.INFO} {step}{C.END}", 0.2)

print(f"\n{C.INFO}Actions: 'run', 'del <#>', 'edit <#> <key=val> <rationale>', 'add <dev> <cmd> <args> <rationale>'{C.END}")
sys.stdout.write("Action > ")
sys.stdout.flush()
typewriter("y", speed=0.1)

# Execution of first plan
print(f"\n{C.INFO}Executing Plan (ID: 339)...{C.END}")
for i in range(1, 4):
    fast_load(f" -> Step {i*2-1}/6: sidekick.to_well()... [{C.OK}OK{C.END}]", 0.4)
    fast_load(f" -> Step {i*2}/6: sidekick.dispense()... [{C.OK}OK{C.END}]", 0.2)
print(f"{C.OK}Plan finished successfully.{C.END}\n")
time.sleep(1.5)

# --- TURN 2: THE REORDER REQUEST (image_1c08e6.jpg) ---
sys.stdout.write(f"{C.OK}[RUN S:5 🔒]{C.END} {C.WARN}>{C.END} ")
sys.stdout.flush()
# The prompt you wanted to capture:
typewriter("do the same thing in well h8 but change the order of the solutions added", speed=0.05)

fast_load(f"[*] Goal received: 'do the same thing in well h8 but change the order of the solutions added'", 0.3)
typewriter("[*] Thinking...", speed=0.04)
time.sleep(2.5) # A bit more thinking for the logic of reordering
print()

# The Reordered Plan Review
print(f"{C.WARN}--- PLAN REVIEW (CTRL-C to abort) ---{C.END}")
# Notice the pump order changed: p3 (100ul) is now first
steps_h8 = [
    "1. SIDEKICK: to_well {\"well\": \"h8\", \"pump\": \"p3\"}",
    "2. SIDEKICK: dispense {\"pump\": \"p3\", \"vol\": 100}",
    "3. SIDEKICK: to_well {\"well\": \"h8\", \"pump\": \"p1\"}",
    "4. SIDEKICK: dispense {\"pump\": \"p1\", \"vol\": 50}",
    "5. SIDEKICK: to_well {\"well\": \"h8\", \"pump\": \"p2\"}",
    "6. SIDEKICK: dispense {\"pump\": \"p2\", \"vol\": 50}"
]
for step in steps_h8:
    fast_load(f"{C.INFO} {step}{C.END}", 0.2)

print(f"\n{C.INFO}Actions: 'run', 'del <#>', 'edit <#> <key=val> <rationale>', 'add <dev> <cmd> <args> <rationale>'{C.END}")
sys.stdout.write("Action > ")
sys.stdout.flush()
typewriter("y", speed=0.1)

# Final Execution
print(f"\n{C.INFO}Executing Plan (ID: 342)...{C.END}")
for i in range(1, 4):
    fast_load(f" -> Step {i*2-1}/6: sidekick.to_well()... [{C.OK}OK{C.END}]", 0.4)
    fast_load(f" -> Step {i*2}/6: sidekick.dispense()... [{C.OK}OK{C.END}]", 0.2)
print(f"{C.OK}Plan finished successfully.{C.END}")

# --- ANIMATION END ---

input("")