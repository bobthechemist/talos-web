import sys
import time
import random
import os
import json

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

# Programmatically generate the original 45-step AI proposal to match the transcript logic
ai_proposal = []
# 1. Start the motor
ai_proposal.append({"device": "minion", "command": "motor_on", "args": {}})
# 2. Add copper (pump p1) and EDTA (pump p2) in various ratios to C1-C11
for i in range(1, 12):
    well_name = f"C{i}"
    vol_p1 = 200 - (i - 1) * 20
    vol_p2 = (i - 1) * 20
    
    ai_proposal.append({"device": "sidekick", "command": "to_well", "args": {"well": well_name, "pump": "p1"}})
    ai_proposal.append({"device": "sidekick", "command": "dispense", "args": {"pump": "p1", "vol": vol_p1}})
    ai_proposal.append({"device": "sidekick", "command": "to_well", "args": {"well": well_name, "pump": "p2"}})
    ai_proposal.append({"device": "sidekick", "command": "dispense", "args": {"pump": "p2", "vol": vol_p2}})

current_plan = list(ai_proposal)

def print_plan_review(plan):
    print(f"{C.WARN}--- PLAN REVIEW (CTRL-C to abort) ---{C.END}")
    for i, step in enumerate(plan):
        step_str = f"{i+1}. {step['device'].upper()}: {step['command']} {json.dumps(step['args'])}"
        fast_load(f"{C.INFO} {step_str}{C.END}", 0.02)
    print(f"\n{C.INFO}Actions: 'run', 'del <#>', 'edit <#> <key=val> <rationale>', 'add <dev> <cmd> <args> <rationale>'{C.END}")

# --- PRE-RECORDING BUFFER ---
time.sleep(0.5) 

# --- ANIMATION START ---
clear_terminal()
time.sleep(2) 

# Initial status update from the previous transaction success
print(f"{C.OK}[INFO] Plan executed successfully. (Plan ID: 292){C.END}\n")
time.sleep(1.0)

# --- TURN 1: THE COMPLEX RATIO REQUEST ---
sys.stdout.write(f"{C.OK}[RUN S:5 🔒]{C.END} {C.WARN}>{C.END} ")
sys.stdout.flush()
goal_text = "turn on the motor. now add copper and edta to these wells in various ratios start with 200 ul of copper and no edta in well c1 then change the amounts by 20 ul so that the final well si 200 ul of edta and no copper."
typewriter(goal_text, speed=0.02)

fast_load(f"[*] Goal received: '{goal_text}'", 0.3)
typewriter("[*] Thinking...", speed=0.03)
time.sleep(1.5)
print()

# Initial Plan Review (45 steps)
print_plan_review(current_plan)

# Edit 1: Delete Step 5 (dispense p2 vol 0 in C1)
sys.stdout.write("Action > ")
sys.stdout.flush()
typewriter("del 5", speed=0.1)
time.sleep(0.5)

# Applying deletion (Step 5 maps to index 4)
current_plan.pop(4)
print(f"{C.WARN}Step 5 removed (Rationale: sidekick does not like to dispense 0).{C.END}\n")
time.sleep(1.0)

# Revised Plan Review (44 steps remaining)
print_plan_review(current_plan)

# Edit 2: Delete Step 42 (dispense p1 vol 0 in C11)
sys.stdout.write("Action > ")
sys.stdout.flush()
typewriter("del 42", speed=0.1)
time.sleep(0.5)

# Applying deletion (the old step 43 is now step 42, which maps to index 41)
current_plan.pop(41)
print(f"{C.WARN}Step 42 removed (Rationale: sidekick does not like to dispense 0).{C.END}\n")
time.sleep(1.0)

# Final Plan Review (43 steps remaining)
print_plan_review(current_plan)

sys.stdout.write("Action > ")
sys.stdout.flush()
typewriter("run", speed=0.1)

# Execution of first plan
print(f"\n{C.INFO}Executing Plan (ID: 307)...{C.END}")
total_steps = len(current_plan)
for i, step in enumerate(current_plan):
    dev = step['device']
    cmd = step['command']
    fast_load(f" -> Step {i+1}/{total_steps}: {dev}.{cmd}()... [{C.OK}OK{C.END}]", 0.04)
print(f"{C.OK}Plan finished successfully.{C.END}\n")
time.sleep(1.5)


# --- TURN 2: THE STIRRING REQUEST ---
sys.stdout.write(f"{C.OK}[RUN S:5 🔒]{C.END} {C.WARN}>{C.END} ")
sys.stdout.flush()
goal_text_2 = "let the stirring go for anouther 30 seconds"
typewriter(goal_text_2, speed=0.03)

fast_load(f"[*] Goal received: '{goal_text_2}'", 0.3)
typewriter("[*] Thinking...", speed=0.03)
time.sleep(1.2)
print()

# Stirring Plan Review
print(f"{C.WARN}--- PLAN REVIEW (CTRL-C to abort) ---{C.END}")
stir_plan = [
    {"device": "minion", "command": "stir", "args": {"duration_seconds": 30}}
]
for i, step in enumerate(stir_plan):
    step_str = f"{i+1}. {step['device'].upper()}: {step['command']} {json.dumps(step['args'])}"
    fast_load(f"{C.INFO} {step_str}{C.END}", 0.2)

print(f"\n{C.INFO}Actions: 'run', 'del <#>', 'edit <#> <key=val> <rationale>', 'add <dev> <cmd> <args> <rationale>'{C.END}")
sys.stdout.write("Action > ")
sys.stdout.flush()
typewriter("run", speed=0.1)

# Stirring Execution
print(f"\n{C.INFO}Executing Plan (ID: 308)...{C.END}")
for i, step in enumerate(stir_plan):
    dev = step['device']
    cmd = step['command']
    fast_load(f" -> Step {i+1}/1: {dev}.{cmd}()...", 0.4)
    # Visual countdown simulation for the stirring timer
    for remaining in range(30, 0, -10):
        fast_load(f"    [Stirring... {remaining}s remaining]", 0.4)
    fast_load(f" -> Step {i+1}/1: {dev}.{cmd}()... [{C.OK}OK{C.END}]", 0.2)
print(f"{C.OK}Plan finished successfully.{C.END}")

# --- ANIMATION END ---

input("")