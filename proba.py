lista = [{"id": 1, "name": "s"}, {"id": 3, "name": "a"},
         {"id": 4, "name": "f"}, {"id": 2, "name": "gf"}]

# {
#     "id":[1,3,4,2],
#     "name":"s,a,f,gf"
# }

save_csv = {}
for d in lista:
    for k, v in d.items():
        save_csv[k] = save_csv.get(k, []) + [v]

print(save_csv)
