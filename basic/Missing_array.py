n = int(input("Enter n (max number): ").strip())

arr_input = input("Enter array elements separated by commas: ").strip()
if not arr_input:
	arr = []
else:
	arr = [int(x) for x in arr_input.replace(" ", "").split(",") if x != ""]

missing = sorted(set(range(1, n + 1)) - set(arr))
if missing:
	print("Missing numbers:", ",".join(map(str, missing)))
else:
	print("No missing numbers")

