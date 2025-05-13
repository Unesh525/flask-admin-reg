from flask import Flask, render_template, request
import pymysql

app=Flask(__name__)

@app.route('/admin_reg',methods=['GET','POST'])
def admin_reg():
    if request.method == 'POST':
        conn = pymysql.connect(host='localhost',user='root',password='',db='project1',port=3306,autocommit=True)
        cur1 = conn.cursor()
        cur2 = conn.cursor()
        a = request.form['T1']
        b = request.form['T2']
        c = request.form['T3']
        d = request.form['T4']
        e = request.form['T5']
        ut = "admin"

        sql1 = "insert into admindata values('"+a+"','"+b+"','"+c+"','"+d+"')"
        sql2 = "insert into logindata values('"+d+"','"+e+"','"+ut+"')"

        cur1.execute(sql1)
        cur2.execute(sql2)

        n1 = cur1.rowcount
        n2 = cur2.rowcount

        if n1==1 and n2==1:
            msg = "AdminData and LoginData Saved"
        elif n1==1 and n2!=1:
            msg = "AdminData Saved but LoginData     not Saved"
        elif n1!=1 and n2==1:
            msg = "AdminData not Saved but LoginData Saved"
        else:
            msg = "Neither AdminData nor LoginData Saved"

        return render_template("AdminReg.html",data=msg)

    else:
        return render_template("AdminReg.html")



if __name__=='__main__':
    app.run(debug=True)