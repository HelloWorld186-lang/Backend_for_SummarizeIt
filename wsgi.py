from app import app

if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0')
    except Exception as e:
        print(f"An error occurred: {e}")