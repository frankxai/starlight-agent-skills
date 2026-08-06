# Example 01 — orbital speed vs distance (p5.js)

## Input

```
goal: "show how orbital speed changes with distance from the central body"
params: ["orbit_radius"]
stack: p5js
```

## Output

```json
{
  "goal": "Show that, for a stable circular orbit, the further out you go, the slower the orbital speed.",
  "model_notes": "Circular-orbit approximation: v = sqrt(G*M / r). Units are scaled for the canvas; G*M is a single tunable constant. Simplifications: two-body, perfectly circular, no perturbations.",
  "code": "let r = 150, GM = 6000, a = 0;\nfunction setup(){ createCanvas(480, 480); }\nfunction draw(){\n  background(8);\n  translate(width/2, height/2);\n  noStroke(); fill(255, 210, 80); circle(0, 0, 30); // central body\n  const v = Math.sqrt(GM / r);      // orbital speed\n  a += v / r;                        // angular step ~ v/r\n  const x = r * Math.cos(a), y = r * Math.sin(a);\n  stroke(80); noFill(); circle(0, 0, r * 2); // orbit\n  noStroke(); fill(120, 200, 255); circle(x, y, 12);\n  fill(255); text('r=' + r.toFixed(0) + '  v=' + v.toFixed(2), -width/2 + 10, -height/2 + 20);\n}\nfunction keyPressed(){ if (key === '+') r = Math.min(220, r + 10); if (key === '-') r = Math.max(50, r - 10); }",
  "experiments": [
    "Press '-' to move the planet closer. Does v go up or down?",
    "Press '+' to move it farther. Watch v shrink — slower orbits at larger r.",
    "Find an r where the planet barely crawls. Why does distance slow it down?"
  ],
  "stack": "p5js"
}
```

## Why this is a good result

The model is physically honest (v = √(GM/r), with simplifications stated); the
`orbit_radius` control measurably changes the speed readout; the experiments lead
directly to the stated insight.
