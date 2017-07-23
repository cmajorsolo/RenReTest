def extract_contract_info(coverage_list):git
    includes = []
    excludes = []
    for coverage in coverage_list:
        if 'Include' in coverage:
            includes += (coverage['Include'])
        if 'Exclude' in coverage:
            excludes += (coverage['Exclude'])
    return includes, excludes

def process_claim(claimValue, maxClaimValue):
    if claimValue > maxClaimValue:
        claimValue = maxClaimValue
    return claimValue