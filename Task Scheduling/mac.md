###### How to Schedule Python Scripts to run at specified time frame / intervals

> _Syntax_: * * * * * command to execute/path to file <br>
>         MIN HR DAY MONTH WEEKDAY CmdToExecute/PathToFile

* To view task running in .txt file, add
`with open('path/helloworld.txt', 'a')as f:`
    `f.write(HelloWorld)` to your python script.

* Type in cmd:
> $  crontab -e

* Choose an editor from the options
> /bin/nano <br>
> /bin/vim.basic <br>
> /bin/vim.tiny <br>
> /bin/ed

* To schedule your command, in this case `path/helloworld.txt` to run every 2hours after midnight only for March on Mondays, Type:
> 0 */2 * 3 mon path/helloworld.txt

_For more info on cronjobs, see: https://www.seobility.net/en/wiki/CronJob_

* Can also track changes in realtime
> $  watch cat path/helloworld.txt
