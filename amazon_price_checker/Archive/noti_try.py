# Desktop Notification
import notify2
notify2.init('Notification')
n = notify2.Notification(
    'Testing NOTIFICATIONS...', 'It Works!!')
n.show()
