from bakery import assert_equal


def biggest_bed(garden: str) -> str:
    if garden == "":
        return "no flowers"
    flower_beds = garden.split(',')
    most_popular = flower_beds[0]
    taking = True
    for flower_bed in flower_beds:
        if 'π³' in flower_bed:
            taking = False
        elif taking and 'π±' not in flower_bed:
            if len(flower_bed) > len(most_popular):
                most_popular = flower_bed
    if 'π±' in most_popular or 'π³' in most_popular:
        return "no flowers"
    return most_popular


assert_equal(biggest_bed("πΉπΉ,π·π·,π»π»π»,πΈ"), "π»π»π»")
assert_equal(biggest_bed("πΉπΉ,π·π·,πΌπΌπΌ,πΈ,πΊπΊπΊπΊ,π»π»π»"), "πΊπΊπΊπΊ")
assert_equal(biggest_bed("πΉπΉ,π·π·,πΌπΌπΌ,π±π±π±π±π±,π³,πΈ,πΊπΊπΊπΊ,π»π»π»"), "πΌπΌπΌ")
assert_equal(biggest_bed("πΉπΉ,π·π·,πΌπΌπΌ,π³,πΈ,πΊπΊπΊπΊ,π»π»π»"), "πΌπΌπΌ")
assert_equal(biggest_bed("πΉπΉ,π·π·,πΌπΌπΌ,π±π±π±π±π±,πΈ,πΊπΊπΊπΊ,π»π»π»"), "πΊπΊπΊπΊ")
assert_equal(biggest_bed("π±π±,π±π±π±,π³,πΈ,πΊπΊπΊπΊ"), "no flowers")
assert_equal(biggest_bed("π³,πΈ,πΊπΊπΊπΊ"), "no flowers")
assert_equal(biggest_bed(""), "no flowers")
assert_equal(biggest_bed("π³π³π³"), "no flowers")
assert_equal(biggest_bed("π±π±"), "no flowers")
assert_equal(biggest_bed("π±π±π±,πΉπΉπΉπΉ"), "πΉπΉπΉπΉ")