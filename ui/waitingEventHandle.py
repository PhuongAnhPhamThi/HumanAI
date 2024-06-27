
from ui.main_ui import start_wait_ui, html_generated, MyThread

import threading

# help function for wait UI
def controlled_start_wait_ui(stop_event):
    start_wait_ui(stop_event)


#stop_event = threading.Event()
#wait_thread = threading.Thread(target=controlled_start_wait_ui, args=(stop_event,))
wait_thread = MyThread(1)  # iD: 1 = start_wait_ui()
chapter_thread = MyThread(2)
def stop_waitUI():
    #stop_event.set()
    html_generated()
    #wait_thread.join()
