"""Compare the measured weight of the guitar with the SolidWorks model.

Usage:
    python mass_properties.py
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "mass_properties.json"


def percent_error(measured: float, theoretical: float) -> float:
    """% error = (measured - theoretical) / theoretical * 100"""
    return (measured - theoretical) / theoretical * 100


def deviation(measured: float, theoretical: float) -> float:
    """deviation = measured - (measured + theoretical) / 2"""
    return measured - (measured + theoretical) / 2


def main() -> None:
    data = json.loads(DATA_FILE.read_text())
    measured = data["measured"]["mass_lb"]
    theoretical = data["theoretical"]["mass_lb"]

    print(f"Assembly:          {data['assembly']}")
    print(f"Measured weight:   {measured:.2f} lb")
    print(f"SolidWorks weight: {theoretical:.2f} lb")
    print(f"Model volume:      {data['theoretical']['volume_in3']:.2f} in^3")
    print(f"% error:           {percent_error(measured, theoretical):+.2f} %")
    print(f"Deviation:         {deviation(measured, theoretical):+.2f} lb")


if __name__ == "__main__":
    main()
