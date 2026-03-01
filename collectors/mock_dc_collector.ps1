
# Mock DC Collector - outputs JSON

function Get-MockDCStatus {
    $dcList = @(
        @{ Name='DC-01'; Replication='Healthy'; SYSVOL='OK'; LDAPBind='Success'; DHCPScope='80% Used'; Services=@{'DNS'='Running';'DHCP'='Running';'ADWS'='Stopped'}; LastChecked=(Get-Date).ToString('yyyy-MM-dd HH:mm:ss') },
        @{ Name='DC-02'; Replication='Warning'; SYSVOL='OK'; LDAPBind='Success'; DHCPScope='50% Used'; Services=@{'DNS'='Running';'DHCP'='Stopped';'ADWS'='Running'}; LastChecked=(Get-Date).ToString('yyyy-MM-dd HH:mm:ss') }
    )
    return $dcList
}

$dcStatus = Get-MockDCStatus | ConvertTo-Json -Depth 5 -Compress
$OutputPath = "$PSScriptRoot\..\mock_dc_status.json"
$dcStatus | Out-File -FilePath $OutputPath -Encoding UTF8
Write-Host "✅ Mock DC Status JSON created at: $OutputPath"

# LDAP placeholder
<#
# Example: restart services via LDAP
$LDAPServer = "ldap://DC-01"
$Username = "<DOMAIN_USER>"
$Password = "<PASSWORD>"
# To be implemented
#>

# Notifications placeholder
function Send-TeamsNotification { param([string]$Message) Write-Host "📣 Teams placeholder: $Message" }
function Send-TelegramNotification { param([string]$Message) Write-Host "📣 Telegram placeholder: $Message" }
