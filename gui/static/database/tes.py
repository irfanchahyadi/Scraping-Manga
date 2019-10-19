import sqlite3


con = sqlite3.connect('manga.db')
def get_manga(id):
	cur = con.cursor()
	if id == 'all':
		cur.execute('SELECT * FROM manga_list;')
	else:
		cur.execute('SELECT * FROM manga_list WHERE id=?', (id,))
	return cur.fetchall()

print(get_manga(1))