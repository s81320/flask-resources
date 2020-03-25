def print_html_intro():
	print("<!DOCTYPE html>")
	print("<html lang="+str('"')+"en"+str('"')+">") # make " printable!
	print("<head>")
	print("<meta charset="+str('"')+"UTF-8"+str('"')+">")
	print("<title>reversi pet project</title>")
	print("</head>")
	pass

def print_header():
	"""Print a row of labels for the reversi board display."""
	print("<tr>")
	for i in ['','A','B','C','D','E','F','G','H','']:
		print("<th>"+str(i)+"</th>",end='')
	print("</tr>")
	
def print_data_row(j:int, data:list):
	print("<tr>")
	print("<td>"+str(j)+"</td>",end='')
	for i in range(8):
		print("<td>"+str(data[i])+"</td>",end='')
	print("</tr>")
	
def print_table():
	print("<table>")
	print_header()
	print_data_row(1,[1,2,3,4,5,6,7,8])
	print_header()
	print("</table>")

if __name__ == '__main__':
	print_html_intro()
	print("<body>")
	print_table()
	print("</body>")
	print("</html>")
