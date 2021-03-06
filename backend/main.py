from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import json
from datetime import datetime
from utils import cursor_result_to_json
import branchs, shareholder, country, employees, utils, product, product_in_branch, publicity, \
    manufacturer, manufacturer_expenses

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'freedb.tech'
app.config['MYSQL_DB'] = 'freedbtech_market'
app.config['MYSQL_USER'] = 'freedbtech_osher'
app.config['MYSQL_PASSWORD'] = '123456'
mysql = MySQL(app)


@app.route('/')
def index():
    query = "select * from country"
    with mysql.connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/tables')
def get_table():
    table_name = request.args.get('table')
    return jsonify(utils.get_table(table_name))


# -------------------------------------- branchs --------------------------------------
# Select
@app.route('/branchs/select')
def branchs_select():
    result = utils.get_table(mysql, 'branchs')
    return jsonify({'data': result})


# delete
@app.route('/branchs/delete')
def delete_row():
    id = request.args.get('ID')
    try:
        utils.delete_from_table(mysql, "branchs", id)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/branchs/update')
def branchs_update():
    id = request.args.get('ID')
    town = request.args.get('TOWN')
    revenue = request.args.get('REVENUE')
    address = request.args.get('ADDRESS')
    area = request.args.get('AREA')
    try:
        branchs.update(mysql, id, town, revenue, address, area)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Insert
@app.route('/branchs/insert')
def branchs_insert():
    id = request.args.get('id')
    town = request.args.get('town')
    revenue = request.args.get('revenue')
    address = request.args.get('address')
    area = request.args.get('area')
    try:
        branchs.insert(mysql, town, revenue, address, area)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- Employee --------------------------------------
# Select
@app.route('/employees/select')
def employees_select():
    result = utils.get_table(mysql, 'employees')
    return jsonify({'data': result})


# delete
@app.route('/employees/delete')
def employees_delete_row():
    id = request.args.get('ID')
    try:
        utils.delete_from_table(mysql, "employees", id)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/employees/update')
def employees_update():
    id = request.args.get('ID')
    name = request.args.get('name')
    email = request.args.get('EMAIL')
    salary = request.args.get('SALARY')
    seniority = request.args.get('SENIORITY')
    branch_id = request.args.get('BARNCH_ID')
    job = request.args.get('JOB')
    is_manager = request.args.get('is_manager')
    try:
        employees.update(mysql, id, name, email, salary, seniority, branch_id, job, is_manager)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Insert
@app.route('/employees/insert')
def employees_insert():
    name = request.args.get('name')
    email = request.args.get('EMAIL')
    salary = request.args.get('SALARY')
    seniority = request.args.get('SENIORITY')
    branch_id = request.args.get('BARNCH_ID')
    job = request.args.get('JOB')
    is_manager = request.args.get('is_manager')
    try:
        employees.insert(mysql, name, email, salary, seniority, branch_id, job, is_manager)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- Country --------------------------------------

# Select
@app.route('/country/select')
def country_select():
    result = utils.get_table(mysql, 'country')
    return jsonify({'data': result})


# delete
@app.route('/country/delete')
def country_delete_row():
    id = request.args.get('id')
    try:
        utils.delete_from_table(mysql, "country", id)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# insert
@app.route('/country/insert')
def country_insert():
    name = request.args.get('country_name')
    try:
        country.insert(mysql, name)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/country/update')
def country_update():
    id = request.args.get('id')
    name = request.args.get('country_name')
    try:
        country.update(mysql, id, name)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- manufacturer --------------------------------------

# Select
@app.route('/manufacturer/select')
def manufacturer_select():
    result = utils.get_table(mysql, 'Manufacturer')
    return jsonify({'data': result})


# delete
@app.route('/manufacturer/delete')
def manufacturer_delete_row():
    id = request.args.get('id')
    try:
        utils.delete_from_table(mysql, "Manufacturer", id)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# insert
@app.route('/manufacturer/insert')
def manufacturer_insert():
    countryid = request.args.get('countryid')
    name = request.args.get('name')
    try:
        manufacturer.insert(mysql, name, countryid)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/manufacturer/update')
def manufacturer_update():
    id = request.args.get('id')
    countryid = request.args.get('countryid')
    name = request.args.get('name')
    try:
        manufacturer.update(mysql, id, name, countryid)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- manufacturer_expenses --------------------------------------

# Select
@app.route('/manufacturer_expenses/select')
def manufacturer_expenses_select():
    result = utils.get_table(mysql, 'manufacturer_expenses')
    return jsonify({'data': result})


# delete
@app.route('/manufacturer_expenses/delete')
def manufacturer_expenses_delete_row():
    id = request.args.get('id')
    try:
        utils.delete_from_table(mysql, "manufacturer_expenses", id)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# insert
@app.route('/manufacturer_expenses/insert')
def manufacturer_expenses_insert():
    manufacturer_id = request.args.get('manufacturer_id')
    expenses = request.args.get('expenses')
    date_of_expenses = request.args.get('date_of_expenses')
    try:
        manufacturer_expenses.insert(mysql, manufacturer_id, expenses, date_of_expenses)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/manufacturer_expenses/update')
def manufacturer_expenses_update():
    id = request.args.get('id')
    manufacturer_id = request.args.get('manufacturer_id')
    expenses = request.args.get('expenses')
    date_of_expenses = request.args.get('date_of_expenses')
    try:
        manufacturer_expenses.update(mysql, id, manufacturer_id, expenses, date_of_expenses)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- product --------------------------------------

# Select
@app.route('/product/select')
def product_select():
    result = utils.get_table(mysql, 'product')
    return jsonify({'data': result})


# delete
@app.route('/product/delete')
def product_delete_row():
    barcode = request.args.get('barcode')
    try:
        utils.delete_from_table(mysql, "product", barcode, 'barcode')
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/product/update')
def product_update():
    barcode = request.args.get('barcode')
    name = request.args.get('name')
    manufacturld = request.args.get('manufacturld')
    description = request.args.get('description')
    unitQty = request.args.get('unitQty')
    Quantity = request.args.get('Quantity')
    bIsWeighted = request.args.get('bIsWeighted')
    QtyInPackage = request.args.get('QtyInPackage')
    ItemPrice = request.args.get('ItemPrice')
    try:
        product.update(mysql, barcode, name, manufacturld, description, unitQty, Quantity, bIsWeighted, QtyInPackage,
                       ItemPrice)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Insert
@app.route('/product/insert')
def product_insert():
    barcode = request.args.get('barcode')
    name = request.args.get('name')
    manufacturld = request.args.get('manufacturld')
    description = request.args.get('description')
    unitQty = request.args.get('unitQty')
    Quantity = request.args.get('quantity')
    bIsWeighted = request.args.get('bIsWeighted')
    QtyInPackage = request.args.get('qtyInPackage')
    ItemPrice = request.args.get('itemPrice')
    try:
        product.insert(mysql, barcode, name, manufacturld, description, unitQty, Quantity, bIsWeighted, QtyInPackage,
                       ItemPrice)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- product_in_branch --------------------------------------

# Select
@app.route('/product_in_branch/select')
def product_in_branch_select():
    result = utils.get_table(mysql, 'product_in_branch')
    return jsonify({'data': result})


# delete
@app.route('/product_in_branch/delete')
def product_in_branch_delete_row():
    id = request.args.get('id')
    try:
        utils.delete_from_table(mysql, "product_in_branch", id)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/product_in_branch/update')
def product_in_branch_update():
    id = request.args.get('id')
    branch_id = request.args.get('branch_id')
    product_barcode = request.args.get('product_barcode')
    amount_in_stock = request.args.get('amount_in_stock')
    try:
        product_in_branch.update(mysql, id, branch_id, product_barcode, amount_in_stock)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Insert
@app.route('/product_in_branch/insert')
def product_in_branch_insert():
    branch_id = request.args.get('branch_id')
    product_barcode = request.args.get('product_barcode')
    amount_in_stock = request.args.get('amount_in_stock')
    try:
        product_in_branch.insert(mysql, branch_id, product_barcode, amount_in_stock)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- publicity--------------------------------------

# Select
@app.route('/publicity/select')
def publicity_select():
    result = utils.get_table(mysql, 'publicity')
    return jsonify({'data': result})


# delete
@app.route('/publicity/delete')
def publicity_delete_row():
    id = request.args.get('id')
    try:
        utils.delete_from_table(mysql, "publicity", id)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/publicity/update')
def publicity_update():
    id = request.args.get('id')
    price = request.args.get('price')
    location = request.args.get('location')
    goal = request.args.get('goal')
    try:
        publicity.update(mysql, id, price, location, goal)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Insert
@app.route('/publicity/insert')
def publicity_insert():
    price = request.args.get('price')
    location = request.args.get('location')
    goal = request.args.get('goal')
    try:
        publicity.insert(mysql, price, location, goal)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# -------------------------------------- shareholder--------------------------------------

# Select
@app.route('/shareholder/select')
def shareholder_select():
    result = utils.get_table(mysql, 'shareholder')
    return jsonify({'data': result})


# delete
@app.route('/shareholder/delete')
def shareholder_delete_row():
    ID = request.args.get('ID')
    try:
        utils.delete_from_table(mysql, "shareholder", ID)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Update
@app.route('/shareholder/update')
def shareholder_update():
    ID = request.args.get('ID')
    STOCK = request.args.get('STOCK')
    EMAIL = request.args.get('EMAIL')
    NAME = request.args.get('NAME')
    try:
        shareholder.update(mysql, ID, STOCK, EMAIL, NAME)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# Insert
@app.route('/shareholder/insert')
def shareholder_insert():
    STOCK = request.args.get('stock')
    EMAIL = request.args.get('email')
    NAME = request.args.get('name')
    try:
        shareholder.insert(mysql, STOCK, EMAIL, NAME)
        return "success"
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ************************************************************************************************
# --------------------------------------------------querys----------------------------------------
# ************************************************************************************************
@app.route('/query/avg_country_price')  #
def avg_country_price():
    result = utils.execute_select(mysql, 'querys/avg_country_price.sql')
    return jsonify({'data': result})


@app.route('/query/avg_manu_price')  #
def avg_manu_price():
    result = utils.execute_select(mysql, 'querys/avg_manu_price.sql')
    return jsonify({'data': result})


@app.route('/query/best_manufaturer_of_each_branch')  #
def best_manufaturer_of_each_branch():
    result = utils.execute_select(mysql, 'querys/best_manufaturer_of_each_branch.sql')
    return jsonify({'data': result})


@app.route('/query/big_seniority')  #
def big_seniority():
    result = utils.execute_select(mysql, 'querys/big_seniority.sql')
    return jsonify({'data': result})


@app.route('/query/biggest_shareholders')  #
def biggest_shareholders():
    result = utils.execute_select(mysql, 'querys/biggest_shareholders.sql')
    return jsonify({'data': result})


@app.route('/query/count_of_employees_in_each_branch')  #
def count_of_employees_in_each_branch():
    result = utils.execute_select(mysql, 'querys/count_of_employees_in_each_branch.sql')
    return jsonify({'data': result})


@app.route('/query/maneger_manege_branch_by_bigest_revenue')  #
def maneger_manege_branch_by_bigest_revenue():
    result = utils.execute_select(mysql, 'querys/maneger_manege_branch_by_bigest_revenue.sql')
    return jsonify({'data': result})


@app.route('/query/max_manu_cuntry')  #
def max_manu_cuntry():
    result = utils.execute_select(mysql, 'querys/max_manu_cuntry.sql')
    return jsonify({'data': result})


@app.route('/query/max_manu_product')  #
def max_manu_product():
    result = utils.execute_select(mysql, 'querys/max_manu_product.sql')
    return jsonify({'data': result})


@app.route('/query/min_salary')  #
def min_salary():
    result = utils.execute_select(mysql, 'querys/min_salary.sql')
    return jsonify({'data': result})


@app.route('/query/num_of_town')  #
def num_of_town():
    result = utils.execute_select(mysql, 'querys/num_of_town.sql')
    return jsonify({'data': result})


@app.route('/query/number_of_employs')  #
def number_of_employs():
    result = utils.execute_select(mysql, 'querys/number_of_employs.sql')
    return jsonify({'data': result})


@app.route('/query/number_of_manager')  #
def number_of_manager():
    result = utils.execute_select(mysql, 'querys/number_of_manager.sql')
    return jsonify({'data': result})


@app.route('/query/nums_emploeeys+sum_of_salary')  #
def nums_emploeeys_sum_of_salary():
    result = utils.execute_select(mysql, 'querys/nums_emploeeys+sum_of_salary.sql')
    result[0]['sum_of_salary'] = str(result[0]['sum_of_salary'])
    return jsonify({'data': result})


@app.route('/query/our_biggest_manufaturer')  #
def our_biggest_manufaturer():
    result = utils.execute_select(mysql, 'querys/our_biggest_manufaturer.sql')
    return jsonify({'data': result})


@app.route('/query/over_ten_thousand')  #
def over_ten_thousand():
    result = utils.execute_select(mysql, 'querys/over_ten_thousand.sql')
    return jsonify({'data': result})


@app.route('/query/product_of_min_manu')  #
def product_of_min_manu():
    result = utils.execute_select(mysql, 'querys/product_of_min_manu.sql')
    return jsonify({'data': result})


@app.route('/query/salary_of_employee')  #
def salary_of_employee():
    result = utils.execute_select(mysql, 'querys/salary_of_employee.sql')
    return jsonify({'data': result})


@app.route('/query/The_branch_with_the_most_products')  #
def The_branch_with_the_most_products():
    result = utils.execute_select(mysql, 'querys/The_branch_with_the_most_products.sql')
    return jsonify({'data': result})


@app.route('/query/sum_of_meters_in_all_sopers')  #
def sum_of_meters_in_all_sopers():
    result = utils.execute_select(mysql, 'querys/sum_of_meters_in_all_sopers.sql')
    result[0]['sum_of_meters_in_all_sopers'] = str(result[0]['sum_of_meters_in_all_sopers'])
    return jsonify({'data': result})


@app.route('/query/the_number_os_branchs')  #
def the_number_os_branchs():
    result = utils.execute_select(mysql, 'querys/the_number_os_branchs.sql')
    return jsonify({'data': result})


@app.route('/query/total_profit_all_branchs')  #
def total_profit_all_branchs():
    result = utils.execute_select(mysql, 'querys/total_profit_all_branchs.sql')
    result[0]['total_profit'] = str(result[0]['total_profit'])
    return jsonify({'data': result})


@app.route('/query/total_publicity_cost')  #
def total_publicity_cost():
    result = utils.execute_select(mysql, 'querys/total_publicity_cost.sql')
    result[0]['Total_publicity_cost'] = str(result[0]['Total_publicity_cost'])
    return jsonify({'data': result})


# ************************************************************************************************
# --------------------------------------------------querys with param----------------------------------------
# ************************************************************************************************


@app.route('/query/publicity_price_of_specific_goal')  #
def publicity_price_of_specific_goal():
    goal = request.args.get('goal')
    with open(r"param/publicity_price_of_specific_goal.sql") as query:
        with mysql.connection.cursor() as cursor:
            temp = query.read().replace(":goal", goal)
            cursor.execute(temp)
            result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/employees_earn_more_than_x')  #
def employees_earn_more_than_x():
    min_salary = request.args.get('min_salary')
    with open(r"param/employees_earn_more_than_x.sql") as query:
        with mysql.connection.cursor() as cursor:
            temp = query.read().replace(":min_salary", min_salary)
            cursor.execute(temp)
            result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/almost_out_of_stock')  #
def almost_out_of_stock():
    min_amount = request.args.get('min_amount')
    with open(r"param/almost_out_of_stock.sql") as query:
        with mysql.connection.cursor() as cursor:
            temp = query.read().replace(":min_amount", min_amount)
            cursor.execute(temp)
            result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/almost_out_of_stock_in_country')  #
def almost_out_of_stock_in_country():
    country_name = '"' + str(request.args.get('country_name')) + '"'
    min_amount = request.args.get('min_amount')
    with open(r"param/almost_out_of_stock_in_country.sql") as query:
        with mysql.connection.cursor() as cursor:
            temp = query.read().replace(":min_amount", min_amount).replace(":country_name", country_name)
            cursor.execute(temp)
            result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/products_of_specific_manu')  #
def products_of_specific_manu():
    manu = '"' + str(request.args.get('manu_name')) + '"'
    with open(r"param/products_of_specific_manu.sql") as query:
        with mysql.connection.cursor() as cursor:
            temp = query.read().replace(":manu_name", manu)
            cursor.execute(temp)
            result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/products_of_specific_country')  #
def prosucts_of_specific_country():
    country_name = '"' + str(request.args.get('country_name')) + '"'
    with open(r"param/products_of_specific_country.sql") as query:
        with mysql.connection.cursor() as cursor:
            temp = query.read().replace(":country_name", country_name)
            cursor.execute(temp)
            result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/list_of_brenchs_in_specific_town')  #
def list_of_brenchs_in_specific_jerusalem():
    town = '"' + str(request.args.get('town')) + '"'
    with open(r"param/list_of_brenchs_in_specific_town.sql") as query:
        with mysql.connection.cursor() as cursor:
            temp = query.read().replace(":town", town)
            cursor.execute(temp)
            result = cursor_result_to_json(cursor)
    return jsonify({'data': result})


# ************************************************************************************************
# --------------------------------------------------views----------------------------------------
# ************************************************************************************************


@app.route('/view/almost_out_of_stock_view')  #
def almost_out_of_stock_view():
    result = utils.get_table(mysql, 'almost_out_of_stock_view')
    return jsonify({'data': result})


@app.route('/view/branch_manu_prod_amount_view')  #
def branch_manu_prod_amount_view():
    result = utils.get_table(mysql, 'branch_manu_prod_amount')
    return jsonify({'data': result})


# ************************************************************************************************
# --------------------------------------------------procudure----------------------------------------
# ************************************************************************************************


@app.route('/procedure/addProductsToBranch')
def addProductsToBranch():
    barcode = request.args.get('barcode')
    amount = request.args.get('amount')
    price = request.args.get('price')
    branchId = request.args.get('branch_id')
    date = request.args.get('date')
    date = datetime.strptime(date, '%Y-%m-%d')
    with mysql.connection.cursor() as cursor:
        try:
            cursor.callproc('addProductsToBranch', [barcode, amount, price, branchId, date])
            return "success"
        except():
            return "failed"


@app.route('/procedure/buyProductFromBranch')
def buyProductFromBranch():
    barcode = request.args.get('barcode')
    amount = request.args.get('amount')
    branchId = request.args.get('branch_id')
    with mysql.connection.cursor() as cursor:
        try:
            cursor.callproc('buyProductFromBranch', [barcode, amount, branchId])
            return "success"
        except():
            return "failed"


app.run('localhost', 5000)
