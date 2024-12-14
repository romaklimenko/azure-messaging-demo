if command -v python &>/dev/null; then
    python -m venv .venv
else
    python3 -m venv .venv
fi
source .venv/bin/activate

pip install --upgrade pip
pip install -r ./python/requirements.txt

echo 'If the virtual environment is not activated, run the following command:'
echo 'source .venv/bin/activate'

