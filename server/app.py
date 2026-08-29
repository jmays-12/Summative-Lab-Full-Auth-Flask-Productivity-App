#!/usr/bin/env python3
from config import app
import routes # appears unused but is used by add_resource() when routes.py gets imported

if __name__ == '__main__':
    app.run(port=5555, debug=True)
