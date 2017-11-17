ls -l | awk '{print ;}' | grep -E -- '-r--r--r--' | wc -l
