import os
import time
import pandas as pd
from datetime import datetime, timedelta
import win32evtlog
import pywintypes

# Function to read Windows event logs
def read_event_logs(log_name, since_time=None):
    events = []

    try:
        # Connect to the event log
        log_handle = win32evtlog.OpenEventLog(None, log_name)

        # Set the time to read events from (optional)
        if since_time:
            since_time = since_time.timestamp()
        else:
            since_time = 0  # Default to all events

        # Read events from the log
        while True:
            events_batch = win32evtlog.ReadEventLog(log_handle, win32evtlog.EVENTLOG_BACKWARDS_READ |
                                                    win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
            if not events_batch:
                break

            for event in events_batch:
                try:
                    # Convert pywintypes.datetime to Unix timestamp
                    event_time = event.TimeGenerated.timestamp()
                    if event_time >= since_time:
                        events.append({
                            "EventTime": datetime.fromtimestamp(event_time),
                            "EventID": event.EventID,
                            "EventType": event.EventType,
                            "EventSource": event.SourceName,
                            "EventCategory": event.EventCategory,
                            "EventMessage": event.StringInserts,
                        })
                except pywintypes.error:
                    pass

        # Close the event log
        win32evtlog.CloseEventLog(log_handle)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return events

# Main function for event log analytics
def main():
    # Specify the event log name (e.g., "Application", "System", "Security")
    log_name = "Application"

    # Set the time to go back 7 days from the current date and time
    since_time = datetime.now() - timedelta(days=7)  # Capture events from the last 7 days

    # Read event logs
    events = read_event_logs(log_name, since_time)

    if not events:
        print("No event logs found or an error occurred.")
    else:
        # Create a DataFrame from the events
        df = pd.DataFrame(events)

        # Display the DataFrame
        print("Event Log Summary:")
        print(df.head())  # Display the first few events as a sample

if __name__ == "__main__":
    main()
