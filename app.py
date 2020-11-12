from flask import Flask, render_template, url_for,flash, redirect
from form import AddForm, searchForm
import sqlite3	


app = Flask(__name__)
app.config['SECRET_KEY'] = 'random text'


@app.route('/Action', methods = ['GET'])
def Action():
	conn = sqlite3.connect('students.db')
	c = conn.cursor()
	var = c.execute("SELECT * FROM students")
	var = var.fetchall()
	holder = []
	for data in var:
		x = c.execute("SELECT colleges FROM colleges WHERE course = '%s' " % data[2]).fetchone()
		try:
			holder.append(data + x)
		except:
			pass
	return render_template('action.html', title= 'Edit' , var = holder)

	
@app.route('/Search', methods = ['GET','POST'])
def Search():
	form = searchForm()
	if form.validate_on_submit():
		try:
			conn = sqlite3.connect('students.db')
			c = conn.cursor()
			student_data = []
			var = c.execute("SELECT * FROM students WHERE idnumber LIKE '%s'" % ('%%'+form.key.data+'%%')).fetchmany() or c.execute("SELECT * FROM students WHERE course LIKE '%s'" % ('%%'+form.key.data+'%%')).fetchall()	
			if not var:				
				temp = c.execute("SELECT * FROM colleges WHERE colleges LIKE '%s'" % ('%%'+form.key.data+'%%')).fetchall()
				for data in temp:
					holder = c.execute("SELECT * FROM students WHERE course LIKE '%s'" % ('%%'+data[0]+'%%')).fetchall()
					for info in holder:
						info = list(info)
						info.append(data[1])
						info = tuple(info)
						student_data.append(info)
			else:
				print(var)
				for data in var:
					x = c.execute("SELECT colleges FROM colleges WHERE course = '%s' " % data[2]).fetchone()
					try:
						student_data.append(data + x)
					except:
						pass
			if student_data:
				flash('Search Successfully!')
			else:	
				flash('No Data Existed!')

			return render_template('search.html', title='Search', form= form, var = student_data)
		except Exception as e:
			flash('Query Error!')
			print(e)
	return render_template('search.html',title='Search', form= form)


@app.route('/', methods = ['GET','POST'])
def View():
	form = searchForm()
	conn = sqlite3.connect('students.db')
	c = conn.cursor()
	var = c.execute("SELECT * FROM students")
	var = var.fetchall()
	holder = []
	for data in var:
		x = c.execute("SELECT colleges FROM colleges WHERE course = '%s' " % data[2]).fetchone()
		try:
			holder.append(data + x)
		except:
			pass
	return render_template('view.html', title= 'View' , var = holder, form=form)

@app.route('/Register', methods=['GET','POST'])
def Register():
	form = AddForm()
	if form.validate_on_submit():
		try:
			conn = sqlite3.connect('students.db')
			c = conn.cursor()
			c.execute("INSERT INTO students(fullname,course,idnumber,year,gender) VALUES('%s','%s','%s','%s','%s')" % (form.fullName.data,form.Course.data,form.idNumber.data,form.year.data,form.gender.data))
			conn.commit()
			conn.close()
			flash('Registered Successfully!')
		except:
			flash('Information Already Exist!')
		return redirect(url_for('View'))
	return render_template('register.html',title='Register', form=form)

@app.route('/Delete/<string:id_number>', methods = ['GET'])
def Delete(id_number):
	conn = sqlite3.connect('students.db')
	c = conn.cursor()
	c.execute("DELETE FROM students WHERE idNumber= '%s'" % (id_number)).fetchone()
	conn.commit()
	conn.close()

	return redirect(url_for('View'))

@app.route('/Edit/<string:id_number>', methods = ['GET','POST'])
def Edit(id_number):
	form = AddForm()
	conn = sqlite3.connect('students.db')
	c = conn.cursor()
	var = c.execute("SELECT * FROM students WHERE idNumber= '%s'" % (id_number)).fetchone()
	if form.validate_on_submit():
		c.execute("UPDATE students SET fullname='%s', course='%s', idnumber ='%s', year='%s', gender='%s' WHERE idnumber='%s'" % (form.fullName.data,form.Course.data,form.idNumber.data,form.year.data,form.gender.data,id_number))
		conn.commit()
		conn.close()
		return redirect(url_for('View'))

	return render_template('edit.html',title='Edit', var = var,form = form)


if __name__ == '__main__':
	app.run(debug=True)
