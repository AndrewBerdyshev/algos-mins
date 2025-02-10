import sys
import subprocess
import os

def call(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr, process.returncode

def check(cmd):
    return call(cmd)[2]

def getprev(hash):
    return str(call(f"git rev-parse {hash}^")[0])[2:][:7]

def mybisect(repopath, start, end, checkcommand):
    os.chdir(repopath)

    prev = end
    cur = end
    while True:
        call(f"git checkout {cur}")
        if check(checkcommand) == 0:
            return prev
        prev = cur
        cur = getprev(prev)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit(-1)
    bad = mybisect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(f"{bad} is bad")

# python3 solution.py <repo path> 6747dbf d0dce63 "python -m pytest main.py"
# https://github.com/AndrewBerdyshev/git-bisect-test-repo