@echo off
set DB_USER=odoo
set DB_PASSWORD=odoo
set ADDONS_PATH="addons,custom-addons"
set DATABASE=ctnews

REM Base command without the update argument
set CMD=python odoo-bin -r %DB_USER% -w %DB_PASSWORD% --addons-path=%ADDONS_PATH% -d %DATABASE%

REM Initialize the full command
set FULL_CMD=%CMD%

REM Check if --dev flag is present
for %%A in (%*) do (
    if "%%A"=="--dev" (
        set FULL_CMD=%FULL_CMD% --dev=reload
    )
)

REM Check if an argument was provided (-u)
if "%1"=="" (
    REM If no argument is given, just run the command
    set FINAL_CMD=%FULL_CMD%
) else (
    REM If an argument is given, add it to the command
    set FINAL_CMD=%FULL_CMD% %*
)

REM Echo the final command to be executed
echo Executing: %FINAL_CMD%
%FINAL_CMD%