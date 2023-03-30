from flask import Flask, request, render_template, jsonify, session, redirect, url_for
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecretkey"

@app.route("/")
def main():
	return render_template("login.html")

@app.route('/input', methods=['POST','GET'])
def input():
  inputValueNama = request.form['inputValueNama']
  inputValueWa = request.form['inputValueWa']
  
  folder_name = inputValueNama
  file_name = f"user.txt"

  if not os.path.exists(f"DataBase/{folder_name}"):

    os.makedirs(f"DataBase/{folder_name}")
    print(f"Folder '{folder_name}' berhasil dibuat.")
    
    if not os.path.exists(os.path.join(f"DataBase/{folder_name}/{file_name}")):
    	with open(os.path.join(f"DataBase/{folder_name}/{file_name}"), "w") as f:
    		f.write(f'wa:{inputValueWa}')
    		print(f"File teks '{file_name}' berhasil dibuat di dalam folder '{folder_name}'.")
    if os.path.exists(os.path.join(f"DataBase/{folder_name}/{file_name}")):
    	print(f"Folder '{folder_name}' dan file teks '{file_name}' sudah ada.")
   
  response = {'success': True}

  return jsonify(response)
  


@app.route("/question/<username>",methods=['GET','POST'])
def question(username):
	if os.path.exists(os.path.join(f"./DataBase/{username}")):
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
		
		ab=open(f"./DataBase/{username}/data.txt", "a+")
		ab.write(f"\nnama :{name}\nsomeone said :{forum}\n")
		session["userSesi"] = name
		return redirect(url_for('hal',name=name))
		
	
	else :
		name=request.args.get('name')
		forum=request.args.get('forum')
		return redirect(url_for('hal',name=name))
  
if __name__ =="__main__":
	app.run(debug=True,port="5000")