# pip install "jupyter-book<2" ghp-import

# Build the Jupyter book version

# build the HTML version
jupyter-book build ../chapters

# push it to GitHub
ghp-import -n -p -f ../chapters/_build/html
