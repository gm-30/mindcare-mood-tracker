
def generate_ai_insights(avg_mood, avg_sleep):
    insights = []

    if avg_sleep < 6:
        insights.append(
            "You have been sleeping less than recommended."
        )

    if avg_mood <= 2:
        insights.append(
            "Frequent low moods detected. Consider reaching out to supportive people."
        )

    if avg_sleep >= 7 and avg_mood >= 4:
        insights.append(
            "Healthy sleep patterns may be supporting your wellbeing."
        )

    if not insights:
        insights.append("Keep tracking consistently!")

    return insights
