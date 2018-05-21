# -*- coding: utf-8 -*-
from __future__ import print_function
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for,jsonify
from flask_paginate import Pagination, get_page_args
from flask import request
import json
import pypyodbc
from connectDB import select_history_query, insert_query
import pysolr


solr = pysolr.Solr('http://localhost:8983/solr/searchpr', timeout=10)

@app.route('/query', methods=['GET','POST'])
def fetchQuery(result=[]):
    a = request.args['a']
    result = select_history_query(a)
    # return str(result[0][0].encode('utf-8'))

    if len(result): 

        array =[]
        for i in result:
            array.append(i[0])
        str1 = ','.join(array)
        return str1
    else:
        return str(result)

@app.route('/', methods=['GET', 'POST'])
def index(result=""):
    if request.args.get('mail', None):
        result = request.args['mail']
        insert_query(result)    
    results = solr.search(result,rows=100)
    if len(results)==0:
        results= ""
    page = request.args.get('page', 1, type=int)
    pagination = Pagination(
            page=page,
            total=len(results),
            error_out=False,
            record_name='results',
            per_page=10,
            css_framework='bootstrap4'
            ) 
    if len(results)==0:
        return render_template(
            'search.html',
            inputsearch= result,
            )
    else:
        results=list(results)
        return render_template(
            'search.html',
            results=results[(page-1)*10:page*10],
            pagination=pagination,
            page=page,
            len=len(results),
            format_total=True,
            format_number=True,
            per_page=10,
            inputsearch= result,
            )










  