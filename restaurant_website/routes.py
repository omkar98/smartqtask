import os
from os.path import join, dirname, realpath
from flask import render_template, url_for, redirect, flash, Markup, abort, request, jsonify
from restaurant_website import app
# from sqlalchemy import asc, desc, update
import csv

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    Cuisines=[]
    print(request.args)
    print(request.data)
    with open("restaurant_website/restaurantsa9126b3.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        next(csv_reader)
        # csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            dishes = line['Cuisines'].split(", ")
            for dish in dishes:
                if dish not in Cuisines and not dish=="":
                    Cuisines.append(dish)
                # print(Cuisines)
                # print(Cuisines)
        # print(data)
        csv_file.seek(0)
        next(csv_reader)
        # return render_template('home.html', data=csv_reader, Cuisines=Cuisines)
        required_res=[]
        if request.args:
            # print("We are in:")
            required_cuisine=[]
            for i in request.args.get('data').split(" "):
                if not i is '':
                    required_cuisine.append(i)
            for line in csv_reader:
                # print(line['Cuisines'].split(", "))
                # any_in = lambda a, b: any(i in required_cuisine for i in  line['Cuisines'].split(", ")
                check =  any(item in required_cuisine for item in line['Cuisines'].split(", "))
                print(check)
                if check:
                    print("We have entered")
                    # print(line['Cuisines'])
                    required_res.append(line)
            return render_template('home.html', data=required_res, Cuisines=Cuisines)
        return render_template('home.html', data=list(csv_reader), Cuisines=Cuisines)

@app.route("/get_restaurants", methods=['GET', 'POST'])
def get_restaurants():
    required_cuisine=""
    if request.method == 'POST':
        print(request.form)
        for each_cuisine in request.form:
            required_cuisine+=" "+each_cuisine
        print(required_cuisine)
        return redirect(url_for('home', data=required_cuisine))
        # return render_template('home.html', data=csv_reader, Cuisines=jsonify(required_cuisine))
    return "Bad Request"
    # return render_template('home.html')
