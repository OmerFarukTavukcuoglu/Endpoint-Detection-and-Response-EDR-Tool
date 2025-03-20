#!/usr/bin/env python3
"""
Advanced Endpoint Detection and Response (EDR) Tool
---------------------------------------------------
Features:
- Continuously monitors local system processes using psutil.
- Detects suspicious processes based on a configurable list and resource usage thresholds.
- Logs detailed alerts (including PID, name, user, CPU, memory usage) using a rotating log file.
- Designed for continuous deployment on endpoints.

Usage:
  python advanced_edr.py --interval 5 --threshold 5
"""

import time
import argparse
import logging
import psutil
from logging.handlers import RotatingFileHandler

# Configure rotating log handler
logger = logging.getLogger("AdvancedEDR")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("advanced_edr.log", maxBytes=1000000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Configurable list of suspicious keywords (can be extended or loaded from a configuration file)
SUSPICIOUS_PROCS = ["netcat", "nmap", "hydra", "john", "sqlmap"]

def monitor_processes(interval, threshold):
    """
    Monitors processes and logs any process whose name contains suspicious keywords
    and has CPU usage above a threshold.
    """
    logger.info("Starting advanced process monitoring (interval=%s sec, CPU threshold=%s%%)", interval, threshold)
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
            try:
                pname = proc.info['name'].lower()
                if any(keyword in pname for keyword in SUSPICIOUS_PROCS) and proc.info['cpu_percent'] > threshold:
                    alert = (f"Suspicious process detected: PID={proc.info['pid']}, Name={proc.info['name']}, "
                             f"User={proc.info['username']}, CPU={proc.info['cpu_percent']}%, Memory={proc.info['memory_percent']:.2f}%")
                    logger.info(alert)
                    print(alert)
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                logger.debug("Process iteration error: %s", e)
                continue
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Advanced Endpoint Detection and Response (EDR) Tool")
    parser.add_argument("--interval", type=int, default=5, help="Monitoring interval in seconds (default: 5)")
    parser.add_argument("--threshold", type=int, default=5, help="CPU usage threshold percentage (default: 5)")
    args = parser.parse_args()
    monitor_processes(args.interval, args.threshold)

if __name__ == "__main__":
    main()
