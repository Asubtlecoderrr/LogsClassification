import re
def classify_with_regex(log_msg):
    patterns = {
                r'Backup completed successfully.' : 'System Notification',
                r'Backup started at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.' : 'System Notification',
                r'Disk cleanup completed successfully.' : 'System Notification',
                r'Backup ended at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.' : 'System Notification',
                r'\d{4}-\d{2}-\d{2}( \d{2}:\d{2}:\d{2})?' : 'System Notification',
            }
    
    for pattern, label in patterns.items():
        if re.search(pattern, log_msg):
            return label
        elif 'email' in log_msg.lower():
            return 'Email Service'
        elif 'user' in log_msg.lower():
            return 'User Activity'
        
    return None
