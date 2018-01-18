@REM This script should only be invoked by the wlp/bin/isadc.bat script.

@REM De-quote input environment variable WAS_ISADC_DIR.
if defined WAS_ISADC_DIR set WAS_ISADC_DIR=!WAS_ISADC_DIR:"=!

if "%~1" == "-help" (
  !TOOL_JAVA_CMD_QUOTED! -help
  set JAVA_RC=!errorlevel!
  goto:eof
)

@REM Execute the tool script or JAR
if exist "!WAS_ISADC_DIR!/isadc.bat" (
  call "!WAS_ISADC_DIR!/isadc.bat"
  set RC=!errorlevel!
  goto:eof
)

set WAS_ISADC_DIR=!WLP_INSTALL_DIR!\..\lib\was-isadc

if not exist "!WAS_ISADC_DIR!\was_liberty" (
  !TOOL_JAVA_CMD_QUOTED! -error
  set JAVA_RC=!errorlevel!
  goto:eof
)

call "!WAS_ISADC_DIR!\isadc\isadc_liberty.bat" -outputzip "%TEMP%\WLP-ISADC.zip" -collectorBase "!WLP_ISADC_DIR!\was_liberty" %*
set RC=%errorlevel%
