from flask import Blueprint, jsonify
from .db import test_database_connection, get_all_products

# Crear blueprint
api_bp = Blueprint("api", __name__)


# 🔹 Endpoint de prueba
@api_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "code": 200,
        "message": "API de supermercado funcionando correctamente"
    })


# 🔹 Endpoint para obtener productos desde Supabase
@api_bp.route("/productos", methods=["GET"])
def obtener_productos():
    try:
        productos = get_all_products()

        return jsonify({
            "code": 200,
            "total": len(productos),
            "data": productos
        })

    except Exception as e:
        return jsonify({
            "code": 500,
            "message": "Error al obtener productos desde la base de datos",
            "error": str(e)
        }), 500


# 🔹 Endpoint para probar conexión con la base de datos
@api_bp.route("/db-test", methods=["GET"])
def db_test():
    try:
        result = test_database_connection()

        return jsonify({
            "code": 200,
            "message": "Conexión a Supabase/PostgreSQL exitosa",
            "database_time": result["server_time"]
        })

    except Exception as e:
        return jsonify({
            "code": 500,
            "message": "Error al conectar con la base de datos",
            "error": str(e)
        }), 500