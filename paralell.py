import subprocess

# Paths to your scripts
script_paths = ["/home/xxx/xxx/xxx/xxx/eyes_detection.py", "/home/xxx/xxx/xxx/xxx/motor_control.py", "/home/xxx/xxx/xxx/xxx/obstacle_avoidance.py"]

processes = []

for script in script_paths:
    # Start each script as a subprocess
    processes.append(subprocess.Popen(['python3', script]))

# Wait for all processes to finish
for proc in processes:
    proc.wait()
