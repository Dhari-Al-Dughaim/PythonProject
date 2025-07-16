# هنا بنضيف الدوال المساعدة مثل حساب الدرجات وغيرها
def calculate_score(answers, correct_answers):
    return sum([1 for a, b in zip(answers, correct_answers) if a == b])