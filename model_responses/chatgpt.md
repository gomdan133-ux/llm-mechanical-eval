# chatgpt responses

**Model / setting:** ChatGPT (chatgpt.com, Free plan, default model, no Think mode)  
**Date collected:** Nov 10, 2026  
**Method:** Questions sent in two batches (Q01-Q10, Q11-Q20), each in a new chat, no system prompt.  
**Note:** Answers are condensed to the final answer and the reasoning or caveats that matter for grading. Math formatting was removed.

## Q01

**Prompt:** A 20-tooth drive gear turning at 1800 RPM with 50 N*m of torque meshes with a 60-tooth driven gear. What are the output speed and torque? Then repeat assuming 95% mesh efficiency.

**Response (condensed):** Ratio 3:1. 600 RPM, 150 N*m ideal; 142.5 N*m at 95% (speed still 600 RPM). Noted output gear turns the opposite direction.

## Q02

**Prompt:** A lug nut spec is 80 lb-ft. What is that in N*m?

**Response (condensed):** 80 x 1.35582 = 108.47, final 108.5 N*m.

## Q03

**Prompt:** A brake caliper piston is 2.0 in in diameter. Line pressure is 1000 psi. What force does the piston produce?

**Response (condensed):** A = pi*d^2/4 = 3.1416 in^2. F = 3,142 lbf (about 13,972 N).

## Q04

**Prompt:** A 1.000 m steel rod (alpha = 12 x 10^-6 /K) is heated by 100 K. How much longer does it get?

**Response (condensed):** dL = alpha*L*dT = 0.0012 m = 1.2 mm; final length 1.0012 m.

## Q05

**Prompt:** An M10 bolt is torqued to 50 N*m. Using the short-form torque equation with a nut factor K = 0.20, estimate the clamp load.

**Response (condensed):** F = T/(K*D) = 50/(0.20*0.010) = 25,000 N (25 kN). Noted preload depends on threads, lubrication and friction.

## Q06

**Prompt:** A car braking at 0.8 g from 60 mph. The driver takes 1.5 s to react. What is the total stopping distance in meters?

**Response (condensed):** Reaction 40.23 m + braking 45.82 m = 86.05 m (about 86.1 m). NOTE: an embedded interactive widget in the same answer showed '40.2 + 51.4 = 91.6 m', which contradicts the written result.

## Q07

**Prompt:** An engine makes 250 lb-ft of torque at 4000 RPM. What horsepower is that?

**Response (condensed):** HP = 250*4000/5252 = 190.4 hp.

## Q08

**Prompt:** A cylinder has 500 cc swept volume and 50 cc clearance volume. What is the compression ratio?

**Response (condensed):** CR = (500+50)/50 = 11:1.

## Q09

**Prompt:** A starter draws 150 A through a battery cable with 0.004 ohm of resistance. What is the voltage drop across the cable? Is that acceptable?

**Response (condensed):** V = 0.60 V. Generally too high; guideline about 0.5 V or less on the positive side. Inspect connections, terminals, cable condition and size.

## Q10

**Prompt:** Can torque-to-yield (TTY) cylinder head bolts be reused?

**Response (condensed):** Generally no; TTY bolts stretch past the elastic limit. Replace, follow sequence and torque-angle procedure. Some manufacturers specify reusable bolts, so check the service manual.

## Q11

**Prompt:** Why should lug nuts be tightened in a star (crisscross) pattern with a torque wrench?

**Response (condensed):** Even clamp force, proper seating, reduces rotor distortion and vibration, prevents uneven stud stress; torque wrench gives spec torque. Did not explain the lateral runout mechanism.

## Q12

**Prompt:** A tire is set to 32 psi (gauge) at 20 C. What will the gauge read at 50 C if the volume stays the same? Use 14.7 psi for atmospheric pressure.

**Response (condensed):** Absolute pressure and Kelvin used. 46.7 x 323.15/293.15 = 51.48 psia, gauge 36.78 psi.

## Q13

**Prompt:** A coil spring has a rate of 25 N/mm. How much force does it take to compress it 40 mm?

**Response (condensed):** F = kx = 1000 N.

## Q14

**Prompt:** A 150 mm diameter crankshaft pulley turns at 2000 RPM. What is the belt speed in m/s?

**Response (condensed):** v = pi*0.15*2000/60 = 15.71 m/s.

## Q15

**Prompt:** A driver pushes the brake pedal with 100 N. The pedal ratio is 4:1. What force reaches the master cylinder pushrod (no booster)?

**Response (condensed):** 400 N.

## Q16

**Prompt:** Can DOT 5 brake fluid be mixed with DOT 3 or DOT 4? What about DOT 5.1?

**Response (condensed):** DOT 5 silicone, do not mix with 3, 4 or 5.1. DOT 3, 4, 5.1 glycol based and generally compatible (mix performs like the lower-rated fluid). Follow OEM spec.

## Q17

**Prompt:** A 10 mm diameter pin in double shear carries a 10 kN load. What is the shear stress in the pin?

**Response (condensed):** A = 78.54 mm^2, double shear 157.08 mm^2, tau = 63.66 MPa.

## Q18

**Prompt:** A part made from steel with a yield strength of 250 MPa sees a maximum working stress of 100 MPa. What is the factor of safety against yielding?

**Response (condensed):** FoS = 250/100 = 2.5.

## Q19

**Prompt:** On a 4-stroke engine at 6000 RPM, a sequential fuel injector has a 10 ms pulse width. What is the injector duty cycle?

**Response (condensed):** One revolution 10 ms, cycle 20 ms, duty 50%.

## Q20

**Prompt:** A hydraulic jack has a 1 cm^2 pump piston and a 50 cm^2 lift piston. With 200 N on the pump piston, what force does the lift piston make? If the pump piston moves 5 cm, how far does the lift piston move?

**Response (condensed):** 10,000 N; lift piston moves 0.1 cm (1 mm).
