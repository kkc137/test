import datetime
import typing
import operator

def parse_data(patient_filename: str, lab_filename: str)->list[dict[str, str]]:
    records = {}
    for line in open(patient_filename).readlines()[1:]:
        arr = line.strip().split("\t")
        records[arr[0]] = {"Birth" : arr[2]}
    for line in open(lab_filename).readlines()[1:]:
        arr = line.strip().split("\t")
        if arr[2] not in records[arr[0]]:
            records[arr[0]][arr[2]] = [float(arr[3])]
        else:
            records[arr[0]][arr[2]].append(float(arr[3]))

    return(records)

def patient_age(records: list, patient_id: str) -> float:
    nowdate = datetime.datetime.now()
    birthdate = datetime.datetime.strptime(records[patient_id]["Birth"], "%Y-%m-%d %H:%M:%S.%f")
    age = nowdate.year - birthdate.year - ((nowdate.month, nowdate.day) < (birthdate.month, birthdate.day))
    print(age)

def patient_is_sick(records: list, patient_id: str, lab_name: str, oper: str, value: float)->bool:
    value_list = records[patient_id][lab_name]
    flag = False
    if oper == ">":
        for i in value_list:
            if operator.gt(i, value):
                flag = True
    elif oper == "<":
        for i in value_list:
            if operator.lt(i, value):
                flag = True
    print(flag)

records = parse_data("PatientCorePopulatedTable.txt", "LabsCorePopulatedTable.txt")
patient_age(records, "1A8791E3-A61C-455A-8DEE-763EB90C9B2C")
patient_age(records, "80D356B4-F974-441F-A5F2-F95986D119A2")
patient_is_sick(records, "1A8791E3-A61C-455A-8DEE-763EB90C9B2C", "METABOLIC: ALBUMIN", ">", 2)
patient_is_sick(records, "80D356B4-F974-441F-A5F2-F95986D119A2", "CBC: PLATELET COUNT", "<", 4)