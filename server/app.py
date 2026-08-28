#!/usr/bin/env python3
from config import app
import routes

if __name__ == '__main__':
    app.run(port=5555, debug=True)
