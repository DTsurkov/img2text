class Img2Text {
    [string]$Server

    Img2Text([string]$Server) {
        $this.Server = $Server
    }

    hidden [PSCustomObject] CallPost([string]$Uri, [hashtable] $Params) {
        try {
            $Response = Invoke-RestMethod -Uri "http://$($this.Server)$Uri" -Method Post @Params
            if ($Response) {
                return $Response
            }
            else {
                throw "Error: No response from server"
            }
        }
        catch {
            throw "Error: $($_.Exception.Message)"
        }
    }

    [string] RecognizeText([string]$ImgPath) {
        $Params = @{
            "Headers" = @{
                "Content-Type" = "multipart/form-data"
            }
            "Form"    = @{
                "file" = Get-Item -Path $ImgPath -ErrorAction Stop
            }
        }
        return $this.CallPost("/ocr", $Params).text
    }
}

$Client = [Img2Text]::new("127.0.0.1:8000")

$Result = $Client.RecognizeText("$PSScriptRoot/bitlocker.png")
Write-Output "Result: $Result"

if ($Result -match "PIN") {
    Write-Output "Pattern found!"
}