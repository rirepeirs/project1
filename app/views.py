"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import Form
from werkzeug.utils import secure_filename
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/properties/create", methods=['POST','GET'])
def new():
    from . import db
    from .models import property
    form= Form()
    if form.validate_on_submit:
        name= form.name.data
        no_of_beds= form.no_of_beds.data
        no_of_baths= form.no_of_baths.data
        location= form.location.data
        amount= form.amount.data
        type= form.type.data
        description= form.description.data
        if 'photo' in request.files:
            photo = secure_filename(photo.filename)  # Secure the filename
            if  photo.filename != '':
                filename = secure_filename(photo.filename)
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo))
        flash('Successfully added!', 'success')
        return redirect(url_for("properties"))
    return render_template("forms.html", form=form)

@app.route('/properties', methods=['GEt'])
def properties():
    from . import db
    prop_q=db.property.query.all()
    return render_template('properties.html', properties=prop_q)

@app.route('/properties/<propertyid>', methods=['GET'])
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
