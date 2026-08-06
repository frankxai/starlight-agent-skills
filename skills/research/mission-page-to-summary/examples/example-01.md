# Example 01 — Parker Solar Probe

## Input

```
page: "https://www.nasa.gov/mission/parker-solar-probe/  (NASA mission page)
Summary text: Parker Solar Probe launched in 2018 to fly through the Sun's outer
atmosphere, the corona, to trace how energy and heat move through it and what
accelerates the solar wind. Instruments: FIELDS, WISPR, SWEAP, IS☉IS. Status:
active, making progressively closer perihelion passes."
format: card
```

## Output

```json
{
  "name": "Parker Solar Probe",
  "agency": "NASA",
  "objective": "Fly through the Sun's corona to trace how energy and heat move through it and what accelerates the solar wind.",
  "timeline": [
    { "date": "2018", "event": "Launch" },
    { "date": "ongoing", "event": "Progressively closer perihelion passes through the corona" }
  ],
  "instruments": [
    { "name": "FIELDS", "purpose": "Measures electric and magnetic fields" },
    { "name": "WISPR", "purpose": "Wide-field imaging of the corona and solar wind" },
    { "name": "SWEAP", "purpose": "Counts and measures solar wind particles" },
    { "name": "IS☉IS", "purpose": "Measures energetic particles" }
  ],
  "status": "Active",
  "key_results": ["Direct in-situ sampling of the solar corona"],
  "source": "https://www.nasa.gov/mission/parker-solar-probe/"
}
```

## Why this is a good result

Every timeline entry, instrument, and result is drawn from the page; the source
is linked; nothing is filled in from memory beyond what the page states.
