import time
import notify2
from DesktopNotifier import topStories
ICON_PATH = ""

newsitems = topStories()

notify2.init("News Notifier")

n = notify2.Notification(None, None)

n.set_timeout(10000)
for newsitem in newsitems:
 
    n.update(newsitem['title'], newsitem['description'])
 
    n.show()
 
    time.sleep(15)