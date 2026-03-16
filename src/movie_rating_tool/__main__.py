"""
Entry point when running the package with: uv run -m movie_rating_tool
"""

from .cli import run_cli

if __name__ == "__main__":
    run_cli()
