@echo off
set DB_USER=odoo
set DB_PASSWORD=odoo
set ADDONS_PATH="addons,custom-addons"
set DATABASE=ctnews

REM Base command without the update argument
set CMD=python odoo-bin -r %DB_USER% -w %DB_PASSWORD% --addons-path=%ADDONS_PATH% -d %DATABASE% --dev=reload

REM Check if an argument was provided (-u)
if "%1"=="" (
    echo Running without the -u argument
    %CMD%
) else (
    echo Running with the -u argument
    %CMD% %*
)