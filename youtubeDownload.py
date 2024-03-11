import pytube as yt
from pytube.exceptions import AgeRestrictedError, VideoUnavailable
from pytube.innertube import _default_clients
import PySimpleGUI as sg

_default_clients["ANDROID_MUSIC"] = _default_clients["WEB_CREATOR"]
url = 'https://www.youtube.com/watch?v=ho08YLYDM88'
fileName = 'HappyBirthDay'

# video download
video = yt.YouTube(url,
                   use_oauth=True,
                   allow_oauth_cache=True)
stream = video.streams.get_highest_resolution()
fileExtn = stream.mime_type.split('/')[1]
stream.download('F:\Youtube', filename=fileName + '.' + fileExtn)
"""

#_default_clients["ANDROID_MUSIC"]=_default_clients["ANDROID"]
windows_layout = [[sg.Text('Enter Url : '),sg.InputText()]
                  ,[sg.Text('Output File name : '),sg.InputText()]
                  ,[sg.Button('Download'),sg.Button('Exit')]
                  ,[sg.Text('Status:'),sg.Input(key='-Display-')]]

execution = sg.Window('Youtube Videos Download',windows_layout)

while True:
    event,value = execution.read()

    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break
    url=value[0]
    fileName=value[1]
    try:
        #video download
        video=yt.YouTube(url)
        stream=video.streams.get_highest_resolution()
        fileExtn=stream.mime_type.split('/')[1]
        stream.download('F:\Youtube',filename=fileName+'.'+fileExtn)

        #Display Status
        execution['-Display-'].update('Download Complete')
    except AgeRestrictedError:
        execution['-Display-'].update('Age Restricted Video')
    except Exception:
        execution['-Display-'].update(Exception)

execution.close()
"""
