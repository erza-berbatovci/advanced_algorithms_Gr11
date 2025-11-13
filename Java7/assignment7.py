import json

def findLongestQuestionPath(questionnaire):
    # Map each question by its ID for fast lookup
    questions = {q["id"]: q for q in questionnaire["questions"]}
    
    def dfs(question_id, visited_questions, visited_answers):
        """Recursive DFS to explore all possible paths."""
        if question_id is None:
            return {
                "length": len(visited_questions),
                "question_ids": visited_questions.copy(),
                "answer_path": visited_answers.copy()
            }
        
        q = questions[question_id]
        visited_questions.append(q["id"])
        
        # If question has answers (radio/select), branch by each answer
        if "answers" in q and q["answers"]:
            best_path = {"length": 0, "question_ids": [], "answer_path": []}
            for ans in q["answers"]:
                visited_answers.append(ans["id"])
                result = dfs(ans["next_question_id"], visited_questions, visited_answers)
                if result["length"] > best_path["length"]:
                    best_path = result
                visited_answers.pop()  # backtrack
            visited_questions.pop()
            return best_path
        
        # If text/checkbox type, go directly to next question
        elif "next_question_id" in q:
            result = dfs(q["next_question_id"], visited_questions, visited_answers)
            visited_questions.pop()
            return result
        
        # If neither next_question_id nor answers — end of path
        else:
            result = {
                "length": len(visited_questions),
                "question_ids": visited_questions.copy(),
                "answer_path": visited_answers.copy()
            }
            visited_questions.pop()
            return result
    
    # Start from start_question_id
    start_id = questionnaire["start_question_id"]
    return dfs(start_id, [], [])


# =====================
# Example Test
# =====================

# Example JSON data (shortened version — you can load full from file if needed)
data = {
    "start_question_id": "q1",
    "questions": [
        {
            "id": "q1",
            "text": "Do you own a car?",
            "type": "radio",
            "answers": [
                {"id": "a1_yes", "text": "Yes", "next_question_id": "q2"},
                {"id": "a1_no", "text": "No", "next_question_id": "q5"}
            ]
        },
        {
            "id": "q2",
            "text": "What type of car do you own?",
            "type": "select",
            "answers": [
                {"id": "a2_sedan", "text": "Sedan", "next_question_id": "q3"},
                {"id": "a2_suv", "text": "SUV", "next_question_id": "q3"},
                {"id": "a2_truck", "text": "Truck", "next_question_id": "q4"},
                {"id": "a2_sports", "text": "Sports Car", "next_question_id": "q4"}
            ]
        },
        {
            "id": "q3",
            "text": "How many passengers can your vehicle seat?",
            "type": "radio",
            "answers": [
                {"id": "a3_2to5", "text": "2-5", "next_question_id": "q6"},
                {"id": "a3_6plus", "text": "6+", "next_question_id": "q6"}
            ]
        },
        {
            "id": "q4",
            "text": "Do you use your vehicle for work purposes?",
            "type": "radio",
            "answers": [
                {"id": "a4_yes", "text": "Yes", "next_question_id": "q7"},
                {"id": "a4_no", "text": "No", "next_question_id": "q6"}
            ]
        },
        {
            "id": "q5",
            "text": "What is your primary mode of transportation?",
            "type": "select",
            "answers": [
                {"id": "a5_public", "text": "Public Transit", "next_question_id": "q6"},
                {"id": "a5_bike", "text": "Bicycle", "next_question_id": "q6"},
                {"id": "a5_walk", "text": "Walking", "next_question_id": "q6"}
            ]
        },
        {
            "id": "q6",
            "text": "What is your annual commute distance?",
            "type": "text",
            "next_question_id": "q8"
        },
        {
            "id": "q7",
            "text": "What percentage of your vehicle use is for work?",
            "type": "text",
            "next_question_id": "q8"
        },
        {
            "id": "q8",
            "text": "Are you satisfied with your current transportation situation?",
            "type": "radio",
            "answers": [
                {"id": "a8_yes", "text": "Yes", "next_question_id": None},
                {"id": "a8_no", "text": "No", "next_question_id": "q9"}
            ]
        },
        {
            "id": "q9",
            "text": "What would you like to improve?",
            "type": "text",
            "next_question_id": None
        }
    ]
}

# Run
result = findLongestQuestionPath(data)
print(json.dumps(result, indent=2))
