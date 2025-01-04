from flask import Blueprint, request, jsonify
from app.models import db, User, Book, Order
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

# Register
@api.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Login
@api.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Convert user ID to string for JWT identity
    access_token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": access_token}), 200

# Add Book
@api.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    try:
        user_id = int(get_jwt_identity())
    except Exception as e:
        return jsonify({"message": "Invalid token"}), 401

    data = request.json
    title = data.get('title')
    author = data.get('author')
    price = data.get('price')

    book = Book(title=title, author=author, price=price)
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book added successfully"}), 201

# Update Book
@api.route('/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.price = data.get('price', book.price)
    db.session.commit()
    return jsonify({"message": "Book updated successfully"}), 200

# Get Books
@api.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    books = Book.query.all()
    result = [{"id": b.id, "title": b.title, "author": b.author, "price": str(b.price)} for b in books]
    return jsonify(result), 200

# Delete Book
@api.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}), 200

# Get Orders
@api.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    orders = Order.query.all()
    result = [{"id": o.id, "user_id": o.user_id, "book_id": o.book_id, "order_date": o.order_date} for o in orders]
    return jsonify(result), 200

@api.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    """
    Endpoint untuk membuat pesanan baru.
    """
    user_id = int(get_jwt_identity())  # Ambil user ID dari JWT token
    data = request.json
    book_id = data.get('book_id')

    # Validasi keberadaan buku
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    # Buat order baru
    order = Order(user_id=user_id, book_id=book_id)
    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order created successfully"}), 201

@api.route('/test-db', methods=['GET'])
def test_db():
    from sqlalchemy import create_engine
    try:
        engine = create_engine(
            'postgresql://postgres:mXK8f5R32A3awd4W@db.mlvjbuusruadndqlhyop.supabase.co:5432/postgres?sslmode=require'
        )
        connection = engine.connect()
        connection.close()
        return {"message": "Database connection successful!"}, 200
    except Exception as e:
        return {"error": str(e)}, 500