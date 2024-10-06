import pyAgrum as gum

bn = gum.BayesNet('StudentAdmission')

exam_level = bn.add(gum.LabelizedVariable('ExamLevel', 'Exam Level', 2))  # 0: easy, 1: difficult
iq_level = bn.add(gum.LabelizedVariable('IQLevel', 'IQ Level', 2))  # 0: low, 1: high
marks = bn.add(gum.LabelizedVariable('Marks', 'Marks', 2))  # 0: fail, 1: pass
aptitude_score = bn.add(gum.LabelizedVariable('AptiScore', 'Aptitude Score', 2))  # 0: low, 1: high
admission = bn.add(gum.LabelizedVariable('Admission', 'Admission', 2))  # 0: no, 1: yes

bn.addArc(exam_level, marks)
bn.addArc(iq_level, marks)
bn.addArc(iq_level, aptitude_score)
bn.addArc(marks, admission)

bn.cpt(exam_level).fillWith([0.7, 0.3])

bn.cpt(iq_level).fillWith([0.8, 0.2])

bn.cpt(marks)[{'ExamLevel': 0, 'IQLevel': 0}] = [0.6, 0.4]
bn.cpt(marks)[{'ExamLevel': 1, 'IQLevel': 0}] = [0.5, 0.5]
bn.cpt(marks)[{'ExamLevel': 0, 'IQLevel': 1}] = [0.9, 0.1]
bn.cpt(marks)[{'ExamLevel': 1, 'IQLevel': 1}] = [0.8, 0.2]

bn.cpt(aptitude_score)[{'IQLevel': 0}] = [0.75, 0.25]
bn.cpt(aptitude_score)[{'IQLevel': 1}] = [0.4, 0.6]

bn.cpt(admission)[{'Marks': 0}] = [0.6, 0.4]
bn.cpt(admission)[{'Marks': 1}] = [0.9, 0.1]

model = gum.LazyPropagation(bn)
model.makeInference()

model.setEvidence({'ExamLevel': 1, 'IQLevel': 0, 'AptiScore': 0})
prob_case_1 = model.posterior('Admission')[1]
print(f"Probability for Case 1 (Admission | ExamLevel=1, IQLevel=0, AptiScore=0): {prob_case_1:.4f}")

model.setEvidence({'ExamLevel': 0, 'IQLevel': 1, 'AptiScore': 1})
prob_case_2 = model.posterior('Admission')[0]
print(f"Probability for Case 2 (No Admission | ExamLevel=0, IQLevel=1, AptiScore=1): {prob_case_2:.4f}")

model.setEvidence({'ExamLevel': 1, 'Marks': 1})  

nodes = bn.names()
predictions = {node: model.posterior(node) for node in nodes if node != 'Marks'}

for node, prediction in predictions.items():
    print(f"{node}:")
    for i, value in enumerate(bn.variable(node).labels()):
        probability = prediction[i]
        print(f"    {value}: {probability:.4f}")
