$ppt = New-Object -ComObject PowerPoint.Application
try {
    $pptxPath = (Resolve-Path "Feasibility_and_Risk_Analysis_Slide.pptx").Path
    $outPath = Join-Path (Resolve-Path ".").Path "Feasibility_and_Risk_Analysis_Slide.png"
    $pres = $ppt.Presentations.Open($pptxPath, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
    $slide = $pres.Slides.Item(1)
    $slide.Export($outPath, "PNG", 1920, 1080)
    $pres.Close()
    Write-Host "SUCCESS: Exported to $outPath"
} finally {
    $ppt.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
