import os
import time
import platform
from datetime import datetime
from collections import defaultdict

class USBWriteBlocker:
    def __init__(self):
        self.write_attempts = defaultdict(int)
        self.running = False
        self.platform = platform.system().lower()
        self.blocked_count = 0
        self.last_device = None
        
        self.print_banner()
        self.print_message("USB Write Blocker Initialized", "success")
        self.print_message(f"Operating System: {platform.system()} {platform.release()}", "info")
        
    def print_banner(self):
        print("\n" + "="*50)
        print("=== USB WRITE BLOCKER EMULATOR ===".center(50))
        print("="*50 + "\n")
        
    def print_message(self, message, msg_type="info"):
        colors = {
            "success": "\033[92m",  # Green
            "error": "\033[91m",    # Red
            "warning": "\033[93m",  # Yellow
            "info": "\033[94m",     # Blue
            "blocked": "\033[95m",  # Purple
        }
        reset = "\033[0m"
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = {
            "success": "[SUCCESS]",
            "error": "[ERROR]",
            "warning": "[WARNING]",
            "info": "[INFO]",
            "blocked": "[BLOCKED]"
        }.get(msg_type, "[INFO]")
        
        print(f"{colors.get(msg_type, '')}{timestamp} {prefix} {message}{reset}")
        
    def start(self):
        if self.running:
            self.print_message("Monitor is already running", "warning")
            return
            
        self.running = True
        self.print_message("Starting USB device monitoring", "success")
        
        try:
            while self.running:
                self.simulate_activity()
                time.sleep(3)
        except KeyboardInterrupt:
            self.stop()
            
    def stop(self):
        self.running = False
        self.print_message("\nStopping USB Write Blocker...", "info")
        self.generate_report()
        
    def simulate_activity(self):
        """Simulate USB device activity for demonstration"""
        devices = self.detect_devices()
        
        # Simulate device connection/disconnection
        if int(time.time()) % 10 == 0:
            new_device = f"USB_Drive_{int(time.time()) % 1000}"
            self.print_message(f"New device connected: {new_device}", "info")
            self.last_device = new_device
            
        # Simulate write attempts
        if int(time.time()) % 5 == 0 and self.last_device:
            self.block_write_attempt(self.last_device, f"file_{int(time.time()) % 100}.txt")
            
    def detect_devices(self):
        """Simulate device detection"""
        return ["USB_Drive_123", "USB_Drive_456"] if self.last_device else []
        
    def block_write_attempt(self, device, filename):
        """Simulate write blocking"""
        self.write_attempts[device] += 1
        self.blocked_count += 1
        
        self.print_message(
            f"Blocked write attempt to {device}: {filename} (Total blocks: {self.blocked_count})", 
            "blocked"
        )
        
        if self.write_attempts[device] % 3 == 0:
            self.print_message(
                f"Multiple write attempts detected from {device} (Count: {self.write_attempts[device]})", 
                "warning"
            )
            
    def generate_report(self):
        """Generate a summary report"""
        print("\n" + "="*50)
        print("=== FINAL REPORT ===".center(50))
        print("="*50)
        
        print(f"\nTotal blocked attempts: {self.blocked_count}")
        print("Blocked attempts per device:")
        
        for device, count in self.write_attempts.items():
            print(f"  - {device}: {count} attempts")
            
        print("\n" + "="*50 + "\n")

def main():
    blocker = USBWriteBlocker()
    blocker.start()

if __name__ == "__main__":
    main()
