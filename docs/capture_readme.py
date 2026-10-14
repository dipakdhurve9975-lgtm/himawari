"""Capture the real renamed application for the repository README."""
import os
from pathlib import Path
import sys
import tempfile
import time
from PIL import ImageGrab
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root))
os.environ['HIMAWARI_DATA_DIR']=tempfile.mkdtemp(prefix='himawari-readme-')
from app import Himawari
app=Himawari();app.geometry('1080x640+40+40');app.set_theme('Dark');app.attributes('-topmost',True)
try:
    end=time.monotonic()+1
    while time.monotonic()<end:app.update();time.sleep(.01)
    ImageGrab.grab(bbox=(app.winfo_rootx(),app.winfo_rooty(),app.winfo_rootx()+app.winfo_width(),app.winfo_rooty()+app.winfo_height())).save(root/'screenshots/downloader-dark.png')
finally:app.close()
