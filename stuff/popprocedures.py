import sqlite3

data = sqlite3.connect('data.db')
cursor = data.cursor()

procedures = ["Knee Replacement", 'Percutaneous Coronary Angioplasty (PTCA)', 'Laminectomy',
'Hip Replacement','Spinal Fusion','Cholecystectomy','Bone Excision','Hysterectomy',
'Colon Resection','Scar Excision','Appendectomy','Hip/Femur Fracture','Coronary Artery Bypass Graft (CABG)',
'Lower Extremity Fracture', 'MRI', 'CT Scan']

descriptions = ["Knee replacement, also known as knee arthroplasty, is a surgical procedure to replace the weight-bearing surfaces of the knee joint to relieve pain and disability, most commonly offered when joint pain is not diminished by conservative sources and also for other knee diseases such as rheumatoid arthritis and psoriatic arthritis.",
                "Angioplasty, is also known as balloon angioplasty and percutaneous coronary transluminal angioplasty (PCTA), is a minimally invasive endovascular procedure used to widen narrowed or obstructed arteries or veins, typically to treat arterial atherosclerosis.",
                "A laminectomy is a surgical procedure that removes a portion of a vertebra called the lamina, which is the roof of the spinal canal.",
                "Hip replacement is a surgical procedure in which the hip joint is replaced by a prosthetic implant, that is, a hip prosthesis. Hip replacement surgery can be performed as a total replacement or a hemi (half) replacement. Such joint replacement orthopaedic surgery is generally conducted to relieve arthritis pain or in some hip fractures.",
                "Spinal fusion, also called spondylodesis or spondylosyndesis, is a neurosurgical or orthopedic surgical technique that joins two or more vertebrae. This procedure can be performed at any level in the spine (cervical, thoracic, or lumbar) and prevents any movement between the fused vertebrae. ",
                "Cholecystectomy is the surgical removal of the gallbladder. Cholecystectomy is a common treatment of symptomatic gallstones and other gallbladder conditions.",
                "A bone excision is the removal of a portion or growth of bone.",
                "Hysterectomy is the surgical removal of the uterus. It may also involve removal of the cervix, ovaries (oophorectomy), Fallopian tubes (salpingectomy), and other surrounding structures.",
                "Colectomy is bowel resection of the large bowel (colon). It consists of the surgical removal of any extent of the colon, usually segmental resection (partial colectomy).",
                "NULL",
                "An appendectomy, also termed appendicectomy, is a surgical operation in which the vermiform appendix (a portion of the intestine) is removed. Appendectomy is normally performed as an urgent or emergency procedure to treat complicated acute appendicitis.",
                "A hip fracture is a break that occurs in the upper part of the femur (thigh bone). Symptoms may include pain around the hip, particularly with movement, and shortening of the leg.[2] Usually the person cannot walk.",
                "Coronary artery bypass surgery, also known as coronary artery bypass graft (CABG, pronounced cabbage) is a surgical procedure for coronary artery disease (CAD) aiming to relieve angina, stall progression of ischemic heart disease and increase life expectancy.",
                "NULL",
                "Magnetic resonance imaging is a medical imaging technique used in radiology to form pictures of the anatomy and the physiological processes of the body. MRI scanners use strong magnetic fields, magnetic field gradients, and radio waves to generate images of the organs in the body.",
                "A computerized tomography (CT) scan combines a series of X-ray images taken from different angles around your body and uses computer processing to create cross-sectional images (slices) of the bones, blood vessels and soft tissues inside your body."]

for i in range(1, len(procedures) + 1):
    cursor.execute("INSERT INTO procedures VALUES(?, ?, ?)", (i, procedures[i-1], descriptions[i-1]))

data.commit()



