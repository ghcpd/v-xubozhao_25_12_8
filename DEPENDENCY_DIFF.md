# Dependency diff (Before -> After)

scikit-learn: 0.24.1 -> 1.5.2
numpy: 1.18.0 -> 2.3.5
pandas: 1.1.5 -> 2.3.3
matplotlib: 3.3.2 -> 3.10.7
scipy: 1.5.2 -> 1.16.3
pytest: 5.4.3 -> 8.4.2
fastapi: 0.63.0 -> 0.95.2
uvicorn: 0.13.3 -> 0.22.0
httpx: (not present) -> 0.25.2

# Quick justifications
- Upgrades ensure compatibility with Python 3.10+ and 3.13 in our CI environment.
- Final set chosen to prefer binary wheels to avoid build-from-source failures on Windows/CI.
- Pytest upgrade enables modern testing features and better plugin ecosystem.
