@ECHO OFF
for %%* in (.) do set CurrDirName=%%~nx*
FOR %%A IN (%Date:/=%) DO SET Today=%%A


for %%f in (*_cons_*) do ( type "%%f" >> "..\EGLGENERIC_POS_0_%CurrDirName%.psv"
ECHO %%f
) 