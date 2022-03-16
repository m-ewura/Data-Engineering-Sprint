###### How to Schedule Python Scripts to run at specified time frame / intervals

> _Syntax_: schtasks /create /sc <scheduletype> /tn <taskname> /tr <taskrun> [/s <computer> [/u [<domain>\]<user> [/p <password>]]] [/ru {[<domain>\]<user> | system}] [/rp <password>] [/mo <modifier>] [/d <day>[,<day>...] | *] [/m <month>[,<month>...]] [/i <idletime>] [/st <starttime>] [/ri <interval>] [{/et <endtime> | /du <duration>} [/k]] [/sd <startdate>] [/ed <enddate>] [/it] [/z] [/f]

* Change python script to an executable file
> pip install pyinstaller <br>
> pyinstaller --onefile {filename}.py

* The filename.exe can be found in the dist folder created and can be used anywhere.
* To schedule your app, in this case `helloworld.exe` to run at 8am everyday, Run this in the CLI:
> SCHTASKS /CREATE /SC DAILY /TN "TaskScheduling\helloworld.txt" /TR "C:\Windows\dist\helloworld.exe" /ST 08:00 /ET 08:15

_For more info on task scheduling, see: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create_

* Open Task Scheduler -> Task Scheduler Library -> History to see the logs on your tasks created.


* You can also create tasks directly from the Task Scheduler or using the Task Scheduler CLI.
_See: https://medium.com/@sameakin/automating-python-scripts-with-windows-task-scheduler-42f656d79401_
