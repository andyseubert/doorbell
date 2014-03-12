Param([string]$port="8888",[string]$doorbellpath="e:\scripts\doorbell\doorbell\dist\DoorBellService.exe",[switch]$verbose)
## check if doorbellservice.exe is running by making sure this PC is listening on the right port

$verbose=$false

$ErrorActionPreference = "SilentlyContinue"
 
if($verbose){Write-Host "checking netstat"}
$netstat = $(netstat -an | select-string 8888)

if (!($netstat)) {
    if($verbose){write-host "starting $doorbellpath"}
    
    start-process $doorbellpath
    
    $dts= "{0:yyyy/MM/dd/ HH:mm}" -f (Get-Date)
    $from= (hostname) + "@collegenet.com"
    send-mailmessage -to "5035228381@vtext.com" -From "$from" -Subject "X" -Body "doorbellservice on $(hostname) Restart at $dts" -smtpserver "mailout.collegenet.com"

}else{
    if($verbose){Write-Host $netstat}
}