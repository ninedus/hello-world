import os
import time
import threading

def create_thread(command):
        return threading.Thread(target=os.system, args=(command, ))

interval = 20 #unit : sec

script_map = {}
script_map['recv_coparn'] = "ls -la; sleep 3; ls -la"

thread_map = {}

for each_id in script_map.keys():
        thread_map[each_id] = create_thread(script_map[each_id])
        thread_map[each_id].start()

while True:
        for each_id in script_map.keys():
                if thread_map[each_id].isAlive():
                        continue

                thread_map[each_id] = create_thread(script_map[each_id])
                thread_map[each_id].start()

        time.sleep(interval)
