import subprocess
import os

def find_pid(port):
    """
    Find the pid of a running msfrpcd process
    """
    cmd = "lsof -i -P -n"
    proc = subprocess.run(cmd.split(), capture_output=True)
    output = proc.stdout.decode("utf-8")
    output = output.split("\n")

    res = None

    for i in range(len(output)):
        if output[i].find(str(port)) != -1:
            res = i
            break
    
    if res is not None:
        output = output[res].split()[1]
        return output


def up():
    pid = find_pid(55553)
    if pid is not None:
        return pid

    cmd = "msfrpcd -P password -S"
    res = os.system(cmd)
    if res == 0:
        return find_pid(55553)


def down():
    pid = find_pid(55553)
    if pid is not None:
        cmd = "kill -9 " + pid
        subprocess.run(cmd.split())
        return 0
    return 0

        