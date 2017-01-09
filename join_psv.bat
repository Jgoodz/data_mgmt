@ECHO OFF
for %%* in (.) do set CurrDirName=%%~nx*
FOR %%A IN (%Date:/=%) DO SET Today=%%A


for %%f in (*.psv) do ( type "%%f" >> "EGLGENERIC_PRF_0_%CurrDirName%.psv"
ECHO %%f
) 