@ECHO OFF
for %%* in (.) do set CurrDirName=%%~nx*
FOR %%A IN (%Date:/=%) DO SET Today=%%A


for %%f in (*_idx_*) do ( type "%%f" >> "%CurrDirName%.psv"
ECHO %%f
) 
