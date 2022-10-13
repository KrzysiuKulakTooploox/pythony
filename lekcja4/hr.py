candidates = [["Adam", 15000, "Mid"], ["Basia", 20000, "Senior"], ["Celina", 19000, "Mid"]]


def analyze_presenting_offer_to_a_candidate(candidate):
    analyze_candidate_for_seniority(candidate, "Mid", 16000)
    analyze_candidate_for_seniority(candidate, "Senior", 25000)


def is_expectation_within_budget(expectation, max_budget_for_seniority):
    return expectation <= max_budget_for_seniority

def test_is_expectation_within_budget():
    assert (is_expectation_within_budget(10000, 15000)) is True
    assert (is_expectation_within_budget(15000, 15000)) is True
    assert (is_expectation_within_budget(15000, 10000)) is False


def analyze_candidate_for_seniority(candidate, seniority, max_budget_for_seniority):
    if candidate[2] == seniority:
        if is_expectation_within_budget(candidate[1], max_budget_for_seniority):
            print(candidate[0] + " dostanie ofertę.")
        else:
            print(candidate[0] + " nie dostanie oferty")


for candidate in candidates:
    analyze_presenting_offer_to_a_candidate(candidate)

test_is_expectation_within_budget()