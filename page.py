from flask import (
	Blueprint,
	flash,
	g,
	redirect,
	render_template,
	request,
	url_for,
)
from werkzeug.exceptions import abort

from ranger.rangefinder import rangefinder
from ranger.db import get_db

bp = Blueprint('page', __name__)

@bp.route('/', methods=('GET', 'POST'))
def search():
	if request.method == 'POST':
		query = [int(i) for i in request.form['query'].split(',')]
		answer = rangefinder(query)
		
		db = get_db()
		db.execute(
			'INSERT INTO history (query, answer)'
			' VALUES (?, ?)',
			(str(query), str(answer))
		)
		db.commit()
		return render_template('result.html', query=query, answer=answer)
	
	return render_template('search.html')
	

@bp.route('/history')
def history():
	db = get_db()
	searches = db.execute(
		'SELECT created, query, answer'
		' FROM history'
		' ORDER BY created desc'
	).fetchall()
	return render_template('history.html', searches=searches)