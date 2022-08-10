col = {
    "nums": [77, 95],
    "Student": {
        "Name": "Avi",
        "ID": 111111,
        "Grades": {
            "score": [89, 96, 100]
        }
    }
}

nums = col["nums"]
score = col["Student"]["Grades"]["score"]
print(nums, ' and ', score)

avg_nums = sum(nums) / len(nums)
avg_score = sum(score) / len(score)

if avg_nums > avg_score:
    print('avg_nums is max:', avg_nums)
else:
    print('avg_score is max:', avg_score)
