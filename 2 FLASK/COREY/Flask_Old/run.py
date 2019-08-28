from flaskblog import create_app

app = create_app()

# if we want to run the code with in the python instead of the flask environment variables
if __name__ == "__main__":
    app.run(debug=True)
