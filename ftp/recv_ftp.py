import os
import time
import threading

def create_thread(command):
        return threading.Thread(target=os.system, args=(command, ))

interval = 20 #unit : sec

script_map = {}
script_map['recv_coparn'] = "/tesroot/shell/get_msg_WEST_FTP_COPARN.sh"
script_map['recv_coprar_ld'] = "/tesroot/shell/get_msg_WEST_FTP_COPRAR_LD.sh"
script_map['recv_coprar_ds'] = "/tesroot/shell/get_msg_WEST_FTP_COPRAR_DS.sh"

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
