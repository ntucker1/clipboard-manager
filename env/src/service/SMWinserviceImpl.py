import time
import random

from pathlib import Path
from SMWinservice import SMWinservice

class SMWinserviceImpl(SMWinservice):
    
    _svc_name_ = 'clipboardManager'
    _svc_display_name_ = 'Clipboard Manager Service'
    _svc_description_ = 'View and manage clipboard entries.'

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:\\{x}.txt').touch()
            time.sleep(5)

if __name__ == '__main__':
    SMWinserviceImpl.parse_command_line()