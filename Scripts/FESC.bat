@echo off
:menu
echo ------------------------------------------------
echo                WELCOME TO FESC 
echo ------------------------------------------------
echo Press 1 to move a file from Drive (Z:) to (E:)
echo Press 2 to move a folder from Drive (Z:) to (E:)
echo Press 0 to exit
set /p choice=Enter your choice: 

if "%choice%"=="1" (
    python "D:\Windows\Scripts\moveFileToAnotherDrive.py"
    if %errorlevel%==0 (
        echo File has been successfully moved.
    ) else (
        echo Failed to move the file.
    )
) else if "%choice%"=="2" (
    python "D:\Windows\Scripts\moveFolderToAnotherDrive.py"
    if %errorlevel%==0 (
        echo Folder has been successfully moved.
    ) else (
        echo Failed to move the folder.
    )
) else if "%choice%"=="0" (
    exit
) else (
    echo Invalid choice. Please try again:
)

pause
goto menu
