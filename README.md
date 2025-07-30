
- [Approximating Arcs Using Cubic Bézier Curves](https://ecridge.com/bezier.pdf)

```sh
uv venv --seed --python=3.12
uv pip install -r requirements.txt

source .venv/bin/activate
python cubic_bezier.py
python quadratic_bezier.py
python cubic_arc_approximation.py
```