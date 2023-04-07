from flask import Flask, request, render_template, jsonify, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route("/")
def main():
	return render_template("regist.html")

@app.route('/input', methods=['POST','GET'])
def input():
  inputValueNama = request.form['inputValueNama']
  inputValueWa = request.form['inputValueWa']
  
  folder_name = inputValueNama
  file_name = f"user.txt"

  if not os.path.exists(f"DataBase/user/{folder_name}/"):

    os.makedirs(f"DataBase/user/{folder_name}/")
    print(f"Folder '{folder_name}' berhasil dibuat.")
    
    if not os.path.exists(os.path.join(f"DataBase/user/{folder_name}/{file_name}")):
    	with open(os.path.join(f"DataBase/user/{folder_name}/{file_name}"), "w") as f:
    		f.write(f'{inputValueWa}')
    		
    		print(f"File teks '{file_name}' berhasil dibuat di dalam folder '{folder_name}'.")
    if os.path.exists(os.path.join(f"DataBase/user/{folder_name}/{file_name}")):
    	print(f"Folder '{folder_name}' dan file teks '{file_name}' sudah ada.")
   
  response = {'success': True}

  return jsonify(response)


@app.route("/question/<username>",methods=['GET','POST'])
def question(username):
	if os.path.exists(os.path.join(f"./DataBase/user/{username}")):
		session["useSesi"] =  username
		return render_template("Card.html",username=username)
		
	else:
		return 'Data tidak ada'
	
	
@app.route('/hal/<name>') 
def  hal(name) :
	data = session["userSesi"]
	return render_template("Card2.html",name=data)
	
	
	
@app.route("/pros",methods=['GET','POST'])
def inpt():
	#username = request.args.get('username')
	if request.method=="POST":
		name=request.form['name']
		forum=request.form['forum']
		username = session["useSesi"]
		if not os.path.exists(f"DataBase/data/{username}/"):
			os.makedirs(f"DataBase/data/{username}/")
		ab=open(f"./DataBase/data/{username}/data.txt", "w")
		ab.write(f"\n{forum}\n")
		session["userSesi"] = name
		
		return redirect(url_for('hal',name=name))
		
	
	else :
		name=request.args.get('name')
		forum=request.args.get('forum')
		return redirect(url_for('hal',name=name))


@app.route('/login')
def index():
	return render_template('login.html')

@app.route('/input2', methods=['POST','GET'])
def input_data():
	nama = request.form['nama']
	wa = request.form['wa']

	# cek nama folder pada direktori 'database'
	if nama in os.listdir('database/user/'):
		# cek isi file 'user.txt' pada folder yang sesuai
		with open(f"database/user/{nama}/user.txt") as f:
			if wa.strip() == f.read().strip():
				session['nama'] = nama
				return {'redirect': url_for('success')}
			else:
				return {'message': 'WA yang dimasukkan salah!'}
	else:
		return {'message': 'Nama yang dimasukkan tidak ditemukan!'}

@app.route('/success')
def success():
	if 'nama' in session:
		nama = session['nama']
		database = os.listdir(f'./database/data/{nama}')
		
		return render_template('index.html', database=database,nama=nama)
	else:
		return redirect(url_for('index'))


@app.route('/get_file/<filename>')
def get_file(filename):
    nama = session['nama']
    if not filename.endswith('.txt'):
    	return {'message': 'File tidak ditemukan!'}
    if filename.endswith('.txt'):
    	if filename == 'user.txt':
    		return {'message': 'Access denied'}
    	else:
    	    try:

    	    	# ambil isi file
    	    	with open(f'./database/data/{nama}/{filename}', 'r') as f:
    	    		file_content = f.read()
    	    		return {'content': file_content}
    	    except FileNotFoundError:
    	    	return {'message': 'File not found'}
    # return isi


if __name__ == '__main__':
	app.run(debug=True)

