wmic.exe /Namespace:\\root\default Path SystemRestore Call CreateRestorePoint "Before optimizing", 100, 7
DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
sfc/scannow
cd C:\ProgramData\Microsoft\Windows Defender\Platform\4.18*
MpCmdRun -Scan -ScanType 2
MpCmdRun -Scan -ScanType -BootSectorScan