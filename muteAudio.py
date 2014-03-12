
import sys
import winsound
import win32com.client

autoit = win32com.client.Dispatch( "AutoItX3.Control" )
#autoit.Run("NotePad.exe")
autoit.Send("{VOLUME_MUTE}")