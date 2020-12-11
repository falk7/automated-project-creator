@echo off

set fn=%1
set flag="web"
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    @REM python create.py %fn% %flag%
    python create.py %fn% %flag%
)