from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 실제 배포 시에는 고정된 시크릿 키 사용 권장
app.permanent_session_lifetime = timedelta(minutes=30)

# 임시 사용자 데이터 저장소 (실제로는 데이터베이스 사용 필요)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # AJAX 요청 처리
            username = request.form.get('username')
            password = request.form.get('password')
            
            if username in users and check_password_hash(users[username]['password'], password):
                session['user_id'] = username
                return jsonify({'success': True, 'message': '로그인 성공!'})
            return jsonify({'success': False, 'message': '아이디 또는 비밀번호가 잘못되었습니다.'})
        else:
            # 일반 폼 제출 처리
            username = request.form.get('username')
            password = request.form.get('password')
            
            if username in users and check_password_hash(users[username]['password'], password):
                session['user_id'] = username
                flash('로그인 성공!', 'success')
                return redirect(url_for('user'))
            flash('아이디 또는 비밀번호가 잘못되었습니다.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('로그아웃되었습니다.', 'info')
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users:
            flash('이미 존재하는 사용자입니다.', 'danger')
        else:
            users[username] = {
                'password': generate_password_hash(password),
            }
            flash('회원가입이 완료되었습니다. 로그인해주세요.', 'success')
            return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/user')
def user():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'danger')
        return redirect(url_for('login'))
    return render_template('MyPage.html')

@app.route('/exercise')
def getexercise():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'danger')
        return redirect(url_for('login'))
    return render_template('exercise.html')

@app.route('/diet')
def getdiet():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'danger')
        return redirect(url_for('login'))
    return render_template('food.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)