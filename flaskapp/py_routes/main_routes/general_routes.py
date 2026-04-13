from flask import render_template, jsonify, request, redirect, url_for, flash


from flaskapp.py_routes.main_routes import main


# LANDING PAGE
# ===================================================================
@main.route('/', methods=['GET', 'POST'])
@main.route('/dashboard', methods=['GET', 'POST'])
def main_dashboard():
    page_title = 'Ashgard Industries'
    
    return render_template('index.html', page_title=page_title)
    



# @main.route('/crud_view', methods=['GET'])
# def crud_view():
#     if request.method == 'GET':
#         views = Crud_tbl.query.all()
#         tmp_list = list()
#         for i in views:
#             k = {
#                 'ct_id'        : i.ct_id,
#                 'some_string'  : i.some_string,
#                 'some_text'    : i.some_text,
#                 'some_int'     : i.some_int,
#                 'dtg'     : i.dtg
#             }
#             tmp_list.append(k)
#         # return jsonify(tmp)

#             tmp = table_builder.crud_dt_serverside(request, tmp_list)
#         return jsonify(tmp)
        


# @main.route('/crud_update', methods=['GET', 'POST'])
# def crud_update():
#     pass

# @main.route('/crud_delete', methods=['GET', 'POST'])
# def crud_delete():
#     pass






