import os
from supabase import create_client, Client
from flask import Flask, jsonify, request, Response

url = 'https://zvxlqpfkfudfdqedqoyu.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp2eGxxcGZrZnVkZmRxZWRxb3l1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjE5NTY2OTgsImV4cCI6MTk3NzUzMjY5OH0.1MfObcGD01cJhUEJC6sowQ71xWyXD__HNmDcM5ALwig'
supabase = create_client(url, key)

app = Flask(__name__)

def insert_approval(user_id, title, content):
    approval = {
        "user_id": user_id,
        "title": title,
        "content": content
    }
    data = supabase.table("posts").insert(approval).execute()
    return data.data


@app.route('/articles', methods=['POST'])
def add_approval():
    data = request.get_json()
    user_id = data['user_id']
    title = data['title']
    content = data['content']
    res = insert_approval(user_id, title, content)
    return jsonify(res), 201

insert_approval('b67db583-0a47-4d32-a5c4-35eb9e28704c', 'test', 'test')