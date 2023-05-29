@echo off

:add_environment_variable
if "%~1"=="" (
    echo Error: Please provide both the name and value of the environment variable.
    exit /b 1
)

setx %~1 %~2
if "%errorlevel%" neq "0" (
    echo Error adding the environment variable.
    exit /b 1
)

echo The environment variable %~1 has been added with the value %~2.
exit /b 0
