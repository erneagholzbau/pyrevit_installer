# pyrevit_installer
non-admin installer for Erne Holzbau version of pyRevit.

## download & install
download installer pyRevit_installer.exe from [latest release](https://github.com/erneagholzbau/pyrevit_installer/releases/latest) 
and install with a simple double click.

## build standalone exe with pyinstaller
#### install python dependencies:<br>
`python pip install --user pythonnet colorful pyinstaller`

#### needed dependencies in directory /deps:
* colorful <br>
    rgb.txt [github file link](https://github.com/timofurrer/colorful/blob/master/colorful/data/rgb.txt)
* libgit2sharp:
    * LibGit2Sharp [github file link](https://github.com/eirannejad/pyRevit/blob/master/bin/LibGit2Sharp.dll)
    * git2-106a5f2 [github file link]()

#### pyinstaller build command:

`pyinstaller --onefile pyRevit_installer.spec`

will build in `/build` and create a single file executable in `/dist`
