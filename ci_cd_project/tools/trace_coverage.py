
import os
import sys
import trace
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVER_DIR = ROOT / "tracecov"

def run():
    COVER_DIR.mkdir(exist_ok=True)
    tracer = trace.Trace(count=True, trace=False)
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
    tracer.runfunc(unittest.TextTestRunner(verbosity=2).run, suite)
    results = tracer.results()
    results.write_results(show_missing=True, coverdir=str(COVER_DIR))
    print(f"Cobertura por 'trace' escrita en: {COVER_DIR}")

if __name__ == "__main__":
    run()
