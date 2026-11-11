# claude responses

**Model / setting:** Claude (claude.ai, Opus 5.5, Medium effort)  
**Date collected:** Nov 10, 2026  
**Method:** Questions sent in two batches (Q01-Q10, Q11-Q20), each in a new chat, no system prompt.  
**Note:** Answers are condensed to the final answer and the reasoning or caveats that matter for grading. Math formatting was removed.

## Q01

**Prompt:** A 20-tooth drive gear turning at 1800 RPM with 50 N*m of torque meshes with a 60-tooth driven gear. What are the output speed and torque? Then repeat assuming 95% mesh efficiency.

**Response (condensed):** Ratio 3:1. 600 RPM, 150 N*m ideal; 142.5 N*m at 95%. Added a power check (9,425 W in, 8,954 W out = 95%).

## Q02

**Prompt:** A lug nut spec is 80 lb-ft. What is that in N*m?

**Response (condensed):** 80 x 1.3558 = 108.5 N*m.

## Q03

**Prompt:** A brake caliper piston is 2.0 in in diameter. Line pressure is 1000 psi. What force does the piston produce?

**Response (condensed):** A = 3.1416 in^2, F = 3,142 lbf (about 13.98 kN).

## Q04

**Prompt:** A 1.000 m steel rod (alpha = 12 x 10^-6 /K) is heated by 100 K. How much longer does it get?

**Response (condensed):** 1.2 mm.

## Q05

**Prompt:** An M10 bolt is torqued to 50 N*m. Using the short-form torque equation with a nut factor K = 0.20, estimate the clamp load.

**Response (condensed):** 25,000 N (25 kN). Noted real clamp load can vary +/-25% or more with friction and lubrication.

## Q06

**Prompt:** A car braking at 0.8 g from 60 mph. The driver takes 1.5 s to react. What is the total stopping distance in meters?

**Response (condensed):** Reaction 40.2 m + braking 45.9 m = about 86 m.

## Q07

**Prompt:** An engine makes 250 lb-ft of torque at 4000 RPM. What horsepower is that?

**Response (condensed):** 190.4 hp.

## Q08

**Prompt:** A cylinder has 500 cc swept volume and 50 cc clearance volume. What is the compression ratio?

**Response (condensed):** 11:1.

## Q09

**Prompt:** A starter draws 150 A through a battery cable with 0.004 ohm of resistance. What is the voltage drop across the cable? Is that acceptable?

**Response (condensed):** 0.60 V; not acceptable. Rule of thumb 0.5 V max per side, many shops use 0.2-0.3 V per cable. Clean, tighten, retest, replace cable if still high.

## Q10

**Prompt:** Can torque-to-yield (TTY) cylinder head bolts be reused?

**Response (condensed):** Generally no; plastic stretch. Exception only when the OEM manual allows reuse after a measurement check (max length / min diameter), e.g. some Honda and Toyota plastic-region bolts.

## Q11

**Prompt:** Why should lug nuts be tightened in a star (crisscross) pattern with a torque wrench?

**Response (condensed):** Even seating; uneven clamping distorts the rotor causing lateral runout, pulsation and uneven pad deposits ('warped rotors'); torque wrench gives equal preload; tighten in stages; re-check after 50-100 miles.

## Q12

**Prompt:** A tire is set to 32 psi (gauge) at 20 C. What will the gauge read at 50 C if the volume stays the same? Use 14.7 psi for atmospheric pressure.

**Response (condensed):** Absolute pressure and Kelvin; 51.48 psia, about 36.8 psi gauge.

## Q13

**Prompt:** A coil spring has a rate of 25 N/mm. How much force does it take to compress it 40 mm?

**Response (condensed):** 1000 N.

## Q14

**Prompt:** A 150 mm diameter crankshaft pulley turns at 2000 RPM. What is the belt speed in m/s?

**Response (condensed):** about 15.7 m/s.

## Q15

**Prompt:** A driver pushes the brake pedal with 100 N. The pedal ratio is 4:1. What force reaches the master cylinder pushrod (no booster)?

**Response (condensed):** 400 N, ignoring pivot friction.

## Q16

**Prompt:** Can DOT 5 brake fluid be mixed with DOT 3 or DOT 4? What about DOT 5.1?

**Response (condensed):** DOT 3/4/5.1 glycol and compatible (mix performs like lowest rated). DOT 5 silicone must never be mixed; switching needs a full flush and usually new seals; not recommended for most ABS. DOT 5.1 can mix with 3/4 but not 5.

## Q17

**Prompt:** A 10 mm diameter pin in double shear carries a 10 kN load. What is the shear stress in the pin?

**Response (condensed):** Double shear 157.08 mm^2, tau = 63.7 MPa.

## Q18

**Prompt:** A part made from steel with a yield strength of 250 MPa sees a maximum working stress of 100 MPa. What is the factor of safety against yielding?

**Response (condensed):** 2.5.

## Q19

**Prompt:** On a 4-stroke engine at 6000 RPM, a sequential fuel injector has a 10 ms pulse width. What is the injector duty cycle?

**Response (condensed):** 50%.

## Q20

**Prompt:** A hydraulic jack has a 1 cm^2 pump piston and a 50 cm^2 lift piston. With 200 N on the pump piston, what force does the lift piston make? If the pump piston moves 5 cm, how far does the lift piston move?

**Response (condensed):** 10,000 N; 0.1 cm (1 mm). Work in equals work out.
