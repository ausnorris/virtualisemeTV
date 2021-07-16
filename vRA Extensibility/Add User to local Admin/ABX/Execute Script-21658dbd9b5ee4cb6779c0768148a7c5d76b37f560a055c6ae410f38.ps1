function handler($context, $inputs) {
    $script_pass = $context.getSecret($inputs.winpass)
    $script_user = "administrator"
    $vcuser = $context.getSecret($inputs.vcUsername)
    $vcpassword = $context.getSecret($inputs.vcpassword)  
    $vcfqdn = $context.getSecret($inputs.customProperties.vcfqdn)
    $vrss = $context.getSecret($inputs.vrss) 
    $requser = $inputs.customProperties.requser
    Write-Host $requser
    $name = $inputs.resourceNames[0]

    Write-Host $name
    Connect-VIServer $vcfqdn -User $vcuser -Password $vcpassword -Force
    write-host “Waiting for VM Tools to Start”
    do {
    $toolsStatus = (Get-vm -name $name | Get-View).Guest.ToolsStatus
    write-host $toolsStatus
    sleep 3
    } until ( $toolsStatus -eq 'toolsOk' -or $toolsStatus -eq 'toolsOld' )
    $vm = Get-vm -name $name

    $output = $inputs.customProperties.osType
    Write-Host "VM OS Type is "$output
    
    $windowsString = 'WINDOWS'
    
    if ($output.Equals($windowsString)) {
        $script = 'Add-LocalGroupMember -Group "Administrators" -Member ' + '"' + $requser +'"'
        Write-Host $script
        Start-Sleep -s 240
        $runscript = Invoke-VMScript -VM $vm -ScriptText $script -GuestUser "$script_user" -GuestPassword "$script_pass" -ToolsWaitSecs 300
        <#Write-Host $runscript.ScriptOutput#>
        Write-Host "executed script"
    }

}


