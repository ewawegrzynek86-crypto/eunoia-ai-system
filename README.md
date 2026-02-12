EUNOIA – A System Supporting Cognitive Autonomy and Stress Regulation
Final project for the Building AI course
Summary
EUNOIA is a personalized AI system designed to operate alongside a wearable device in order to support cognitive autonomy through the analysis of individual physiological patterns and—optionally—linguistic patterns.
The system functions fully locally, under complete user control, and reports only correlations and trends — never causes, diagnoses, or behavioral judgments.
Background
Modern environments are saturated with constant stimulation, rapid communication, and sustained cognitive pressure. Many individuals:
fail to recognize early physiological signs of overload,
struggle to detect manipulative communication patterns (e.g., subtle invalidation),
operate under gradually increasing chronic tension,
face difficulties with emotional regulation, especially neurodivergent individuals.
Existing technological tools rely mainly on generic relaxation exercises or population-level models.
There is a clear need for systems that adapt to the individual rather than requiring individuals to conform to generalized norms.
EUNOIA is grounded in the idea that people benefit from tools which enhance reflective awareness — without interpreting, correcting, or judging their experience.
How is it used?
EUNOIA consists of two independent functional layers:
1. Continuous Physiological Calibration (Local)
The system analyzes:
heart rate (HR),
heart rate variability (HRV),
breathing rhythm (if available),
activity level,
recovery time to baseline.
From these signals, it constructs a personal regulatory baseline unique to the user.
Physiological signals are treated strictly as biological measurements — not as emotional labels.
2. On-Demand Linguistic Analysis
The user may voluntarily submit text (typed or obtained via speech-to-text).
EUNOIA then:
generates a semantic vector representation (embedding),
compares it only to the user’s previous embeddings (if enabled),
correlates linguistic features with physiological data from the corresponding timeframe,
returns a neutral, correlation-based report.
Nothing is interpreted as intent, diagnosis, personality, or interpersonal meaning.
Alerts appear only when stable deviations from the personal baseline persist.
Confidence levels describe signal stability — not interpretative certainty.
Stakeholders and Context
Primary stakeholders
Individuals seeking improved self-regulation and self-awareness, particularly in high-stress or high-stimulation environments.
Secondary stakeholders
developers,
data protection auditors,
researchers analyzing ethical AI architectures.
EUNOIA is designed for everyday personal use, without institutional oversight.
Data Sources and AI Methods
Data Sources
Physiological data:
HR / HRV
breathing rhythm
activity
recovery time
Optional linguistic data:
manually entered text
speech-to-text input
Variability in wearable sensors may affect signal accuracy and trend detection reliability.
AI Methods
unsupervised anomaly detection relative to individual baseline,
short- and long-term trend modeling,
semantic vector representations (embeddings),
threshold-based alert mechanisms,
architectural separation of global and personal on-device models.
EUNOIA – Data Flow
Step 1: Physiological Data Collection
Wearable device → HR / HRV / breathing / activity → local transfer.
Step 2: Local Calibration Module
Incoming data is compared to the personal baseline; the model updates incrementally.
Step 3: Deviation Detection
Detector classifies deviations as:
temporary,
repeated,
emerging trends (requiring ≥3 consecutive periods).
No causal interpretation is performed.
Step 4: Optional Linguistic Module
User submits text → embedding generated → correlated with physiological timeline.
Step 5: Fusion Layer
Biological and linguistic data are integrated strictly within a correlation-only framework (causal barrier principle).
Step 6: Reporting
The system provides:
gentle alerts for sustained trends,
a visual map of changes,
confidence levels (low / medium / high).
Confidence reflects the stability of data, not interpretative accuracy.
Step 7: Local Storage
Encrypted, user-controlled, stored exclusively on device.
Step 8: Optional Backup
Encrypted backup secured with a user-controlled key.
Global systems never receive personal data.
Local System Architecture
Wearable device
→ physiological signal capture
→ calibration module
→ personal regulatory model (on-device)
→ optional linguistic module
→ fusion layer
→ reporting layer
→ encrypted storage
→ optional encrypted backup
If a global model exists, it never accesses personal data.
Color Design and Interface Philosophy
EUNOIA’s visual identity serves regulatory stability rather than branding.
White → perceptual neutrality
Cobalt blue → precise and controlled intervention
Soft gradients → regulation as a continuous process
The interface avoids overstimulation, prioritizing clarity and low sensory load.
Ethical Principles
Causal Barrier Principle
Only correlations and trends — never causes, diagnoses, or inferred intent.
Full User Control
Linguistic analysis is optional; all data can be selectively deleted or fully reset.
No Behavioral Steering
EUNOIA does not instruct users what to do, feel, or conclude.
Model Separation
Personal on-device models remain isolated from global systems.
Privacy by Design
No personal data leaves the device without explicit and reversible consent.
Right to Erasure
Selective or complete deletion is always available.
Evaluation Perspective
Effectiveness would be assessed through:
false positive rate in anomaly detection,
long-term stability of trend recognition,
user-reported usefulness,
independent ethical and security audits.
The system prioritizes epistemic transparency over predictive assertiveness.
Challenges
EUNOIA does not:
diagnose mental health conditions,
infer emotional causes,
evaluate interpersonal relationships,
replace psychological care.
Limitations include:
potential false positives,
risk of overinterpretation by users,
difficulty with irony and complex social cues,
sensor inaccuracies,
possible over-reliance on technological mediation.
What Next?
Future development may include:
early smartwatch prototype integration,
interface refinement,
pilot studies with volunteers,
interdisciplinary collaboration (AI ethics, cognitive science, HCI),
calibration research in anomaly detection,
formal ethical and security review.
Long-term, EUNOIA could contribute to research on privacy-preserving affect-aware AI systems.
Acknowledgments
Inspired by:
HRV research and autonomic regulation studies,
on-device machine learning architectures,
contemporary ethical AI frameworks,
a synesthetic perceptual concept combining color and motion.
No licensed or proprietary code was used.
The project is conceptual and exploratory.
