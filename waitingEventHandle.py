
from ui.main_ui import start_wait_ui, html_generated, MyThread

import threading

# help function for wait UI
def controlled_start_wait_ui(stop_event):
    start_wait_ui(stop_event)

"""Thread and Wait UI can be started with:

wait_thread.start()

# Title selection should look like this:

select_title(title_json)        # just transforms the UI
while get_wait_for_title():     # we need this, to wait for the User to select one title
    time.sleep(1)               # without sleep CPU goes crazy
final_title = get_final_title() # get_final_title() returns the title selected by User

# and should be stopped with:

stop_event.set()
html_generated()
thread.join()
"""

#stop_event = threading.Event()
#wait_thread = threading.Thread(target=controlled_start_wait_ui, args=(stop_event,))
wait_thread = MyThread(1)  # iD: 1 = start_wait_ui()
chapter_thread = MyThread(2)
def stop_waitUI():
    #stop_event.set()
    html_generated()
    #wait_thread.join()
