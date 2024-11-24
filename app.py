from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql

app = Flask(__name__)


db = pymysql.connect( host= "" , port= "", user="", passwd="", db="", charset="")
cur = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

#로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sqlstring = "SELECT * FROM Authentication WHERE User_id = %s AND Password_hash = %s"
        cur.execute(sqlstring, (username, password))
        auth = cur.fetchone()
        if auth:
            return jsonify({'success': True})
        return jsonify({'success': False})
    return render_template('login.html')

#Users 기록 조회
@app.route('/users')
def user():
    id = request.args.get('id')
    sqlstring = "SELECT * from Users where Users_id ='"+id+"'"
    cur.execute(sqlstring) 

    Users = cur.fetchall() #사용하실 때에는 배열로 사용하시면 됩니다.
    return render_template('Users.html', Users=Users)


#음식 기록 조회
@app.route('/diet', methods=['GET','POST'])
def getdiet():
    if request.method == 'POST': #갱신
        new_diet = request.args.get('new_diet')
        new_diet_much = request.args.get('new_diet_much')
        new_diet_cal = request.args.get('new_diet_cal')
        sqlstring = "INSERT INTO Dietrecords VALUES('"+new_diet+"','"+new_diet_much+"',"+new_diet_cal+"')"
        cur.execute(sqlstring)
        return
    elif request.method == 'GET': #검색
        diet = request.args.get('diet')
        sqlstring_2 = "SELECT * from Dietrecords where user_id='"+id+"' AND diet_id='"+diet+"'"
        cur.execute(sqlstring_2)
        Dietrecords_2 = cur.fetchall()
        return render_template('Dietrecords.html', Dietrecords_2=Dietrecords_2)
    

    id = request.args.get('Users')
    sqlstring = "SELECT * from Dietrecords where user_id='"+id+"'"
    cur.execute(sqlstring)

    Dietrecords = cur.fetchall() #사용하실 때에는 배열로 사용하시면 됩니다.
    
    return render_template('Dietrecords.html', Dietrecords=Dietrecords)


#운동기록 조회
@app.route('/exercise', method=['GET','POST'])
def getexercise():
    if request.method == 'POST':
        new_exercise = request.args.get('new_exercise')
        new_exercise_time = request.args.get('new_exercise_time')
        new_exercise_cal = request.args.get('new_exercise_cal')
        sqlstring = "INSERT INTO Exerciserecords VALUES('"+new_exercise+"','"+new_exercise_cal+"',"+new_exercise_time+"')"
        cur.execute(sqlstring)
        return 
    elif request.method == 'GET': #검색
        exercise = request.args.get('exercise')
        sqlstring_2 = "SELECT * from Exerciserecords where user_id='"+id+"' AND exercise_id='"+exercise+"'"
        cur.execute(sqlstring_2)
        Exerciserecords_2 = cur.fetchall()
        return render_template('Exerciserecords.html', Exerciserecords_2=Exerciserecords_2)
    
    id = request.args.get('users')
    sqlstring = "SELCET * from Exerciserecords where Users_id='"+id+"'"
    cur.execute(sqlstring)

    Exerciserecords = cur.fetchall() #사용하실 때에는 배열로 사용하시면 됩니다.
    
    return render_template('Exerciserecords.html', Exerciserecords=Exerciserecords)

if __name__ == '__main__':
    app.run('0.0.0.0')
