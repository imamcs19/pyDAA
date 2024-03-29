# Koding Contoh MK Desain dan Analisis Algoritma (DAA) Semester Ganjil 2022/2023 Filkom UB
# Rencana Pembelajaran MK DAA Semester Ganjil 2022/2023 Kelas H
# Fakultas Ilmu Komputer (Filkom), Universitas Brawijaya (UB) 2022.

# Dosen Pengampu:
# 1. Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | Filkom UB

from flask import Flask,render_template, Response, redirect,url_for,session,request,jsonify
from flask import render_template_string
import sqlite3
from flask_cors import CORS

from flask import send_file
from flask_qrcode import QRcode

from io import BytesIO
import os

import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
# from bokeh.util.string import encode_utf8

app = Flask(__name__, static_folder='static')
qrcode = QRcode(app)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "static/qr_app/db/qrdata.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# DB untuk qr_app
db_qr = SQLAlchemy(app)
migrate = Migrate(app, db_qr)

# Operasi untuk migrate
# flask db_qr init
# flask db_qr migrate
# flask db_qr upgrade

from static.qr_app.model.StudentModel import Student
from static.qr_app.model.AttendanceModel import Attendance
from static.qr_app.module.Camera import Scanner
# import pyqrcode
import uuid

CORS(app, resources=r'/api/*')

app.secret_key = 'filkomub2223^&&*(&^(filkom#BJH#G#VB#DAA99nDataPyICS_ap938255bnUB'

# keterangan:
# "#" adalah untuk comment
# <br> adalah new line
# &nbsp; adalah spasi
# <!-- --> atau <!--- ---> adalah untuk comment

# FrameWeb_atas & FrameWeb_bawah untuk dekorasi web
# agar menjadi Web yang Responsif

FrameWeb_atas = """
{% extends "extends/base.html" %}
{% block title %}
    <title>Web App DAA Dgn Python</title>
{% endblock title %}
{{ self.title() }}
    Home
{{ self.title() }}
<button onclick="window.location.href='/'" class="btn btn-outline btn-rounded btn-info">
    <i class="ti-arrow-left m-l-5"></i>
    <span>Back Home</span>
</button> Project 1

{{ self.title() }}
    Project 1

{% block content %}
"""
A_a = FrameWeb_atas

FrameWeb_bawah = """
{% endblock content %}
"""
Z_z = FrameWeb_bawah

# @app.route('/')
# def hello_daa():
#    return 'Hello Students | Koding Desain dan Analisis Algoritma (DAA) pada Teknologi Cloud :D'

@app.route("/testView_dari_project2_regresi_sbg_fp", methods=['GET', 'POST'])
def testView_dari_project2_regresi_sbg_fp():

    template_view = '''
        <script type="text/javascript" src="{{ url_for('static', filename = 'js/jquery.min.js') }}"></script>
        <div class="row">
                <div class="col-md-6">
                    <div class="white-box">
                        <h3 class="box-title m-b-0">Prediksi Hasil Pengujian (misal ambil contoh dari topik Project 2 Kel. Anda): </h3>
                        <p class="text-muted m-b-30 font-13"> masukkan nilai parameter Anda </p>
                        <form action="/testView_dari_project2_regresi_sbg_fp" method="post" class="form-horizontal">
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x1 = Suhu badan*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var1" {% if var1 is defined and var1 %} value="{{var1}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x2 = Intensitas batuk*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var2" {% if var2 is defined and var2 %} value="{{var2}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x3 = Intensitas interaksi dgn lingkungan*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var3" {% if var3 is defined and var3 %} value="{{var3}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x4 = Pola nafas (sesak atau tidak)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var4" {% if var4 is defined and var4 %} value="{{var4}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x5 = Kondisi kesadaran (sadar atau tidak)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var5" {% if var5 is defined and var5 %} value="{{var5}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x6 = warna cairan hidung (hijau = 100, kuning = 67, bening = 33)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var6" {% if var6 is defined and var6 %} value="{{var6}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x7 = frekuensi buang air kecil*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var7" {% if var7 is defined and var7 %} value="{{var7}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group m-b-0">
                                <div class="col-sm-offset-3 col-sm-9 text-right">
                                    <button type="submit" class="btn btn-info waves-effect waves-light m-t-10">Hitung Hasil Prediksi</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="white-box row">
                        <h3 class="box-title m-b-0">Estimasi hasil prediksinya adalah </h3>
                        {% if c_save is defined and c_save %}
                        <p class="text-5xl font-bold"> nama Cov-19 & Var. baru (y1) = {{'%0.4f'|format(c_save[0][0]|float)}} (hasil pembulatannya =  {{ c_save_round[0][0]}}) </p>
                        <p class="text-5xl font-bold"> imunitas tubuh (y2) = {{'%0.4f'|format(c_save[0][1]|float)}} (hasil pembulatannya =  {{ c_save_round[0][1]}}) </p>
                        {% endif %}
                    </div>
                </div>
                <div class="col-md-6">
                <div class="white-box mt-8 row">
                <div class="justify-around bg-white rounded-lg">
                        <img class="col-md-3 col-xs-12" src="{{ url_for('static', filename = 'img/filkom.png') }}" alt="logo-filkom">
                        <img class="col-md-3 col-xs-12" src="{{ url_for('static', filename = 'img/conan.jpg') }}" alt="kartun-conan">
                </div>
                 </div>
                </div>
            </div>
    '''

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /testView_dari_project2_regresi_sbg_fp

        import numpy as np

        def persamaan_beta (x,y):
            hasilbeta = np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.matmul(np.transpose(x),y))
            return hasilbeta

        def y_bar(x_uji,beta):
            hasil_y_bar = np.matmul(x_uji, beta)
            return hasil_y_bar


        x = np.array ([
            [4, 4, 3, 3, 6, 3, 3],
            [6, 6, 9, 7, 8, 7, 6],
            [4, 7, 9, 7, 3, 6, 4],
            [7, 6, 5, 3, 4, 7, 8],
            [4, 3, 6, 6, 5, 7, 3],
            [6, 4, 5, 6, 2, 7, 3],
            [3, 4, 6, 3, 3, 3, 4]
        ])

        y = np.array ([
            [5, 2],
            [8, 3],
            [10, 4],
            [5, 2],
            [5, 2],
            [8, 3],
            [5, 2]
        ])

        var1_in = float(request.form['var1'])
        var2_in = float(request.form['var2'])
        var3_in = float(request.form['var3'])
        var4_in = float(request.form['var4'])
        var5_in = float(request.form['var5'])
        var6_in = float(request.form['var6'])
        var7_in = float(request.form['var7'])

        beta = persamaan_beta(x,y)

        # Memasukkan data uji (x_uji)
        x_uji = np.array([
           [var1_in,var2_in,var3_in,var4_in,var5_in,var6_in,var7_in]
           ])
        hitung_y_bar = y_bar(x_uji,beta)

        hitung_y_bar_round = hitung_y_bar.copy()

        # Agar angkanya menjadi bulat, maka dibulatkan ke atas
        hitung_y_bar_round = np.ceil(hitung_y_bar_round)

        # yang nilainya < 0, set = 0
        hitung_y_bar_round[hitung_y_bar_round < 0] = 0

        return render_template_string(A_a+template_view+Z_z, var1 = var1_in,
        var2 = var2_in, var3 = var3_in, var4 = var4_in, var5 = var5_in,
        var6 = var6_in, var7 = var7_in, c_save = list(hitung_y_bar), c_save_round = list(hitung_y_bar_round))

    else: # untuk yang 'GET' data awal untuk di send ke /testView_dari_project2_regresi_sbg_fp
        return render_template_string(A_a+template_view+Z_z)

@app.route("/testView_dari_project2_klasifikasi_sbg_fp", methods=['GET', 'POST'])
def testView_dari_project2_klasifikasi_sbg_fp():

    template_view = '''
        <script type="text/javascript" src="{{ url_for('static', filename = 'js/jquery.min.js') }}"></script>
        <div class="row">
                <div class="col-md-6">
                    <div class="white-box">
                        <h3 class="box-title m-b-0">Prediksi Hasil Pengujian (misal ambil contoh dari topik Project 2 Kel. Anda): </h3>
                        <p class="text-muted m-b-30 font-13"> masukkan nilai parameter Anda </p>
                        <form action="/testView_dari_project2_klasifikasi_sbg_fp" method="post" class="form-horizontal">
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x1 = Suhu badan*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var1" {% if var1 is defined and var1 %} value="{{var1}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x2 = Intensitas batuk*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var2" {% if var2 is defined and var2 %} value="{{var2}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x3 = Intensitas interaksi dgn lingkungan*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var3" {% if var3 is defined and var3 %} value="{{var3}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x4 = Pola nafas (sesak atau tidak)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var4" {% if var4 is defined and var4 %} value="{{var4}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x5 = Kondisi kesadaran (sadar atau tidak)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var5" {% if var5 is defined and var5 %} value="{{var5}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x6 = warna cairan hidung (hijau = 100, kuning = 67, bening = 33)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var6" {% if var6 is defined and var6 %} value="{{var6}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x7 = frekuensi buang air kecil*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var7" {% if var7 is defined and var7 %} value="{{var7}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group m-b-0">
                                <div class="col-sm-offset-3 col-sm-9 text-right">
                                    <button type="submit" class="btn btn-info waves-effect waves-light m-t-10">Hitung Hasil Prediksi</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="white-box row">
                        <h3 class="box-title m-b-0">Estimasi hasil prediksinya adalah </h3>
                        {% if c_save is defined and c_save %}
                        <p class="text-5xl font-bold"> nama Cov-19 & Var. baru (y1) = {{'%0.4f'|format(c_save[0][0]|float)}} (hasil pembulatannya =  {{ c_save_round[0][0]}}) </p>
                        <p class="text-5xl font-bold"> imunitas tubuh (y2) = {{'%0.4f'|format(c_save[0][1]|float)}} (hasil pembulatannya =  {{ c_save_round[0][1]}}) </p>
                        {% endif %}
                    </div>
                </div>
                <div class="col-md-6">
                <div class="white-box mt-8 row">
                <div class="justify-around bg-white rounded-lg">
                        <img class="col-md-3 col-xs-12" src="{{ url_for('static', filename = 'img/filkom.png') }}" alt="logo-filkom">
                        <img class="col-md-3 col-xs-12" src="{{ url_for('static', filename = 'img/conan.jpg') }}" alt="kartun-conan">
                </div>
                 </div>
                </div>
            </div>
    '''

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /testView_dari_project2_klasifikasi_sbg_fp

        import numpy as np

        def persamaan_beta (x,y):
            hasilbeta = np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.matmul(np.transpose(x),y))
            return hasilbeta

        def y_bar(x_uji,beta):
            hasil_y_bar = np.matmul(x_uji, beta)
            return hasil_y_bar


        x = np.array ([
            [4, 4, 3, 3, 6, 3, 3],
            [6, 6, 9, 7, 8, 7, 6],
            [4, 7, 9, 7, 3, 6, 4],
            [7, 6, 5, 3, 4, 7, 8],
            [4, 3, 6, 6, 5, 7, 3],
            [6, 4, 5, 6, 2, 7, 3],
            [3, 4, 6, 3, 3, 3, 4]
        ])

        y = np.array ([
            [5, 2],
            [8, 3],
            [10, 4],
            [5, 2],
            [5, 2],
            [8, 3],
            [5, 2]
        ])

        var1_in = float(request.form['var1'])
        var2_in = float(request.form['var2'])
        var3_in = float(request.form['var3'])
        var4_in = float(request.form['var4'])
        var5_in = float(request.form['var5'])
        var6_in = float(request.form['var6'])
        var7_in = float(request.form['var7'])

        beta = persamaan_beta(x,y)

        # Memasukkan data uji (x_uji)
        x_uji = np.array([
           [var1_in,var2_in,var3_in,var4_in,var5_in,var6_in,var7_in]
           ])
        hitung_y_bar = y_bar(x_uji,beta)

        hitung_y_bar_round = hitung_y_bar.copy()

        # Agar angkanya menjadi bulat, maka dibulatkan ke atas
        hitung_y_bar_round = np.ceil(hitung_y_bar_round)

        # yang nilainya < 0, set = 0
        hitung_y_bar_round[hitung_y_bar_round < 0] = 0

        return render_template_string(A_a+template_view+Z_z, var1 = var1_in,
        var2 = var2_in, var3 = var3_in, var4 = var4_in, var5 = var5_in,
        var6 = var6_in, var7 = var7_in, c_save = list(hitung_y_bar), c_save_round = list(hitung_y_bar_round))

    else: # untuk yang 'GET' data awal untuk di send ke /testView_dari_project2_klasifikasi_sbg_fp
        return render_template_string(A_a+template_view+Z_z)

@app.route('/tugas_project_ke_2_regresi', methods=['GET'])
def tugas_project_ke_2_regresi():

    import time
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Study Kasus ke-1: Prediksi Harga Rumah (Regresi)
    # Study Kasus Regresi:
    import numpy as np
    import matplotlib.pyplot as plt

    dataset = np.array([[41,1250],
                       [54,1380],
                       [63,1425],
                       [54,1425],
                      [48,1450],
                      [46,1300],
                      [62,1400],
                      [61,1510],
                      [64,1575],
                      [71,1650]])
    print(dataset)

    # No X Y
    # 1 41 1250
    # 2 54 1380
    # 3 63 1425
    # 4 54 1425
    # 5 48 1450
    # 6 46 1300
    # 7 62 1400
    # 8 61 1510
    # 9 64 1575
    # 10 71 1650

    # Solusi dengan Gradient Descent 2D::
    alpha=0.00001 #learning rate
    [byk_data,dim]=dataset.shape

    # inisialisasi b0 dan b1
    b0=0.0
    b1=0.0

    byk_iter=1000;
    for j in range(1,byk_iter+1):
      sum_error=0.0
      for i in range(0,byk_data):
        x=dataset[i,0]
        y=dataset[i,1]
        y_topi=b0 + b1*x
        error=(y_topi-y)
        sum_error=sum_error+(error**2)
        # update nilai b0 dan b1
        b0=b0-alpha*error
        b1=b1-alpha*error*x

    print()
    print('b0 =',b0)
    print('b1 =',b1)
    print('Y = b0 + b1*X = ', b0,' + ',b1,'*X')

    # # ploting
    # plt.title('Regresi Linier:')
    # plt.xlabel('Ukuran Rumah')
    # plt.ylabel('Harga Rumah (x 50K)')
    #plt.plot(dataset)
    # plt.scatter(dataset[:,0], dataset[:,1])

    # plot garis regresi
    x = np.arange(40,80)
    y = b0 + b1*x
    # plt.plot(x, y, color='red')
    # plt.show()

    y_aktual = dataset[:,1]
    y_predict = b0 + b1*dataset[:,0]
    y_predict = np.round(y_predict, 2)

    # hitung nilai evaluasi, misal dengan MAPE
    nilai_mape = mape_value(y_aktual,y_predict)

    def fn_reg(dataset):
        # Solusi dengan Gradient Descent 2D::
        alpha=0.00001 #learning rate
        [byk_data,dim]=dataset.shape

        # inisialisasi b0 dan b1
        b0=0.0
        b1=0.0

        byk_iter=1000;
        for j in range(1,byk_iter+1):
          sum_error=0.0
          for i in range(0,byk_data):
            x=dataset[i,0]
            y=dataset[i,1]
            y_topi=b0 + b1*x
            error=(y_topi-y)
            sum_error=sum_error+(error**2)
            # update nilai b0 dan b1
            b0=b0-alpha*error
            b1=b1-alpha*error*x

        # plot garis regresi
        x = np.arange(np.min(dataset[:,0])-5,np.max(dataset[:,0])+5)
        y = b0 + b1*x
        # plt.plot(x, y, color='red')
        # plt.show()

        return b0,b1,x,y


    template_view = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
            <h2>
                <p style="text-decoration: underline;">
                  Log Analisis Algoritma Regresi dgn Timer:
                </p>
            </h2>
                  <form method="post">
                    Input Size (N) = {{ dataset|length }}
                    <br>
                    Data: <br>
                    {{ dataset}}
                    <br>
                    Y Aktual = {{ y_aktual}}
                    <br>
                    Y Predik = {{y_predict}}
                    <br><br>
                  </form>
                  <h2>Hasil:  </h2>
                  {% for data_hasil in hasil  %}
                    {{ data_hasil }}
                    <br>
                  {% endfor %}

                  <h2>Plot Waktu by Timer:  </h2>
                  <img src={{url_image}} alt="Chart" height="480" width="640">
                  <br>
                   <h2>Plot Regresi Linier (Nilai MAPE = {{'%0.2f'|format(nilai_mape|float)}}%):  </h2>
                  <img src={{image_regresi}} alt="Chart" height="480" width="640">

            <!--- </body> --->
            <!--- </html> --->
        '''


    input_size = 30
    array_waktu_dalam_detik = np.zeros([input_size,2])

    hasil_temp_b0 = []
    hasil_temp_b1 = []
    for i in range(input_size):
        if i == 0:
             dataset_Temp = np.zeros(shape=((i+1)*10, 2))
             dataset_Temp = dataset.copy()
        else:
            randomData_x = random.sample(range(0, 1000), ((i+1)*10))
            randomData_factor = random.sample(range(0, 11), 1)
            randomData_factor = randomData_factor[0]/10
            randomData_y = 2.*float(randomData_factor)* np.array(randomData_x)
            dataset_Temp = np.zeros(shape=((i+1)*10, 2))
            dataset_Temp[:,0] = np.array(randomData_x)
            dataset_Temp[:,1] = randomData_y

        start_time = time.time()

        hasil_temp_b0,hasil_temp_b1,hasil_temp_x,hasil_temp_y = fn_reg(dataset_Temp)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # hasil_save_b0.append(hasil_temp_b0)
        # hasil_save_b1.append(hasil_temp_b1)

        np.set_printoptions(suppress=True)
        array_waktu_dalam_detik[i][0] = round((i+1),0)
        array_waktu_dalam_detik[i][1] = round(elapsed_time,6)
        #print()

        hasil = []
        for idx, time_val in enumerate(list(array_waktu_dalam_detik[:,1])):
            hasil.append('Input Size (N) = ' + str((idx+1)*10) + ', dgn waktu  ' +str('{0:.10f}'.format(time_val)) + ' (detik)')

    # plot hasil waktunya
    n=list(range(1,input_size+1))

    # Cara ke-1 => untuk plot Regresi
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Plot Data Regresi Linier")
    axis.set_xlabel("Ukuran Rumah")
    axis.set_ylabel("Harga Rumah (x 50K)")
    axis.grid()
    # print('Y = b0 + b1*X = ', b0,' + ',b1,'*X')
    axis.scatter(dataset[:,0], dataset[:,1])
    axis.plot(x, y, 'r.-', label='Y = b0 + b1*X = ' + str(b0) +' + ' + str(b1) +'*X')

    axis.legend(loc="upper left")

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    # Cara ke-2 => untuk plot Regresi by Timer
    # simpan dalam path + nama file /static/img/new_timer.png
    url_simpan = "static/img/new_timer.png"

    fig = plt.figure()
    plt.plot(n,list(array_waktu_dalam_detik[:,1][:len(n)]), 'g.-', label='Regresi by Timer') # TimSort

    plt.xlabel('Banyak Data (N) x 10')
    plt.ylabel('Waktu Komputasi')
    plt.legend(loc="upper left")
    plt.show()

    url_file_image_simpan = os.path.join(BASE_DIR, url_simpan)
    plt.savefig(url_file_image_simpan)

    # return hasil
    return render_template_string(A_a+template_view+Z_z, dataset = dataset, y_aktual = y_aktual, y_predict = y_predict, hasil = hasil, image_regresi = pngImageB64String, url_image = url_simpan, nilai_mape = nilai_mape)

def mape_value(aktual, predict):

    #  5. hitung nilai evaluasi, misal menggunakan MAPE
    # buat def myMAPE yg return-nya detail_mape, final_single_mape = myMAPE(....)
    #
    # Rumus MAPE yang digunakan, jika data aktualnya ada yang nol atau tidak ada yg nol
    # dan untuk memastikan MAPE pada interval = [0%;100%] --> dengan kondisi ini
    # Ref: (Berretti,Thampi,danSrivastava,2015) dalam
    # Hapsari,KD.,Cholissodin,I.,Santoso,E.,2016 --> link: https://bit.ly/2EJRzXE
    #
    konstanta_smooting = 0.00000001
    c = konstanta_smooting

    # aktual = (np_raw_target_by_non_rdd_data_test.copy())
    # predict = (y_topi.copy())

    # aktual = labels.copy()
    # predict = predictions.copy()

    if predict.ndim == 1: # untuk target 1Dim
      byk_target_by_non_rdd = 1
    else: # untuk target 2Dim
      byk_target_by_non_rdd = predict.shape[1]

    mape_init = np.abs((( (aktual+c) - (predict+c) )/ (aktual+c) )*100)
    # mape_norm = np.sum(np.where(mape_init>100, 100, mape_init))/(len(predict)*byk_fitur_by_non_rdd)
    mape_norm = np.sum(np.where(mape_init>100, 100, mape_init))/(len(predict)*byk_target_by_non_rdd)
    #print('MAPE Norm [0% ; 100%] = ', mape_norm.round(2),'%')

    #print()

    # detail mape
    #print('mape_init = ', mape_init.round(2),'%')
    #print(mape_init.shape)

    loss = mape_norm.copy()

    return loss

# from re import M

def listToString(aList):
  return ''.join(str(aList))

import random
import numpy as np

MIN_MERGE = 32

def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, l, m, r):

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)


    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))


            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

    return arr

@app.route('/code_timsort', methods=['GET'])
def code_timsort():
    # a = 12
    # b = 7
    # return str(a+b)

    import time
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    template_view = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
            <h2>
                <p style="text-decoration: underline;">
                  Log Analisis Algoritma Timsort dgn Timer:
                </p>
            </h2>
                  <form method="post">
                   {%for data_get in data_sblm_stlh %}
                    Input Size (N) = {{ loop.index }}
                    <br>
                    Data Sebelum di-Sorting: <br>
                    {{ data_get[0] }}
                    <br>
                    Data Setelah di-Sorting: <br>
                    {{ data_get[1] }}
                    <br><br>
                   {%endfor%}
                  </form>
                  <h2>Hasil:  </h2>
                  {% for data_hasil in hasil  %}
                    {{ data_hasil }}
                    <br>
                  {% endfor %}

                  <h2>Plot Waktu by Timer:  </h2>
                  <img src={{url_image}} alt="Chart" height="480" width="640">
                  <br>
                  <img src={{image_timer}} alt="Chart" height="480" width="640">

            <!--- </body> --->
            <!--- </html> --->
        '''


    input_size = 30
    array_waktu_dalam_detik = np.zeros([input_size,2])
    data_sblm_sort = []
    data_stlh_sort = []
    for i in range(input_size):
        randomData = random.sample(range(0, 1000), (i+1))
        data_sblm_sort.append(listToString(randomData))
        start_time = time.time()
        listData = randomData

        # print(f'Data sebelum sorted : {stringToFloat}')
        timSort(listData) # bisa diganti dengan fibo/ unique element
        # print(f'Data setelah sorted : {listData}')

        y = (len(listData)) - 1

        end_time = time.time()
        elapsed_time = end_time - start_time

        data_stlh_sort.append(listToString(listData))


        # print('Waktu dengan Timer (detik): ', elapsed_time, ' vs Waktu dengan T(n) = ',(i+1), 'Log (',(i+1),'): ', (i+1)*np.log2(i+1))
        np.set_printoptions(suppress=True)
        array_waktu_dalam_detik[i][0] = round((i+1),0)
        array_waktu_dalam_detik[i][1] = round(elapsed_time,6)
        #print()

        hasil = []
        for idx, time_val in enumerate(list(array_waktu_dalam_detik[:,1])):
            hasil.append('Input Size (N) = ' + str(idx+1) + ', dgn waktu  ' +str('{0:.10f}'.format(time_val)) + ' (detik)')

    # plot hasil waktunya
    n=list(range(1,input_size+1))

    # Cara ke-1
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Plot Waktu by Timer Alg. Timsort")
    axis.set_xlabel("Banyak Data (N)")
    axis.set_ylabel("Waktu Komputasi")
    axis.grid()
    axis.plot(n, [x*math.log(x,2) for x in n], 'r.-', label='TimSort by T(n)')
    axis.plot(n,list(array_waktu_dalam_detik[:,1][:len(n)]), 'go-', label='TimSort by Timer')
    # axis.plot(range(5), range(5), "ro-")

    # legend = axis.legend(loc='upper center', shadow=True, fontsize='x-large')

    # # Put a nicer background color on the legend.
    # legend.get_frame().set_facecolor('C0')

    axis.legend(loc="upper left")

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    # Cara ke-2
    # simpan dalam path + nama file /static/img/new_timer.png
    url_simpan = "static/img/new_timer.png"

    fig = plt.figure()
    # plt.plot(n, [math.log(x,2) for x in n], 'g.-', label='logN') # logN
    # plt.plot(n, n, 'b.-', label='N') # N
    plt.plot(n, [x*math.log(x,2) for x in n], 'r.-', label='TimSort by T(n)') # NlogN
    # plt.plot(n, [x*x for x in n], 'r.-') # N^2
    # plt.plot(n, [x*x*x for x in n], 'r.-') # N^3
    # plt.plot(n, [math.pow(2,x) for x in n], 'r.-') # 2^N
    # plt.plot(n, [math.factorial(x) for x in n], 'r.-') # N!
    plt.plot(n,list(array_waktu_dalam_detik[:,1][:len(n)]), 'g.-', label='TimSort by Timer') # TimSort

    plt.xlabel('Banyak Data (N)')
    plt.ylabel('Waktu Komputasi')
    plt.legend(loc="upper left")
    plt.show()

    url_file_image_simpan = os.path.join(BASE_DIR, url_simpan)
    plt.savefig(url_file_image_simpan)

    # Cara ke-3
    # /bokeh


    # return hasil
    return render_template_string(A_a+template_view+Z_z, data_sblm_stlh = zip(data_sblm_sort, data_stlh_sort), hasil = hasil, image_timer = pngImageB64String, url_image = url_simpan)

@app.route('/unik_el', methods=['GET'])
def unik_el():

    # /**
    #  *
    #  * @author Imam Cholissodin
    #  *
    #  * Contoh Membuat Koding Algoritma uniqueElement
    #  */

    def uniqueElement(A):
      n = len(A)
      for i in range(0,n-1,1):
        for j in range(i+1,n,1):
          if(A[i]==A[j]):
            return 'False'
      return 'True'

    # if __name__ == '__main__':
    # A = [9,87,52,3,33,58,74,57,89,57,48,61,33,83,28]
    A = [6,9,12,58,39,10,53,82,90]

    # print("Cek keunikan = ", uniqueElement(A))

    return uniqueElement(A)

    # return 'Silahkan koding Alg. Unik Elemen disini'

@app.route('/unik_el_dgn_timer', methods=['GET'])
def unik_el_dgn_timer():

    import time
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def uniqueElement(A):
      n = len(A)
      for i in range(0,n-1,1):
        for j in range(i+1,n,1):
          if(A[i]==A[j]):
            return 'False'
      return 'True'

    template_view = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
            <h2>
                <p style="text-decoration: underline;">
                  Log Analisis Algoritma Unik Elemen dgn Timer:
                </p>
            </h2>
                  <form method="post">
                   {%for data_get in data_sblm_stlh %}
                    Input Size (N) = {{ loop.index }}
                    <br>
                    Data Sebelum dicek Uniknya: <br>
                    {{ data_get[0] }}
                    <br>
                    Hasil cek Uniknya: <br>
                    {{ data_get[1] }}
                    <br><br>
                   {%endfor%}
                  </form>
                  <h2>Hasil:  </h2>
                  {% for data_hasil in hasil  %}
                    {{ data_hasil }}
                    <br>
                  {% endfor %}

                  <h2>Plot Waktu by Timer:  </h2>
                  <img src={{url_image}} alt="Chart" height="480" width="640">
                  <br>
                  <img src={{image_timer}} alt="Chart" height="480" width="640">

            <!--- </body> --->
            <!--- </html> --->
        '''


    input_size = 30
    array_waktu_dalam_detik = np.zeros([input_size,2])
    data_sblm_cek_unik = []
    # data_stlh_sort = []
    hasil_cek_unik = []
    for i in range(input_size):
        randomData = random.sample(range(0, 1000), (i+1))
        data_sblm_cek_unik.append(listToString(randomData))
        start_time = time.time()
        listData = randomData

        # print(f'Data sebelum sorted : {stringToFloat}')
        hasil_temp = uniqueElement(listData) # bisa diganti dengan fibo/ unique element
        # print(f'Data setelah sorted : {listData}')

        # y = (len(listData)) - 1

        end_time = time.time()
        elapsed_time = end_time - start_time

        # hasil_cek_unik.append(listToString(hasil_temp))
        hasil_cek_unik.append(hasil_temp)


        # print('Waktu dengan Timer (detik): ', elapsed_time, ' vs Waktu dengan T(n) = ',(i+1), 'Log (',(i+1),'): ', (i+1)*np.log2(i+1))
        np.set_printoptions(suppress=True)
        array_waktu_dalam_detik[i][0] = round((i+1),0)
        array_waktu_dalam_detik[i][1] = round(elapsed_time,6)
        #print()

        hasil = []
        for idx, time_val in enumerate(list(array_waktu_dalam_detik[:,1])):
            hasil.append('Input Size (N) = ' + str(idx+1) + ', dgn waktu  ' +str('{0:.10f}'.format(time_val)) + ' (detik)')

    # plot hasil waktunya
    n=list(range(1,input_size+1))

    # Cara ke-1
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Plot Waktu by Timer Alg. Timsort")
    axis.set_xlabel("Banyak Data (N)")
    axis.set_ylabel("Waktu Komputasi")
    axis.grid()
    axis.plot(n, [x*math.log(x,2) for x in n], 'r.-', label='TimSort by T(n)')
    axis.plot(n,list(array_waktu_dalam_detik[:,1][:len(n)]), 'go-', label='TimSort by Timer')
    # axis.plot(range(5), range(5), "ro-")

    # legend = axis.legend(loc='upper center', shadow=True, fontsize='x-large')

    # # Put a nicer background color on the legend.
    # legend.get_frame().set_facecolor('C0')

    axis.legend(loc="upper left")

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    # Cara ke-2
    # simpan dalam path + nama file /static/img/new_timer.png
    url_simpan = "static/img/new_timer.png"

    fig = plt.figure()
    # plt.plot(n, [math.log(x,2) for x in n], 'g.-', label='logN') # logN
    # plt.plot(n, n, 'b.-', label='N') # N
    plt.plot(n, [(x**2 - x)/2 for x in n], 'r.-', label='Unique Element by T(n)') # (N^2 - N)/2
    # plt.plot(n, [x*x for x in n], 'r.-') # N^2
    # plt.plot(n, [x*x*x for x in n], 'r.-') # N^3
    # plt.plot(n, [math.pow(2,x) for x in n], 'r.-') # 2^N
    # plt.plot(n, [math.factorial(x) for x in n], 'r.-') # N!
    plt.plot(n,list(array_waktu_dalam_detik[:,1][:len(n)]), 'g.-', label='Unique Element by Timer') # TimSort

    plt.xlabel('Banyak Data (N)')
    plt.ylabel('Waktu Komputasi')
    plt.legend(loc="upper left")
    plt.show()

    url_file_image_simpan = os.path.join(BASE_DIR, url_simpan)
    plt.savefig(url_file_image_simpan)

    # Cara ke-3
    # /bokeh


    # return hasil
    return render_template_string(A_a+template_view+Z_z, data_sblm_stlh = zip(data_sblm_cek_unik, hasil_cek_unik), hasil = hasil, image_timer = pngImageB64String, url_image = url_simpan)


@app.route('/bokeh')
def bokeh():
    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure(plot_width=300, plot_height=300)
    fig.vbar(
        x=[1, 2, 3, 4],
        width=0.5,
        bottom=0,
        top=[1.7, 2.2, 4.6, 3.9],
        color='navy'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    template_view ='''
    <!-- <!doctype html> -->
    <!-- <html lang="en"> -->
    <!--  <head> -->
        <meta charset="utf-8">
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <title>Embed Demo</title>
        {{ js_resources|indent(4)|safe }}
        {{ css_resources|indent(4)|safe }}
        {{ plot_script|indent(4)|safe }}
    <!--  </head> -->
    <!--  <body> -->
        {{ plot_div|indent(4)|safe }}
    <!--  </body> -->
    <!-- </html> -->
    '''

    # render template
    script, div = components(fig)
    html = render_template_string(
        A_a+template_view+Z_z,
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )

    return html

@app.route('/db/<aksi>')
def manipulate_tabel(aksi):
    conn = connect_db()
    db = conn.cursor()

    # Aksi => Buat, Hapus

    if aksi == 'c':
        str_info = 'tabel berhasil dibuat :D'
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS data_cronjob
        (tipe_run TEXT, date_pembuatan DATETIME,
        teks_call_sintaks TEXT,
        keterangan TEXT,
        date_masa_berlaku DATETIME)
        """)
    elif aksi== 'd':
        str_info = 'tabel berhasil dihapus :D'
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS data_cronjob
        """)

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air/<aksi>')
def manipulate_tabel_CloundAI_Air(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air_Rev/<aksi>')
def manipulate_tabel_CloundAI_Air_Rev(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air_Rev (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air_Rev
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/user')
def data_user():
    try:
        conn = connect_db()
        db = conn.cursor()

        rs = db.execute("SELECT * FROM user order by id")
        userslist = rs.fetchall()
        return render_template('data_user.html',userslist=userslist)

    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

@app.route("/update_user",methods=["POST","GET"])
def update_user():
    try:
        conn = connect_db()
        db = conn.cursor()
        if request.method == 'POST':
            field = request.form['field']
            value = request.form['value']
            editid = request.form['id']

            if field == 'mail':
                db.execute("""UPDATE user SET Mail=? WHERE id=?""",(value,editid))
            if field == 'name':
                db.execute("""UPDATE user SET Name=? WHERE id=?""",(value,editid))
            if field == 'pwd':
                db.execute("""UPDATE user SET Password=? WHERE id=?""",(value,editid))
            if field == 'level':
                db.execute("""UPDATE user SET Level=? WHERE id=?""",(value,editid))

            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

# ================ awal - dasar ke-2 ===============
#

# buat input dari url, untuk penjumlahan misal 2 bilangan
@app.route('/add/<a>/<b>')
def add_ab(a,b):
    c = int(a) + float(b)
    return 'a + b = ' + str(c)
    # return 'a + b = %s' % c
# https://userAnda.pythonanywhere.com/add/1/2.5
# hasil => a + b = 3.5

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return kode html dalam flask python Web App
@app.route('/post_add2', methods=["POST", "GET"])
def inputkan_ab():
    # membuat penjumlahan 2 bilangan

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return '''
        <html>
            <head>
            </head>
            <body>
              <form method="post">
                <input type="text" name="a" value="%s" />
                <input type="text" name="b" value="%s" />
                <input type="submit" value="Hitung a + b"/>

              </form>
              <h2>Hasil a + b = %s + %s = %s </h2>
            </body>
        </html>
        ''' % (a_in, b_in, a_in, b_in, c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add2
        return '''
            <html>
                <head>
                </head>
                <body>
                  <form action="/post_add2" method="post">
                    Masukkan nilai a = <input type="text" name="a" value="" />
                    <br>
                    Masukkan nilai b = <input type="text" name="b" value="" />
                    <input type="submit" value="Hitung a + b"/>
                  </form>
                </body>
            </html>
        '''

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return file "form_add3.html" dalam folder "mysite/templates", flask python Web App
@app.route('/post_add3', methods=["POST", "GET"])
def inputkan_ab3():
    # membuat penjumlahan 2 bilangan
    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return render_template('form_add3.html', a_save = a_in, b_save = b_in, c_save = c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add3
        return render_template('form_add3.html')


# ================================================================================
# Contoh koding dasar operasi CRUD pada tabel CloudAI_Air,
# mulai dari "def dasar2_create_database():" sampai sebelum "# ================ akhir - dasar ke-2 ==============="
#
# membuat render_template_string sebagai pengganti render_template
# agar semua kodenya hanya dalam 1 file, sehingga lebih mudah untuk membuat dan run kodingnya
#
def dasar2_create_database():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
                """)

    conn.commit()
    conn.close()

def dasar2_generate_data():
    """Generate sintesis atau dummy data untuk percontohan."""
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM CloudAI_Air')
    entry = cur.fetchone()

    if entry is None:
        import numpy as np
        import pandas as pd
        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))


        # Misal skema dataset-nya seperti berikut: => Silahkan dimodifikasi sesuai case Anda
        kolomFitur_X_plus_Target_Y = ['Suhu (X1)','Kelembaban (X2)', 'Curah Hujan (X3)','Angin (X4)','Durasi Air Dlm Menit (Y)']

        # set bykData = 3*np.power(10,7)
        bykData = 10
        bykFitur = len(kolomFitur_X_plus_Target_Y)-1

        # Interval atau Variasi nilai fitur
        nilaiFitur_Suhu = [17,35]
        nilaiFitur_Kelembaban = [70,90]
        nilaiFitur_Curah_Hujan = [2,95]
        nilaiFitur_Angin = [0,15]
        labelTargetY = [0.0,90.0]

        # generate isi dataset
        content_dataGenerate = np.array([np.arange(bykData)]*(bykFitur+1)).T
        df_gen = pd.DataFrame(content_dataGenerate, columns=kolomFitur_X_plus_Target_Y)

        df_gen ['Suhu (X1)'] = np.random.randint(nilaiFitur_Suhu[0], nilaiFitur_Suhu[1], df_gen.shape[0])
        df_gen ['Kelembaban (X2)'] = np.random.randint(nilaiFitur_Kelembaban[0], nilaiFitur_Kelembaban[1], df_gen.shape[0])
        df_gen ['Curah Hujan (X3)'] = np.random.randint(nilaiFitur_Curah_Hujan[0], nilaiFitur_Curah_Hujan[1], df_gen.shape[0])
        df_gen ['Angin (X4)'] = np.random.randint(nilaiFitur_Angin[0], nilaiFitur_Angin[1], df_gen.shape[0])
        df_gen ['Durasi Air Dlm Menit (Y)'] = np.round(np.random.uniform(labelTargetY[0], labelTargetY[1], df_gen.shape[0]),2)

        # save dataframe generate ke *.csv
        import os
        userhome = os.path.expanduser("~").split("/")[-1]

        path = "/home/"+userhome+"/mysite/static/data_contoh"
        if not os.path.exists(path):
            os.makedirs(path)
        # file_name_data_generate = 'static/data_contoh/Data_CloudAI_Air.csv'
        # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)
        url_file_name_data_generate = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")
        df_gen.to_csv(url_file_name_data_generate, encoding='utf-8', index=False)

        # read file *.csv dan tampilkan
        # data_generate = pd.read_csv(file_name_data_generate)

        url = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")

        # Importing the dataset => ganti sesuai dengan case yg anda usulkan
        dataset = pd.read_csv(url)
        # X = dataset.iloc[:, :-1].values
        # y = dataset.iloc[:, 1].values

        def pushCSVdatasetToDB(x1,x2,x3,x4,y):
            #inserting values inside the created table

            cmd = "INSERT INTO CloudAI_Air(suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES('{}','{}','{}','{}','{}')".format(x1,x2,x3,x4,y)
            cur.execute(cmd)
            conn.commit()

        # CSV_to_SQLite3 dari file dataset
        for i in range(0,len(dataset)):
            pushCSVdatasetToDB(dataset.iloc[i][0],dataset.iloc[i][1],dataset.iloc[i][2],dataset.iloc[i][3],dataset.iloc[i][4])
    else:
        ket_hasil = 'Tidak dilakukan Insert, karena Tabel tidak kosong'
        print(ket_hasil)

    conn.commit()
    cur.close()
    conn.close()

@app.route('/dasar2_crud')
def dasar2_index():
    return '<a href="/dasar2_list">Demo Menampilkan List dari Tabel + Support => Create, Read, Update, Delete (CRUD)</a>'

@app.route('/dasar2_list')
def dasar2_list():

    # buat tabel dan generate data dummy
    dasar2_create_database()
    dasar2_generate_data()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM CloudAI_Air")
    rows = cur.fetchall()

    conn.close()

    #return render_template("list.html", rows=rows)
    return render_template_string(template_list, rows=rows)


@app.route('/dasar2_edit/<int:number>', methods=['GET', 'POST'])
def dasar2_edit(number):
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        # suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit

        cur.execute("UPDATE CloudAI_Air SET suhu_dlm_celcius = ?, humidity_kelembaban_dlm_persen = ?, precipitation_curah_hujan_dlm_persen = ?, wind_angin_dlm_km_per_jam = ?, durasi_air_dlm_menit = ? WHERE id = ?",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi, item_id))
        conn.commit()

        return redirect('/dasar2_list')

    cur.execute("SELECT * FROM CloudAI_Air WHERE id = ?", (number,))
    item = cur.fetchone()

    conn.close()

    #return render_template("edit.html", item=item)
    return render_template_string(template_edit, item=item)

@app.route('/dasar2_delete/<int:number>')
def dasar2_delete(number):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM CloudAI_Air WHERE id = ?", (number,))

    conn.commit()
    conn.close()

    return redirect('/dasar2_list')

@app.route('/dasar2_add', methods=['GET', 'POST'])
def dasar2_add():
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        # item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES (?, ?, ?, ?, ?)""",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi))
        conn.commit()

        return redirect('/dasar2_list')

    #return render_template("add.html", item=item)
    return render_template_string(template_add)

@app.route('/dasar2_add2')
def dasar2_add2():
    conn = connect_db()
    cur = conn.cursor()

    # get data dari iot API
    import requests
    # from datetime import datetime
    # import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    # list_kota = ['Jakarta','Los Angeles','Chicago','New York City','Toronto','São Paulo', \
    #              'Lagos', 'London', 'Johannesburg', 'Kairo', 'Paris', 'Zurich', 'Istanbul', 'Moskwa', 'Dubai', \
    #             'Mumbai','Hong Kong','Shanghai','Singapura','Tokyo','Sydney']
    list_kota = ['Malang']


    for nama_kota in list_kota:
        #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
        each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
        resp=requests.get(each_list_link)

        # print(nama_kota)

        #http_respone 200 means OK status
        if resp.status_code==200:
            resp=resp.json()
            suhu = resp['current']['temp_c']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']
        else:
            # print("Error")
            suhu = '-'
            curah_hujan = '-'
            lembab = '-'
            angin = '-'

        # print(nama_kota, 'dengan suhu = ', round(float(suhu),2),'°C', end='\n')

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?, ?, ?, ?)""",
                (suhu, lembab, curah_hujan, angin))

        conn.commit()
        cur.close()
        conn.close()

    return redirect('/dasar2_list')

template_list = """
<h2>Menampilkan Data CloudAI Air + Support Create, Read, Update, delete (CRUD)</h2>
<a href="{{ url_for( "dasar2_add" ) }}">Tambah Data</a> |
<a href="{{ url_for( "dasar2_add2" ) }}">Tambah Data dari iot_api (tanpa nilai Durasi Waktu)</a>
{% if rows %}
<table border="1">
    <thead>
        <td>No</td>
        <td>Suhu (°C)</td>
        <td>Kelembaban (%)</td>
        <td>Curah Hujan (%)</td>
        <td>Kecepatan Angin (Km/Jam)</td>
        <td>Durasi Waktu Pengairan / Penyiraman (Menit)</td>
    </thead>

    {% for row in rows %}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>
        <td>{{row[5]}}</td>
        <td>
            <a href="{{ url_for( "dasar2_edit", number=row[0] ) }}">Edit</a> |
            <a href="{{ url_for( "dasar2_delete", number=row[0] ) }}">Hapus</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% else %}
Empty</br>
{% endif %}
"""

template_add = """
<h1>Tambah Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_add" ) }}">
    Suhu: <input name="suhu" value=""/></br>
    Kelembaban: <input name="kelembaban" value=""/></br>
    Curah Hujan: <input name="hujan" value=""/></br>
    Kecepatan Angin: <input name="angin" value=""/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value=""/></br>
    <button>Simpan Data</button></br>
</form>
"""

template_edit = """
<h1>Edit Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_edit", number=item[0] ) }}">
    Suhu: <input name="suhu" value="{{item[1]}}"/></br>
    Kelembaban: <input name="kelembaban" value="{{item[2]}}"/></br>
    Curah Hujan: <input name="hujan" value="{{item[3]}}"/></br>
    Kecepatan Angin: <input name="angin" value="{{item[4]}}"/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value="{{item[5]}}"/></br>
    <button>Simpan Update Data</button></br>
</form>
"""

# ================ akhir - dasar ke-2 ===============

# ================ awal - dasar ke-1 ===============
# #

# @app.route('/add')
# def add():
#     # membuat penjumlahan 2 bilangan
#     a = 10
#     b = 90
#     c = a + b

#     return str(c)

# # buatlah halaman perkalian
# # antara a*b
# @app.route('/kali')
# def kali():
#     # membuat perkalian 2 bilangan
#     a = 10
#     b = 90
#     c = a * b

#     return str(c)

# # buatlah tampilan indeks looping 1..10
# @app.route('/loop')
# def loop():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '  '

#     return str(c)

# # buatlah tampilan indeks looping 1..10 dengan new line (<br> dari tag html)
# @app.route('/loop_new_line')
# def loop_new_line():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '<br>'

#     return str(c)

# # buatlah tampilan indeks looping 1 sampai 10
# # yang ganjil
# @app.route('/ganjil')
# def ganjil():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         if((i+1)%2!=0):
#             c +=str(i+1) + '  '

#     return str(c)
# # ================ akhir - dasar ke-1 ===============

# ========= untuk Tugas Ke-1 & 2 | Project =================

@app.route("/")
def index():
    # return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
  conn = connect_db()
  db = conn.cursor()
  msg = ""
  if request.method == "POST":
      mail = request.form["mail"]
      passw = request.form["passw"]

      rs = db.execute("SELECT * FROM user WHERE Mail=\'"+ mail +"\'"+" AND Password=\'"+ passw+"\'" + " LIMIT 1")

      conn.commit()

      hasil = []
      for v_login in rs:
          hasil.append(v_login)

      if hasil:
          session['name'] = v_login[3]
          return redirect(url_for("launchpad_menu"))
      else:
          msg = "Masukkan Username (Email) dan Password dgn Benar!"

  return render_template("login.html", msg = msg)

@app.route("/register", methods=["GET", "POST"])
def register():
  conn = connect_db()
  # db = conn.cursor()
  if request.method == "POST":
      mail = request.form['mail']
      uname = request.form['uname']
      passw = request.form['passw']

      cmd = "insert into user(Mail, Password,Name,Level) values('{}','{}','{}','{}')".format(mail,passw,uname,'1')
      conn.execute(cmd)
      conn.commit()

      # conn = db

      return redirect(url_for("login"))
  return render_template("register.html")

def connect_db():
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data.db")

    return sqlite3.connect(db_path)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def internal_server_error(error):
    userhome = os.path.expanduser("~").split("/")[-1]
    link_error_debug = "https://www.pythonanywhere.com/user/"+userhome+"/files/var/log/"+userhome+".pythonanywhere.com.error.log"

    return render_template("500.html", link_error_debug = link_error_debug)

@app.route('/iot', methods=["GET", "POST"])
def iot():

    if 'name' in session:
        name = session['name']
    else:
        name = 'Guest'

    # start kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv
    if request.method == "POST":

        from io import StringIO
        import csv

        # date_var = request.args.get('date_var')
        # kota_var = request.args.get('kota_var')
        conn = connect_db()
        db = conn.cursor()

        output = StringIO()
        writer = csv.writer(output)
        c = db.execute("SELECT * FROM data_suhu_dll")

        result = c.fetchall()
        writer.writerow([i[0] for i in c.description])

        for row in result:
            line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
            writer.writerow(line)

        output.seek(0)

        conn.commit()
        db.close()
        conn.close()

        return Response(output, mimetype="text/csv",
                        headers={"Content-Disposition": "attachment;filename=data_suhu_iot_all.csv"})
    # ending kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv


    # menampilkan data dari tabel data_suhu_dll
    conn = connect_db()
    db = conn.cursor()

    c = db.execute(""" SELECT * FROM  data_suhu_dll """)

    mydata = c.fetchall()
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    hasil = []
    for v_login in c:
        hasil.append(v_login)

    conn.commit()
    db.close()
    conn.close()


    return render_template("getsuhu_dll.html", header = mydata)

@app.route('/del_iot/', methods=["GET"])
def del_iot():
    date_var = request.args.get('date_var')
    kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    db.execute("DELETE FROM data_suhu_dll WHERE date =\'"+ date_var +"\' AND  kota =\'"+ kota_var +"\'")

    conn.commit()
    db.close()
    conn.close()

    return redirect(url_for("iot"))

@app.route('/dw_iot/', methods=["GET"])
def dw_iot():

    from io import StringIO
    import csv

    date_var = request.args.get('date_var')
    # kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    output = StringIO()
    writer = csv.writer(output)
    c = db.execute("SELECT * FROM data_suhu_dll WHERE date =\'"+ date_var +"\'")

    result = c.fetchall()
    writer.writerow([i[0] for i in c.description])

    for row in result:
        line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
        writer.writerow(line)

    output.seek(0)

    conn.commit()
    db.close()
    conn.close()

    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=data_suhu_iot.csv"})

@app.route('/logout')
def logout():
   # remove the name from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))


# ================
# Ergo Project

@app.route("/in")
def index_qrcode():
    return render_template("qrcode.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")

@app.route('/qr_index')
def qr_index():
    attendance = Attendance.getAll()
    return render_template("qr_scan2.html", data=enumerate(attendance, 1))


@app.route("/qr_scan", methods=["GET"])
def qr_scan():
    return Response(scanner(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/qr_student", methods=["GET", "POST"])
def qr_student():
    if request.method == "POST":
        name = request.form['name']
        nim = request.form['nim']
        UUID = str(uuid.uuid4())
        qr_code_mark = "static/img/tmp_qr/{}.png".format(UUID)
        student = Student(nim=nim, name=name, qr_code=qr_code_mark)
        student.save()

        import qrcode

        # # /qrcode
        # qrcode_img = qrcode.make(student.id)
        # # buf = io.BytesIO()
        # buf_qrcode = BytesIO()
        # qrcode_img.save(buf_qrcode)
        # buf_qrcode.seek(0)
        # # return send_file(buf_qrcode, mimetype='image/jpeg')

        qrcode_img = qrcode.make(student.id)
        # qrcode_img = qrcode(student.id)
        # canvas = Image.new('RGB', (290,290), 'white')
        # draw = ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # fname = f'qr_code_{self.name}.png'
        fname = f'static/img/tmp_qr/qr_code_{student.id}.png'.format(UUID)
        buffer = BytesIO()
        # canvas.save(buffer,'PNG')
        # qrcode_img.save(fname, File(buffer), save=False)
        # qrcode_img.save(fname, buffer, save=False)
        # qrcode_img.save(buffer)

        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        url_file_name_qrcode = os.path.join(BASE_DIR, fname)

        qrcode_img.save(url_file_name_qrcode, format="PNG")
        # canvas.close()
        # super().save(*args, **kwargs)

        # img = pyqrcode.create(student.id, error="L", mode="binary", version=5)
        # img.png(qr_code, scale=10)
    students = Student.getAll()
    return render_template("qr_student.html", data=enumerate(students, 1))


def scanner():
    camera = Scanner()
    while True:
        frame = camera.get_video_frame()

        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            break

@app.route('/myadmin/', methods = ['GET','POST'])
@app.route('/myadmin/<none_atau_lainnya>', methods = ['GET','POST'])
def myadmin(none_atau_lainnya=None):

    template_view = '''
                <div class="row">
                    <div class="col-12">
                        <div class="white-box">
                                <div class="card-body">
                                    <form action="/myadmin" method="post">
                                    <h4 class="card-title">Masukkan tabel yang akan dibuat</h4>
                                    <h6 class="card-subtitle"></h6>
                                    <button type="button" class="btn btn-info btn-rounded m-t-10 float-right" data-toggle="modal" data-target="#add-contact">Buat Tabel</button>

                                    <!-- Add Contact Popup Model -->
                                    <!--<div id="add-contact" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;"> -->
                                    <div id="add-contact" class="modal fade in" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                                                    <h4 class="modal-title" id="myModalLabel">Buat Tabel baru</h4> </div>
                                                <div class="modal-body">
                                                    <from class="form-horizontal form-material">
                                                        <div class="form-group">
                                                            <div class="col-md-12 m-b-20">
                                                                <input type="text" name="nama_tabel" class="form-control" placeholder="Nama tabel" required="required"> </div>
                                                            <div class="col-md-12 m-b-20">
                                                                <textarea class="form-control" name="teks_sintaks" rows="4" placeholder="Teks sintaks"></textarea> </div>
                                                        </div>
                                                    </from>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="submit" class="btn btn-info waves-effect">Simpan</button>
                                                    <button type="button" class="btn btn-default waves-effect" data-dismiss="modal">Batal</button>
                                                    <!-- <button type="reset" class="btn btn-default waves-effect" data-dismiss="modal">Batal</button> -->
                                                </div>
                                            </div>
                                            <!-- /.modal-content -->
                                        </div>
                                        <!-- /.modal-dialog -->
                                    </div>

                                    </form>

                                    <div class="table-responsive">
                                        <!-- <table id="footable-addrow" class="table table-bordered m-t-30 table-hover contact-list footable footable-5 footable-paging footable-paging-center breakpoint-lg" data-paging="true" data-paging-size="7" style=""> -->
                                        <!-- <table id="footable-addrow" class="table footable footable-6 footable-editing footable-editing-right footable-editing-no-view footable-filtering footable-filtering-right footable-paging footable-paging-center breakpoint-lg" data-paging="true" data-filtering="true" data-sorting="true" data-editing="true" data-state="true" style=""> -->
                                        <!-- <table id="example23" class="display nowrap table table-hover table-striped table-bordered" cellspacing="0" width="100%"> -->
                                        <!-- <table id="footable-addrow" class="table" data-paging="true" data-filtering="true" data-sorting="true" data-editing="true" data-state="true">-->

                                        <!-- <table id="example23" class="display nowrap table table-hover table-striped table-bordered" data-paging="true" data-filtering="true" data-sorting="true" data-editing="true" data-state="true">-->
                                        <table id="example23" class="display nowrap table table-hover table-striped table-bordered" cellspacing="0" width="100%">
                                        <!-- <table id="myTable" class="table table-striped"> -->
                                            <thead>
                                                <tr class="footable-header">
                                                    <th style="display: table-cell;" class="footable-first-visible">No</th>
                                                    <th style="display: table-cell;">Nama</th>
                                                    <th style="display: table-cell;">Tanggal Pembuatan</th>
                                                    <th style="display: table-cell;" class="th-inner">Teks Sintaks</th>
                                                    <th style="display: table-cell;" class="footable-last-visible"></th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {% for item in var_tabel_myadmin %}
                                                <tr class={{ loop.cycle('odd', 'even') }}>
                                                    <td style="display: table-cell;" class="footable-first-visible">{{ loop.index }}</td>
                                                    <td style="display: table-cell;">{{item[1]}}</td>
                                                    <td style="display: table-cell;">{{item[2]}}</td>
                                                    <td style="display: table-cell;">
                                                        {{item[3]}} </td>
                                                    <td style="display: table-cell;" class="footable-last-visible">

                                                        <a href="" data-toggle="modal" data-target="#editor-modal{{item[1]}}">
                                                        <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-pencil-alt"></i></button></a>

                                                        <!-- <a href="/myadmin/edit-nama_tabel_var-{{item[1]}}"> -->
                                                        <!-- <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-pencil-alt"></i></button></a> -->

                                                        <!-- <a href="/myadmin/del-nama_tabel_var-{{item[1]}}"> -->
                                                        <!-- <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-trash"></i></button></a> -->

                                                        <a href="" data-toggle="modal" data-target="#hapus-modal{{item[1]}}">
                                                        <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-trash"></i></button></a>


                                                        <a href="/myadmin/run-nama_tabel_var-{{item[1]}}">
                                                        <button type="button" class="btn btn-info btn-outline btn-circle btn-lg m-r-5"><i class="ti-control-play"></i></button></a>

                                                        <!-- Start Popup Model utk Edit -->
                                                        <!-- <div class="modal fade" id="editor-modal" tabindex="-1" role="dialog" aria-labelledby="editor-title"> -->
                                                        <!-- <div id="editor-modal{{item[1]}}" class="modal fade in" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> -->
                                                        <div class="modal fade in" id="editor-modal{{item[1]}}" tabindex="-1" role="dialog" aria-labelledby="editor-title">
                                                            <!--<div class="modal-dialog" role="document"> -->
                                                            <div class="modal-dialog">
                                                                <form action="/myadmin/edit-nama_tabel_var-{{item[1]}}" class="modal-content form-horizontal" id="editor" method="post">
                                                                    <div class="modal-content">
                                                                        <div class="modal-header">
                                                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                                                                            <h4 class="modal-title" id="editor-title">Ubah Data ke-{{item[0]}}</h4>
                                                                        </div>
                                                                        <div class="modal-body">
                                                                            <from class="form-horizontal form-material">
                                                                                <div class="form-group">
                                                                                    <label for="firstName" class="col-sm-3 control-label">Nama</label>
                                                                                    <div class="col-sm-9">
                                                                                        <input type="text" class="form-control" name="nama_tabel_edit_{{item[1]}}" value="{{item[1]}}" placeholder="Nama Tabel" readonly>
                                                                                    </div>
                                                                                </div>
                                                                                <!-- <div class="form-group"> -->
                                                                                    <!-- <label for="dob" class="col-sm-3 control-label">Tanggal Pembuatan</label> -->
                                                                                    <!-- <label class="col-sm-3 control-label">Tanggal Pembuatan</label> -->
                                                                                    <!-- <div class="col-sm-9"> -->
                                                                                        <!-- <input type="date" class="form-control" name="tgl_buat_tabel_edit" value="{{item[2]}}" placeholder="Tanggal Pembuatan Tabel"> -->
                                                                                        <!-- <input type="date" data-date="" data-date-format="dd-mm-YYYY HH:MM:SS" class="form-control" name="tgl_buat_tabel_edit" value="{{item[2]}}" placeholder="Tanggal Pembuatan Tabel"> -->

                                                                                    <!-- </div> -->
                                                                                <!-- </div> -->
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Sintaks</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_edit_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                            </from>
                                                                        </div>
                                                                        <div class="modal-footer">
                                                                            <!-- <button type="submit" class="btn btn-primary">Save changes</button> -->
                                                                            <!-- <a href="/myadmin/edit-nama_tabel_var-{{item[1]}}" class="btn btn-info" role="button">Simpan</a>-->
                                                                            <!-- <button type="submit" class="btn btn-primary">Simpan</button>-->
                                                                            <button type="submit" class="btn btn-info waves-effect">Simpan</button>
                                                                            <button type="button" class="btn btn-default" data-dismiss="modal">Batal</button>
                                                                        </div>
                                                                    </div>
                                                                    <!-- /.modal-content -->
                                                                </form>
                                                            </div>
                                                            <!-- /.modal-dialog -->
                                                        </div>
                                                        <!-- End Popup Model utk Edit -->

                                                        <!-- Start Popup Model utk Hapus -->
                                                        <div class="modal fade in" id="hapus-modal{{item[1]}}" tabindex="-1" role="dialog" aria-labelledby="editor-title">
                                                            <div class="modal-dialog">
                                                                <form action="/myadmin/del-nama_tabel_var-{{item[1]}}" class="modal-content form-horizontal" id="editor" method="post">
                                                                    <div class="modal-content">
                                                                        <div class="modal-header">
                                                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                                                                            <h4 class="modal-title" id="editor-title">Hapus Data ke-{{item[0]}}</h4>
                                                                        </div>
                                                                        <div class="modal-body">
                                                                            <from class="form-horizontal form-material">
                                                                                <div class="form-group">
                                                                                    <label for="firstName" class="col-sm-3 control-label">Nama</label>
                                                                                    <div class="col-sm-9">
                                                                                        <input type="text" class="form-control" name="nama_tabel_hapus_{{item[1]}}" value="{{item[1]}}" placeholder="Nama Tabel" readonly>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Sintaks</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_hapus_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                            </from>
                                                                        </div>
                                                                        <div class="modal-footer">
                                                                            <button type="submit" class="btn btn-info waves-effect">Hapus</button>
                                                                            <button type="button" class="btn btn-default" data-dismiss="modal">Batal</button>
                                                                        </div>
                                                                    </div>
                                                                    <!-- /.modal-content -->
                                                                </form>
                                                            </div>
                                                            <!-- /.modal-dialog -->
                                                        </div>
                                                        <!-- End Popup Model utk Hapus -->

                                                        <!-- Start Popup Model utk Generate Kode untuk flask_app.py -->
                                                        <div class="modal fade in" id="gen-modal{{item[1]}}" tabindex="-1" role="dialog" aria-labelledby="editor-title">
                                                            <div class="modal-dialog">
                                                                <form action="/myadmin/gen-nama_tabel_var-{{item[1]}}" class="modal-content form-horizontal" id="editor" method="post">
                                                                    <div class="modal-content">
                                                                        <div class="modal-header">
                                                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                                                                            <h4 class="modal-title" id="editor-title">Hapus Data ke-{{item[0]}}</h4>
                                                                        </div>
                                                                        <div class="modal-body">
                                                                            <from class="form-horizontal form-material">
                                                                                <div class="form-group">
                                                                                    <label for="firstName" class="col-sm-3 control-label">Nama</label>
                                                                                    <div class="col-sm-9">
                                                                                        <input type="text" class="form-control" name="nama_tabel_gen_{{item[1]}}" value="{{item[1]}}" placeholder="Nama Tabel" readonly>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Sintaks</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_tabel_gen_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="form-group">
                                                                                    <label for="status" class="col-sm-3 control-label">Generate Kode untuk flask_app.py</label>
                                                                                    <div class="col-sm-9">
                                                                                        <!--input type="text" class="form-control" id="status" name="status" placeholder="Status Here" required> -->
                                                                                        <textarea class="form-control" name="teks_sintaks_page_gen_{{item[1]}}" rows="4" placeholder="Teks sintaks">{{item[3]}}</textarea>
                                                                                    </div>
                                                                                </div>
                                                                            </from>
                                                                        </div>
                                                                        <div class="modal-footer">
                                                                            <button type="submit" class="btn btn-info waves-effect">Hapus</button>
                                                                            <button type="button" class="btn btn-default" data-dismiss="modal">Batal</button>
                                                                        </div>
                                                                    </div>
                                                                    <!-- /.modal-content -->
                                                                </form>
                                                            </div>
                                                            <!-- /.modal-dialog -->
                                                        </div>
                                                        <!-- End Popup Model utk utk Generate Kode untuk flask_app.py -->

                                                    </td>
                                                </tr>
                                                {% endfor %}
                                            </tbody>
                                        </table>
                                    </div>
                                    <!-- </form> -->
                                </div>
                            </div>



                    </div>
                </div>



                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/footable.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/custom.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/footable-init.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/jQuery.style.switcher.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/jquery.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/bootstrap.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/jquery.slimscroll.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/moment.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/sidebar-nav.min.js') }}"></script>-->
                <!--<script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_foo/waves.js') }}"></script>-->

                <!-- There could be multiple reasons for this error. -->
                    <!-- jQuery DataTables library is missing. -->
                    <!-- jQuery library is loaded after jQuery DataTables. -->
                    <!-- Multiple versions of jQuery library is loaded. -->


                <!-- ./wrapper -->
                <!-- REQUIRED SCRIPTS -->
                <!-- jQuery -->
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.min.js.download') }}"></script>
                <!-- Bootstrap 4 -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/bootstrap.bundle.min.js.download') }}"></script> -->
                <!-- AdminLTE App -->
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/adminlte.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/sweetalert2-9.10.12.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/site.js.download') }}"></script>


                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.validate.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.validate.unobtrusive.min.js.download') }}"></script>
                <!-- <script> -->
                <!--$("#main_form").validate(); -->
                <!-- </script> -->

                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/css_tabel_suhu/dataTables.bootstrap4.min.css') }}" />
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/jquery.dataTables.min.js.download') }}"></script>
                <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_suhu/dataTables.bootstrap4.min.js.download') }}"></script>


                <!-- /#wrapper -->

                <!-- Bootstrap Core JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/bootstrap.min.js') }}"></script> -->
                <!-- Menu Plugin JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/sidebar-nav.min.js') }}"></script> -->
                <!--slimscroll JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/jquery.slimscroll.js') }}"></script> -->
                <!--Wave Effects -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/waves.js') }}"></script> -->
                <!-- Custom Theme JavaScript -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/custom.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/datatables.min.js') }}"></script> -->
                <!-- start - This is for export functionality only -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/dataTables.buttons.min.js') }}"></script> -->
                <!-- jQuery -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/jquery.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/buttons.flash.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/jszip.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/pdfmake.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/vfs_fonts.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/buttons.html5.min.js') }}"></script> -->
                <!-- <script type="text/javascript" src="{{ url_for('static', filename = 'js/mylib_tabel_data/buttons.print.min.js') }}"></script> -->
                <!-- end - This is for export functionality only -->




                <script>
                    /*
                    $(document).ready(function() {
                        $('#myTable').DataTable();
                        $(document).ready(function() {
                            var table = $('#example').DataTable({
                                "columnDefs": [{
                                    "visible": false,
                                    "targets": 2
                                }],
                                "order": [
                                    [2, 'asc']
                                ],
                                "displayLength": 25,
                                "drawCallback": function(settings) {
                                    var api = this.api();
                                    var rows = api.rows({
                                        page: 'current'
                                    }).nodes();
                                    var last = null;
                                    api.column(2, {
                                        page: 'current'
                                    }).data().each(function(group, i) {
                                        if (last !== group) {
                                            $(rows).eq(i).before('<tr class="group"><td colspan="5">' + group + '</td></tr>');
                                            last = group;
                                        }
                                    });
                                }
                            });
                            // Order by the grouping
                            $('#example tbody').on('click', 'tr.group', function() {
                                var currentOrder = table.order()[0];
                                if (currentOrder[0] === 2 && currentOrder[1] === 'asc') {
                                    table.order([2, 'desc']).draw();
                                } else {
                                    table.order([2, 'asc']).draw();
                                }
                            });
                        });
                    }); */
                    $('#example23').DataTable({
                        dom: 'Bfrtip',
                        buttons: [
                            'copy', 'csv', 'excel', 'pdf', 'print'
                        ]
                    });
                    $('.buttons-copy, .buttons-csv, .buttons-print, .buttons-pdf, .buttons-excel').addClass('btn btn-primary m-r-10');
                </script>
            '''

    if(none_atau_lainnya is not None):

        list_none_atau_lainnya = none_atau_lainnya.split("-")
        str_none_atau_lainnya = ' '.join(list_none_atau_lainnya)

        # get jenis query edit atau del atau run
        get_jenis_query = list_none_atau_lainnya[0]
        get_nama_tabel = list_none_atau_lainnya[-1]

        conn = connect_db()
        db = conn.cursor()

        if(get_jenis_query == 'edit'):

            # var1_in_edit = request.form.get['nama_tabel_edit_'+get_nama_tabel]
            var1_in_edit = request.form['nama_tabel_edit_'+get_nama_tabel]
            # var1_in_edit = get_nama_tabel
            # var2_in_edit = "CREATE TABLE IF NOT EXISTS data_tabel_myadmin (id INTEGER PRIMARY KEY AUTOINCREMENT, kolom1 TEXT, kolm2 DATETIME, kolom3 TEXT) ok"
            # var2_in_edit = request.form.get['teks_sintaks_edit_'+get_nama_tabel]
            var2_in_edit = request.form['teks_sintaks_edit_'+get_nama_tabel]

            # if(request.form['teks_sintaks_edit'] is not None):
            #     var2_in_edit = request.form['teks_sintaks_edit']
            # else:
            #     var2_in_edit = "CREATE TABLE IF NOT EXISTS data_tabel_myadmin (id INTEGER PRIMARY KEY AUTOINCREMENT, kolom1 TEXT, kolm2 DATETIME, kolom3 TEXT) ok"

            # update pada Tabel data_tabel_myadmin, pada kolom teks_sintaks
            db.execute("UPDATE data_tabel_myadmin SET teks_sintaks = ? WHERE nama_tabel = ?",(var2_in_edit, var1_in_edit))

            conn.commit()

        elif(get_jenis_query == 'del'):
            var1_in_hapus = request.form['nama_tabel_hapus_'+get_nama_tabel]

            # hapus data pada Tabel data_tabel_myadmin, pada kolom nama_tabel
            db.execute("DELETE FROM data_tabel_myadmin WHERE nama_tabel = ?",(var1_in_hapus,))

            conn.commit()

        elif(get_jenis_query == 'gen'):

            var1_in_gen = request.form['nama_tabel_gen_'+get_nama_tabel]
            var2_in_gen = request.form['teks_sintaks_tabel_gen_'+get_nama_tabel]
            var3_in_gen = request.form['teks_sintaks_page_gen_'+get_nama_tabel]

            # hapus data pada Tabel data_tabel_myadmin, pada kolom nama_tabel
            # db.execute("DELETE FROM data_tabel_myadmin WHERE nama_tabel = ?",(var1_in_hapus,))

            # conn.commit()

            # generate kode @app.route.. untuk flask_app.py
            var3_in_gen += """



            """

        # return 'Hello ' + str_none_atau_lainnya + ' Tipe request = ' + request.method + ' ' + list_none_atau_lainnya[0]+ ' ' + list_none_atau_lainnya[-1]

        # # menampilkan data dari tabel data_tabel_myadmin
        # # conn = connect_db()
        # # db = conn.cursor()

        # c = db.execute(""" SELECT * FROM  data_tabel_myadmin """)

        # var_tabel_myadmin_in = c.fetchall()

        # conn.commit()
        # # db.close()
        # # conn.close()

        db.close()
        conn.close()

        # return render_template_string(A_a+template_view+Z_z, var_tabel_myadmin = var_tabel_myadmin_in)

        return redirect(url_for('myadmin'))

    else:
        # Aksi => Buat, Hapus Tabel data_tabel_myadmin
        aksi = 'c'

        if aksi == 'c':
            conn = connect_db()
            db = conn.cursor()

            str_info = 'tabel berhasil dibuat :D'
            # create tabel
            db.execute("""
            CREATE TABLE IF NOT EXISTS data_tabel_myadmin
            (id INTEGER PRIMARY KEY AUTOINCREMENT, nama_tabel TEXT, date_pembuatan DATETIME,
            teks_sintaks TEXT)
            """)

            conn.commit()

        elif aksi== 'd':
            conn = connect_db()
            db = conn.cursor()

            str_info = 'tabel berhasil dihapus :D'
            # hapus tabel
            db.execute("""
            DROP TABLE IF EXISTS data_tabel_myadmin
            """)

            conn.commit()
            # db.close()
            # conn.close()

            # untuk membersihkan semacam cache setelah proses hapus tabel
            # conn = connect_db_to_vacuum()
            # db = conn.cursor()

            db.execute("""
            vacuum
            """)

            conn.commit()
            # db.close()
            # conn.close()

        # return str_info

        if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route lain, misal /myadmin

            var1_in = request.form['nama_tabel']
            var2_in = request.form['teks_sintaks']

            # untuk mengkondisikan nama tabel tidak boleh ada spasi dan hanya a-z dan angka
            # var1_in = var1_in.replace(" ","_").lower()
            filter_var1_in = "_1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

            getVals_base_filter_var1_in = list(filter(lambda x: x in filter_var1_in, var1_in))
            var1_in = "".join(getVals_base_filter_var1_in).lower()

            # Aksi => Buat, Hapus Tabel dari Tabel data_tabel_myadmin
            aksi_sub = 'c'

            if aksi_sub == 'c':
                # conn = connect_db()
                # db = conn.cursor()

                str_info = 'tabel berhasil dibuat :D'
                # create tabel
                db.execute("""
                CREATE TABLE IF NOT EXISTS """ + var1_in + """
                (kolom2 TEXT, kolom3 DATETIME, kolom4 TEXT)
                """)

                conn.commit()
                # db.close()
                # conn.close()

                """Mengisi data untuk spesifikasi tabel."""
                # conn = connect_db()
                # db = conn.cursor()

                db.execute("SELECT * FROM data_tabel_myadmin WHERE nama_tabel = ?", (var1_in,))
                entry = db.fetchone()

                if entry is None:
                    import numpy as np
                    import pandas as pd

                    from datetime import datetime
                    import pytz
                    Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

                    db.execute("""INSERT INTO data_tabel_myadmin (nama_tabel, date_pembuatan, teks_sintaks) VALUES (?, ?, ?)""",
                        (var1_in, Date, var2_in))

                else:
                    ket_hasil = 'Tidak dilakukan Insert, karena Tabel tidak kosong'

                conn.commit()
                # db.close()
                # conn.close()

            elif aksi_sub== 'd':
                # conn = connect_db()
                # db = conn.cursor()

                str_info = 'tabel berhasil dihapus :D'
                # hapus tabel
                db.execute("""
                DROP TABLE IF EXISTS """ + var1_in + """
                """)

                conn.commit()
                # db.close()
                # conn.close()

                # untuk membersihkan semacam cache setelah proses hapus tabel
                # conn = connect_db_to_vacuum()
                # db = conn.cursor()

                db.execute("""
                vacuum
                """)

                conn.commit()
                # db.close()
                # conn.close()

            # menampilkan data dari tabel data_tabel_myadmin
            # conn = connect_db()
            # db = conn.cursor()

            c = db.execute(""" SELECT * FROM  data_tabel_myadmin """)

            var_tabel_myadmin_in = c.fetchall()

            conn.commit()
            # db.close()
            # conn.close()

            db.close()
            conn.close()

            return render_template_string(A_a+template_view+Z_z, var1 = var1_in, var2 = var2_in, var_tabel_myadmin = var_tabel_myadmin_in)

        else: # untuk yang 'GET' data awal untuk di send ke /myadmin

            # menampilkan data dari tabel data_tabel_myadmin
            # conn = connect_db()
            # db = conn.cursor()

            c = db.execute(""" SELECT * FROM  data_tabel_myadmin """)

            var_tabel_myadmin_in = c.fetchall()

            conn.commit()
            # db.close()
            # conn.close()

            db.close()
            conn.close()
            return render_template_string(A_a+template_view+Z_z, var_tabel_myadmin = var_tabel_myadmin_in)
            

@app.route('/launchpad_menu')
def launchpad_menu():
   return render_template("launchpad_menu.html")
