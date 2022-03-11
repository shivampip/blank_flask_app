from flask import Blueprint, jsonify, render_template, request



sandbox = Blueprint("sandbox", __name__)





@sandbox.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to Sandbox"})


@sandbox.route("/hello", methods=["GET"])
def imgimg():
    return jsonify({"message": "Hello World from Sandbox"})

