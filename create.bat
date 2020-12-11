@echo off

set fn=%1
@REM set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    @REM python create.py %fn% %flag%
    python create.py %fn%
)