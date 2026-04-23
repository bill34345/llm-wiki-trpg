[CmdletBinding()]
param(
    [switch]$ForceRelink
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $repoRoot "skills"
$targetRoot = Join-Path $HOME ".codex\skills"

if (-not (Test-Path -LiteralPath $sourceRoot)) {
    throw "Skills directory not found: $sourceRoot"
}

New-Item -ItemType Directory -Force -Path $targetRoot | Out-Null

$skills = Get-ChildItem -LiteralPath $sourceRoot -Directory | Sort-Object Name

foreach ($skill in $skills) {
    $target = Join-Path $targetRoot $skill.Name
    $targetExists = Test-Path -LiteralPath $target

    if ($targetExists) {
        $item = Get-Item -LiteralPath $target -Force
        $isLink = $item.Attributes -band [IO.FileAttributes]::ReparsePoint

        if (-not $isLink) {
            Write-Warning "Skip existing non-link target: $target"
            continue
        }

        $matchesTarget = $false
        try {
            $resolvedTarget = [System.IO.Path]::GetFullPath((Join-Path $target "..\"))
            $matchesTarget = $item.Target -contains $skill.FullName
        } catch {
            $matchesTarget = $false
        }

        if ($matchesTarget -and -not $ForceRelink) {
            Write-Host "[ok] already linked: $($skill.Name)"
            continue
        }

        if (-not $ForceRelink) {
            Write-Warning "Skip existing link target without -ForceRelink: $target"
            continue
        }

        Remove-Item -LiteralPath $target -Force
    }

    New-Item -ItemType Junction -Path $target -Target $skill.FullName | Out-Null
    Write-Host "[link] $($skill.Name) -> $($skill.FullName)"
}

Write-Host ""
Write-Host "Codex skill links are ready in $targetRoot"
Write-Host "Restart Codex to rescan skills."
