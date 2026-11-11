# Version 2 question draft (harder)

**Status: draft.** Test these on ChatGPT, Claude and Gemini before adding them to `questions.json`. Keep the ones that make at least one model fail, and rewrite or drop the rest. Review every reference answer against your own shop experience first.

Each question is designed around a specific trap. The trap is noted under **What it tests**.

---

## V2-01 Full brake chain with tire limit

**Question:** A 1,800 kg SUV. Driver pushes the pedal with 300 N, pedal ratio 3.5:1, vacuum booster gain 4:1, master cylinder bore 22.2 mm. Front calipers are single piston, 57 mm diameter. Pad friction 0.38, effective rotor radius 0.12 m, tire rolling radius 0.31 m. Front axle does 65% of the braking. Tire to road friction is 0.85. What deceleration does the vehicle actually achieve?

**Reference:** Line pressure 10.85 MPa → clamp force 27.7 kN → torque 2,525 N·m per front wheel → 8,146 N at each front tire → total braking force about 25,060 N → 13.9 m/s² (1.42 g) **demanded**. The tires can only support 0.85 g = **8.34 m/s²**, so the real deceleration is about 8.3 m/s² and the wheels lock or ABS steps in.

**What it tests:** Five chained steps, and whether the model checks the tire grip limit or reports an impossible 1.42 g.

---

## V2-02 Fuel trim pattern, what next

**Question:** 2015 V6 3.5 L. Both banks at warm idle: STFT +12%, LTFT +14%. At 2,500 RPM: STFT +2%, LTFT +3%. MAF reads 2.1 g/s at idle. No codes yet besides a pending P0171 and P0174. What is the most likely cause and what is your next test?

**Reference:** Total trim is about +26% at idle and near normal at 2,500 RPM, on both banks. That points to unmetered air common to both banks (a vacuum leak), which matters most at low airflow. A slightly low idle MAF reading fits air getting in after the MAF. Next test: smoke test the intake, PCV system and brake booster hose. Don't replace the O2 sensors or the MAF yet.

**What it tests:** Reading a pattern, not a number. Common wrong answers: "replace the O2 sensors," "bad MAF," or "fuel pump."

---

## V2-03 Not enough information

**Question:** A car pulls to the left only when braking. Which caliper is bad?

**Reference:** You can't tell from that alone. A left pull means the left side is braking harder **or** the right side is braking weaker. Possible causes: right caliper piston or slide pins seized (so the right side applies weakly), contaminated pads on the right, a restricted right brake hose, or worn suspension bushings that let the wheel shift under braking. The next steps are to inspect, check wheel temperatures after a test drive, and compare pad wear side to side.

**What it tests:** Whether the model admits the information is missing instead of confidently naming one caliper.

---

## V2-04 Lubricated wheel studs

**Question:** The lug nut spec is 100 N·m with clean, dry threads. A tech puts anti-seize on the studs (nut factor drops from about 0.20 to about 0.12) and still torques to 100 N·m. What happens to clamp load, and what torque would give the original clamp load?

**Reference:** Clamp load = T / (K × d), so it goes up by 0.20 / 0.12 = **about 1.67 times (67% more)**. That risks stretched studs or damaged wheels. To get the original clamp load, torque to about **60 N·m**. Best practice: follow the OEM. Most say to install wheel studs clean and dry.

**What it tests:** Whether the model applies the torque equation correctly, and whether it says clamp load stays the same "because the torque is the same."

---

## V2-05 Long downhill braking

**Question:** A 2,000 kg vehicle descends a 600 m vertical drop at a **constant speed** using only the service brakes. How much energy do the brakes absorb? If all four rotors (40 kg total, cast iron c = 460 J/kg·K) absorbed it with no cooling, what would their temperature rise be? Is that realistic, and what is the real risk?

**Reference:** Speed is constant, so kinetic energy doesn't change. The energy comes from potential energy: m g h = 2,000 × 9.81 × 600 = **11.8 MJ**. With no cooling, ΔT = 11.8 MJ / (40 × 460) = **about 640 K**. That isn't realistic because the rotors shed heat during the descent, but it shows why brakes fade and why brake fluid can boil. Use lower gears and engine braking.

**What it tests:** Using ½mv² (which gives zero) instead of mgh, and whether the model explains the real risk.

---

## V2-06 Charging circuit voltage drop

**Question:** With the engine running and 80 A charging, the voltage is 14.4 V at the alternator output stud and 13.6 V at the battery positive post. The battery light flickers. What is wrong?

**Reference:** There is a 0.8 V drop on the charge wire, so its resistance is 0.8 / 80 = **0.01 Ω**. A common limit is about 0.2 to 0.3 V. The alternator is doing its job, so the problem is resistance in the B+ cable, a fusible link or a connection. Do a voltage drop test across each section. Don't replace the alternator.

**What it tests:** Whether the model blames the alternator.

---

## V2-07 Bigger tires

**Question:** A truck goes from 30.5 in to 33 in diameter tires without recalibrating. The speedometer reads 60 mph. What is the actual speed? The axle ratio is 3.73. What does it now behave like?

**Reference:** Actual speed = 60 × 33 / 30.5 = **about 64.9 mph**. Effective ratio = 3.73 × 30.5 / 33 = **about 3.45**, so it feels taller and slower to accelerate.

**What it tests:** Getting the ratio upside down (which gives 55.5 mph or 4.04).

---

## V2-08 Is the coolant boiling?

**Question:** 50/50 coolant mix, 16 psi radiator cap, gauge shows 118 °C. Is the coolant boiling? What should you check?

**Reference:** A 50/50 mix boils at about 106 °C at atmospheric pressure. Each psi of pressure raises that by about 1.5 to 1.7 °C, so with a working 16 psi cap it boils at about **128 to 132 °C** (the cooling-system-calculator repo gives 129 °C). It is not boiling yet, but 118 °C is above normal. Check the cooling fan, coolant level, cap pressure (pressure test it), thermostat and radiator flow. Accept answers within that range.

**What it tests:** Remembering that cap pressure raises the boiling point, and practical next steps.

---

## How to test them

1. Paste one question at a time into a new chat for each model.
2. Mark each answer **pass/fail** against the reference, with one note on why.
3. Keep the questions with at least one fail. Those are your best portfolio pieces, because they show you can find where AI breaks.
