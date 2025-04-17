import sys
import subprocess
import os

def call(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr, process.returncode

def checkout(hash):
    call(f"git checkout {hash}")

def check(cmd):
    return call(cmd)[2]

def getfullhash(hash):
    return str(call(f"git rev-parse {hash}")[0])[2:-3]

def getprev(hash):
    return str(call(f"git rev-parse {hash}^")[0])[2:][:7]

def getlist(start, end):
    s = getfullhash(start)
    res = str(call(f"git rev-list {end}")[0])[2:-3].replace("\\n", " ").split(getfullhash(s))[0].split()
    res.reverse()
    res.insert(0, s)
    return res

def getsep(list, start, end):
    return list[list.index(start):list.index(end)+1]

def mybisect(repopath, start, end, checkcommand):
    os.chdir(repopath)
    list = getlist(start, end)
    start = list[0]
    end = list[-1]
    while start != end:
        list = getsep(list, start, end)
        cur = list[int(len(list)/2)]
        checkout(cur)
        if check(checkcommand) == 0:
            end = cur
        else:
            start = cur
    checkout(start)
    return start if check(checkcommand) == 1 else None

# bad = mybisect("C:\\Users\\anber\\syspro\\git-bisect-test-repo", "6747dbf", "d0dce63", "python -m pytest main.py")
# print(f"{bad} is bad")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit(-1)
    bad = mybisect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(f"{bad} is bad")

# python3 solution.py <repo path> 6747dbf d0dce63 "python -m pytest main.py"
# https://github.com/AndrewBerdyshev/git-bisect-test-repo