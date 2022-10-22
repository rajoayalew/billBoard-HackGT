import sqlite3
import random

procedures = ["Knee Replacement", 'Percutaneous Coronary Angioplasty (PTCA)', 'Laminectomy',
'Hip Replacement','Spinal Fusion','Cholecystectomy','Bone Excision','Hysterectomy',
'Colon Resection','Scar Excision','Appendectomy','Hip/Femur Fracture','Coronary Artery Bypass Graft (CABG)',
'Lower Extremity Fracture', 'MRI', 'CT Scan']


data = sqlite3.connect('data.db')
cursor = data.cursor()
procedure = procedures[random.randint(0,15)]

output = cursor.execute("SELECT proc_id FROM procedures WHERE name LIKE " + procedure)

print(output[0]) 