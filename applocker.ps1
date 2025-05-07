$logName = "ForwardedEvents"
$provider = "Microsoft-Windows-AppLocker"
$eventId = 0
$outFile = "C:\temp\applocker_export.log"

New-Item -ItemType Directory -Path (Split-Path $outFile) -Force | Out-Null

$events = Get-WinEvent -FilterHashtable @{
    LogName = $logName
    #StartTime=(Get-Date).AddMinutes(-60)
    #EndTime=Get-Date
} -ErrorAction Stop

$out = New-Object System.IO.StreamWriter($outFile, $false, [System.Text.Encoding]::UTF8)

foreach ($event in $events) {
    if ($eventId -eq 0) {
        if ($event.ProviderName -ne $provider) { continue }
    } else {
        if ($event.ProviderName -ne $provider -or $event.Id -ne $eventId) { continue }
    }
    $xml = [xml]$event.ToXml()

    # SID2Name
    $sid = $xml.Event.System.Security.UserID
    try {
        $user = (New-Object System.Security.Principal.SecurityIdentifier($sid)).Translate([System.Security.Principal.NTAccount]).Value
    } catch {
        $user = $sid
    }

    $computer = $xml.Event.System.Computer
    $policy = $xml.Event.UserData.RuleAndFileData.PolicyName
    $filepath = $xml.Event.UserData.RuleAndFileData.FilePath

    $out.WriteLine("<User>$user</User><Computer>$computer</Computer><PolicyName>$policy</PolicyName><FilePath>$filepath</FilePath>")
}

$out.Close()
Write-Host "Export abgeschlossen: $outFile"
