from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm

def classify(logs):
    labels=[]
    for log in logs:
        result = classify_logs(log)
        labels.append(result)
    return labels

def classify_logs(log):
    source, log_message = log
    if source == "LegacyCRM":
        label = classify_with_llm(log_message)
    else:
        label = classify_with_regex(log_message)
        if label is None:
            label = classify_with_bert(log_message)
    return label
        
logs = [
    ("LegacyCRM", "Lead conversion failed for prospect ID 7842 due to missing contact information."),
    ("LegacyCRM", "API endpoint 'getCustomerDetails' is deprecated and will be removed in version 3.2. Use 'fetchCustomerInfo' instead."),
    ("LegacyCRM", "Customer follow-up process for lead ID 5621 failed due to missing next action"),
    ("MorderCRM","User authentication failed for user ID 12345 due to invalid credentials."),
    ("MorderCRM", "Email notification failed to send for user ID 54321 due to SMTP server timeout."),
    ("MordernHR","12:30:45 12-10-2023 System Notification: Backup completed successfully."),
    ("MordernHR", "2023-10-12 14:15:30 Disk cleanup completed successfully."),
    ("MordernHR", "Security alert: Unauthorized access attempt detected on server."),
    ("MorderCRM", "Error: Database connection lost while processing transaction ID 9987."),
    ("MordernHR", "Failed to generate payroll report due to missing employee records."),
    ("MorderCRM", "Critical error: Unable to parse JSON response from external API."),
    ("MordernHR", "Error: Insufficient disk space to complete backup operation."),
    ("MorderCRM", "System error: Timeout occurred during user session validation."),
    ("LegacyCRM",	"Escalation rule execution failed for ticket ID 9807 - undefined escalation level."),
    ("LegacyCRM", "The 'ExportToCSV' feature is outdated. Please migrate to 'ExportToXLSX' by the end of Q3."),
    ("LegacyCRM", "Support for legacy authentication methods will be discontinued after 2025-06-01."),
    ("LegacyCRM", "Task assignment for TeamID 3425 could not complete due to invalid priority level.")
]

labels = classify(logs)
for log, label in zip(logs, labels):
    print(f"Log: {log[1]} | Label: {label} \n")
    