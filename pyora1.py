import cx_Oracle, csv, time

todaysdate = time.strftime("%d.%m.%Y")
conn_str = u'USER/PASS@IP:PORT/service_name'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()
entity_list = []

#start_date = '31-dec-2009'
start_date = '01-jan-1980'

eagle_entity_list = 'RMS_TOT'
PERF_FREQ_CODE = 'D'
dest_csv_file = 'C:/Users/195499454/Desktop/' + eagle_entity_list + '_' + PERF_FREQ_CODE + '_missing_dates_' + str(todaysdate) + '.csv'


def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")
	
#grab list of entities from from eagle and store in entity_list
c.execute(u"select TRIM(CODE_VALUE) from rulesdbo.entity_list where entity_id = '" + eagle_entity_list + "'")
for row in c:
	entity_list.append(row[0])

#output entity list to be appended in terminal
for row in entity_list:
	print("".join(str(e) for e in row))
print("\n")
print "Eagle entity list " + eagle_entity_list + " contains a total of " + str(len(entity_list)) + " entities."
print "Press enter to search for missing dates for " + eagle_entity_list + "..."
pause()
print "Working... please wait..."

#define size of output_list from entity_list and add entity list to first row of output_list
output_list = [[] for n in range(len(entity_list))]
for i in range(0,len(entity_list)):
	output_list[i].append(entity_list[i])

#grab query results and save to output_list
for entity_col in range(0,len(entity_list)):
	if PERF_FREQ_CODE == 'D':
		c.execute(u"WITH alldates AS (SELECT (TO_DATE('" + start_date + "')-1) + ROWNUM AS d FROM dual CONNECT BY ROWNUM <= (sysdate - TO_DATE('" + start_date + "')-1) ) SELECT TO_CHAR(alldates.d, 'DD-FMMON-YYYY') AS ALL_DATES FROM alldates LEFT JOIN (select ps.level_type, ps.perf_freq_code,ps.begin_effective_date,ps.end_effective_date,psr.* from  performdbo.perf_sec_returns psr inner join performdbo.perf_summary ps on ps.perf_sum_inst = psr.perf_sum_inst where ps.entity_id in ('" + entity_list[entity_col] + "') and PERF_FREQ_CODE = '" + PERF_FREQ_CODE + "') t ON ( t.end_effective_date = alldates.d ) WHERE t.end_effective_date IS NULL ORDER BY alldates.d")
	elif PERF_FREQ_CODE == 'M':
		c.execute(u"WITH all_dates AS (SELECT add_months('" + start_date + "',level - 1) AS d FROM dual CONNECT BY sysdate >= add_months('" + start_date + "',level - 1) ) SELECT TO_CHAR(all_dates.d, 'DD-FMMON-YYYY') FROM all_dates LEFT JOIN (select ps.level_type, ps.perf_freq_code,ps.begin_effective_date,ps.end_effective_date,psr.* from  performdbo.perf_sec_returns psr inner join performdbo.perf_summary ps on ps.perf_sum_inst = psr.perf_sum_inst  where ps.entity_id in ('" + entity_list[entity_col] + "') and PERF_FREQ_CODE = '" + PERF_FREQ_CODE + "') t ON ( t.end_effective_date = all_dates.d ) WHERE t.end_effective_date IS NULL ORDER BY all_dates.d")

	#ORACLE EXAMPLE TO FORMATE DATE: TO_CHAR(START_DATE, 'YYYY/MM/DD HH:MI:SS')
	for row in c:
		#output_list.append(x(c) for x in output_list)
		output_list[entity_col].append(row[0]) 
		#output_list[entity_col].append(", ".join(str(e) for e in row))
		#print(", ".join(str(e) for e in row) + "\n")
print("\n")

#print entire output_list to terminal inclusing headers
print "Data output to CSV file: "
for row in output_list:
	print(", ".join(str(e) for e in row))

with open(dest_csv_file,'wb') as outfile:
	csv_file=csv.writer(outfile, lineterminator='\n') #, delimiter=',',lineterminator='\n\n'
	for row in output_list:
		csv_file.writerow(row)	

conn.close()
outfile.close()

print "Output successfully saved to " + dest_csv_file
