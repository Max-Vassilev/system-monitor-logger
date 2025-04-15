import psutil
import time
import logging


logging.basicConfig(
    filename="system_usage.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

def log_system_usage():
    # Get CPU usage as a percentage (Processor)
    cpu_usage = psutil.cpu_percent(interval=1)
    # Get memory usage as a percentage (RAM)
    memory_usage = psutil.virtual_memory().percent
    # Get disk usage as a percentage (SSD/HDD)
    disk_usage = psutil.disk_usage("/Users").percent
    
    # Log the results to a file
    logging.info(
        f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}%"
    )

if __name__ == "__main__":
    while True:
        log_system_usage()
        time.sleep(600)
