@ECHO OFF
for %%* in (.) do set CurrDirName=%%~nx*
FOR %%A IN (%Date:/=%) DO SET Today=%%A

for %%f in (*.csv) do ( type "%%f" >> "CSV_eagle_default_in_csv_smf_1_%CurrDirName%.csv"
ECHO %%f
) 