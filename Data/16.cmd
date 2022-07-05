powercfg -h off
Powershell.exe -Command "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"
Powershell.exe -Command "powercfg /s e9a42b02-d5df-448d-aa00-03f14749eb61"
bcdedit /set disabledynamictick yes
bcdedit /deletevalue useplatformclock
bcdedit /set useplatformtick yes
Reg Add HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications /v GlobalUserDisabled /t REG_DWORD /d 1 /f
Powershell.exe -ExecutionPolicy Bypass -File "1.ps1"
regedit.exe /S Data\1.reg
regedit.exe /S Data\2.reg
regedit.exe /S Data\3.reg
regedit.exe /S Data\4.reg
regedit.exe /S Data\5.reg
regedit.exe /S Data\6.reg
regedit.exe /S Data\7.reg
regedit.exe /S Data\8.reg
regedit.exe /S Data\9.reg
regedit.exe /S Data\10.reg
regedit.exe /S Data\11.reg
regedit.exe /S Data\12.reg