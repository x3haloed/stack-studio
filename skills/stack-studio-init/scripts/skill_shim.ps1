[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Root,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$RemainingArguments
)

$ErrorActionPreference = 'Stop'

function Show-Usage {
    'usage: skill_shim.bat [-h] [root]'
    ''
    'Print file path, name, and description for all SKILL.md files.'
    ''
    'positional arguments:'
    '  root        Directory to scan recursively. Defaults to the repository root.'
    ''
    'options:'
    '  -h, --help  show this help message and exit'
}

if ($Root -in @('-h', '--help')) {
    Show-Usage
    exit 0
}

if ($RemainingArguments.Count -gt 0) {
    [Console]::Error.WriteLine(((Show-Usage) -join [Environment]::NewLine))
    exit 2
}

if (-not $Root) {
    $Root = Join-Path $PSScriptRoot '..\..\..'
}

if (-not (Test-Path -LiteralPath $Root -PathType Container)) {
    [Console]::Error.WriteLine("error: root is not a directory: $Root")
    exit 2
}
$resolvedRoot = (Resolve-Path -LiteralPath $Root).Path.TrimEnd('\', '/')

function ConvertTo-OneLine([string]$Value) {
    return (($Value -split '\s+' | Where-Object { $_ }) -join ' ').Trim()
}

function Remove-OuterQuotes([string]$Value) {
    $trimmed = $Value.Trim()
    if ($trimmed.Length -ge 2) {
        $first = $trimmed[0]
        $last = $trimmed[$trimmed.Length - 1]
        if (($first -eq '"' -or $first -eq "'") -and $first -eq $last) {
            return $trimmed.Substring(1, $trimmed.Length - 2)
        }
    }
    return $trimmed
}

function Read-SkillFrontmatter([string]$Path) {
    $lines = @(Get-Content -LiteralPath $Path)
    $result = @{ name = ''; description = '' }
    if ($lines.Count -eq 0 -or $lines[0].Trim() -ne '---') {
        return $result
    }

    $index = 1
    while ($index -lt $lines.Count -and $lines[$index].Trim() -ne '---') {
        $line = $lines[$index]
        if ($line -match '^(name|description):\s*(.*)$') {
            $key = $Matches[1]
            $value = $Matches[2].Trim()
            if ($value -match '^[|>]([+-])?$') {
                $block = [System.Collections.Generic.List[string]]::new()
                $index++
                while ($index -lt $lines.Count) {
                    $next = $lines[$index]
                    if ($next.Trim() -eq '') {
                        $block.Add('')
                    }
                    elseif ($next -match '^\s+') {
                        $block.Add($next.Trim())
                    }
                    else {
                        $index--
                        break
                    }
                    $index++
                }
                $result[$key] = ConvertTo-OneLine ($block -join ' ')
            }
            else {
                $result[$key] = ConvertTo-OneLine (Remove-OuterQuotes $value)
            }
        }
        $index++
    }
    return $result
}

"path`tname`tdescription"

$excludedSegments = @('.git', 'node_modules', '.venv', 'venv', '__pycache__')
Get-ChildItem -LiteralPath $resolvedRoot -Filter 'SKILL.md' -File -Recurse |
    Where-Object {
        $relative = $_.FullName.Substring($resolvedRoot.Length).TrimStart('\', '/')
        $segments = $relative -split '[\\/]'
        -not ($segments | Where-Object { $_ -in $excludedSegments })
    } |
    Sort-Object FullName |
    ForEach-Object {
        $metadata = Read-SkillFrontmatter $_.FullName
        $relative = $_.FullName.Substring($resolvedRoot.Length).TrimStart('\', '/') -replace '\\', '/'
        "$relative`t$($metadata.name)`t$($metadata.description)"
    }
