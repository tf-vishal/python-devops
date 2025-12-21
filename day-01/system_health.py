# https://github.com/TrainWithShubham/python-for-devops/tree/main/day-01
import psutil

def user_threshold():
    cpu_threshold = int(input("Write Down the CPU Threshold You Want : "))
    memory_threshold = int(input("Whats the threshold for Memory usage: "))
    disk_threshold = int(input("Enter Disk Threshold: "))

    return cpu_threshold, memory_threshold, disk_threshold

def system_health():

    cpu_threshold, memory_threshold, disk_threshold = user_threshold()

    current_cpu_usage = psutil.cpu_percent(interval=1)
    current_vmemory_usage = psutil.virtual_memory()
    current_disk_stats = psutil.disk_usage("/")

    print("--------------------------------------------")


    # CPU Usage
    if current_cpu_usage > cpu_threshold:
        print("WARNING: CPU UNDER HIGH USAGE!! ", current_cpu_usage)
    else:
        print("CPU is working within the threshold!!", current_cpu_usage)
    

    # Memory Usage
    if current_vmemory_usage.percent > memory_threshold:
        print("WARNING: MEMORY UNDER HIGH USAGE!! ", current_vmemory_usage.percent)
    else:
        print("Memory is working within the threshold !!", current_vmemory_usage.percent)
    

    # Disk Usage
    if current_disk_stats.percent > disk_threshold:
        print("WARNING: DISK UNDER HIGH USAGE!! ", current_disk_stats.percent)
    else:
        print("DISK is working within the threshold", current_disk_stats.percent)

system_health()
    